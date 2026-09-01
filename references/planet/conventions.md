# planet — reference pack

`open-learning-exchange/planet`. Angular / TypeScript, npm, sources under
`src/app/`, with `chatapi/`, `gateway/`, `design/` and `docker/` alongside.

Read this together with the shared grammar in `SKILL.md`. The shapes, the
`smoother` default and the `(fixes #N)` rules are identical to myplanet's and
live in `SKILL.md`; everything here is what planet does differently.

Corpus: `references/planet/title-corpus.md` (last 500 merged PRs).

## The one big divergence from myplanet

**myplanet reads the noun phrase off the filenames. planet reads it off the
screen.**

myplanet's Kotlin classes carry role suffixes (`*ViewModel`, `*Adapter`,
`*Manager`) and its titles convert them mechanically. Angular's do too —
`.component.ts`, `.service.ts`, `.directive.ts` — but planet's log **throws them
away**. Across 500 titles, `component` appears as a noun 3 times, `service` 2,
and `directive`, `pipe` and `guard` zero. There is no suffix→gerund table here.

Instead the noun phrase names **the feature and the thing on screen that
changed**, and the gerund names **the operation or the CSS concern**:

```
home/home.component.html                        → all: smoother user profile language handling
users/users-update/users-update.component.html  → all: smoother profile picture uploading
resources/view-resources/resources-viewer.*     → resources: smoother viewer fullscreen button handling
teams/teams-reports.* + teams-view-finances.*   → teams: smoother finances reports buttons hovering
surveys/surveys.component.{html,scss,ts}        → teams: smoother surveys button resizing
manager-dashboard/reports/reports-detail.scss   → manager: less reports chart button top margin is more
```

Note the third and fourth: the file path supplies the *feature* words
(`viewer`, `finances`, `reports`), and the rest of the phrase — `fullscreen
button`, `buttons` — comes from reading the diff and asking what a user would
notice. Don't write `resources: smoother resources viewer component handling`.

The myplanet rules that still apply unchanged: walk the phrase across every
changed area rather than picking one file, aim for three to five words between
the scope and the gerund, and for `less … is more` name the thing being removed
(`teams: less submissions service import is more`).

## Scopes

`all:` is the workhorse (138/500) — the right default whenever the change
reaches `src/app/shared/`, `src/app/users/`, `src/i18n/`, `src/styles.scss`,
`src/app/_variables.scss` / `_mixins.scss`, root docs and config, or spans more
than one feature.

| Scope | Owns | Share |
|---|---|---|
| `teams` | `teams/`, `surveys/`, `meetups/`, `tasks/`; `exams/` when the artefact is a **survey** | 93 |
| `manager` | `manager-dashboard/**` — `reports/`, `certifications/`, `requests/`, `configuration/`, plus `design/` docs | 80 |
| `courses` | `courses/`; `exams/` when the artefact is an **exam or quiz**; course `submissions/` | 53 |
| `community` | `community/`, `news/` (the community voices feed) | 29 |
| `dashboard` | `dashboard/`, `home/` tiles | 25 |
| `actions` | `.github/workflows/`, `docker/`, `gateway/`, `scripts/`, `couchdb-setup.sh` | 21 |
| `chat` | `chat/`, `chatapi/` | 18 |
| `resources` | `resources/` | 16 |
| `login` | `login/`, the install/configuration screens | 12 |
| `life` | `health/`, `users/` achievements and certifications | 8 |
| `enterprises` | rare — enterprise finances | 1 |

Same centre-of-gravity test as myplanet: a change confined to
`manager-dashboard/reports/` is `manager:`; the same change plus a
`shared/forms/` tweak is `all:`.

**`life` was called `mylife`.** The rename landed around the turn of 2026 — the
last `mylife:` title is 2025-11-26, the first `life:` is 2026-01-29. Write
`life:`. `mylife:` in the corpus is legacy, not a live alternative.

**planet has no `sync:` scope, no `feedback:` scope and no `notifications:`
scope** — the myplanet table's `sync`, and the `ui/notifications` trap, have no
counterpart here. Feedback and notifications work lands under `all:`.

**Three shared-ish directories to be careful with.** `exams/`, `submissions/`
and `news/` are each claimed by more than one scope, and in the last 300
commits the most common answer for all three is `all:` — because a diff big
enough to touch them usually touches something else too. Decide by what the
change is *for*, not by the directory:

| Directory | `all:` | Otherwise |
|---|---|---|
| `exams/` | 17 | `courses:` 8 (exams), `teams:` 7 (surveys) |
| `submissions/` | 14 | `teams:` 7, `manager:` 3, `courses:` 3 |
| `news/` | 12 | `teams:` 6 (team voices) — `community:` for the public feed |

## Gerunds

**`handling` is the dominant fallback and it is not close — 86 of 456
`smoother` titles, roughly one in five.** myplanet reserves `handling` for
Fragments and Activities with no sharper word; planet reaches for it whenever
the change is "this UI now behaves properly" and no more specific operation
fits. Don't strain for a novel gerund; `handling` is idiomatic here.

