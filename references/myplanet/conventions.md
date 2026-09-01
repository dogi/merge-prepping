# myplanet — reference pack

`open-learning-exchange/myplanet`. Kotlin / Android, Gradle, sources under
`app/src/main/java/org/ole/planet/myplanet/`.

Read this together with the shared grammar in `SKILL.md`. Everything here is
what myplanet does *differently* from planet; the shapes, the `smoother`
default and the `(fixes #N)` rules are shared and live in `SKILL.md`.

Corpus: `references/myplanet/title-corpus.md` (last 500 merged PRs).

One myplanet-specific note on the body line `SKILL.md` requires: the automerge
drain (`.github/scripts/automerge.sh`, `link_title_issues`) mirrors a title's
closing reference into the PR body just before it squash-merges, so PRs that go
out through the queue are covered. **PRs merged by hand are not.** Write the
body line at prep time regardless — the drain's pass is a safety net, not the
mechanism, and it is idempotent about refs the body already links.

## Scopes

`all:` is the workhorse (133/500) and the right default whenever the change
reaches shared layers — `model/`, `repository/`, `di/`, `base/`, `callback/`,
`utils/`, `data/`, `MainApplication.kt` — or spans more than one feature.

Reach for a feature scope only when the change sits squarely inside one domain,
including that domain's own repository:

| Scope | Owns | Share |
|---|---|---|
| `teams` | `ui/teams/**`, `ui/voices/`, `ui/events/`, `ui/surveys/`, team tasks | 76 |
| `courses` | `ui/courses/`, `ui/exam/`, `ui/submissions/`, `ui/ratings/`, progress, tags | 68 |
| `sync` | `services/sync/`, `services/upload/`, `services/retry/`, uploads, downloads | 55 |
| `resources` | `ui/resources/`, `ui/viewer/`, webview, media playback | 51 |
| `login` | `ui/settings/`, `ui/user/`, onboarding; `ui/sync/` — see below | 28 |
| `life` | `ui/health/`, `ui/life/` | 26 |
| `dashboard` | `ui/dashboard/` and the bell — but **not** `ui/notifications/` | 23 |
| `chat` | `ui/chat/` | 21 |
| `actions` | `.github/workflows/` | 6 |
| `enterprises` | `ui/enterprises/` | 5 |
| `community` | `ui/community/` | 3 |
| `feedback` | `FeedbackDao` / feedback repository work | 1 |

When torn between a feature scope and `all:`, look at where the *centre of
gravity* of the diff sits. A change to `TeamsRepositoryImpl` alone is `teams:`;
the same change plus a shared `RealmRepository` tweak is `all:`.

`ui/notifications/` is a trap: the bell *icon* on the dashboard is `dashboard`,
but the notifications package itself is always `all` — four for four in the log
(`all: smoother notifications text caching`, `all: smoother notification item
sorting`, `all: less notification bell icon list item is more`, `all: smoother
view model scoping`). Notifications are surfaced across the app, not owned by
one screen, which is presumably why.

`ui/sync/` is genuinely ambiguous in the log — `GuestLoginExtensions.kt` has
landed as both `sync: smoother guest login validating` and `login: smoother
guest extensions validating`. Don't agonise: `sync` if the change is about the
sync or login *transaction*, `login` if it's about the screen and what the user
sees. Anything under `services/sync/` is unambiguously `sync`.

## Reading the phrase off the filenames

myplanet titles are close to a **mechanical function of the changed files** —
216/500 diffs touch a single file beyond the version bump, and 372/500 touch
three or fewer. Once you see that, most titles write themselves:

**The noun phrase is the principal changed file, de-CamelCased and lowercased,
with its role suffix dropped. The gerund comes from that suffix.**

```
ui/dashboard/BellDashboardFragment.kt   → dashboard: smoother bell reminding
services/upload/PhotoUploader.kt        → sync: smoother photo uploading
ui/health/HealthUsersAdapter.kt         → life: smoother health users item callback diffing
utils/DispatcherProvider.kt (+ manager) → sync: smoother upload immediate dispatcher providing
repository/UserRepositoryImpl.kt        → sync: smoother user repository shelf batch uploading
di/NetworkDependenciesEntryPoint.kt ✗   → all: less network dependencies entry point is more
```

### Suffix → gerund

| Principal file | Gerund |
|---|---|
| `*Provider`, `*Module`, `*Logger`, `*Interceptor` | providing |
| `*ViewModel` | **view** modelling (always both words — 40 of 40, never bare `modelling`) |
| `*Fragment`, `*Activity` with no sharper operation | handling |
| anything under `app/src/test/` only | testing |
| `*Adapter` — `DiffUtil` / `ItemCallback` changes | diffing |
| `*Adapter` — binding, layout, anything else | adapting |
| `*Uploader`, upload repositories | uploading |
| `*Manager` | managing |
| `*RepositoryImpl` reads, DAO queries | querying |
| a repository/DAO/controller *starts exposing* a `Flow` | flowing |
| a Fragment/Activity *collects* a `Flow` | collecting |
| lazy init, memoisation, reuse of a computed value | caching |

The `testing` row is worth its own note: **a diff touching only `app/src/test/`
always ends in `testing`**, and the noun phrase names the class under test —
`ServerUrlMapperTest.kt` → `all: smoother server url mapper testing`,
`TagsRepositoryTest.kt` → `all: smoother tags repository database testing`.
This holds for every one of the 27 `testing` commits in the last 500.

The Flow pair splits cleanly on producer/consumer: `SubmissionsRepositoryImpl`
→ `courses: smoother submissions repository flowing`; `BellDashboardFragment`
→ `dashboard: smoother bell flow collecting`. 21 titles, no exceptions.

