---
name: pr-prep
description: Rewrite a pull request title into the myPlanet house style (`scope: smoother thing doing (fixes #N)`) and make sure a tracking issue is attached, creating one from the PR's current title when none exists. Use this whenever preparing, cleaning up, retitling, or getting a PR ready to merge in this repo — including when the user says "prep this PR", "fix the title", "massage the title", "does this need an issue?", or just points at a PR number or branch and asks to tidy it up. Also use it before opening a new PR, so the title is right the first time.
---

# PR prep

Every commit that lands on `master` here reads the same way. That consistency is
the point: the log doubles as a changelog, and every line traces back to an issue.
This skill turns an arbitrary PR title into that form and guarantees the issue link
exists.

## The grammar

Three shapes cover the last 200 commits. All lowercase, no trailing period, no
conventional-commit types (`feat:`, `fix:`, `refactor:` never appear).

| Shape | When | Share |
|---|---|---|
| `<scope>: smoother <noun phrase> <gerund> (fixes #N)` | Anything that improves, fixes, adds, or reworks | 184/200 |
| `<scope>: less <noun phrase> is more (fixes #N)` | A named thing *ceases to exist* | 9/200 |
| `all: bump \`<coordinate>\` to <version> (fixes #N)` | Dependency version bumps only | 6/200 |

**`smoother` is the default and it isn't close — 92% of titles.** Reach for it
unless you can point at the specific class, method, file, layout, or feature that
is gone after the change. A net-negative diff is *not* the signal: a refactor that
restructures code into a tidier shape deletes plenty of lines and is still
`smoother`. Ask what the PR is *for*. If its purpose is "get rid of X", use `less`;
if its purpose is "make X work better" and deletion is a side effect, use `smoother`.

Worked failure: a PR converting `LoginSyncManager.login` to a `suspend` function
was 89 additions against 106 deletions, and stripped a dozen
`withContext(dispatcherProvider.main)` wrappers. Net-negative, lots of removal — so
`less login sync main dispatcher is more` looked right. It wasn't. Nothing named
ceased to exist; the login path was restructured. The correct title was
`sync: smoother login auth utils managing`.

Never type the trailing `(#<pr>)` you see in the git log — GitHub appends that at
squash-merge time. The PR title stops after `(fixes #N)`.

`(fixes #N)` belongs in the **title**, not the body. GitHub only auto-closes from
the body or the commit message, and the squash commit message *is* the PR title —
so putting it in the title is what actually closes the issue on merge. Get the
spelling exact: lowercase `fixes`, a space, `#`, the number, wrapped in round
parens. Real typos in the log (`{fixes #14889)`, `(fixes 14801)` with no `#`)
broke the link and the issue stayed open.

## Choosing the scope

`all:` is the workhorse (59/200) and the right default whenever the change reaches
shared layers — `model/`, `repository/`, `di/`, `base/`, `callback/`, `utils/`,
`data/`, `MainApplication.kt` — or spans more than one feature.

Reach for a feature scope only when the change sits squarely inside one domain,
including that domain's own repository:

| Scope | Owns |
|---|---|
| `teams` | `ui/teams/**`, `ui/voices/`, `ui/events/`, `ui/surveys/`, team tasks |
| `courses` | `ui/courses/`, `ui/exam/`, `ui/submissions/`, `ui/ratings/`, progress, tags |
| `sync` | `services/sync/`, `services/upload/`, `services/retry/`, uploads, downloads |
| `resources` | `ui/resources/`, `ui/viewer/`, webview, media playback |
| `dashboard` | `ui/dashboard/` and the bell — but **not** `ui/notifications/` |
| `chat` | `ui/chat/` |
| `login` | `ui/settings/`, `ui/user/`, onboarding; `ui/sync/` — see below |
| `life` | `ui/health/`, `ui/life/` |
| `community` | `ui/community/` |
| `enterprises` | `ui/enterprises/` |
| `actions` | `.github/workflows/` |

