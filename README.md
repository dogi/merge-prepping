# prepping — Claude Code plugin marketplace

A personal marketplace hosting `merge-prepping`: a PR title rewriter and
tracking-issue enforcer for the Open Learning Exchange house style. Maintain the
skill here once; opt any project into it — including **Claude Code on the web /
cloud** sessions.

The skill is **repo-dependent**. The grammar is shared across OLE repos, but the
scope table, the way the noun phrase comes off the diff, the gerund vocabulary
and the per-PR version-bump file are not — so each repo gets its own reference
pack and the skill picks one at step 0.

| Repo | Pack | Corpus | Stack |
|---|---|---|---|
| `open-learning-exchange/myplanet` | `references/myplanet/` | its own | Kotlin / Android |
| `open-learning-exchange/planet` | `references/planet/` | its own | Angular / TypeScript |
| `open-learning-exchange/myplanet-lite` | `references/myplanet-lite/` | borrows myplanet's | Kotlin / Android |

## Structure

```
SKILL.md                                 # shared grammar, pack selection, procedure
references/
├── myplanet/
│   ├── conventions.md                   # scopes, suffix→gerund mechanics, version bump
│   └── title-corpus.md                  # 500 past titles + the files that produced them
├── myplanet-lite/
│   └── conventions.md                   # borrowing pack: myplanet's corpus + the deltas
└── planet/
    ├── conventions.md
    └── title-corpus.md                   # 500 landed titles + their files
scripts/
└── build-corpus.py                      # regenerates a title-corpus.md from a repo's log
.claude-plugin/marketplace.json          # marketplace catalog
plugins/merge-prepping/
├── .claude-plugin/plugin.json           # plugin manifest
└── skills/prepping/
    ├── SKILL.md      -> ../../../../SKILL.md
    └── references    -> ../../../../references
```

The repo root doubles as a skill directory so it works when mounted as a git
submodule (planet does this at `.agents/skills/merge-prepping/`); the two
symlinks under `plugins/` project the same files onto Claude Code's plugin path.

⚠️ **Those symlinks need `core.symlinks=true`.** Where Git runs without it —
Windows outside Developer Mode — the checkout writes them as plain files
containing the target path, and a loader will read the literal string
`../../../../SKILL.md` as the skill body instead of failing loudly. Check with
`git config core.symlinks` and `test -L plugins/merge-prepping/skills/prepping/SKILL.md`.

## How the skill picks a pack

In order: the `owner/repo` of the PR it was handed → `git remote get-url origin`
→ a fingerprint of the checkout (`angular.json` + `src/app/` → planet; the
`lite` package segment + `build.gradle.kts` → myplanet-lite; otherwise
myplanet).

If none match, it says so up front rather than silently applying another repo's
scope table, falls back to the shared grammar plus the repo's own `git log`, and
offers to add a pack.

## Adding a repo

1. Generate the corpus from that repo's log:

   ```
   scripts/build-corpus.py --repo ~/src/<repo> --name <repo> \
       --strip <source root>/ --skip <version bump file> \
       > references/<repo>/title-corpus.md
   ```

   It pairs each merged title with the files that produced it, groups by scope,
   and prints the shape / scope / gerund league tables — plus a warning if the
   log changed its mind about a convention partway through the window, which
   planet's did in October 2025.

2. Read the last ~50 PRs' "changed the title" timelines. The landed log records
   only the answers; the edits that got there are where the sharper rules are.
3. Write `references/<repo>/conventions.md` from all of that — from what you
   actually see, not from what the other packs say.
4. Add a row to the table in step 0 of `SKILL.md`.

Nothing else in `SKILL.md` should need to change. If it does, what you are
writing is probably shared grammar and belongs there rather than in the pack.

