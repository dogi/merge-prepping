---
name: prepping
description: 'Rewrite a pull request title into the Open Learning Exchange house style (`scope: smoother thing doing (fixes #N)`) and make sure a tracking issue is attached and linked from the PR body so it closes on merge, creating one from the PR''s current title when none exists. Carries per-repo reference packs — myplanet (Kotlin/Android) and planet (Angular/TypeScript) — and picks the right one from the repo it is invoked against. Use this whenever preparing, cleaning up, retitling, or getting a PR ready to merge in these repos — including when the user says "prep this PR", "fix the title", "massage the title", "does this need an issue?", or just points at a PR number or branch and asks to tidy it up. Use it too when an issue stayed open after its PR merged, or when asked why a `(fixes #N)` title did not close anything. Also use it before opening a new PR, so the title is right the first time.'
---

# PR Title massaging

Every commit that lands on the default branch of an OLE repo reads the same way.
That consistency is the point: the log doubles as a changelog, and every line
traces back to an issue. This skill turns an arbitrary PR title into that form
and guarantees the issue link exists.

## Step 0 — pick the reference pack

The grammar below is shared across repos. The **scopes**, the way the noun
phrase is derived, the gerund vocabulary and the per-PR version bump are all
repo-specific and live in a pack under `references/`. Load the right one before
composing anything.

| Repo | Pack | Corpus | Stack |
|---|---|---|---|
| `open-learning-exchange/myplanet` | `references/myplanet/` | its own | Kotlin / Android |
| `open-learning-exchange/planet` | `references/planet/` | its own | Angular / TypeScript |
| `open-learning-exchange/myplanet-lite` | `references/myplanet-lite/` | **borrows myplanet's** | Kotlin / Android |

Each pack holds `conventions.md` (read it in full — it is short) and, unless it
borrows one, `title-corpus.md` (skim it for the nearest precedent at step 6 of
the procedure).

A **borrowing pack** is thin on purpose: it names the corpus and conventions it
inherits, then overrides only what actually differs. Read the pack first, then
the file it points at. myplanet-lite borrows from myplanet — same language, so
the phrase mechanics carry over whole — but overrides the scope table, four
suffix rows and the version-bump file, and none of those substitutions are
optional.

Work out which repo you are in, in this order:

1. **The PR you were given.** If the user named a PR or you resolved one, you
   already know its `owner/repo` from the tool call — use that.
2. **The checkout.** `git remote get-url origin`.
3. **Fingerprint.** `angular.json` and `src/app/` → planet. Otherwise, for the
   two Kotlin repos, read the package root: `…/org/ole/planet/myplanet/lite/`
   and a `build.gradle.kts` → myplanet-lite; `…/org/ole/planet/myplanet/` with
   `ui/`, `repository/` and `services/` under it, and a Groovy
   `app/build.gradle` → myplanet.

**myplanet and myplanet-lite are easy to confuse and the packs are not
interchangeable.** Both are Kotlin/Android under `org.ole.planet.myplanet`; lite
adds one path segment. Getting it wrong hands lite myplanet's directory-keyed
scope table, which matches none of its paths, and a `*ViewModel` gerund rule for
classes that do not exist in it. Check the `lite` segment before you commit to a
pack.

**If none of them match a pack**, say so before you start — do not silently
apply another repo's scope table, which is the one part of this skill that
does not transfer. Fall back to the shared grammar below plus the repo's own
log, and derive its scope table on the spot:

```
git log --format=%s -300 | grep -oE '^[a-z0-9-]+:' | sort | uniq -c | sort -rn
```

Then offer to add a pack for that repo.

## The grammar

Three shapes cover the logs. All lowercase, no trailing period, no
conventional-commit types (`feat:`, `fix:`, `refactor:` never appear).