When torn between a feature scope and `all:`, look at where the *centre of gravity*
of the diff sits. A change to `TeamsRepositoryImpl` alone is `teams:`; the same
change plus a shared `RealmRepository` tweak is `all:`.

`ui/notifications/` is a trap: the bell *icon* on the dashboard is `dashboard`, but
the notifications package itself is always `all` — four for four in the log
(`all: smoother notifications text caching`, `all: smoother notification item
sorting`, `all: less notification bell icon list item is more`, `all: smoother view
model scoping`). Notifications are surfaced across the app, not owned by one
screen, which is presumably why.

`ui/sync/` is genuinely ambiguous in the log — `GuestLoginExtensions.kt` has landed
as both `sync: smoother guest login validating` and `login: smoother guest
extensions validating`. Don't agonise: `sync` if the change is about the sync or
login *transaction*, `login` if it's about the screen and what the user sees.
Anything under `services/sync/` is unambiguously `sync`.

## Building the phrase — read it off the diff, not the old title

The title is close to a mechanical function of the files changed. Once you see
that, most titles write themselves:

**The noun phrase is the principal changed file, de-CamelCased and lowercased,
with its role suffix dropped. The gerund comes from that suffix.**

```
ui/dashboard/BellDashboardFragment.kt   → dashboard: smoother bell reminding
services/upload/PhotoUploader.kt        → sync: smoother photo uploading
ui/health/HealthUsersAdapter.kt         → life: smoother health users item callback diffing
ui/health/HealthExaminationAdapter.kt   → life: smoother health examination item callback diffing
utils/DispatcherProvider.kt (+ manager) → sync: smoother upload immediate dispatcher providing
repository/UserRepositoryImpl.kt        → sync: smoother user repository shelf batch uploading
di/NetworkDependenciesEntryPoint.kt ✗   → all: less network dependencies entry point is more
```

This is why the frequency ranking of gerunds looks the way it does — it mirrors the
class-suffix vocabulary of the codebase:

| Principal file | Gerund |
|---|---|
| `*Provider`, `*Module`, `*Logger`, `*Interceptor` | providing |
| `*ViewModel` | **view** modelling (always both words — 24 uses, no bare `modelling`) |
| anything under `app/src/test/` only | testing |
| `*Adapter` — `DiffUtil` / `ItemCallback` changes | diffing |
| `*Adapter` — binding, layout, anything else | adapting |
| `*Uploader`, upload repositories | uploading |
| `*Manager` | managing |
| `*RepositoryImpl` reads, DAO queries | querying |
| lazy init, memoisation, reuse of a computed value | caching |

That `testing` row is worth its own note: **a diff touching only `app/src/test/`
always ends in `testing`**, and the noun phrase names the class under test —
`ServerUrlMapperTest.kt` → `all: smoother server url mapper testing`,
`TagsRepositoryTest.kt` → `all: smoother tags repository database testing`. This
holds for every one of the 11 `testing` commits in the last 200.

### Multi-file diffs: name them all

When the diff spans two or three files, the noun phrase **walks across all of
them** — each contributes a word or two, in diff order — and only the gerund is
picked, from whichever file's suffix best describes the change. Don't pick one file
and drop the rest; that loses the information the title exists to carry.

What a file contributes is its **layer word** — `repository`, `dao`, `utils` — not
the entity it happens to be named after. The domain is already carried by the scope
plus one feature word, so repeating the entity is noise, while the layer word tells
a reader how deep the change goes. `VoicesRepositoryImpl.kt` + `NewsDao.kt` becomes
**voices repository dao** — one feature word, then the two layers — not `voices news
dao`. `News` is what the voices domain stores, so it adds nothing `voices` didn't
already say.

The reason those three layers keep their noun is that none of them has a natural
gerund — nobody writes *repositorying* — so the gerund comes from the operation
instead (`querying`, `uploading`, `deleting`, `marking`) and the layer stays a
noun. That makes `repository` the most common word in the whole corpus after the
scopes: 70 uses, plus 9 of `repositories` and 18 of `utils`.