After that the league table is long and flat:

> filtering 10 · aligning 10 · loading 9 · formatting 8 · styling 7 ·
> navigating 7 · paginating 7 · linking 7 · creating 7 · building 7 ·
> selecting 5 · showing 5 · padding 4 · viewing 4 · linting 4 · testing 4 ·
> spacing 4 · reporting 4 · routing 4 · validating 4 · uploading 3 ·
> exporting 3 · translating 3 · sorting 3 · downloading 3 · counting 3

### The CSS family

Roughly a fifth of planet's PRs are `.scss`-only, and they have their own
vocabulary that myplanet has no use for. Pick the gerund from the property
being adjusted, and the noun phrase from the element:

| The diff adjusts | Gerund |
|---|---|
| general appearance, a theme, a Material density | styling |
| `margin` / `padding` | padding, spacing |
| `width` / `height` / `font-size` | sizing, resizing |
| flex/grid placement, icon position | aligning, placing |
| `:hover` state | hovering |
| number/date/text presentation | formatting |
| a colour | coloring |

```
teams/teams-view-finances.scss          → teams: smoother finances date button size handling
surveys/surveys.component.scss          → teams: smoother surveys question options spacing
dashboard/dashboard.scss (grid removed) → dashboard: less grid is more
src/styles.scss                         → all: smoother letter spacing
```

### `.spec.ts` does not get `testing`

myplanet's rule — a diff touching only `app/src/test/` always ends in `testing`
— has **no planet equivalent**. Angular specs live next to the code they test
and ride along in the same commit; there is not one spec-only PR in the last
500. planet's four `testing` titles are all about the *test harness*
(`.github/workflows/planet.yml`, `karma.conf.js`, `test.ts`), which is why one
of them is scoped `actions:`.

### Titles older than 2025-10-14 have no gerund at all

Before mid-October 2025 planet titles stopped at a bare noun phrase — `manager:
smoother survey list`, `community: smoother voices`, `teams: smoother finances
loading message`. 25 of 162; after the changeover, 287 of 294 carry a gerund.
The corpus marks the boundary inside each scope section. Take scope and
noun-phrase precedent from either half, but take the **ending** only from the
recent one, and always write a gerund.

## `connects` as well as `fixes`

planet uses `(connects #N)` — 21 of 500 — for work that advances a tracking
issue without closing it, typically one PR in a multi-PR campaign. myplanet's
log has no equivalent. Default to `(fixes #N)`; use `connects` only when the
issue explicitly stays open after this PR merges, and say so when you propose
the title.

`closes #N` appears twice and is not house style — don't reach for it.

It follows that a `connects` title gets no `Fixes #N` line in the PR body: that
line is what actually closes an issue, and this shape exists to keep one open.

## Dependency bumps

planet bumps frameworks and the app itself, not Gradle coordinates. Backtick
the package or framework name:

> `` all: bump `angular` to 20 (fixes #9926) ``
> `` all: bump `planet` to 0.20.75 (fixes #9317) ``
> `` all: bump `ramda` to 0.29.0 ``

## Version bump to check

Every merged PR bumps the `version` field in `package.json` — it is present in
essentially every diff in the corpus, which is why the corpus omits it. If the
PR touches app code and doesn't bump it, mention it. Read the current value off
`master` rather than the branch, since a stale branch will have drifted behind.

Note `package-lock.json` moves with it; a PR that bumps `package.json` and not
the lockfile is worth flagging too.

## Worked examples

**Multi-area UI fix.** Diff touches `teams/teams-reports.component.{html,ts}`
and `teams/teams-view-finances.component.{html,ts}`. Confined to `teams/`, so
`teams:`. Two features contribute words — finances and reports — and the change
is to `:hover` on buttons.

> `teams: smoother finances reports buttons hovering (fixes #10190)`

**One template, broad subject.** Diff is a single file,
`home/home.component.html`. `home/` is shared surface, so `all:`, and the
filename contributes nothing to the phrase — the subject is the profile
language selector.

> `all: smoother user profile language handling (fixes #10157)`

**Style-only removal.** Diff is `dashboard/dashboard.scss` and it drops a grid
layout. A named thing ceases to exist, so the `less` shape.

> `dashboard: less grid is more (fixes #10084)`

**Sweep across the app.** Diff touches 30 files across `chat/`, `community/`,
`dashboard/`, `exams/`, `login/`, `manager-dashboard/`, `news/`, `shared/`,
`teams/`, `upgrade/`, `users/`, plus `_variables.scss` and `styles.scss`. Far
past any one feature, so `all:`, and the subject is the SCSS variables
themselves.

> `all: smoother system variables handling (fixes #10057)`

**Agent PR, no issue.** Same procedure as myplanet: promote the PR's
descriptive title to a new issue verbatim, then rewrite the PR title from the
diff.