| Shape | When | myplanet | planet |
|---|---|---|---|
| `<scope>: smoother <noun phrase> <gerund> (fixes #N)` | Anything that improves, fixes, adds, or reworks | 454/500 | 456/500 |
| `<scope>: less <noun phrase> is more (fixes #N)` | A named thing *ceases to exist* | 38/500 | 33/500 |
| ``<scope>: bump `<coordinate>` to <version> (fixes #N)`` | Dependency version bumps only — `all:` for language/framework coordinates, the CI scope for workflow actions | 8/500 | 10/500 |

myplanet-lite has no column because it has no house-style log yet — running this
skill there **establishes** the style rather than matching it. Its pack covers
what that changes.

**`smoother` is the default and it isn't close — around 90% of titles in both
repos with a log to measure.** Reach for it unless you can point at the specific class, method, file,
layout, or feature that is gone after the change. A net-negative diff is *not*
the signal: a refactor that restructures code into a tidier shape deletes plenty
of lines and is still `smoother`. Ask what the PR is *for*. If its purpose is
"get rid of X", use `less`; if its purpose is "make X work better" and deletion
is a side effect, use `smoother`.

There is a tell in the other direction: a draft ending in `removing`, `cleanup`
or `encapsulation` is usually a `less … is more` title wearing `smoother`.
Re-read the diff before switching — one such draft was really about its tests.

Worked failure (myplanet, but the trap is general): a PR converting
`LoginSyncManager.login` to a `suspend` function was 89 additions against 106
deletions, and stripped a dozen `withContext(dispatcherProvider.main)` wrappers.
Net-negative, lots of removal — so `less login sync main dispatcher is more`
looked right. It wasn't. Nothing named ceased to exist; the login path was
restructured. The correct title was `sync: smoother login auth utils managing`.

Never type the trailing `(#<pr>)` you see in the git log — GitHub appends that
at squash-merge time. The PR title stops after `(fixes #N)`.

`(fixes #N)` goes in the **title** — that is what makes the log traceable, since
the squash commit subject is the PR title. It is not what closes the issue:
**GitHub reads closing keywords from the PR description only**, and not from the
squash subject it synthesises out of the title, which is the trap. So the title
stamp gets mirrored into the body as `Fixes #N`. Both, every time.

Get the title spelling exact: lowercase `fixes`, a space, `#`, the number,
wrapped in round parens. Real typos in the logs (`{fixes #14889)`, `(fixes
14801)` and `(fixes 9105)` with no `#`, `(fixes: #9423)` with a stray colon)
broke even the cosmetic link.

planet also uses `(connects #N)` for work that advances an issue without closing
it; myplanet does not. See its pack.

## Choosing the scope

Both repos share the same principle and the same default. `all:` is the
workhorse in each — the right choice whenever the change reaches shared layers
or spans more than one feature. Reach for a feature scope only when the change
sits squarely inside one domain, including that domain's own data layer.

When torn between a feature scope and `all:`, look at where the **centre of
gravity** of the diff sits. One feature's files alone → that feature; the same
change plus a shared-layer tweak → `all:`.

**Which directories map to which scope is entirely repo-specific.** Take the
table from the pack. planet's `manager:` and `community:` do not exist on
myplanet; myplanet's `sync:` does not exist on planet; `life:` covers different
ground in each. Each pack also lists its own traps — directories claimed by more
than one scope, and scopes that have been renamed.

**The vocabulary is closed.** Inventing a scope out of the feature or layer word
in front of you is the most common way to get a title wrong; that word belongs
in the noun phrase, and when nothing in the table fits the answer is the pack's
default (`all:` in both repos). Each pack lists the ones people reach for.

## Building the phrase — read it off the diff, not the old title

The single most important shared rule: **the changed files are the primary input
to the title, and the old title is not.** Its only job is to become the issue
title. Agent-written titles in particular are consistently vaguer than their
diffs — on myplanet, over half of landed titles share no content word at all
with the title the PR arrived with. You are re-deriving, not editing.

Beyond that the two repos diverge, and this is where using the wrong pack does
the most damage:

- **The Kotlin repos are mechanical.** The noun phrase is the principal changed
  file, de-CamelCased and lowercased with its role suffix dropped; the gerund
  comes from that suffix (`*Adapter` → diffing or binding, `*Manager` →
  managing). There is a full suffix table in myplanet's pack, and myplanet-lite
  amends four rows of it — including deleting `*ViewModel`, myplanet's single
  most common gerund, because lite has no such classes.
- **planet is descriptive.** Angular's `.component.ts` / `.service.ts` suffixes
  are thrown away — `component` appears as a noun 3 times in 500 titles. The
  path supplies the feature words and the rest of the phrase names what a user
  would notice changing.

What holds in both:

- When the diff spans two or three areas, the noun phrase **walks across all of
  them** — each contributes a word or two, in diff order — and only the gerund is
  picked, from whichever part best describes the change. Don't pick one file and
  drop the rest; that loses the information the title exists to carry.
- Prefer the **layer or concept word** over the entity name. The domain is
  already carried by the scope plus one feature word, so repeating the entity is
  noise.
- **Keep it a bare chain of nouns.** No prepositions, articles, `and`, commas or
  hyphenated compounds — outside the `bump` shape, near-zero titles in either log
  have any. `courses: smoother filtered-course sort without per-item lowercase`
  is a draft; `courses: smoother repository sorting` is a title.
- Aim for **one to three words between the scope and the gerund**, median two in
  both logs. `all: smoother importing` is fine when the change genuinely is that
  broad; padding a narrow change with words it doesn't need is worse than being
  terse.
- Near-duplicates are fine and common. The qualifier and the issue number
  distinguish them; picking a less accurate word to look novel is the worse
  trade.
- For the `less … is more` shape, the noun phrase names **the thing being
  removed**, not what remains: deleting `PagerAdapterDiffUtils` gives `all: less
  pager adapter diff utils is more`.
- Era vocabulary is fine. Titles name what the diff touches *today*; don't sand
  off project-phase words.

## Finding or creating the issue

This is the half that's easy to get wrong, because the right move depends on who
opened the PR. The mechanics are the same everywhere; what differs is how often
each branch fires. On myplanet most PRs are agent-opened, and most of those were
dispatched *from* an existing issue. On myplanet-lite no PR has an issue — not
one of the last 200 titles links one — so the create-an-issue branch is the
normal path there.

**A human contributor's PR usually already has an issue.** They filed it first,
and it shows up in one of three places — check all three before concluding there
isn't one:

1. `(fixes #N)` already in the title
2. `fixes #N` / `closes #N` / `resolves #N` in the body
3. The branch name, which GitHub's "create branch from issue" button formats as
   `<N>-slug` — e.g. `14932-task-deadline-notifications-silently-overwrite-each-other`

If you find a number, reuse it. Confirm it's a real open issue **in this repo**
rather than a stale or cross-repo reference before you build the title around
it. myplanet and planet issue numbers are in overlapping ranges, so a number
copied from the sibling repo will look plausible and resolve to the wrong thing.

**An agent-generated PR may have none.** Jules, OpenHands, Copilot, Codex and
similar bots open PRs directly, with descriptive prose titles like `Refactor:
Consolidate duplicate EntryPoints`. Branch names give them away: a task-id
suffix (`consolidate-entrypoints-1618928943660463448`) or an agent prefix
(`openhands/…`, `jules-…`, `claude/…`, `codex/…`). Check the three places above
anyway: an agent dispatched from an issue quotes its number somewhere, and on
myplanet that is the common case.

When there really is none, create the issue — and this is the key move: **the
PR's current title becomes the issue title, verbatim.** That descriptive title
is a perfectly good issue title and a poor commit subject, so it gets promoted
rather than discarded. Nothing is lost when the PR title is then rewritten into
house style.

```
before  PR #15048  "Refactor: Consolidate duplicate EntryPoints"      (no issue)
        ↓ create issue #15143 titled "Refactor: Consolidate duplicate EntryPoints"
after   PR #15048  "all: less network dependencies entry point is more (fixes #15143)"
```

Give the new issue a body describing the problem the PR solves — the PR's own
description is the natural source. Don't paste the bot's automation footer or a
CodeRabbit summary into it.

Because the issue is created after the PR, its number will be *higher* than the
PR number. That's expected and common in both repos; it is not a sign you picked
the wrong number.

Then write `Fixes #N` into the PR body as its own last line — that, not the
title, is what closes the issue on merge. Skip it when the body already links
**that** number with a closing keyword, so re-running the prep pass doesn't
stack duplicate lines; anchor the number, since `Fixes #1234` does not link
`#123` and a bare `#123` with no keyword links nothing.

## Procedure

1. **Identify the repo and load its pack** (step 0). If the repo has no pack,
   say so and fall back as described there.
2. Identify the PR. If the user gave a number, use it. Otherwise find the PR for
   the current branch (`mcp__github__list_pull_requests` with `head`).
3. Read it: `mcp__github__pull_request_read` with `method: "get"` for title,
   body, branch and author, then `method: "get_files"` — **the file list is the
   primary input to the title**.
4. Hunt for an existing issue in the three places above. Verify any hit with
   `mcp__github__issue_read`, and check it belongs to this repo.
5. If there is none, create one with `mcp__github__issue_write`
   (`method: "create"`) using the PR's current title.
6. Compose the title using the pack's scope table and phrase mechanics. Skim the
   pack's `title-corpus.md` for the nearest precedent — matching an existing
   line beats inventing a phrasing. When the diff leaves a real choice open,
   present **two to four candidate titles** with the AskUserQuestion tool, the
   diff-derived favourite first and marked "(Recommended)", varying only the
   genuinely open axes — one candidate per plausible value:
   - **scope** — torn between a feature scope and `all:`, or in one of the
     pack's named border zones: offer both
   - **gerund** — where the pack lists a pair (myplanet's `diffing`/`binding`
     and `flowing`/`collecting`; planet's `handling` versus a sharper operation
     word): offer both
   - **shape** — a borderline removal: offer the `less … is more` form as an
     alternate

   Never vary the noun-phrase mechanics or the `(fixes #N)` — those aren't
   choices. When nothing is genuinely open, skip the menu and use the single
   title.
7. Apply it with `mcp__github__update_pull_request`.
8. Append `Fixes #N` to the body in the same call, unless it already links that
   number. Without it the issue stays open when the PR merges.
9. Check the version bump the pack names (`app/build.gradle` on myplanet,
   `app/build.gradle.kts` on myplanet-lite, `package.json` on planet) and
   mention it if the PR touches app code without bumping it.
10. Report the before/after title and the issue number, saying which pack you
    used, whether you reused an existing issue or opened a new one, and that the
    body now links it (or already did).

Step 5 creates a public issue and steps 7-8 rewrite someone's PR title and body.
All of it is visible to the whole project, so when the PR isn't the user's own,
show the proposed title, issue and body line first and get a nod before writing.

## Adding a repo

To teach this skill another repo, add `references/<repo>/conventions.md` and
`references/<repo>/title-corpus.md`, then add a row to the table in step 0.
Nothing else in this file should need to change — if it does, the thing you are
writing is probably shared grammar and belongs here rather than in the pack.

**If the new repo is a sibling of one already covered** — same language, same
class-naming idiom — write a *borrowing* pack instead: name the corpus and
conventions it inherits, then override only what differs, as
`references/myplanet-lite/` does. Resist the urge to copy the parent pack and
edit it; a borrowing pack that stays thin makes the differences legible, and a
fix to the parent's mechanics reaches both.

Be honest about what actually differs before you borrow. Two Kotlin/Android apps
still diverged on scopes, four suffix rows and the version-bump file, and one of
those — a `*ViewModel` rule for a codebase with no view models — would have
produced confidently wrong titles on every PR.

Build the corpus from the repo's own log: pair each squash-merged title with the
files that produced it, strip the trailing `(#NNNN)` GitHub appends, group by
scope, and note the per-PR version-bump file so it can be omitted. Then read the
result and write `conventions.md` from what you actually see — scope league
table, how the noun phrase is derived, the gerund vocabulary, and any point
where the log changed its mind about a convention partway through the window.

On a squash-merged repo, go one step further and recover what those titles
looked like *before* they were prepped: GitHub keeps `refs/pull/<n>/head` after
the merge, so the draft-versus-landed pairs are still there. myplanet's corpus
has the method and what it turned up.