The opposite holds wherever the suffix *does* supply the gerund. `Adapter`,
`ViewModel`, `Manager`, `Provider`, `Fragment`, `Activity`, and `Worker` are
converted, not repeated — which is why `fragment`, `activity`, and `worker` appear
as nouns exactly zero times in 310 titles, and `adapter` and `module` just once
each. Don't write `smoother courses adapter adapting`; write `smoother courses
adapting`.

```
VoicesRepositoryImpl.kt + NewsDao.kt       → teams: smoother voices repository dao querying
LoginSyncManager.kt + AuthUtils.kt         → sync: smoother login auth utils managing
UploadManager.kt + DispatcherProvider.kt   → sync: smoother upload immediate dispatcher providing
ChatHistoryAdapter + ChatShareTargetAdapter → chat: smoother history share target item adapting
SharedPrefManager.kt + LoginActivity.kt    → login: smoother shared preferences credentials managing
GuestLoginExtensions.kt + LoginActivity.kt → login: smoother guest extensions validating
```

Don't swerve away from a layer word just because a similar title already exists.
Near-duplicates are fine and common here — the qualifier and the issue number
distinguish them. Picking a less accurate word to look novel is the worse trade:
`voices repository dao querying` sits happily alongside the earlier `voices
repository querying`, and says more than a contrived alternative would.

Read the second one closely, since it's the whole rule in miniature:
`LoginSyncManager` contributes **login** (drop `Sync`, drop the `Manager` suffix),
`AuthUtils` contributes **auth utils**, and `Manager` supplies the gerund
**managing**. Every changed file is represented and nothing is invented.

Other gerunds in circulation, for when no suffix rule applies:

> handling · importing · coloring · scoping · linking · loading · requesting ·
> filtering · deleting · viewing · sorting · searching · marking · listing ·
> joining · inserting · fetching · creating · configuring · syncing · validating ·
> binding · building · checking · finding · mapping · naming · notifying ·
> posting · selecting · sharing · starting · updating

Note `modelling` and `coloring` — the log is inconsistent about doubling, but those
two spellings are the established ones.

Aim for three to five words between the scope and the gerund. `all: smoother
importing` is fine when the change genuinely is that broad; padding a narrow change
with words it doesn't need is worse than being terse.

For the `less ... is more` shape, the noun phrase names **the thing being removed**,
not what remains: deleting `PagerAdapterDiffUtils` gives `all: less pager adapter
diff utils is more`.

For `bump`, backtick the full Gradle coordinate and use `*` for a family of
artifacts: `` all: bump `org.jetbrains.kotlin:kotlin-*` to 2.4.10 (fixes #14767) ``.

## Finding or creating the issue

This is the half that's easy to get wrong, because the right move depends on who
opened the PR.

**A human contributor's PR usually already has an issue.** They filed it first, and
it shows up in one of three places — check all three before concluding there isn't
one:

1. `(fixes #N)` already in the title
2. `fixes #N` / `closes #N` / `resolves #N` in the body
3. The branch name, which GitHub's "create branch from issue" button formats as
   `<N>-slug` — e.g. `14932-task-deadline-notifications-silently-overwrite-each-other`

If you find a number, reuse it. Confirm it's a real open issue in this repo rather
than a stale or cross-repo reference before you build the title around it.

**An agent-generated PR usually has no issue.** Jules, Copilot, and similar bots
open PRs directly, with descriptive prose titles like `Refactor: Consolidate
duplicate EntryPoints` and a body ending in *"PR created automatically by Jules
for task …"*. Branch names look like `consolidate-entrypoints-1618928943660463448`.

In that case, create the issue — and this is the key move: **the PR's current title
becomes the issue title, verbatim.** That descriptive title is a perfectly good
issue title and a poor commit subject, so it gets promoted rather than discarded.
Nothing is lost when the PR title is then rewritten into house style.

```
before  PR #15048  "Refactor: Consolidate duplicate EntryPoints"      (no issue)
        ↓ create issue #15143 titled "Refactor: Consolidate duplicate EntryPoints"
after   PR #15048  "all: less network dependencies entry point is more (fixes #15143)"
```

Give the new issue a body describing the problem the PR solves — the PR's own
description is the natural source. Don't paste the bot's automation footer or a
CodeRabbit summary into it.

Because the issue is created after the PR, its number will be *higher* than the PR
number. That's expected and common here; it is not a sign you picked the wrong
number.

## Procedure

1. Identify the PR. If the user gave a number, use it. Otherwise find the PR for
   the current branch (`mcp__github__list_pull_requests` with `head`).
2. Read it: `mcp__github__pull_request_read` with `method: "get"` for title, body,
   branch and author, then `method: "get_files"` — **the file list is the primary
   input to the title**, per the rule above. The old title is not; its only job is
   to become the issue title. Agent-written titles in particular are consistently
   vaguer than their diffs.
3. Hunt for an existing issue in the three places above. Verify any hit with
   `mcp__github__issue_read`.
4. If there is none, create one with `mcp__github__issue_write` (`method: "create"`)
   using the PR's current title.
5. Compose the new title. Skim `references/title-corpus.md` for the nearest
   precedent — matching an existing line beats inventing a phrasing.
6. Apply it with `mcp__github__update_pull_request`.
7. Report the before/after title and the issue number, saying whether you reused
   an existing issue or opened a new one.

Step 4 creates a public issue and step 6 renames someone's PR. Both are visible to
the whole project, so when the PR isn't the user's own, show the proposed title and
issue first and get a nod before writing.

## Also worth checking

Every merged PR bumps the app version by one patch in `app/build.gradle`
(`versionCode = 6249` / `versionName = "0.62.49"` → `6250` / `"0.62.50"`). If the
PR touches app code and doesn't bump it, mention it — the release workflow tags off
`versionName`, so a missing bump collides with the previous release. Read the
current values off `master` rather than the branch, since a stale branch will have
drifted behind.

## Worked examples

**Human PR, issue already filed.** PR #14933 by Okuro3499, branch
`14932-task-deadline-notifications-silently-overwrite-each-other`, body `fixes
#14932`. Issue exists — reuse it. Diff touches `TaskNotificationWorker` and
`NotificationUtils`, and the subject is team task deadlines, so scope is `teams`.

> `teams: smoother task notifying (fixes #14932)`

**Agent PR, no issue.** PR #14990 titled `Refactor ChipCloudConfig in
ResourcesAdapter`. No `fixes` anywhere, branch has a task-id suffix. Create issue
#15079 with that exact title, then retitle. Diff is confined to `ui/resources/`.

> `resources: smoother chip cloud configuring (fixes #15079)`

**Refactor that deletes a lot but removes nothing.** PR #15040, Jules-authored,
titled `Optimize Dispatchers in LoginSyncManager`, no issue. Create the issue from
that title, then read the diff: `services/sync/LoginSyncManager.kt` (71+/81−) and
`utils/AuthUtils.kt` (18+/25−). `services/sync/` fixes the scope. Both files feed
the noun phrase; `Manager` gives the gerund. Net-negative, but nothing named is
gone — so `smoother`, not `less`.

> `sync: smoother login auth utils managing (fixes #15151)`

**Deletion.** PR removes `NetworkDependenciesEntryPoint` and folds it into
`ServiceDependenciesEntryPoint`; touches `di/` and `MainApplication.kt`, so `all`.
Primarily a removal, so the `less` shape.

> `all: less network dependencies entry point is more (fixes #15143)`

**Dependency bump.**

> `` all: bump `com.android.tools.build:gradle` to 9.3.1 (fixes #15078) ``
