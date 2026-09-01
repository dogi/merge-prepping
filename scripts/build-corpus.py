#!/usr/bin/env python3
"""Build a `title-corpus.md` reference pack from a repo's squash-merge log.

Pairs each merged PR title with the files that produced it, because the changed
files are the primary input to the title. Groups by scope, computes the shape /
scope / gerund league tables the pack quotes, and flags any point where the log
changed its mind about the trailing gerund partway through the window.

    scripts/build-corpus.py --repo ~/src/planet --name planet \
        --strip src/app/ --skip package.json --skip package-lock.json \
        > references/planet/title-corpus.md

    scripts/build-corpus.py --repo ~/src/myplanet --name myplanet \
        --strip app/src/main/java/org/ole/planet/myplanet/ \
        --skip app/build.gradle > references/myplanet/title-corpus.md

Read the output before writing the pack's `conventions.md` — the league tables
tell you what the repo actually does, which is rarely what you assumed.
"""
import argparse
import re
import subprocess
import sys
from collections import Counter, OrderedDict

SQUASH_SUFFIX = re.compile(r"\s*\(#\d+\)\s*$")
SCOPE = re.compile(r"^([a-z0-9-]+):")
# `closes #N` shows up occasionally but is not house style in either repo, so it
# is reported alongside the real typos rather than counted as well-formed.
LINK = re.compile(r"\((fixes|connects) #\d+\)$")
ISSUE = re.compile(r"\((?:fixes|connects|closes)\W*#?(\d+)\)")
PR = re.compile(r"\(#(\d+)\)\s*$")
GERUND = re.compile(r"[a-z]+ing \((?:fixes|connects|closes)")
GERUND_WORD = re.compile(r"\b([a-z]+ing)\b(?=\s*\((?:fixes|connects|closes))")


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", required=True, help="path to the repo checkout")
    p.add_argument("--name", required=True, help="repo name, for the heading")
    p.add_argument("--count", type=int, default=500, help="commits to read")
    p.add_argument(
        "--recent",
        type=int,
        default=100,
        help="size of the recent sub-window reported alongside the full one, "
        "so drift in scope and gerund usage is visible (0 to disable)",
    )
    p.add_argument("--ref", default="HEAD", help="branch or ref to read")
    p.add_argument(
        "--skip",
        action="append",
        default=[],
        help="path to omit from every entry, e.g. the per-PR version bump file "
        "(repeatable)",
    )
    p.add_argument(
        "--strip",
        action="append",
        default=[],
        help="path prefix to drop for readability (repeatable, longest match wins)",
    )
    return p.parse_args()


