# planet — reference pack

`open-learning-exchange/planet`. Angular / TypeScript, npm, sources under
`src/app/`, with `chatapi/`, `gateway/`, `design/` and `docker/` alongside.

Read this together with the shared grammar in `SKILL.md`. The shapes, the
`smoother` default and the `(fixes #N)` rules are identical to myplanet's and
live in `SKILL.md`; everything here is what planet does differently.

Corpus: `title-corpus.md`, the last 500 **landed** titles with the files that
produced them — skim it for precedent.

The landed log only shows the answers, so the rules below were also read off the
*edit history* of the 51 most recent merges (#10169 … #10363) — every "changed
the title" event from first draft to merge. That is where the rejected phrasings
are, and the before → after pairs quoted throughout come from there.

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
changed area rather than picking one file, and for `less … is more` name the
thing being removed (`teams: less submissions service import is more`).

## Two passes: write it, then cut a word

**This is the thing the landed corpus cannot show you.** Of the 51 most recent
merges, 50 were retitled and **38 were retitled twice or more** — because a
correct house-style title is usually still one word too long. Pass one puts it
in shape; pass two deletes something. Do both before you propose a title.

Length is the measure. Counting the gerund, the landed phrase between `smoother`
and the stamp runs 2 words 18 · **3 words 44 · 4 words 30** · 5 words 2 over the
last hundred. So **three or four words including the gerund**, not the "three to
five" the shared grammar suggests. Longer than that and pass two isn't optional.

Four kinds of word come out, one example each:

| What goes | Example |
|---|---|
| the widget noun the gerund already implies — `dialog`, `badge`, `chip`, `tooltip`, `indicator`, `prompt`, `asterisk`, `accordion`, `suite`, `attachment` | `calendar task dialog closing` → `calendar task closing` |
| the generic adjective — `long`, `text`, `archived`, `unsaved`, `single day`, and `actions` when it just means "buttons" | `archived surveys adopt view filtering` → `surveys adopt view filtering` |
| the scope echo | `teams: smoother team names …` → `names …` |
| one half of an `and` clause — cut to one subject, never joined | `no var and object shorthand linting` → `object shorthand linting` |

Two refinements on that. A word that could describe *any* PR is not deleted but
**swapped for a locating word**: `responsive table column sizing` → `requests
table column sizing`. And when dropping the scope echo frees a slot, spend it on
a *new* word rather than putting the echo back: `resource year validating` →
`year validating` → `creation year validating`.

Three more habits, same source:

- **Lead with the feature noun, qualify after it** — `unread notifications
  indicator` → `notifications unread indicator`. The word a user would search
  for goes first.
- **Say what works, not what is prevented** — `feedback forms unsaved changes
  handling` → `feedback forms saving`. Where a negative must survive it is
  spelled `less`, never `no`.
- **Code identifiers become plain words** — `arrow-body-style` → `arrow body
  style`, `.coderabbit.yaml` → `coderabbit`.

### The author's verb is your gerund

Almost every unprepped title opens with an imperative. It is not noise — it is
the ending, in the wrong place and the wrong form. `add`/`display`/`show` →
`showing` or a verbed domain noun; `fix` → the gerund of whatever was broken;
`enable`/`restore` → the gerund of the thing enabled or restored;
`readd`/`reenable` a lint rule → `linting`; `improve`/`standardize`/`centralize`
→ `smoother` plus the noun's own verb; `prevent`/`restrict`/`exclude` →
`validating` or `filtering`; `confirm` → `confirming`.

## Scopes

`all:` is the workhorse (148/500, 35/100) — the right default whenever the change
reaches `src/app/shared/`, `src/app/users/`, `src/i18n/`, `src/styles.scss`,
`src/app/_variables.scss` / `_mixins.scss`, root docs and config, or spans more
than one feature.

The `/500` column is the whole corpus; `/100` is the last hundred merges, which
is the better guide to what the maintainers are choosing today.

| Scope | Owns | /500 | /100 |
|---|---|---|---|
| `teams` | `teams/`, `surveys/`, `meetups/`, `tasks/`; `exams/` when the artefact is a **survey** | 91 | 28 |
| `manager` | `manager-dashboard/**` — `reports/`, `certifications/`, `requests/`, `configuration/`, plus `design/` docs | 72 | 3 |
| `courses` | `courses/`; `exams/` when the artefact is an **exam or quiz**; course `submissions/` | 57 | 9 |
| `community` | `community/`, `news/` (the community voices feed) | 25 | 0 |
| `dashboard` | `dashboard/`, `home/` tiles, the profile page's own chrome | 22 | 5 |
| `actions` | `.github/workflows/`, `docker/`, `gateway/`, `scripts/`, `couchdb-setup.sh`, `.coderabbit.yaml` | 20 | 5 |
| `resources` | `resources/` | 20 | 8 |
| `chat` | `chat/`, `chatapi/` | 16 | 0 |
| `life` | `health/`, `users/` achievements and certifications | 12 | 5 |
| `login` | `login/`, the install/configuration screens | 10 | 0 |
| `enterprises` | enterprise finances, rules and joining | 3 | 2 |

`community:`, `chat:` and `login:` score zero in the last hundred. They are
still live scopes — nothing has been renamed — but there simply has not been
work there lately, so don't read their absence as a signal either way.

**`enterprises:` is small but real, and it beats `teams:`.** Two of the last
fifty landed there and both were moved off `teams:` (#10302, #10155). If the
change is about an enterprise's own money, rules or membership, it is
`enterprises:`, not `teams:`.

### Directory names that are not scopes

The most-corrected field in the whole title is the scope, and the failure is
always the same: the author names the directory they edited. **26 of the last 51
merges needed a different scope word than the one written** — 23 wrong or
non-existent, 3 with none at all. These get rewritten every time:

| Written | Should be |
|---|---|
| `collections:`, `forms:`, `home:`, `notification:`, `notifications:` | `all:` |
| `meetups:`, `surveys:`, `tasks:` | `teams:` |
| `submissions:`, `exams:` | `courses:` (or `teams:` for surveys) |
| `reports:` | `enterprises:` if enterprise finances, else `manager:` |
| `health:`, `myhealth:` | `life:` |
| `ci:` | `actions:` |
| `users:` | see below |

**`users/` has no single answer** — it went three ways in three consecutive PRs,
decided by the screen rather than the directory: profile-page chrome →
`dashboard:` (#10291), member administration → `all:` (#10293), achievements →
`life:` (#10234). Across the last 150 merges `users/` most often lands in `all:`
(21), so that is the fallback.

Same centre-of-gravity test as myplanet: a change confined to
`manager-dashboard/reports/` is `manager:`; the same change plus a
`shared/forms/` tweak is `all:`.

**`life` was called `mylife`.** The rename landed around the turn of 2026 — the
last `mylife:` title is 2025-11-26, the first `life:` is 2026-01-29. Write
`life:`. `mylife:` in the corpus is legacy, not a live alternative.

**planet has no `sync:` scope, no `feedback:` scope and no `notifications:`
scope** — the myplanet table's `sync`, and the `ui/notifications` trap, have no
counterpart here. Feedback and notifications work lands under `all:`.

**Four shared-ish directories to be careful with.** `exams/`, `submissions/`,
`news/` and `home/` are each claimed by more than one scope, and in the last 150
merges the most common answer for all of them is `all:` — because a diff big
enough to touch them usually touches something else too. Decide by what the
change is *for*, not by the directory:

| Directory | `all:` | Otherwise (last 150 merges) |
|---|---|---|
| `exams/` | 8 | `teams:` 5 (surveys), `courses:` 4 (exams and quizzes) |
| `submissions/` | 7 | `teams:` 3, `resources:` 3, `courses:` 1, `manager:` 1 |
| `news/` | 8 | `teams:` 2 (team voices) — `community:` for the public feed |
| `home/` | 13 | `teams:` 2 — `dashboard:` only when the change is a tile |

## Gerunds

**`handling` is being retired, and this is the single biggest change in recent
practice.** It is 91 of 458 `smoother` titles across the corpus — but only **4
of the last 50**. Reading the corpus alone will talk you into it; don't let it.

The reason is visible in the edit history: `handling` is what the *first* draft
of a corrected title ends in, and the maintainer's second pass converts it into
a verb made from the noun in front of it — `configuration patch handling` →
`configuration patching`, `join requests badge handling` → `join requests
alerting`, `enterprises rules agreement handling` → `joining`.

**So: before you write `handling`, try verbing the last noun of your phrase.**
planet verbs its own domain vocabulary freely — `shelfing`, `pressuring`,
`joining`, `describing`, `alerting`, `truncating`, `patching` all landed in the
last fifty. A gerund that is not a word outside this product is fine if it is a
word inside it.

`handling` is still correct when nothing sharper is true — `calendar events
handling`, `collection title handling`, `tiles keyboard handling` all landed —
but it is now the ending of last resort rather than the default.

After that the league table is long and flat. Whole corpus:

> navigating 12 · filtering 11 · linting 10 · aligning 10 · formatting 9 ·
> styling 8 · loading 8 · showing 7 · paginating 7 · linking 7 · creating 7 ·
> building 7 · validating 6 · testing 5 · selecting 5 · hovering 4 · padding 4 ·
> viewing 4 · spacing 4 · reporting 4 · routing 4 · removing 3 · confirming 3

The last hundred are flatter still — 53 distinct gerunds across 97 titles, and
33 distinct across the last 50. **Reuse of a gerund is not a goal here.** Where
the shared grammar says near-duplicates are fine, that is about the noun phrase;
the ending is expected to be specific.

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

### `.spec.ts` rarely gets `testing`

myplanet's rule — a diff touching only `app/src/test/` always ends in `testing`
— has **no planet equivalent**. Angular specs live next to the code they test
and ride along in the same commit; there is not one spec-only PR in the last
500, so specs in a diff are usually invisible in the title.

`testing` is reserved for PRs whose *subject* is the tests: the harness
(`.github/workflows/planet.yml`, `vite.config.mts` — the repo runs vitest now,
there is no `karma.conf.js`), which is why one of them is scoped `actions:`, or
a deliberate restoration of a suite. `dashboard: restore unit testing suite` →
`dashboard: smoother unit testing` (#10246) is the pattern for the latter — note
the second pass dropped `suite` and kept `unit`.

### Titles older than 2025-10-14 have no gerund at all

Before mid-October 2025 planet titles stopped at a bare noun phrase — `manager:
smoother survey list`, `community: smoother voices`, `teams: smoother finances
loading message`. 23 of 108; after the changeover, 343 of 350 carry a gerund.
The corpus marks the boundary inside each scope section. Take scope and
noun-phrase precedent from either half, but take the **ending** only from the
recent one, and always write a gerund.

## `connects` as well as `fixes`

planet uses `(connects #N)` — 27 of 500 — for work that advances a tracking
issue without closing it, typically one PR in a multi-PR campaign. myplanet's
log has no equivalent. Default to `(fixes #N)`; use `connects` only when the
issue explicitly stays open after this PR merges, and say so when you propose
the title.

Every one of the 7 in the last hundred belongs to a single campaign — the
per-rule ESLint restoration against #9082 (`all: smoother one var linting`,
`… quote props linting`, `… arrow body style linting`, …). That is what a
`connects` PR looks like here: one narrow slice of a numbered programme of work,
with the umbrella issue staying open until the last slice lands.

It follows that a `connects` title gets no `Fixes #N` line in the PR body: that
line is what actually closes an issue, and this shape exists to keep one open.

`closes #N` appears twice and is not house style — don't reach for it.

**Two issues get two stamps** — `(fixes #10199) (fixes #10200)`, separate
parens with one space, not a comma list inside one pair and not jammed together.
#10203 was corrected through both errors in turn. Mirror both into the body, one
`Fixes #N` line each.

**Lowercase and US-spell everything.** `All:` → `all:`, `Fixes` → `fixes`,
`labelling` → `labeling` were all corrections in the last fifty.

**The issue number in the branch name can be wrong.** #10228 sat on branch
`10227-meetup-single-day-fixes` and was stamped `(fixes #10227)`; the issue it
actually closed was #10223. The branch is a hint, not a source — read the issue
before you trust its number.

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

**A full second pass.** A course title clipped on mobile, in
`dashboard/dashboard-tile.component.{html,scss}`. Every rule in this file shows
up once in its five titles (#10258):

```
dashboard: fix hidden title text on mobile        ← as written
dashboard: smoother tile title overflow handling  ← in shape, 4 words + handling
dashboard: smoother title tile overflowing        ← verbed, still generic
dashboard: smoother course title tile sizing      ← located, one word too many
dashboard: smoother courses title shelfing        ← landed
```

Read it backwards: the widget noun (`tile`) goes once the domain verb
(`shelfing`) implies it, the feature word (`courses`) leads, and the ending is a
planet word rather than `handling`.

**Agent PR, no issue.** Same procedure as myplanet: promote the PR's
descriptive title to a new issue verbatim, then rewrite the PR title from the
diff. In the last fifty these arrive on `claude/<slug>-<hash>` branches with a
conventional-commit prefix (`refactor: extract configuration patching logic and
add comprehensive tests` → `all: smoother configuration patching (fixes
#10341)`, #10337). Strip the prefix, replace the scope, cut the `and` clause,
verb the noun — all four moves, every time.