`handling` is the **licensed fallback** (27 uses). When the principal file is a
Fragment or Activity and no sharper operation word applies, the log says
`handling` — not `fragmenting`, not a stretched metaphor.

Gerund league table over the 445 `smoother` titles: modelling 40 · handling 27 ·
testing 27 · inserting 17 · providing 17 · caching 15 · managing 12 · diffing 11
· collecting 11 · adapting 10 · importing 10 · flowing 10 · querying 10.

Other gerunds in circulation, for when no suffix rule applies:

> coloring · scoping · linking · loading · requesting · filtering · deleting ·
> viewing · sorting · searching · marking · listing · joining · fetching ·
> creating · configuring · syncing · validating · binding · building · checking
> · finding · mapping · naming · notifying · posting · selecting · sharing ·
> starting · updating · factoring

Note `modelling` and `coloring` — the log is inconsistent about doubling, but
those two spellings are the established ones.

### Layer words, not entity names

When the diff spans two or three files, the noun phrase **walks across all of
them** — each contributes a word or two, in diff order — and only the gerund is
picked, from whichever file's suffix best describes the change.

What a file contributes is its **layer word** — `repository`, `dao`, `utils` —
not the entity it happens to be named after. `VoicesRepositoryImpl.kt` +
`NewsDao.kt` becomes **voices repository dao** — one feature word, then the two
layers — not `voices news dao`. `News` is what the voices domain stores, so it
adds nothing `voices` didn't already say.

Those three layers keep their noun because none of them has a natural gerund —
nobody writes *repositorying* — so the gerund comes from the operation instead
(`querying`, `uploading`, `deleting`, `marking`) and the layer stays a noun.
That makes `repository` the most common word in the corpus after the scopes:
113 uses, plus 11 `repositories` and 28 `utils`.

The opposite holds wherever the suffix *does* supply the gerund. `Adapter`,
`ViewModel`, `Manager`, `Provider`, `Fragment`, `Activity`, and `Worker` are
converted, not repeated — which is why `fragment`, `activity`, and `worker`
appear as nouns **zero** times in 500 titles, and `adapter` and `module` three
each. Don't write `smoother courses adapter adapting`; write `smoother courses
adapting`.

```
VoicesRepositoryImpl.kt + NewsDao.kt        → teams: smoother voices repository dao querying
LoginSyncManager.kt + AuthUtils.kt          → sync: smoother login auth utils managing
UploadManager.kt + DispatcherProvider.kt    → sync: smoother upload immediate dispatcher providing
ChatHistoryAdapter + ChatShareTargetAdapter → chat: smoother history share target item adapting
SharedPrefManager.kt + LoginActivity.kt     → login: smoother shared preferences credentials managing
GuestLoginExtensions.kt + LoginActivity.kt  → login: smoother guest extensions validating
```

Read the second one closely, since it's the whole rule in miniature:
`LoginSyncManager` contributes **login** (drop `Sync`, drop the `Manager`
suffix), `AuthUtils` contributes **auth utils**, and `Manager` supplies the
gerund **managing**. Every changed file is represented and nothing is invented.

Don't swerve away from a layer word just because a similar title already
exists. Near-duplicates are fine and common here — the qualifier and the issue
number distinguish them. `voices repository dao querying` sits happily
alongside the earlier `voices repository querying`.

Era vocabulary is fine: `realm` appears in 21 titles from the Realm-to-Room
migration and then disappears. Titles name what the diff touches *today*; don't
sand off project-phase words.

## Dependency bumps

Backtick the full Gradle coordinate and use `*` for a family of artifacts:

> `` all: bump `org.jetbrains.kotlin:kotlin-*` to 2.4.10 (fixes #14767) ``
> `` all: bump `com.android.tools.build:gradle` to 9.3.1 (fixes #15078) ``

## Version bump to check

Every merged PR bumps the app version by one patch in `app/build.gradle`
(`versionCode = 6249` / `versionName = "0.62.49"` → `6250` / `"0.62.50"`). If
the PR touches app code and doesn't bump it, mention it — the release workflow
tags off `versionName`, so a missing bump collides with the previous release.
Read the current values off `master` rather than the branch, since a stale
branch will have drifted behind.

## Worked examples

**Human PR, issue already filed.** PR #14933 by Okuro3499, branch
`14932-task-deadline-notifications-silently-overwrite-each-other`, body `fixes
#14932`. Issue exists — reuse it. Diff touches `TaskNotificationWorker` and
`NotificationUtils`, and the subject is team task deadlines, so scope is
`teams`.

> `teams: smoother task notifying (fixes #14932)`

**Agent PR, no issue.** PR #14990 titled `Refactor ChipCloudConfig in
ResourcesAdapter`. No `fixes` anywhere, branch has a task-id suffix. Create
issue #15079 with that exact title, then retitle. Diff is confined to
`ui/resources/`.

> `resources: smoother chip cloud configuring (fixes #15079)`

**Refactor that deletes a lot but removes nothing.** PR #15040,
Jules-authored, titled `Optimize Dispatchers in LoginSyncManager`, no issue.
Create the issue from that title, then read the diff:
`services/sync/LoginSyncManager.kt` (71+/81−) and `utils/AuthUtils.kt`
(18+/25−). `services/sync/` fixes the scope. Both files feed the noun phrase;
`Manager` gives the gerund. Net-negative, but nothing named is gone — so
`smoother`, not `less`.

> `sync: smoother login auth utils managing (fixes #15151)`

**Deletion.** PR removes `NetworkDependenciesEntryPoint` and folds it into
`ServiceDependenciesEntryPoint`; touches `di/` and `MainApplication.kt`, so
`all`. Primarily a removal, so the `less` shape.

> `all: less network dependencies entry point is more (fixes #15143)`