def main():
    args = parse_args()
    skip = set(args.skip)
    strips = sorted(args.strip, key=len, reverse=True)

    def git(*rest):
        return subprocess.run(
            ["git", "-C", args.repo, *rest],
            capture_output=True,
            text=True,
            check=True,
        ).stdout

    def shorten(path):
        for prefix in strips:
            if path.startswith(prefix):
                return path[len(prefix):]
        return path

    def clean(subject):
        return SQUASH_SUFFIX.sub("", subject).strip()

    log = git("log", "--format=%H%x1f%s%x1f%ad", "--date=short",
              f"-{args.count}", args.ref).splitlines()
    commits = []
    for line in log:
        if not line.strip():
            continue
        sha, subject, date = line.split("\x1f")
        files = [
            f
            for f in git("show", "--name-only", "--format=", sha).split("\n")
            if f and f not in skip
        ]
        commits.append((sha, subject, date, files))

    if not commits:
        sys.exit(f"no commits found in {args.repo}")

    n = len(commits)
    titles = [clean(s) for _, s, _, _ in commits]
    dates = [d for _, _, d, _ in commits]

    smoother = [i for i, t in enumerate(titles) if " smoother " in t]
    n_less = sum(1 for t in titles if " is more" in t)
    n_bump = sum(1 for t in titles if re.match(r"^[a-z0-9-]+: bump ", t))
    n_other = n - len(smoother) - n_less - n_bump

    scope_counts = Counter()
    by_scope = OrderedDict()
    for idx, (_, subject, _, files) in enumerate(commits):
        title = clean(subject)
        m = SCOPE.match(title)
        scope = m.group(1) if m else "(no scope)"
        scope_counts[scope] += 1
        by_scope.setdefault(scope, []).append((idx, title, files))

    def gerund_counts(subset):
        c = Counter()
        for t in subset:
            m = GERUND_WORD.search(t)
            if m:
                c[m.group(1)] += 1
        return c

    def scope_counts_of(subset):
        c = Counter()
        for t in subset:
            m = SCOPE.match(t)
            c[m.group(1) if m else "(no scope)"] += 1
        return c

    def phrase_lengths(subset):
        """Words between `smoother` and the issue stamp, gerund included."""
        c = Counter()
        for t in subset:
            m = re.match(
                r"^[a-z0-9-]+: smoother (.+?) \((?:fixes|connects|closes)\b", t
            )
            if m:
                c[len(m.group(1).split())] += 1
        return c

    gerunds = gerund_counts(titles)
    recent_n = min(args.recent, n) if args.recent else 0
    recent_titles = titles[:recent_n]

    n_fixes = sum(1 for t in titles if "(fixes #" in t)
    n_connects = sum(1 for t in titles if "(connects #" in t)
    malformed = [t for t in titles if not LINK.search(t)]

    single = sum(1 for _, _, _, f in commits if len(f) == 1)
    upto3 = sum(1 for _, _, _, f in commits if len(f) <= 3)

    # Find the oldest point from which the trailing gerund is near-universal, so
    # the pack can tell readers which half of the window to imitate.
    changeover = None
    for i in reversed(smoother):
        window = [j for j in smoother if i - 40 <= j <= i]
        if window and sum(bool(GERUND.search(titles[j])) for j in window) / len(window) > 0.9:
            changeover = i
            break
    recent = [i for i in smoother if changeover is None or i <= changeover]
    older = [i for i in smoother if changeover is not None and i > changeover]
    recent_g = sum(bool(GERUND.search(titles[i])) for i in recent)
    older_g = sum(bool(GERUND.search(titles[i])) for i in older)
    split = changeover is not None and older and older_g / len(older) < 0.75

    out = []
    w = out.append

    def pct(a, b):
        return f"{a * 100 // b}%" if b else "n/a"

    w(f"# Title corpus — {args.name}, the last {n} merged PRs")
    w("")
    w(
        f"Generated from the {n} most recent squash commits on `{args.ref}` "
        f"(`{commits[0][0][:7]}`, PR #{(PR.search(commits[0][1]) or [None,'?'])[1]} "
        f"/ issue #{(ISSUE.search(commits[0][1]) or [None,'?'])[1]}, back to "
        f"`{commits[-1][0][:7]}`, PR #{(PR.search(commits[-1][1]) or [None,'?'])[1]} "
        f"/ issue #{(ISSUE.search(commits[-1][1]) or [None,'?'])[1]})."
    )
    w(
        "Each line pairs the landed title with the changed files that produced "
        "it — **the changed files are the primary input to the title**. Skim for "
        "the nearest precedent by scope, then by the area of the files you "
        "changed."
    )
    w("")
    if strips:
        w("Path shorthand: bare paths are under "
          + " or ".join(f"`{s}`" for s in strips)
          + "; everything else is written from the repo root.")
    if skip:
        w("Omitted from every entry: " + ", ".join(f"`{s}`" for s in sorted(skip))
          + " — the per-PR version bump, present in nearly every diff.")
    w("")
    w("The trailing `(#NNNN)` GitHub appends at squash time is stripped: what "
      "you see here is what the PR title was.")
    w("")
    w("Regenerate with:")
    w("")
    w("```")
    w("scripts/build-corpus.py --repo <checkout> --name " + args.name
      + (f" --ref {args.ref}" if args.ref != "HEAD" else "")
      + (f" --count {args.count}" if args.count != 500 else "")
      + (f" --recent {args.recent}" if args.recent != 100 else "")
      + "".join(f" --strip {s}" for s in args.strip)
      + "".join(f" --skip {s}" for s in args.skip))
    w("```")
    w("")
    w("## Shape of the window")
    w("")
    w(f"- **Shape shares:** `smoother` {len(smoother)}/{n} "
      f"({pct(len(smoother), n)}), `less … is more` {n_less}, `bump` {n_bump}, "
      f"other {n_other}.")
    w("- **Scope league table:** "
      + " · ".join(f"`{s}` {c}" for s, c in scope_counts.most_common()) + ".")
    w("- **Gerund league table:** "
      + " · ".join(f"{g} {c}" for g, c in gerunds.most_common(24)) + ".")
    w(f"- **Phrase length** (words between `smoother` and the stamp, gerund "
      "included): "
      + " · ".join(f"{k} word{'s' if k != 1 else ''} {v}"
                   for k, v in sorted(phrase_lengths(titles).items())) + ".")
    w(f"- **Issue link:** `fixes` {n_fixes}, `connects` {n_connects}, "
      f"well-formed {n - len(malformed)}/{n}.")
    w(f"- **Diff size:** {single}/{n} diffs touch a single file beyond the "
      f"version bump, {upto3}/{n} touch three or fewer.")
    if split:
        w(f"- **⚠️ The gerund era starts {dates[changeover]}.** The trailing "
          f"gerund is not uniform across this window: of the {len(recent)} "
          f"`smoother` titles from {dates[changeover]} onward, {recent_g} end "
          f"in one ({pct(recent_g, len(recent))}) — but of the {len(older)} "
          f"before it, only {older_g} do ({pct(older_g, len(older))}). Older "
          "titles stop at a bare noun phrase. **Take precedent from the recent "
          "half.** The older entries are kept because their scope and "
          "noun-phrase choices are still good evidence; their missing gerunds "
          "are not.")
    if recent_n:
        rg = gerund_counts(recent_titles)
        rs = scope_counts_of(recent_titles)
        rp = phrase_lengths(recent_titles)
        w("")
        w(f"### The last {recent_n} on their own")
        w("")
        w("Conventions drift. Where these tables disagree with the "
          f"{n}-wide ones above, **the last {recent_n} win** — they are what "
          "the maintainers are correcting titles *towards* right now.")
        w("")
        w(f"- **Scope, last {recent_n}:** "
          + " · ".join(f"`{s_}` {c}" for s_, c in rs.most_common()) + ".")
        w(f"- **Gerund, last {recent_n}:** "
          + " · ".join(f"{g} {c}" for g, c in rg.most_common(24)) + ".")
        w(f"- **Distinct gerunds:** {len(rg)} across {sum(rg.values())} "
          f"titles here, against {len(gerunds)} across {sum(gerunds.values())} "
          "over the whole window.")
        w(f"- **Phrase length, last {recent_n}:** "
          + " · ".join(f"{k} word{'s' if k != 1 else ''} {v}"
                       for k, v in sorted(rp.items())) + ".")
        gone = [s_ for s_ in scope_counts if s_ not in rs]
        if gone:
            w("- **Scopes absent from the recent window:** "
              + " · ".join(f"`{s_}`" for s_ in gone)
              + " — present earlier, not lately. Still valid; just not "
                "evidence of current practice.")
        w("")

    if malformed:
        w("- **Malformed or link-less titles in this window:**")
        for t in malformed[:10]:
            w(f"  - `{t}`")
    w("")

    for scope, entries in sorted(by_scope.items(), key=lambda kv: -len(kv[1])):
        w(f"## {scope} ({len(entries)})")
        w("")
        crossed = False
        left_recent = False
        for idx, title, files in entries:
            if recent_n and idx >= recent_n and not left_recent:
                left_recent = True
                if entries[0][0] >= recent_n:
                    # nothing in this scope is recent; the marker would be noise
                    pass
                else:
                    w("")
                    w(f"*— below here is older than the last {recent_n} "
                      "merges. —*")
                    w("")
            if split and idx > changeover and not crossed:
                crossed = True
                w("")
                w(f"*— below here predates the gerund era ({dates[changeover]}); "
                  "take")
                w("scope and noun-phrase precedent only, not the ending. —*")
                w("")
            w(f"- `{title}`")
            shown = [shorten(f) for f in files[:5]]
            more = len(files) - 5
            tail = f", +{more} more" if more > 0 else ""
            w(f"  ← {', '.join(shown)}{tail}" if shown else "  ← (no files)")
        w("")

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