**For a sibling of a repo already covered**, write a *borrowing* pack instead —
name the corpus and conventions it inherits, override only the deltas, and skip
the corpus entirely. `references/myplanet-lite/` is the worked example: two
Kotlin/Android apps sharing all the phrase mechanics, differing on scopes, four
suffix rows and the version-bump file. Keeping it thin means a fix to myplanet's
mechanics reaches both.

## Hosting

This marketplace is hosted at `dogi/merge-prepping`. The
`.claude-plugin/marketplace.json` catalog lives at the repo root so Claude Code
can discover it when the repo is added as a marketplace.

## Use it in the terminal (CLI)

```
/plugin marketplace add dogi/merge-prepping
/plugin install merge-prepping@prepping
/reload-plugins
```

Then invoke: `/merge-prepping:prepping` (or just ask to "prep this PR" / "fix
the title" — the description auto-triggers it).

## Use it on Claude Code web / cloud

Cloud sessions can't see your local `~/.claude`, and user-scoped `enabledPlugins`
does **not** carry over. Declare the marketplace + plugin in the target repo's
`.claude/settings.json` (this file is part of the clone, so the cloud VM installs
the plugin at session start — needs network access to GitHub, which the default
allowlist covers):

```json
{
  "extraKnownMarketplaces": {
    "prepping": {
      "source": {
        "source": "github",
        "repo": "dogi/merge-prepping"
      }
    }
  },
  "enabledPlugins": {
    "merge-prepping@prepping": true
  }
}
```

Commit that to each repo where you want the skill available in web sessions.
The skill itself stays maintained here — bump `version` in `plugin.json` on each
release so installs pick up updates.

## What the skill does

Turns an arbitrary PR title into the shape every commit on the default branch
already has:

```
<scope>: smoother <noun phrase> <gerund> (fixes #N)
<scope>: less <noun phrase> is more (fixes #N)
<scope>: bump `<coordinate>` to <version> (fixes #N)
```

It picks the scope from where the diff's centre of gravity sits, walks the noun
phrase across every changed area, and reads all of that off the file list rather
than the old title. The old title has one job: becoming the issue title when the
PR arrived without an issue, which is the usual case for Jules- and
Copilot-opened PRs. Human PRs normally already have a number in the title, the
body, or the `<N>-slug` branch name.

`(fixes #N)` goes in the title **and** `Fixes #N` in the body: the title keeps
the log traceable, the body is the only place GitHub reads the link from.

Where the repos differ — and why the packs exist:

|  | myplanet | planet | myplanet-lite |
|---|---|---|---|
| Noun phrase | mechanical, off the filenames | descriptive, off the screen (`component` is a noun 3× in 500 titles) | mechanical, as myplanet |
| Scoped by | directory (`ui/teams/`, `services/sync/`) | directory (`src/app/*/`) | **class-name prefix** — the tree is flat |
| Fallback gerund | `handling` for Fragments/Activities, 27/500 | `handling` for anything, 86/500 | as myplanet |
| Top suffix | `*ViewModel` → view modelling, 40/500 | suffixes discarded | `*Extensions`, 32 files — takes **no** gerund; **zero** view models exist |
| Test diffs | `app/src/test/`-only always ends in `testing` | no spec-only PRs exist; specs ride along | as myplanet, plus `androidTest/` |
| Style diffs | rare | ~a fifth of PRs; own vocabulary (`aligning`, `spacing`, `padding`) | rare |
| Issue link | `fixes` only | `fixes`, plus `connects` when the issue stays open (title only) | none practised yet — expect to open one per PR |
| Version bump | `app/build.gradle` | `package.json` | `app/build.gradle.kts` |
| Scopes absent | — | `sync` | `life`, `chat`, `community`, `enterprises`, `feedback` |

myplanet-lite has **no house style in its log at all** — zero of the last 200
titles link an issue, and they read like `🧹 [Code Health] Refactor
loadNextCoursesPage in DashboardCoursePageActions (#1178)`. Running the skill
there establishes the style rather than matching it, which its pack spells out.
