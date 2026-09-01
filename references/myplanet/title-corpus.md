# Title corpus — myplanet, the last 500 merged PRs

Regenerated 2026-09-01 from the 500 most recent squash commits on `origin/master` (`32f9562`, PR #16641 / issue #16640, back to `9113e26`, PR #15363 / issue #15490).
Each line pairs the landed title with the changed files that produced it — **the changed files are the primary input to the title**. Skim for the nearest precedent by scope, then by the area of the files you changed.

Path shorthand: bare paths are under `app/src/main/java/org/ole/planet/myplanet/`; everything else is written from the repo root.
`test/` is `app/src/test/java/org/ole/planet/myplanet/`.
`res/` is `app/src/main/res/`.
Omitted from every entry: `app/build.gradle` — the per-PR version bump, present in nearly every diff.

The trailing `(#NNNN)` GitHub appends at squash time is stripped: what you see here is what the PR title was.

Regenerate with:

```
scripts/build-corpus.py --repo <checkout> --name myplanet --ref origin/master --strip app/src/main/java/org/ole/planet/myplanet/ --rename app/src/test/java/org/ole/planet/myplanet/=test/ --rename app/src/main/res/=res/ --skip app/build.gradle
```

`## What a prep pass gets wrong` below was written by hand and is not
reproducible from `git log` alone — keep it when you refresh the entries.

## Shape of the window

- **Shape shares:** `smoother` 454/500 (90%), `less … is more` 38, `bump` 8, other 0.
- **Scope league table:** `all` 127 · `sync` 71 · `teams` 69 · `courses` 67 · `resources` 41 · `actions` 28 · `life` 26 · `login` 23 · `dashboard` 17 · `enterprises` 14 · `community` 8 · `chat` 8 · `lifel` 1.
- **Gerund league table:** modelling 65 · handling 40 · querying 34 · caching 33 · testing 17 · managing 16 · providing 12 · flowing 10 · filtering 8 · binding 7 · mapping 6 · uploading 6 · checking 6 · diffing 6 · landscaping 4 · inserting 4 · configuring 4 · importing 4 · injecting 4 · tagging 3 · selecting 3 · formatting 3 · deleting 3 · editing 3.
- **Issue link:** `fixes` 500, `connects` 0, well-formed 500/500.
- **Diff size:** 163/500 diffs touch a single file beyond the version bump, 363/500 touch three or fewer.
- **Bare-noun-chain discipline:** of the 492 non-`bump` titles, 0 contain a function word (preposition, article, `and`) and 0 contain a hyphenated compound.
- **Scopes used once or twice** (check each for a typo or a one-off invention): `lifel` 1.
- **Space before the colon** (malformed): `community : smoother tab pager adapting (fixes #16308)`.

## Scope ↔ directory

Where each scope's diffs actually live, counted over this window. This is the evidence behind the pack's scope table — a directory that shows up under two scopes is a real border zone, not a mistake to iron out.

- **`all`** (127) — repository 102 · test/utils 47 · utils 45 · test/repository 42 · test/ui 39 · model 27 · res/drawable 26 · ui/teams 24 · data/room 19 · test/services 18
- **`sync`** (71) — repository 46 · test/services 37 · services/sync 25 · services 19 · test/repository 11 · di 11 · services/upload 9 · utils 8 · ui/sync 6 · ui/teams 4
- **`teams`** (69) — repository 50 · ui/teams 30 · test/repository 25 · ui/voices 20 · test/ui 17 · data/room 8 · services 6 · ui/surveys 6 · base 5 · ui/events 5
- **`courses`** (67) — ui/courses 49 · repository 39 · test/repository 20 · test/ui 18 · data/room 9 · model 8 · res/layout 7 · utils 6 · base 5 · ui/submissions 4
- **`resources`** (41) — ui/resources 26 · repository 26 · test/repository 19 · test/ui 7 · res/layout 7 · utils 6 · data/room 5 · ui/viewer 5 · ui/settings 4 · res/values 4
- **`actions`** (28) — .github/workflows 29 · .github/scripts 19 · CLAUDE.md 8 · docs 4 · test/services 3 · .coderabbit.yaml 1 · gradle.properties 1 · .github 1 · settings.gradle 1 · test/utils 1
- **`life`** (26) — repository 15 · ui/health 12 · test/repository 10 · test/ui 6 · ui/life 5 · model 4 · data/room 3 · ui/user 2 · test/model 2 · base 2
- **`login`** (23) — repository 7 · ui/sync 6 · ui/settings 5 · test/repository 4 · ui/user 4 · res/values 3 · test/data 2 · test/ui 1 · res/values-ar 1 · res/values-es 1
- **`dashboard`** (17) — ui/dashboard 19 · res/layout 14 · test/ui 9 · res/values 6 · repository 5 · res/layout-sw600dp 5 · test/repository 3 · base 3 · res/layout-land 3 · res/values-ar 3
- **`enterprises`** (14) — ui/enterprises 18 · repository 7 · test/ui 4 · res/layout 4 · test/repository 3 · di 1 · res/values-ar 1 · res/values-es 1 · res/values-fr 1 · res/values-ne 1
- **`community`** (8) — ui/community 14 · repository 7 · test/ui 3 · test/repository 2 · ui/voices 2 · ui/enterprises 2 · ui/settings 1
- **`chat`** (8) — ui/chat 11 · test/ui 6 · repository 2 · test/repository 2 · data/api 1 · test/data 1
- **`lifel`** (1) — repository 1 · utils 1 · test/repository 1

## What a prep pass gets wrong

Every landed title below is the *third* version of its title. The first two are
recoverable — GitHub keeps `refs/pull/<n>/head` after a squash merge, so the
branch name and the branch's own commits survive it:

```
git fetch --depth=40 origin refs/pull/<n>/head:refs/prs/<n>
git log --format='%an :: %s' refs/prs/<n> --not origin/master
```

Done for the 220 merges of 2026-08-25 … 2026-09-01, that gives: how the PR
arrived (203 recoverable titles — 190 of the 220 from agents, and **not one in
house style**: 77 conventional-commit prefixes, 103 capitalised imperatives, 103
CamelCase class names, median 8 words), what someone drafted in house style on
the branch (29 branches), and what landed. **27 of those 29 drafts were still
changed before merging.** Grouped, they are the mistakes to expect:

**Scope invented rather than taken from the table — 13 of 27.**

| Draft | Landed |
|---|---|
| `retry: smoother dead queue api surface` | `sync: less retry repository reset all pending is more` |
| `notifications: smoother type classification in repository` | `all: smoother notifications repository view modelling` |
| `voices: smoother image array size caching in adapter` | `teams: smoother voices image caching` |
| `collections: smoother dead field cleanup` | `resources: smoother collections testing` |
| `health: smoother patient search debouncing` | `life: smoother health search view modelling` |
| `model: smoother achievement json caching` | `life: smoother achievements model caching` |
| `ci: bump upload-artifact to v7 in test workflow` | ``actions: bump `actions/upload-artifact` to 7`` |

**Prose kept instead of compressed to a noun chain.** Drafts carry prepositions,
`and`, commas and hyphenated compounds; landed titles carry none.

| Draft | Landed |
|---|---|
| `dashboard: smoother fragment navigation and tab handling` | `dashboard: smoother navigating` |
| `ui: smoother viewbinding for server address, life, and voices` | `all: smoother data binding` |
| `diagnostics: smoother log building in the batch path` | `all: smoother diagnostics repository log building` |
| `courses: smoother filtered-course sort without per-item lowercase` | `courses: smoother repository sorting` |

The third row shows the other half of that move: compressing does not mean
dropping the layer word. Where the draft names the entity or the symptom, the
landed title names the layer — `repository`, `dao`, `utils`, `view model`.

**The rest, one line each.**

- `*ViewModel` in the diff wins the gerund over a sharper verb (`patient search
  debouncing` → `health search view modelling`).
- A removal-flavoured ending means the `less` shape: `smoother enriched-libraries
  encapsulation` → `less repository enriched libraries is more`. Both ways —
  `smoother … log removing` landed as `… queue testing`, the diff being tests.
- A test-only diff is `testing` whatever the prose said (`smoother dead field
  cleanup` → `smoother collections testing`).
- `handling` is a fallback: `login: smoother edit achievement handling` →
  `life: smoother achievements editing`.
- `bump` normalises to a backticked coordinate and `to <version>` — no `v`, no
  dependabot `from A to B`, no trailing clause.
- A branch of many house-style commits gets **one** title composed for the whole
  branch. The workflow PRs here carried eight to eleven each and landed as one,
  e.g. `actions: smoother workflows playstore automerge priority queuing`.

The transformation is a re-derivation, not a rewording: **118 of the 203 landed
titles share no content word at all with the title the PR arrived with**, and
across all 203 only 18% of a landed title's words were present in the incoming
one.

## all (127)

- `all: smoother callback listeners unifying (fixes #16640)`
  ← callback/OnChangedListener.kt, callback/OnFeedbackSubmittedListener.kt, callback/OnMemberChangeListener.kt, callback/OnSecurityDataListener.kt, callback/OnTeamUpdateListener.kt, +9 more
- `all: smoother utilities hex mapping (fixes #16547)`
  ← utils/Utilities.kt, test/utils/UtilitiesTest.kt
- `all: smoother markdown utils link movement caching (fixes #16499)`
  ← utils/MarkdownUtils.kt, test/utils/MarkdownUtilsTest.kt
- `all: smoother markdown utils image url rewriting (fixes #16498)`
  ← utils/MarkdownUtils.kt, test/utils/MarkdownUtilsTest.kt
- `all: smoother server reachability checking (fixes #16579)`
  ← MainApplication.kt, test/MainApplicationTest.kt
- `all: smoother data binding (fixes #16542)`
  ← ui/life/LifeAdapter.kt, ui/sync/ServerAddressAdapter.kt, ui/voices/VoicesActions.kt, test/ui/life/LifeAdapterTest.kt, test/ui/sync/ServerAddressAdapterTest.kt, +1 more
- `all: smoother json utils log tagging (fixes #16479)`
  ← utils/JsonUtils.kt, test/utils/JsonUtilsTest.kt
- `all: smoother feedback messages caching (fixes #16473)`
  ← model/Feedback.kt, ui/feedback/FeedbackDetailActivity.kt, test/model/FeedbackTest.kt
- `all: smoother notifications repository view modelling (fixes #16582)`
  ← repository/NotificationsRepository.kt, repository/NotificationsRepositoryImpl.kt, ui/notifications/NotificationsViewModel.kt, test/repository/NotificationsRepositoryImplTest.kt, test/ui/notifications/NotificationsViewModelTest.kt
- `all: smoother storage categories sharing (fixes #16570)`
  ← ui/settings/StorageBreakdownFragment.kt, ui/settings/StorageCategories.kt, ui/settings/StorageCategoryDetailFragment.kt, test/ui/settings/StorageCategoriesTest.kt
- `all: smoother repositories mapping (fixes #16560)`
  ← repository/CoursesRepositoryImpl.kt, repository/FeedbackRepositoryImpl.kt, repository/LifeRepositoryImpl.kt, repository/TagsRepositoryImpl.kt
- `all: smoother server config utils networking (fixes #16537)`
  ← utils/ServerConfigUtils.kt, test/utils/ServerConfigUtilsTest.kt
- `all: smoother android decrypter utils payload checking (fixes #16536)`
  ← utils/AndroidDecrypter.kt
- `all: smoother network utils handling (fixes #16528)`
  ← utils/NetworkUtils.kt, test/utils/NetworkUtilsMockTest.kt
- `all: smoother download utils channels configuring (fixes #16483)`
  ← utils/DownloadUtils.kt, test/utils/DownloadUtilsTest.kt
- `all: smoother crash log store caching (fixes #16463)`
  ← utils/CrashLogStore.kt
- `all: smoother notifications group view modelling (fixes #16403)`
  ← ui/notifications/NotificationsViewModel.kt, test/ui/notifications/NotificationsViewModelTest.kt
- `all: smoother server reachability time providing (fixes #16401)`
  ← utils/ServerReachabilityProvider.kt, test/utils/ServerReachabilityProviderTest.kt
- `all: smoother base permission usage handling (fixes #16404)`
  ← base/BasePermissionActivity.kt, test/base/BasePermissionActivityTest.kt
- `all: smoother network utils lazy caching (fixes #16631)`
  ← MainApplication.kt, utils/NetworkUtils.kt, test/utils/NetworkUtilsMockTest.kt, test/utils/NetworkUtilsStateTest.kt, test/utils/NetworkUtilsTest.kt
- `all: smoother download url utils caching (fixes #16411)`
  ← utils/DownloadUtils.kt, utils/UrlUtils.kt, test/utils/DownloadUtilsTest.kt, test/utils/UrlUtilsTest.kt
- `all: smoother personals view model testing (fixes #16377)`
  ← test/ui/personals/PersonalsViewModelTest.kt
- `all: smoother storage category view model testing (fixes #16376)`
  ← test/ui/settings/StorageCategoryViewModelTest.kt
- `all: smoother notification list item html caching (fixes #16334)`
  ← model/NotificationListItem.kt, ui/notifications/NotificationsAdapter.kt, test/ui/notifications/NotificationsAdapterTest.kt
- `all: smoother version utils android id caching (fixes #16317)`
  ← utils/NetworkUtils.kt, utils/VersionUtils.kt, test/utils/NetworkUtilsTest.kt, test/utils/VersionUtilsTest.kt
- `all: smoother diagnostics repository log building (fixes #16342)`
  ← repository/DiagnosticsRepositoryImpl.kt, test/repository/DiagnosticsRepositoryImplTest.kt
- `all: smoother notifications repository dao querying (fixes #16325)`
  ← data/room/dao/NotificationDao.kt, repository/NotificationsRepositoryImpl.kt, test/repository/NotificationsRepositoryImplTest.kt
- `all: less notifications repository exam dao is more (fixes #16318)`
  ← repository/NotificationsRepositoryImpl.kt, test/repository/NotificationsRepositoryImplTest.kt
- `all: smoother configurations repository sha256 utils checking (fixes #16352)`
  ← repository/ConfigurationsRepositoryImpl.kt, utils/Sha256Utils.kt, test/repository/ConfigurationsRepositoryImplTest.kt, test/utils/Sha256UtilsTest.kt
- `all: less notifications repository task team name is more (fixes #16338)`
  ← repository/NotificationsRepository.kt, repository/NotificationsRepositoryImpl.kt
- `all: less team user dao queries is more (fixes #16341)`
  ← data/room/dao/TeamDao.kt, data/room/dao/UserDao.kt
- `all: smoother file utils checking (fixes #16312)`
  ← services/DownloadService.kt, services/DownloadWorker.kt, utils/FileUtils.kt, test/utils/FileUtilsTest.kt
- `all: smoother network module connection pooling (fixes #16305)`
  ← di/NetworkModule.kt, test/di/NetworkModuleTest.kt
- `all: less services submissions hilt injections is more (fixes #16307)`
  ← services/DownloadService.kt, services/sync/SyncManager.kt, services/upload/UploadCoordinator.kt, ui/submissions/SubmissionsFragment.kt, test/services/sync/SyncManagerTest.kt
- `all: less hilt entry point accessors is more (fixes #16298)`
  ← di/CoreDependenciesEntryPoint.kt, di/ServiceDependenciesEntryPoint.kt
- `all: smoother network monitor working (fixes #16299)`
  ← services/NetworkMonitorWorker.kt, test/services/NetworkMonitorWorkerTest.kt
- `all: smoother importing (fixes #16295)`
  ← base/BaseActivity.kt, data/api/ChatApiService.kt, data/auth/AuthSessionUpdater.kt, model/Personal.kt, repository/ActivitiesRepositoryImpl.kt, +50 more
- `all: smoother notifications icons lookup handling (fixes #16286)`
  ← ui/notifications/NotificationsAdapter.kt, ui/notifications/NotificationsFragment.kt, ui/notifications/NotificationsViewModel.kt
- `all: smoother stable id utils generating (fixes #16144)`
  ← ui/courses/CoursesAdapter.kt, ui/resources/ResourcesAdapter.kt, ui/surveys/SurveysAdapter.kt, ui/teams/TeamsAdapter.kt, ui/voices/VoicesAdapter.kt, +2 more
- `all: smoother room dao nullable querying (fixes #16278)`
  ← data/room/dao/CourseProgressDao.kt, data/room/dao/NotificationDao.kt, data/room/dao/RemovedLogDao.kt, data/room/dao/SubmissionDao.kt, data/room/dao/TeamLogDao.kt, +1 more
- `all: smoother skill branch overtaking (fixes #16057)`
  ← .claude/settings.json, CLAUDE.md
- `all: smoother map tile utils handling (fixes #16241)`
  ← base/BaseActivity.kt, data/api/ChatApiService.kt, utils/MapTileUtils.kt, utils/Sha256Utils.kt, test/data/api/ChatApiServiceTest.kt, +1 more
- `all: smoother version utils testing (fixes #16251)`
  ← test/utils/VersionUtilsTest.kt
- `all: smoother notifications view modelling (fixes #16248)`
  ← ui/notifications/NotificationsViewModel.kt
- `all: smoother feedback json parsing (fixes #16247)`
  ← model/Feedback.kt
- `all: smoother image viewer utils handling (fixes #16235)`
  ← utils/ImageViewerUtils.kt, utils/MarkdownUtils.kt
- `all: smoother network utils shared preferences managing (fixes #16230)`
  ← utils/NetworkUtils.kt
- `all: smoother notifications load view modelling (fixes #16227)`
  ← ui/notifications/NotificationsViewModel.kt, test/ui/notifications/NotificationsViewModelTest.kt
- `all: smoother network retry interceptor providing (fixes #16226)`
  ← di/NetworkModule.kt
- `all: less models android imports is more (fixes #16221)`
  ← model/Achievement.kt, model/Feedback.kt, model/News.kt, ui/user/EditAchievementFragment.kt
- `all: smoother layout change listening (fixes #16211)`
  ← ui/courses/CoursesFragment.kt, ui/resources/ResourcesFragment.kt
- `all: smoother view lifecycle owning (fixes #16204)`
  ← ui/dashboard/BellDashboardFragment.kt, ui/resources/ResourceDetailFragment.kt, ui/resources/ResourcesFragment.kt, ui/teams/TeamCalendarFragment.kt, ui/user/AchievementFragment.kt
- `all: smoother myplanet context handling (fixes #16168)`
  ← model/MyPlanet.kt
- `all: smoother feedback caching (fixes #16160)`
  ← ui/feedback/FeedbackAdapter.kt
- `all: smoother guest user role handling (fixes #16158)`
  ← model/UserEntity.kt, test/model/UserEntityEncodeImageTest.kt
- `all: smoother crash log store handling (fixes #16150)`
  ← utils/CrashLogStore.kt, test/utils/CrashLogStoreTest.kt
- `all: smoother download service testing (fixes #16149)`
  ← test/services/DownloadServiceTest.kt
- `all: bump `gradle-wrapper` to 9.7.1 (fixes #16147)`
  ← gradle/wrapper/gradle-wrapper.properties
- `all: smoother code style guide indexing (fixes #16085)`
  ← docs/CODE_STYLE_GUIDE.md
- `all: smoother selection utils membership checking (fixes #16080)`
  ← utils/SelectionUtils.kt
- `all: smoother notifications repository allocations querying (fixes #16078)`
  ← repository/NotificationsRepositoryImpl.kt
- `all: smoother pager list submitting (fixes #16074)`
  ← ui/courses/CoursesPagerAdapter.kt, ui/teams/TeamPagerAdapter.kt
- `all: smoother notifications view modelling (fixes #16071)`
  ← ui/notifications/NotificationsViewModel.kt
- `all: smoother utilities toast handling (fixes #16064)`
  ← utils/Utilities.kt
- `all: smoother colors context caching (fixes #16061)`
  ← ui/sync/ServerAddressAdapter.kt, ui/sync/ServerDialogExtensions.kt, ui/teams/tasks/TeamsTasksFragment.kt, ui/user/UserArrayAdapter.kt
- `all: smoother android decrypter sha utils handling (fixes #16060)`
  ← utils/AndroidDecrypter.kt, utils/Sha256Utils.kt
- `all: smoother fragment manager back stack listening (fixes #16056)`
  ← ui/dashboard/DashboardActivity.kt, ui/surveys/PublicSurveyActivity.kt
- `all: smoother feedback caching (fixes #16053)`
  ← ui/feedback/FeedbackAdapter.kt
- `all: smoother configurations repository versioning (fixes #16049)`
  ← repository/ConfigurationsRepositoryImpl.kt
- `all: smoother user repository markdown view modelling (fixes #16043)`
  ← repository/UserRepository.kt, repository/UserRepositoryImpl.kt, ui/components/MarkdownDialogFragment.kt, ui/components/MarkdownViewModel.kt
- `all: smoother server utils configuring (fixes #16039)`
  ← utils/ServerConfigUtils.kt
- `all: smoother exam utils answering (fixes #16034)`
  ← utils/ExamAnswerUtils.kt, test/utils/ExamAnswerUtilsTest.kt
- `all: smoother search text change flowing (fixes #16020)`
  ← ui/chat/ChatHistoryFragment.kt, ui/submissions/SubmissionsFragment.kt, ui/surveys/SurveyFragment.kt, ui/teams/TeamFragment.kt
- `all: less room models text utils is more (fixes #16018)`
  ← model/Answer.kt, model/HealthExamination.kt, model/StepExam.kt, model/TeamTask.kt
- `all: bump `com.squareup.okhttp3:okhttp` to 5.5.0 (fixes #16017)`
  ← gradle/libs.versions.toml
- `all: smoother feedback composer view modelling (fixes #16014)`
  ← ui/feedback/FeedbackComposerViewModel.kt, ui/feedback/FeedbackFragment.kt, test/ui/feedback/FeedbackComposerViewModelTest.kt
- `all: smoother notifications view modelling (fixes #16011)`
  ← ui/notifications/NotificationsViewModel.kt
- `all: less repositories methods is more (fixes #16008)`
  ← data/room/dao/MyLibraryDao.kt, data/room/dao/SubmissionDao.kt, repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, repository/SubmissionsRepository.kt, +7 more
- `all: smoother tts utils managing (fixes #16006)`
  ← utils/TTSManager.kt
- `all: smoother dictionary repository providing (fixes #16001)`
  ← di/RepositoryModule.kt, repository/DictionaryRepository.kt, repository/DictionaryRepositoryImpl.kt, ui/dictionary/DictionaryActivity.kt, res/values/strings.xml, +1 more
- `all: smoother time utils date formatter caching (fixes #15996)`
  ← utils/TimeUtils.kt
- `all: smoother user entity image url handling (fixes #15993)`
  ← model/UserEntity.kt
- `all: smoother notifications repository dao querying (fixes #15990)`
  ← data/room/dao/NotificationDao.kt, repository/NotificationsRepositoryImpl.kt, test/repository/NotificationsRepositoryImplTest.kt
- `all: smoother recycler viewing (fixes #16086)`
  ← ui/chat/ChatHistoryFragment.kt, ui/dashboard/BellDashboardFragment.kt, ui/feedback/FeedbackDetailActivity.kt, ui/teams/TeamCalendarFragment.kt
- `all: smoother map tile utils handling (fixes #15988)`
  ← utils/MapTileUtils.kt, test/utils/MapTileUtilsTest.kt
- `all: smoother json utils handling (fixes #15984)`
  ← utils/JsonUtils.kt, test/utils/JsonUtilsTest.kt
- `all: less robolectric config sdk pins is more (fixes #15939)`
  ← test/base/BaseRecyclerFragmentTest.kt, test/data/api/RetryInterceptorTest.kt, test/data/room/dao/NewsDaoTest.kt, test/model/UserEntityParseLeadersTest.kt, test/repository/NotificationsRepositoryImplTest.kt, +29 more
- `all: smoother importing (fixes #15826)`
  ← MainApplication.kt, di/ServiceModule.kt, repository/ActivitiesRepository.kt, repository/ActivitiesRepositoryImpl.kt, repository/ChatRepositoryImpl.kt, +42 more
- `all: smoother gson injecting (fixes #15801)`
  ← di/NetworkModule.kt, repository/ChatRepositoryImpl.kt, repository/ConfigurationsRepositoryImpl.kt, repository/HealthRepositoryImpl.kt, repository/SubmissionsRepositoryImpl.kt, +8 more
- `all: bump `androidx.appcompat:appcompat` to 1.8.0 (fixes #15810)`
  ← gradle/libs.versions.toml
- `all: smoother user repository parsing (fixes #15798)`
  ← model/UserEntity.kt, repository/HealthRepository.kt, repository/HealthRepositoryImpl.kt, repository/TeamsRepositoryImpl.kt, repository/UserRepository.kt, +9 more
- `all: smoother flow collecting (fixes #15797)`
  ← base/BaseDashboardFragment.kt, ui/chat/ChatDetailFragment.kt, ui/enterprises/EnterprisesReportsFragment.kt, ui/notifications/NotificationsFragment.kt, ui/ratings/RatingsFragment.kt, +5 more
- `all: bump `androidx.webkit:webkit` from 1.16.0 to 1.17.0 (fixes #15787)`
  ← gradle/libs.versions.toml
- `all: smoother free space worker recursive deleting (fixes #15784)`
  ← services/FreeSpaceWorker.kt
- `all: smoother user repository name unifying (fixes #15781)`
  ← data/room/dao/UserDao.kt, repository/UserRepositoryImpl.kt
- `all: less dialog utils indeterminate is more (fixes #15762)`
  ← utils/DialogUtils.kt
- `all: smoother configurations repository server url updating (fixes #15754)`
  ← repository/ConfigurationsRepository.kt, repository/ConfigurationsRepositoryImpl.kt, ui/courses/CourseProgressViewModel.kt, ui/courses/ProgressViewModel.kt, ui/viewer/ResourceViewerViewModel.kt, +2 more
- `all: smoother view models loading (fixes #15751)`
  ← ui/events/EventsDetailViewModel.kt, ui/health/HealthViewModel.kt, ui/user/UserProfileViewModel.kt
- `all: smoother repositories json parsing (fixes #15748)`
  ← model/News.kt, repository/FeedbackRepositoryImpl.kt, repository/SubmissionsRepositoryImpl.kt, repository/VoicesRepositoryImpl.kt
- `all: smoother feedback repository saving (fixes #15747)`
  ← repository/FeedbackRepository.kt, repository/FeedbackRepositoryImpl.kt, ui/feedback/FeedbackFragment.kt
- `all: smoother user repository dao save searching (fixes #15745)`
  ← data/room/dao/UserDao.kt, repository/HealthRepositoryImpl.kt, repository/SubmissionsRepositoryImpl.kt, repository/UserRepository.kt, repository/UserRepositoryImpl.kt, +2 more
- `all: smoother notification repository destination view modelling (fixes #15606)`
  ← base/BaseTeamFragment.kt, data/room/AppDatabase.kt, model/AppNotification.kt, model/NotificationPayload.kt, repository/NotificationsRepositoryImpl.kt, +6 more
- `all: less database service module is more (fixes #15732)`
  ← CLAUDE.md, data/DatabaseService.kt, di/DatabaseModule.kt, test/data/DatabaseServiceTest.kt, test/services/sync/SyncManagerTest.kt, +1 more
- `all: smoother regex normalizing (fixes #15730)`
  ← model/MyLibrary.kt, ui/chat/ChatViewModel.kt, ui/surveys/SurveysViewModel.kt, utils/TTSManager.kt, utils/Utilities.kt, +1 more
- `all: smoother network utils flowing (fixes #15701)`
  ← utils/NetworkUtils.kt
- `all: smoother base container dispatcher providing (fixes #15638)`
  ← base/BaseContainerFragment.kt, base/BaseTeamFragment.kt, repository/ResourcesRepositoryImpl.kt, services/DownloadService.kt, ui/courses/CourseStepFragment.kt, +3 more
- `all: smoother data room converters type token caching (fixes #15705)`
  ← data/room/Converters.kt, test/data/room/ConvertersTest.kt
- `all: smoother importing (fixes #15586)`
  ← base/BaseDashboardFragment.kt, di/ServiceModule.kt, model/UserEntity.kt, repository/CoursesRepository.kt, repository/CoursesRepositoryImpl.kt, +38 more
- `all: smoother download service testing (fixes #15584)`
  ← test/services/DownloadServiceTest.kt
- `all: smoother merge prepping submodule pinning (fixes #15581)`
  ← .agents/skills/merge-prepping
- `all: smoother refresh job cancelling (fixes #15564)`
  ← ui/courses/CoursesFragment.kt, ui/health/HealthViewModel.kt, ui/resources/ResourcesFragment.kt, ui/teams/tasks/TeamsTasksFragment.kt
- `all: smoother model database indexing (fixes #15573)`
  ← data/room/AppDatabase.kt, model/Achievement.kt, model/ApkLog.kt, model/ChatHistory.kt, model/Community.kt, +3 more
- `all: smoother resources courses grid list viewing (fixes #15440)`
  ← base/BaseAdapterFactory.kt, repository/CoursesRepositoryImpl.kt, services/SharedPrefManager.kt, ui/components/MaxWidthFrameLayout.kt, ui/courses/CourseFilterController.kt, +62 more
- `all: smoother notifications group view modelling (fixes #15256)`
  ← ui/notifications/NotificationsViewModel.kt, test/ui/notifications/NotificationsViewModelTest.kt
- `all: smoother adapters item callback diffing (fixes #15567)`
  ← ui/health/HealthExaminationAdapter.kt, ui/references/ReferencesAdapter.kt, ui/surveys/SurveysAdapter.kt
- `all: bump `androidx.media3:media3-*` to 1.11.0 (fixes #15548)`
  ← gradle/libs.versions.toml
- `all: smoother personals repository upload testing (fixes #15535)`
  ← test/repository/PersonalsRepositoryImplTest.kt
- `all: less repository functions is more (fixes #15546)`
  ← data/room/dao/MyLifeDao.kt, data/room/dao/OfflineActivityDao.kt, repository/CoursesRepository.kt, repository/CoursesRepositoryImpl.kt, repository/EventsRepository.kt, +15 more
- `all: smoother resources courses sorting view modelling (fixes #15544)`
  ← ui/resources/ResourcesAdapter.kt, ui/resources/ResourcesFragment.kt, ui/resources/ResourcesViewModel.kt
- `all: smoother leaders life send survey views modelling (fixes #15543)`
  ← ui/community/LeadersFragment.kt, ui/community/LeadersViewModel.kt, ui/life/LifeFragment.kt, ui/life/LifeViewModel.kt, ui/surveys/SendSurveyFragment.kt, +2 more
- `all: smoother crash log sweeping (fixes #15464)`
  ← MainApplication.kt
- `all: smoother base recycler caching (fixes #15542)`
  ← base/BaseRecyclerFragment.kt, ui/courses/CoursesFragment.kt, ui/resources/ResourcesFragment.kt, ui/teams/TeamFragment.kt
- `all: smoother anr watchdog log persisting (fixes #15534)`
  ← MainApplication.kt
- `all: bump `gradle-wrapper` to 9.7.0 (fixes #15540)`
  ← gradle/wrapper/gradle-wrapper.jar, gradle/wrapper/gradle-wrapper.properties
- `all: smoother apk log building (fixes #15496)`
  ← MainApplication.kt
- `all: smoother server reachability connecting (fixes #15495)`
  ← MainApplication.kt
- `all: smoother notifications repository testing (fixes #15490)`
  ← test/repository/NotificationsRepositoryImplTest.kt

## sync (71)

- `sync: smoother time logger summary generating (fixes #16461)`
  ← utils/SyncTimeLogger.kt, test/utils/SyncTimeLoggerTest.kt
- `sync: smoother repository user data uploading (fixes #16450)`
  ← repository/SyncRepositoryImpl.kt
- `sync: less retry repository reset all pending is more (fixes #16337)`
  ← data/room/dao/RetryDao.kt, repository/RetryRepository.kt, repository/RetryRepositoryImpl.kt, services/retry/RetryQueue.kt, test/repository/RetryRepositoryImplTest.kt
- `sync: smoother realtime flow buffer managing (fixes #16306)`
  ← services/sync/RealtimeSyncManager.kt, test/services/sync/RealtimeSyncManagerTest.kt
- `sync: smoother server url mapper caching (fixes #16533)`
  ← services/sync/ServerUrlMapper.kt, test/services/sync/ServerUrlMapperTest.kt
- `sync: smoother auto worker time providing (fixes #16490)`
  ← services/AutoSyncWorker.kt
- `sync: smoother download service queue caching (fixes #16485)`
  ← services/DownloadService.kt, test/services/DownloadServiceOnDownloadCompleteTest.kt
- `sync: smoother time logger starting (fixes #16462)`
  ← utils/SyncTimeLogger.kt
- `sync: smoother repository error handling (fixes #16336)`
  ← repository/SyncRepositoryImpl.kt, services/sync/LoginSyncManager.kt, services/sync/SyncManager.kt, test/services/sync/LoginSyncManagerTest.kt
- `sync: smoother submissions repository photo dao uploading (fixes #16412)`
  ← data/room/dao/SubmitPhotosDao.kt, repository/SubmissionsRepository.kt, repository/SubmissionsRepositoryImpl.kt, services/upload/PhotoUploader.kt, test/repository/SubmissionsRepositoryImplTest.kt, +1 more
- `sync: smoother download repository file handling (fixes #16356)`
  ← repository/DownloadRepositoryImpl.kt, test/repository/DownloadRepositoryImplTest.kt
- `sync: smoother retry interceptor backoff time providing (fixes #16330)`
  ← data/api/RetryInterceptor.kt, utils/TimeProvider.kt, test/data/api/RetryInterceptorTest.kt, test/utils/TestTimeProvider.kt
- `sync: less upload repository query pending is more (fixes #16329)`
  ← repository/UploadRepository.kt, repository/UploadRepositoryImpl.kt, test/repository/UploadRepositoryImplTest.kt
- `sync: smoother retry repository queue testing (fixes #16351)`
  ← repository/RetryRepositoryImpl.kt, test/repository/RetryRepositoryImplTest.kt
- `sync: smoother importing (fixes #16563)`
  ← ui/sync/SyncActivity.kt
- `sync: smoother login uploading (fixes #16265)`
  ← ui/sync/SyncActivity.kt
- `sync: smoother upload teams managing (fixes #15830)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: smoother retry queue working (fixes #16234)`
  ← services/retry/RetryQueueWorker.kt, test/services/retry/RetryQueueWorkerTest.kt
- `sync: smoother upload coordinating (fixes #16229)`
  ← services/upload/UploadCoordinator.kt
- `sync: smoother login user managing (fixes #16154)`
  ← model/UserEntity.kt, services/sync/LoginSyncManager.kt, test/model/UserEntityTest.kt, test/services/sync/LoginSyncManagerTest.kt
- `sync: smoother url utils managing (fixes #16210)`
  ← services/sync/SyncManager.kt
- `sync: smoother repository time logger providing (fixes #16209)`
  ← di/ServiceModule.kt, repository/SyncRepositoryImpl.kt, services/sync/SyncManager.kt, services/sync/TransactionSyncManager.kt, utils/ServerReachabilityProvider.kt, +4 more
- `sync: smoother download service buffering (fixes #16167)`
  ← services/DownloadService.kt
- `sync: smoother download auth header working (fixes #16161)`
  ← services/DownloadWorker.kt
- `sync: smoother photo url utils uploading (fixes #16159)`
  ← services/upload/PhotoUploader.kt
- `sync: smoother retry repository dao querying (fixes #16153)`
  ← data/room/dao/RetryDao.kt, repository/RetryRepositoryImpl.kt, test/repository/RetryRepositoryImplTest.kt
- `sync: smoother retry interceptor testing (fixes #16082)`
  ← test/data/api/RetryInterceptorTest.kt
- `sync: smoother upload repository querying (fixes #16079)`
  ← repository/UploadRepositoryImpl.kt
- `sync: smoother realtime tables watching (fixes #16068)`
  ← ui/sync/RealtimeSyncMixin.kt
- `sync: smoother realtime table flowing (fixes #16055)`
  ← services/sync/RealtimeSyncManager.kt, ui/chat/ChatViewModel.kt, ui/teams/TeamDetailFragment.kt, ui/teams/TeamViewModel.kt, test/ui/chat/ChatViewModelTest.kt
- `sync: smoother upload url utils coordinating (fixes #16047)`
  ← services/upload/UploadCoordinator.kt
- `sync: less process user data upload manager is more (fixes #16029)`
  ← ui/sync/ProcessUserDataActivity.kt
- `sync: smoother resources managing (fixes #16025)`
  ← services/sync/SyncManager.kt
- `sync: smoother upload batch coordinating (fixes #16021)`
  ← services/upload/UploadCoordinator.kt
- `sync: smoother transaction shared preferences managing (fixes #16005)`
  ← services/SharedPrefManager.kt, services/sync/TransactionSyncManager.kt, test/services/SharedPrefManagerTest.kt, test/services/sync/TransactionSyncManagerCheckpointTest.kt
- `sync: smoother download service next url managing (fixes #15994)`
  ← services/DownloadService.kt
- `sync: smoother upload shelfing (fixes #15983)`
  ← services/UploadToShelfService.kt
- `sync: smoother user repository security data preserving (fixes #15836)`
  ← repository/UserRepositoryImpl.kt, test/repository/UserRepositoryImplTest.kt
- `sync: smoother server url alternative credentials mapping (fixes #15834)`
  ← services/sync/ServerUrlMapper.kt, test/services/sync/ServerUrlMapperTest.kt
- `sync: smoother manager resources cleaning (fixes #15831)`
  ← services/sync/SyncManager.kt
- `sync: less manager courses repository is more (fixes #15802)`
  ← services/sync/SyncManager.kt, test/services/sync/SyncManagerTest.kt
- `sync: smoother repositories interfaces writing (fixes #15786)`
  ← di/RepositoryModule.kt, di/ServiceModule.kt, repository/ChatRepository.kt, repository/ChatRepositoryImpl.kt, repository/ChatSyncWriter.kt, +13 more
- `sync: smoother file uploading streaming (fixes #15794)`
  ← repository/UploadRepositoryImpl.kt, services/UploadManager.kt, services/upload/AchievementUploader.kt, utils/FileUtils.kt, test/utils/FileUtilsTest.kt
- `sync: less upload manager shared preferences is more (fixes #15806)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: less upload shelf service constructor is more (fixes #15805)`
  ← di/ServiceModule.kt, services/UploadToShelfService.kt, test/services/UploadToShelfServiceTest.kt
- `sync: less transaction sync manager application scope is more (fixes #15803)`
  ← di/ServiceModule.kt, services/sync/TransactionSyncManager.kt, test/services/sync/TransactionSyncManagerCheckpointTest.kt, test/services/sync/TransactionSyncManagerTest.kt
- `sync: less manager teams repository is more (fixes #15804)`
  ← services/sync/SyncManager.kt, test/services/sync/SyncManagerTest.kt
- `sync: smoother upload repository attachment dispatcher providing (fixes #15782)`
  ← repository/UploadRepositoryImpl.kt, test/repository/UploadRepositoryImplTest.kt
- `sync: smoother upload repository api routing (fixes #15779)`
  ← repository/UploadRepository.kt, repository/UploadRepositoryImpl.kt, services/UploadManager.kt, services/upload/AchievementUploader.kt, services/upload/PhotoUploader.kt, +1 more
- `sync: less transaction manager teams repository is more (fixes #15764)`
  ← di/ServiceModule.kt, services/sync/TransactionSyncManager.kt, test/services/sync/TransactionSyncManagerCheckpointTest.kt, test/services/sync/TransactionSyncManagerTest.kt
- `sync: less login manager user repository is more (fixes #15763)`
  ← services/sync/LoginSyncManager.kt, test/services/sync/LoginSyncManagerTest.kt
- `sync: less upload manager chat repository is more (fixes #15761)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: less retry queue context is more (fixes #15760)`
  ← services/retry/RetryQueue.kt, test/services/retry/RetryQueueTest.kt
- `sync: less manager events repository is more (fixes #15759)`
  ← services/sync/SyncManager.kt, test/services/sync/SyncManagerTest.kt
- `sync: less upload manager submissions repository is more (fixes #15758)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: less upload manager personals repository is more (fixes #15757)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: less upload manager teams repository is more (fixes #15756)`
  ← services/UploadManager.kt, test/services/UploadManagerTest.kt
- `sync: less manager teams repository is more (fixes #15755)`
  ← services/sync/SyncManager.kt, test/services/sync/SyncManagerTest.kt
- `sync: smoother diagnostics repository configs uploading (fixes #15750)`
  ← MainApplication.kt, di/CoreDependenciesEntryPoint.kt, di/RepositoryModule.kt, repository/ActivitiesRepository.kt, repository/ActivitiesRepositoryImpl.kt, +13 more
- `sync: smoother repository api interface injecting (fixes #15742)`
  ← repository/SyncRepository.kt, repository/SyncRepositoryImpl.kt, services/sync/SyncManager.kt
- `sync: smoother sync repository json tree mapping (fixes #15738)`
  ← model/MyTeam.kt, repository/SyncRepositoryImpl.kt, test/model/MyTeamTest.kt
- `sync: smoother transaction checkpoint applying (fixes #15736)`
  ← services/sync/TransactionSyncManager.kt, test/services/sync/TransactionSyncManagerCheckpointTest.kt
- `sync: less upload shelf api interface is more (fixes #15734)`
  ← di/ServiceModule.kt, services/UploadToShelfService.kt, test/services/UploadToShelfServiceTest.kt
- `sync: smoother status dashboard collecting (fixes #15708)`
  ← ui/dashboard/DashboardActivity.kt, ui/sync/SyncActivity.kt
- `sync: smoother time logger date formatting (fixes #15709)`
  ← services/sync/SyncManager.kt, ui/enterprises/EnterprisesFinancesFragment.kt, ui/notifications/NotificationsAdapter.kt, ui/teams/TeamCalendarFragment.kt, utils/SyncTimeLogger.kt
- `sync: smoother download dialog handling (fixes #15435)`
  ← base/BaseResourceFragment.kt, ui/courses/CoursesFragment.kt, ui/teams/courses/TeamCoursesFragment.kt
- `sync: smoother logger timestamp caching (fixes #15562)`
  ← utils/SyncTimeLogger.kt
- `sync: smoother realtime mixin injecting (fixes #15461)`
  ← di/CoreDependenciesEntryPoint.kt, ui/courses/CoursesFragment.kt, ui/feedback/FeedbackListFragment.kt, ui/resources/ResourcesFragment.kt, ui/surveys/SurveyFragment.kt, +1 more
- `sync: smoother sync repository server pulling (fixes #15466)`
  ← di/RepositoryModule.kt, repository/SyncRepository.kt, repository/SyncRepositoryImpl.kt, services/sync/SyncManager.kt, test/services/sync/SyncManagerTest.kt
- `sync: smoother download service url resolving (fixes #15494)`
  ← services/DownloadService.kt
- `sync: smoother download service early returning (fixes #15493)`
  ← services/DownloadService.kt

## teams (69)

- `teams: smoother voices image url flowing (fixes #16527)`
  ← ui/voices/NewsViewModel.kt, test/ui/voices/NewsViewModelTest.kt
- `teams: smoother voices view modelling (fixes #16557)`
  ← ui/voices/VoicesViewModel.kt, test/ui/voices/VoicesViewModelTest.kt
- `teams: smoother shared preferences name managing (fixes #16532)`
  ← services/SharedPrefManager.kt
- `teams: smoother members view binding (fixes #16416)`
  ← ui/teams/members/MembersAdapter.kt, test/ui/teams/members/MembersAdapterTest.kt
- `teams: smoother tasks members assigning (fixes #16561)`
  ← ui/teams/tasks/TeamsTasksFragment.kt
- `teams: smoother voices image caching (fixes #16552)`
  ← ui/voices/VoicesAdapter.kt, test/ui/voices/VoicesAdapterImagesTest.kt
- `teams: smoother requests view modelling (fixes #16541)`
  ← ui/teams/members/RequestsViewModel.kt
- `teams: smoother tasks assignees view modelling (fixes #16509)`
  ← ui/teams/tasks/TeamsTasksFragment.kt, ui/teams/tasks/TeamsTasksViewModel.kt
- `teams: smoother members date formatting (fixes #16524)`
  ← ui/teams/members/MembersAdapter.kt, utils/TimeUtils.kt, test/ui/teams/members/MembersAdapterTest.kt
- `teams: smoother voices label managing (fixes #16472)`
  ← services/VoicesLabelManager.kt
- `teams: smoother tasks notification worker testing (fixes #16451)`
  ← services/TaskNotificationWorker.kt, test/services/TaskNotificationWorkerTest.kt
- `teams: smoother voices label chip managing (fixes #16469)`
  ← services/VoicesLabelManager.kt, test/services/VoicesLabelManagerTest.kt
- `teams: smoother surveys repository eligibility filtering (fixes #16424)`
  ← data/room/dao/ExamDao.kt, repository/SurveysRepositoryImpl.kt, test/data/room/dao/ExamDaoTest.kt, test/repository/SurveysRepositoryImplTest.kt
- `teams: smoother base members user caching (fixes #16405)`
  ← base/BaseTeamFragment.kt, ui/teams/members/MembersFragment.kt
- `teams: smoother courses filtering (fixes #16408)`
  ← ui/teams/courses/TeamCoursesFragment.kt
- `teams: less members leader handle is more (fixes #16406)`
  ← ui/teams/members/MembersFragment.kt
- `teams: smoother events repository meetup dao querying (fixes #16421)`
  ← data/room/dao/MeetupDao.kt, repository/EventsRepositoryImpl.kt, test/repository/EventsRepositoryImplTest.kt
- `teams: smoother events detail view model testing (fixes #16378)`
  ← test/ui/events/EventsDetailViewModelTest.kt
- `teams: smoother repository member querying (fixes #16300)`
  ← repository/TeamsRepositoryImpl.kt, test/repository/TeamsRepositoryImplTest.kt
- `teams: smoother repository leader candidate querying (fixes #16214)`
  ← data/room/dao/TeamDao.kt, repository/TeamsRepositoryImpl.kt
- `teams: smoother tasks copy uploading (fixes #16242)`
  ← ui/teams/tasks/TeamsTasksFragment.kt
- `teams: smoother base voices members selecting (fixes #16223)`
  ← base/BaseVoicesFragment.kt
- `teams: smoother members repository view modelling (fixes #16219)`
  ← base/BaseTeamFragment.kt, repository/TeamsMembersRepository.kt, repository/TeamsRepositoryImpl.kt, ui/teams/TeamDetailFragment.kt, ui/teams/TeamViewModel.kt, +5 more
- `teams: smoother notifications repository querying (fixes #16206)`
  ← di/RepositoryModule.kt, repository/NotificationsRepositoryImpl.kt, repository/TeamsNotificationsRepository.kt, repository/TeamsRepository.kt, test/repository/NotificationsRepositoryImplTest.kt
- `teams: smoother resources repositories linking (fixes #16208)`
  ← repository/ResourcesRepositoryImpl.kt, repository/TeamsRepository.kt, repository/TeamsRepositoryImpl.kt, test/repository/ResourcesRepositoryBenchmarkTest.kt, test/repository/ResourcesRepositoryImplTest.kt, +2 more
- `teams: smoother members finances ratings repositories querying (fixes #16013)`
  ← repository/RatingsRepository.kt, repository/RatingsRepositoryImpl.kt, ui/resources/ResourceDetailFragment.kt, test/repository/RatingsRepositoryImplTest.kt
- `teams: smoother voices sorting (fixes #16207)`
  ← ui/voices/VoicesFragment.kt
- `teams: smoother events describing (fixes #16171)`
  ← ui/events/EventsDescriptionAdapter.kt, test/ui/events/EventsDescriptionAdapterTest.kt
- `teams: smoother voices label managing (fixes #16170)`
  ← services/VoicesLabelManager.kt
- `teams: smoother surveys repository querying (fixes #16157)`
  ← repository/SurveysRepositoryImpl.kt
- `teams: less voices change overide is more (fixes #16083)`
  ← ui/voices/VoicesFragment.kt
- `teams: smoother voices label managing (fixes #16069)`
  ← services/VoicesLabelManager.kt
- `teams: smoother list caching (fixes #16065)`
  ← ui/teams/TeamsAdapter.kt
- `teams: smoother surveys view modelling (fixes #16062)`
  ← ui/surveys/SurveysViewModel.kt
- `teams: smoother events repository detail view modelling (fixes #16058)`
  ← repository/EventsRepository.kt, repository/EventsRepositoryImpl.kt, ui/events/EventsDetailViewModel.kt, test/repository/EventsRepositoryImplTest.kt
- `teams: smoother voices repository change flowing (fixes #16051)`
  ← repository/VoicesRepositoryImpl.kt
- `teams: less survey resume override is more (fixes #16046)`
  ← ui/surveys/SurveyFragment.kt
- `teams: smoother surveys repository adopting (fixes #16044)`
  ← repository/SurveysRepositoryImpl.kt, test/repository/SurveysRepositoryImplTest.kt
- `teams: smoother events view binding (fixes #16042)`
  ← ui/events/EventsAdapter.kt
- `teams: smoother voices data view modelling (fixes #16040)`
  ← ui/voices/VoicesFragment.kt, ui/voices/VoicesViewModel.kt
- `teams: smoother events detail time picking (fixes #16038)`
  ← ui/events/EventsDetailFragment.kt
- `teams: smoother voices reply counting (fixes #16036)`
  ← ui/voices/VoicesAdapter.kt, res/values/strings.xml
- `teams: smoother voices label view modelling (fixes #16033)`
  ← ui/voices/VoicesViewModel.kt, utils/Constants.kt
- `teams: smoother voices item callback diffing (fixes #16027)`
  ← ui/voices/VoicesAdapter.kt
- `teams: smoother notification repository querying (fixes #16010)`
  ← repository/NotificationsRepository.kt, repository/NotificationsRepositoryImpl.kt, repository/VoicesRepository.kt, repository/VoicesRepositoryImpl.kt, ui/teams/voices/TeamsVoicesViewModel.kt, +3 more
- `teams: smoother repository dao querying (fixes #16009)`
  ← data/room/dao/TeamDao.kt, repository/TeamsRepositoryImpl.kt
- `teams: smoother repository next leader querying (fixes #16000)`
  ← repository/TeamsRepositoryImpl.kt
- `teams: smoother voices repository editing (fixes #15991)`
  ← repository/VoicesEditor.kt, repository/VoicesRepository.kt, ui/teams/voices/TeamsVoicesFragment.kt, ui/voices/ReplyActivity.kt, ui/voices/VoicesActions.kt, +2 more
- `teams: smoother requests dao view modelling (fixes #15992)`
  ← data/room/dao/TeamDao.kt, ui/teams/members/RequestsViewModel.kt, test/ui/teams/members/RequestsViewModelTest.kt
- `teams: smoother surveys item callback diffing (fixes #15989)`
  ← model/SurveyRow.kt, ui/surveys/SurveyFragment.kt, ui/surveys/SurveysAdapter.kt, ui/surveys/SurveysViewModel.kt, test/ui/surveys/SurveysViewModelTest.kt
- `teams: smoother repository dashboard bell view modelling (fixes #15726)`
  ← base/BaseDashboardFragment.kt, repository/TeamsRepository.kt, repository/TeamsRepositoryImpl.kt, ui/dashboard/BellDashboardFragment.kt, ui/teams/TeamFragment.kt, +3 more
- `teams: smoother finances members repositories splitting (fixes #15840)`
  ← callback/OnMemberActionListener.kt, di/RepositoryModule.kt, model/JoinedMemberData.kt, repository/TeamsFinancesRepository.kt, repository/TeamsMembersRepository.kt, +8 more
- `teams: smoother base voices tasks dispatcher providing (fixes #15799)`
  ← base/BaseTeamFragment.kt, ui/sync/ProcessUserDataActivity.kt, ui/teams/tasks/TeamsTasksFragment.kt, ui/teams/voices/TeamsVoicesFragment.kt
- `teams: smoother submissions repositories streamlining (fixes #15796)`
  ← model/ApkLog.kt, repository/SubmissionsRepository.kt, repository/SubmissionsRepositoryImpl.kt, repository/TeamsRepositoryImpl.kt, repository/TeamsSyncRepository.kt, +8 more
- `teams: smoother voices replying (fixes #15792)`
  ← ui/teams/voices/TeamsVoicesFragment.kt, ui/voices/ReplyActivity.kt, ui/voices/VoicesAdapter.kt, ui/voices/VoicesFragment.kt
- `teams: smoother repository csv reports exporting (fixes #15785)`
  ← repository/TeamsRepositoryImpl.kt
- `teams: smoother task json testing (fixes #15783)`
  ← test/model/TeamTaskTest.kt
- `teams: smoother tasks view modelling (fixes #15777)`
  ← repository/TeamsRepository.kt, repository/TeamsRepositoryImpl.kt, ui/teams/tasks/TeamsTasksFragment.kt, ui/teams/tasks/TeamsTasksViewModel.kt, test/ui/teams/tasks/TeamsTasksViewModelTest.kt
- `teams: smoother voices repository view modelling (fixes #15741)`
  ← repository/VoicesRepository.kt, repository/VoicesRepositoryImpl.kt, ui/teams/voices/TeamsVoicesViewModel.kt, ui/voices/VoicesViewModel.kt, test/repository/VoicesRepositoryImplTest.kt, +3 more
- `teams: smoother voices payload diffing (fixes #15733)`
  ← model/News.kt, ui/voices/VoicesAdapter.kt
- `teams: smoother repository dao querying (fixes #15706)`
  ← data/room/dao/TeamDao.kt, repository/TeamsRepositoryImpl.kt
- `teams: smoother voices repository reply bulk querying (fixes #15710)`
  ← data/room/dao/NewsDao.kt, repository/VoicesRepositoryImpl.kt, test/data/room/dao/NewsDaoTest.kt, test/repository/VoicesRepositoryImplTest.kt
- `teams: smoother survey title ordering (fixes #15576)`
  ← ui/surveys/SurveyFragment.kt, res/values-ar/strings.xml, res/values-es/strings.xml, res/values-fr/strings.xml, res/values-ne/strings.xml, +2 more
- `teams: smoother voices repository replying (fixes #15517)`
  ← repository/VoicesRepositoryImpl.kt, ui/voices/VoicesFragment.kt, test/repository/VoicesRepositoryImplTest.kt
- `teams: smoother events repository detail view modelling (fixes #15565)`
  ← repository/EventsRepository.kt, repository/EventsRepositoryImpl.kt, ui/events/EventsDetailViewModel.kt, test/repository/EventsRepositoryImplTest.kt
- `teams: smoother repository members removing (fixes #15172)`
  ← repository/TeamsRepositoryImpl.kt, ui/teams/members/MembersFragment.kt
- `teams: smoother repository dao querying (fixes #15457)`
  ← data/room/dao/TeamDao.kt, repository/TeamsRepositoryImpl.kt
- `teams: smoother repository date formatter caching (fixes #15498)`
  ← repository/TeamsRepositoryImpl.kt
- `teams: smoother voices policy testing (fixes #15492)`
  ← test/repository/VoicePostingPolicyTest.kt

## courses (67)

- `courses: smoother submissions landscaping (fixes #16617)`
  ← res/layout-land/fragment_my_submission.xml, res/layout/fragment_my_submission.xml
- `courses: smoother progress binding (fixes #16413)`
  ← ui/courses/CoursesProgressAdapter.kt, test/ui/courses/CoursesProgressAdapterTest.kt
- `courses: smoother repository member filtering (fixes #16517)`
  ← model/MyCourse.kt, repository/CoursesRepositoryImpl.kt, test/model/MyCourseTest.kt, test/repository/CoursesRepositoryImplTest.kt
- `courses: smoother steps data handling (fixes #16568)`
  ← ui/courses/CourseStepFragment.kt
- `courses: smoother selecting (fixes #16556)`
  ← ui/courses/CoursesAdapter.kt
- `courses: smoother repository sorting (fixes #16512)`
  ← repository/CoursesRepositoryImpl.kt, test/repository/CoursesRepositoryImplTest.kt
- `courses: smoother rating utils factoring (fixes #16491)`
  ← utils/CourseRatingUtils.kt, test/utils/CourseRatingUtilsTest.kt
- `courses: smoother exams questions initializing (fixes #16478)`
  ← model/ExamQuestion.kt
- `courses: smoother progress submissions repositories dao querying (fixes #16484)`
  ← repository/ProgressRepositoryImpl.kt, repository/SubmissionsRepositoryImpl.kt
- `courses: smoother activities repository visiting (fixes #16430)`
  ← repository/ActivitiesRepositoryImpl.kt, test/repository/ActivitiesRepositoryImplTest.kt
- `courses: smoother ratings repository dao aggregating (fixes #16420)`
  ← data/room/dao/RatingDao.kt, repository/RatingsRepositoryImpl.kt, test/repository/RatingsRepositoryImplTest.kt
- `courses: smoother submission view modelling (fixes #16417)`
  ← ui/submissions/SubmissionViewModel.kt, test/ui/submissions/SubmissionViewModelTest.kt
- `courses: smoother exam utils answering (fixes #16350)`
  ← utils/ExamAnswerUtils.kt
- `courses: less submission detail measure is more (fixes #16348)`
  ← ui/submissions/SubmissionDetailFragment.kt
- `courses: smoother resources inline scoping (fixes #16310)`
  ← ui/courses/InlineResourceAdapter.kt, test/ui/courses/InlineResourceAdapterTest.kt
- `courses: smoother base exam markdown caching (fixes #16249)`
  ← base/BaseExamFragment.kt, test/base/BaseExamFragmentTest.kt
- `courses: smoother steps label formatting (fixes #16244)`
  ← ui/courses/TakeCourseFragment.kt
- `courses: smoother submissions repository pdf exporting (fixes #16236)`
  ← repository/SubmissionsRepositoryExporter.kt
- `courses: smoother progress steps handling (fixes #16228)`
  ← ui/courses/CoursesProgressAdapter.kt, test/ui/courses/CoursesProgressAdapterTest.kt
- `courses: smoother inline resources caching (fixes #16225)`
  ← ui/courses/InlineResourceAdapter.kt
- `courses: smoother exam answer utils caching (fixes #16220)`
  ← utils/ExamAnswerUtils.kt, test/utils/ExamAnswerUtilsTest.kt
- `courses: smoother view recycler gliding (fixes #16092)`
  ← ui/courses/CoursesAdapter.kt, test/ui/courses/CoursesAdapterTest.kt
- `courses: smoother submissions repository list flowing (fixes #16163)`
  ← repository/SubmissionsRepositoryImpl.kt
- `courses: smoother submissions repository exporting (fixes #16151)`
  ← repository/SubmissionsRepositoryExporter.kt
- `courses: smoother submissions repository exams starting (fixes #16141)`
  ← model/ExamAnswerData.kt, repository/SubmissionsRepository.kt, repository/SubmissionsRepositoryImpl.kt, ui/exam/ExamTakingFragment.kt, test/repository/SubmissionsRepositoryImplTest.kt
- `courses: smoother ratings repository user querying (fixes #16095)`
  ← repository/RatingsRepository.kt, repository/RatingsRepositoryImpl.kt, ui/courses/CourseDetailViewModel.kt, ui/courses/RatingSummaryProvider.kt, ui/ratings/RatingsViewModel.kt, +3 more
- `courses: smoother progress activities repositories context querying (fixes #16081)`
  ← repository/ActivitiesRepositoryImpl.kt, repository/CoursesRepositoryImpl.kt, repository/ProgressRepositoryImpl.kt, test/repository/ActivitiesRepositoryImplTest.kt, test/repository/ProgressRepositoryImplTest.kt
- `courses: less ui state rating map is more (fixes #16077)`
  ← ui/courses/CoursesFragment.kt, ui/courses/CoursesViewModel.kt, test/ui/courses/CoursesViewModelTest.kt
- `courses: smoother submissions exams view modelling (fixes #16073)`
  ← ui/submissions/SubmissionViewModel.kt
- `courses: smoother base exams regex splitting (fixes #16072)`
  ← base/BaseExamFragment.kt
- `courses: smoother concatenated links saving (fixes #16063)`
  ← model/MyCourse.kt
- `courses: smoother submissions repository detail view modelling (fixes #16059)`
  ← repository/SubmissionsRepository.kt, repository/SubmissionsRepositoryImpl.kt, services/upload/UploadConfigs.kt, ui/submissions/SubmissionDetailViewModel.kt, test/repository/SubmissionsRepositoryImplTest.kt
- `courses: smoother repository step data querying (fixes #16045)`
  ← model/CourseStepData.kt, repository/CoursesRepositoryImpl.kt, ui/courses/CourseStepFragment.kt
- `courses: smoother progress repository data fetching (fixes #16032)`
  ← repository/ProgressRepositoryImpl.kt, test/repository/ProgressRepositoryImplTest.kt
- `courses: smoother submissions repository answers querying (fixes #16023)`
  ← repository/SubmissionsRepositoryImpl.kt
- `courses: smoother exams answers caching (fixes #16022)`
  ← ui/exam/ExamTakingFragment.kt
- `courses: smoother take view modelling (fixes #16015)`
  ← ui/courses/TakeCourseFragment.kt, ui/courses/TakeCourseViewModel.kt, test/ui/courses/TakeCourseViewModelTest.kt
- `courses: smoother layout handling (fixes #16012)`
  ← ui/courses/CoursesFragment.kt
- `courses: smoother progress repository submissions mapping (fixes #16007)`
  ← repository/ProgressRepositoryImpl.kt
- `courses: smoother resources payload adapting (fixes #16002)`
  ← ui/courses/CoursesAdapter.kt, ui/resources/ResourcesAdapter.kt, test/ui/courses/CoursesAdapterTest.kt, test/ui/resources/ResourcesAdapterTest.kt
- `courses: smoother surveys repository exam dao querying (fixes #15997)`
  ← data/room/dao/ExamDao.kt, repository/SurveysRepositoryImpl.kt, test/data/room/dao/ExamDaoTest.kt, test/repository/SurveysRepositoryImplTest.kt
- `courses: smoother progress view modelling (fixes #15995)`
  ← ui/courses/CoursesProgressFragment.kt, ui/courses/ProgressViewModel.kt, test/ui/courses/ProgressViewModelTest.kt
- `courses: smoother repository dao querying (fixes #15987)`
  ← data/room/dao/CourseDao.kt, repository/CoursesRepositoryImpl.kt, test/data/room/dao/CourseDaoTest.kt, test/repository/CoursesRepositoryImplTest.kt
- `courses: smoother progress scrolling (fixes #15553)`
  ← res/layout/activity_course_progress.xml
- `courses: smoother take view modelling (fixes #15800)`
  ← ui/courses/TakeCourseFragment.kt, ui/courses/TakeCourseViewModel.kt
- `courses: smoother steps filter coroutine scoping (fixes #15795)`
  ← ui/courses/CourseFilterController.kt, ui/courses/CourseStepFragment.kt, ui/courses/CoursesFragment.kt, ui/courses/InlineResourceAdapter.kt, utils/ANRWatchdog.kt, +3 more
- `courses: smoother resources caching (fixes #15793)`
  ← ui/courses/CoursesAdapter.kt, ui/courses/CoursesFragment.kt, ui/resources/ResourcesAdapter.kt, ui/resources/ResourcesFragment.kt
- `courses: smoother download dialog handling (fixes #15435)`
  ← base/BaseRecyclerFragment.kt, base/BaseResourceFragment.kt, ui/courses/CoursesFragment.kt, ui/teams/courses/TeamCoursesFragment.kt
- `courses: smoother removed log dao deleting (fixes #15780)`
  ← data/room/dao/RemovedLogDao.kt, repository/CoursesRepositoryImpl.kt, repository/ResourcesRepositoryImpl.kt
- `courses: smoother repository parts matching (fixes #15765)`
  ← repository/CoursesRepositoryImpl.kt
- `courses: smoother surveys refreshing (fixes #15752)`
  ← ui/courses/CoursesAdapter.kt, ui/courses/CoursesFragment.kt, ui/surveys/SurveysAdapter.kt
- `courses: smoother surveys sort views modelling (fixes #15749)`
  ← ui/courses/CoursesViewModel.kt, ui/surveys/SurveysViewModel.kt, test/ui/courses/CoursesViewModelTest.kt, test/ui/surveys/SurveysViewModelTest.kt
- `courses: smoother progress repository state mapping (fixes #15746)`
  ← model/CourseProgressState.kt, repository/ProgressRepository.kt, repository/ProgressRepositoryImpl.kt, ui/courses/CoursesAdapter.kt, ui/courses/CoursesViewModel.kt, +3 more
- `courses: smoother progress repository data fetching (fixes #15735)`
  ← repository/ProgressRepositoryImpl.kt, test/repository/ProgressRepositoryImplTest.kt
- `courses: smoother repository flowing (fixes #15731)`
  ← repository/CoursesRepositoryImpl.kt, test/repository/CoursesRepositoryImplTest.kt
- `courses: smoother view pager listening (fixes #15704)`
  ← ui/courses/TakeCourseFragment.kt, ui/onboarding/OnboardingActivity.kt
- `courses: smoother submissions repository dao bulk inserting (fixes #15707)`
  ← data/room/dao/SubmissionDao.kt, repository/SubmissionsRepositoryImpl.kt, test/repository/SubmissionsRepositoryImplTest.kt
- `courses: smoother repository batch querying (fixes #15703)`
  ← repository/CoursesRepositoryImpl.kt, test/repository/CoursesRepositoryImplTest.kt
- `courses: smoother survey submission syncing (fixes #15593)`
  ← data/room/dao/SubmissionDao.kt, ui/surveys/SurveyFragment.kt
- `courses: smoother empty state controling (fixes #15571)`
  ← ui/courses/CourseFilterController.kt, ui/courses/CoursesFragment.kt, res/layout-land/fragment_my_course.xml, res/layout-sw600dp/fragment_my_course.xml, res/layout/fragment_my_course.xml, +1 more
- `courses: smoother completion rating (fixes #15439)`
  ← ui/courses/TakeCourseFragment.kt, ui/ratings/RatingsFragment.kt, res/layout/fragment_rating.xml
- `courses: smoother grid cover imaging (fixes #15575)`
  ← model/Course.kt, ui/courses/CoursesAdapter.kt, ui/courses/CoursesMapper.kt, res/layout/item_course_grid.xml, res/layout/item_course_list.xml
- `courses: smoother repository leave view modelling (fixes #15156)`
  ← base/BaseRecyclerFragment.kt, data/room/dao/CourseDao.kt, model/MyCourse.kt, repository/CoursesRepository.kt, repository/CoursesRepositoryImpl.kt, +5 more
- `courses: smoother sort toggle view modelling (fixes #15537)`
  ← ui/chat/ChatHistoryAdapter.kt, ui/courses/CoursesAdapter.kt, ui/courses/CoursesFragment.kt, ui/courses/CoursesViewModel.kt, ui/life/LifeAdapter.kt, +2 more
- `courses: smoother repository progess ratings view modelling (fixes #15538)`
  ← repository/CoursesRepository.kt, repository/CoursesRepositoryImpl.kt, ui/courses/CoursesViewModel.kt, ui/courses/TakeCourseViewModel.kt, test/ui/courses/CoursesViewModelTest.kt, +1 more
- `courses: smoother surveys repositories counting (fixes #15473)`
  ← data/room/dao/ExamDao.kt, data/room/dao/SubmissionDao.kt, repository/CoursesRepositoryImpl.kt, repository/SurveysRepositoryImpl.kt, test/repository/CoursesRepositoryImplTest.kt, +1 more
- `courses: smoother progress repository testing (fixes #15497)`
  ← test/repository/ProgressRepositoryImplTest.kt

## resources (41)

- `resources: smoother search utils query normalizing (fixes #16515)`
  ← utils/ResourcesSearchUtils.kt, test/utils/ResourcesSearchUtilsTest.kt
- `resources: smoother storage dialog handling (fixes #16546)`
  ← ui/resources/AddResourceFragment.kt, ui/settings/StorageBreakdownFragment.kt, ui/settings/StorageCategoryDetailFragment.kt
- `resources: smoother collections testing (fixes #16492)`
  ← ui/resources/CollectionsFragment.kt, test/ui/resources/CollectionsFragmentTest.kt
- `resources: smoother repository files downloading (fixes #16493)`
  ← repository/ResourcesRepositoryImpl.kt, test/repository/ResourcesRepositoryImplTest.kt
- `resources: less repository enriched libraries is more (fixes #16453)`
  ← repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, test/repository/ResourcesRepositoryImplTest.kt
- `resources: smoother repository dao querying (fixes #16371)`
  ← data/room/dao/MyLibraryDao.kt, repository/ResourcesRepositoryImpl.kt, test/repository/ResourcesRepositoryImplTest.kt
- `resources: smoother grid dark mode searching (fixes #16129)`
  ← res/layout/layout_search_pill.xml, res/values-night/colors.xml
- `resources: smoother filtering (fixes #16102)`
  ← ui/resources/ResourcesAdapter.kt, ui/resources/ResourcesFragment.kt, res/layout-land/fragment_my_library.xml, res/layout-sw600dp/fragment_my_library.xml, res/layout/fragment_my_library.xml, +6 more
- `resources: smoother filter initializing (fixes #16268)`
  ← ui/resources/ResourcesFilterFragment.kt
- `resources: smoother viewer text truncating (fixes #673)`
  ← ui/viewer/ResourceViewerFragment.kt, res/values-ar/strings.xml, res/values-es/strings.xml, res/values-fr/strings.xml, res/values-ne/strings.xml, +2 more
- `resources: smoother view modelling (fixes #16213)`
  ← ui/resources/ResourcesFragment.kt, ui/resources/ResourcesViewModel.kt, test/ui/resources/ResourcesViewModelTest.kt
- `resources: smoother collections parent tagging (fixes #16246)`
  ← ui/resources/CollectionsFragment.kt
- `resources: smoother search utils filtering (fixes #16245)`
  ← ui/resources/ResourcesFragment.kt, utils/ResourcesSearchUtils.kt, test/utils/ResourcesSearchUtilsTest.kt
- `resources: smoother collections view modelling (fixes #16238)`
  ← ui/resources/CollectionsViewModel.kt
- `resources: less apply filter button is more (fixes #16091)`
  ← ui/resources/ResourcesFilterFragment.kt, res/layout/fragment_library_filter.xml, test/ui/resources/ResourcesFilterFragmentTest.kt
- `resources: smoother repository detail querying (fixes #16143)`
  ← repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, ui/resources/ResourceDetailFragment.kt, res/values-ar/strings.xml, res/values-es/strings.xml, +5 more
- `resources: smoother tagging (fixes #16067)`
  ← ui/resources/ResourcesTagsAdapter.kt
- `resources: smoother title view modelling (fixes #15941)`
  ← ui/resources/ResourcesViewModel.kt, test/ui/resources/ResourcesViewModelTest.kt
- `resources: smoother repository facets filtering (fixes #16048)`
  ← repository/ResourcesRepositoryImpl.kt
- `resources: smoother repository dashboard view modelling (fixes #16031)`
  ← data/room/dao/MyLibraryDao.kt, repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, ui/dashboard/DashboardViewModel.kt, test/ui/dashboard/DashboardViewModelTest.kt
- `resources: smoother collections tag data querying (fixes #16041)`
  ← ui/resources/CollectionsFragment.kt
- `resources: smoother repository image url querying (fixes #16035)`
  ← repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, repository/VoicesRepository.kt, repository/VoicesRepositoryImpl.kt, ui/voices/NewsViewModel.kt, +3 more
- `resources: smoother collections view modelling (fixes #16028)`
  ← ui/resources/CollectionsFragment.kt, ui/resources/CollectionsViewModel.kt, test/ui/resources/CollectionsViewModelTest.kt
- `resources: smoother layout handling (fixes #16016)`
  ← ui/resources/ResourcesFragment.kt
- `resources: smoother repository offline dao marking (fixes #16003)`
  ← data/room/dao/MyLibraryDao.kt, repository/ResourcesRepositoryImpl.kt
- `resources: smoother feedback personals repositories flowing (fixes #15998)`
  ← repository/FeedbackRepositoryImpl.kt, repository/PersonalsRepositoryImpl.kt, repository/ResourcesRepositoryImpl.kt, utils/FlowExtensions.kt, test/repository/FeedbackRepositoryImplTest.kt, +2 more
- `resources: smoother viewer video handling (fixes #15985)`
  ← ui/viewer/ResourceViewerFragment.kt
- `resources: smoother web view nested entry pathing (fixes #15634)`
  ← base/BaseContainerFragment.kt, data/room/AppDatabase.kt, model/MyLibrary.kt, ui/viewer/WebViewActivity.kt, utils/FileUtils.kt, +2 more
- `resources: smoother repository inserting (fixes #15812)`
  ← repository/ResourcesRepositoryImpl.kt, test/repository/ResourcesRepositoryImplTest.kt
- `resources: smoother list grid toggling (fixes #15572)`
  ← ui/resources/ResourcesFragment.kt
- `resources: smoother payload notifying (fixes #15753)`
  ← ui/courses/CoursesAdapter.kt, ui/resources/ResourcesAdapter.kt
- `resources: smoother search view modelling (fixes #15743)`
  ← ui/resources/ResourcesFragment.kt, ui/resources/ResourcesViewModel.kt
- `resources: smoother viewer view modelling (fixes #15729)`
  ← ui/viewer/ResourceViewerFragment.kt, ui/viewer/ResourceViewerViewModel.kt
- `resources: smoother thumbnail preview loading (fixes #15574)`
  ← MainApplication.kt, base/BaseAdapterFactory.kt, ui/courses/InlineResourceAdapter.kt, ui/resources/ResourcesAdapter.kt, ui/resources/ResourcesFragment.kt, +5 more
- `resources: smoother content item callback diffing (fixes #15702)`
  ← ui/resources/ResourcesAdapter.kt
- `resources: smoother guest all selecting (fixes #15514)`
  ← ui/resources/ResourcesFragment.kt
- `resources: smoother list  filter icon spacing (fixes #15438)`
  ← res/layout-land/fragment_my_course.xml, res/layout-land/fragment_my_library.xml, res/layout/fragment_my_course.xml, res/layout/fragment_my_library.xml
- `resources: smoother repository pending downloading (fixes #15557)`
  ← data/room/dao/MyLibraryDao.kt, repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, test/repository/ResourcesRepositoryImplTest.kt
- `resources: smoother repository offline item category detail storing (fixes #15545)`
  ← model/OfflineResourceItem.kt, repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, ui/settings/StorageCategoryDetailFragment.kt, test/repository/ResourcesRepositoryBenchmarkTest.kt, +2 more
- `resources: smoother repository retrieval testing (fixes #15541)`
  ← test/repository/ResourcesRepositoryImplTest.kt
- `resources: smoother retry repositories settings view modelling (fixes #15476)`
  ← repository/ResourcesRepository.kt, repository/ResourcesRepositoryImpl.kt, repository/RetryRepository.kt, repository/RetryRepositoryImpl.kt, services/retry/RetryQueue.kt, +5 more

## actions (28)

- `actions: smoother workflow release versioning (fixes #16349)`
  ← .github/workflows/release.yml
- `actions: smoother workflow automerge coauthoring (fixes #16375)`
  ← .github/scripts/coauthors.sh
- `actions: smoother workflow automerge playstore resuming (fixes #16629)`
  ← .github/scripts/automerge.sh, .github/scripts/playstore.sh, .github/workflows/automerge.yml, .github/workflows/playstore.yml, CLAUDE.md
- `actions: smoother workflow automerge pr picking (fixes #16379)`
  ← .github/scripts/automerge.sh
- `actions: smoother labels workflow handling (fixes #16316)`
  ← .github/workflows/labels.yml
- `actions: smoother workflow automerging (fixes #16301)`
  ← .github/workflows/automerge.yml
- `actions: smoother workflow release caching (fixes #16297)`
  ← .github/workflows/release.yml
- `actions: smoother coderabbit reviewing (fixes #16287)`
  ← .coderabbit.yaml, docs/AGENT_SPELLBOOK.md, docs/CODE_STYLE_GUIDE.md
- `actions: smoother workflow labeling (fixes #16289)`
  ← .github/scripts/labels.sh, .github/workflows/labels.yml, CLAUDE.md
- `actions: smoother gradle configuring (fixes #16250)`
  ← gradle.properties
- `actions: bump `actions/upload-artifact` to 7 (fixes #16240)`
  ← .github/workflows/test.yml
- `actions: smoother workflow test timing (fixes #16239)`
  ← .github/scripts/test_timing_summary.py
- `actions: smoother workflows playstore automerge priority queuing (fixes #16263)`
  ← .github/scripts/automerge.sh, .github/scripts/playstore-quota.sh, .github/scripts/playstore.sh, .github/workflows/automerge.yml, .github/workflows/playstore.yml, +1 more
- `actions: smoother workflow test caching (fixes #16156)`
  ← .github/workflows/test.yml
- `actions: smoother workflow building (fixes #16216)`
  ← .github/workflows/build.yml
- `actions: smoother automerge conflict handling (fixes #16252)`
  ← .github/scripts/automerge.sh, .github/workflows/automerge.yml, CLAUDE.md
- `actions: smoother workflows skipping (fixes #16166)`
  ← .github/workflows/build.yml, .github/workflows/test.yml
- `actions: smoother test workflow handling (fixes #16155)`
  ← .github/workflows/test.yml
- `actions: smoother dependabot configuring (fixes #16152)`
  ← .github/dependabot.yml
- `actions: smoother playstore quota handling (fixes #16146)`
  ← .github/scripts/automerge.sh, .github/scripts/playstore-quota.sh, .github/scripts/playstore.sh, .github/workflows/automerge.yml, .github/workflows/playstore.yml, +2 more
- `actions: smoother robolectric sdk prefetching (fixes #15935)`
  ← .github/workflows/test.yml, CLAUDE.md, docs/TESTING.md
- `actions: smoother workflow automerge base judging (fixes #15829)`
  ← .github/scripts/automerge.sh, .github/workflows/automerge.yml
- `actions: smoother workflow automerge release retrying (fixes #15814)`
  ← .github/scripts/automerge.sh, .github/workflows/automerge.yml, CLAUDE.md
- `actions: bump `actions/cache` from 4 to 6 (fixes #15788)`
  ← .github/workflows/build.yml, .github/workflows/test.yml
- `actions: smoother workflow automerge playstore quota handling (fixes #15790)`
  ← .github/scripts/automerge.sh, .github/workflows/automerge.yml, .github/workflows/release.yml
- `actions: smoother workflow automerge drain cancelling (fixes #15561)`
  ← .github/scripts/automerge.sh, .github/workflows/release.yml
- `actions: smoother workflow test sharding (fixes #15721)`
  ← .github/scripts/test_timing_summary.py, .github/workflows/build.yml, .github/workflows/test.yml, CLAUDE.md, test/services/DownloadServiceTest.kt, +3 more
- `actions: smoother workflow automerge retrying (fixes #15713)`
  ← .github/scripts/automerge.sh, test/services/UploadToShelfServiceTest.kt, test/utils/SecurePrefsTest.kt

## life (26)

- `life: smoother user repository view modelling (fixes #16575)`
  ← repository/UserRepository.kt, repository/UserRepositoryImpl.kt, ui/life/LifeViewModel.kt, test/repository/UserRepositoryImplTest.kt, test/ui/life/LifeViewModelTest.kt
- `life: smoother repository dao visibility filtering (fixes #16447)`
  ← data/room/dao/MyLifeDao.kt, repository/LifeRepositoryImpl.kt, test/repository/LifeRepositoryImplTest.kt
- `life: smoother dictionary repository inserting (fixes #16434)`
  ← repository/DictionaryRepositoryImpl.kt, test/repository/DictionaryRepositoryImplTest.kt
- `life: smoother achievements references info handling (fixes #16446)`
  ← ui/user/EditAchievementFragment.kt
- `life: smoother personals repository dao deleting (fixes #16431)`
  ← data/room/dao/PersonalDao.kt, repository/PersonalsRepositoryImpl.kt, test/repository/PersonalsRepositoryImplTest.kt
- `life: smoother health search view modelling (fixes #16454)`
  ← ui/health/HealthViewModel.kt, ui/health/MyHealthFragment.kt, test/ui/health/HealthSearchDebounceTest.kt, test/ui/health/HealthViewModelTest.kt
- `life: smoother key deduping (fixes #16435)`
  ← repository/LifeRepositoryImpl.kt, test/repository/LifeRepositoryImplTest.kt
- `life: smoother achievements model caching (fixes #16355)`
  ← model/Achievement.kt, test/model/AchievementTest.kt
- `life: smoother achievements editing (fixes #16253)`
  ← ui/user/EditAchievementFragment.kt, res/layout/fragment_edit_achievement.xml, test/ui/user/EditAchievementFragmentTest.kt
- `life: smoother health examining (fixes #1939)`
  ← ui/health/HealthExaminationActivity.kt
- `life: smoother health view binding (fixes #16233)`
  ← ui/health/AddHealthActivity.kt
- `life: smoother dashboard plugin view modelling (fixes #16231)`
  ← model/MyLife.kt, ui/dashboard/DashboardPluginFragment.kt, ui/life/LifeViewModel.kt
- `life: smoother personals repository serializing (fixes #16224)`
  ← model/Personal.kt, repository/PersonalsRepositoryImpl.kt, test/model/PersonalTest.kt
- `life: smoother health examination handling (fixes #16169)`
  ← ui/health/HealthExaminationAdapter.kt
- `life: smoother repository view modelling (fixes #16162)`
  ← repository/LifeRepositoryImpl.kt, ui/life/LifeViewModel.kt, test/repository/LifeRepositoryImplTest.kt, test/repository/LifeRepositoryTest.kt
- `life: smoother personals repository querying (fixes #16148)`
  ← repository/PersonalsRepositoryImpl.kt, test/repository/PersonalsRepositoryImplTest.kt
- `life: smoother health examination blood pressure handling (fixes #16076)`
  ← ui/health/HealthExaminationActivity.kt
- `life: smoother personals resources opening (fixes #16070)`
  ← ui/personals/PersonalsAdapter.kt
- `life: smoother personals repository dao querying (fixes #16019)`
  ← data/room/dao/PersonalDao.kt, repository/PersonalsRepositoryImpl.kt, test/repository/PersonalsRepositoryImplTest.kt
- `life: smoother health examination view modelling (fixes #15986)`
  ← ui/health/HealthExaminationActivity.kt, ui/health/HealthExaminationViewModel.kt, test/ui/health/HealthExaminationViewModelTest.kt
- `life: smoother health examination dispatcher providing (fixes #15740)`
  ← ui/health/HealthExaminationAdapter.kt, ui/health/MyHealthFragment.kt
- `life: smoother list adapter caching (fixes #15739)`
  ← ui/life/LifeFragment.kt
- `life: smoother health user repositories view modelling (fixes #15563)`
  ← repository/HealthRepository.kt, repository/HealthRepositoryImpl.kt, repository/UserRepository.kt, repository/UserRepositoryImpl.kt, ui/health/HealthViewModel.kt, +2 more
- `life: smoother options visibility updating (fixes #15236)`
  ← base/BaseDashboardFragment.kt, model/MyLife.kt, ui/life/LifeAdapter.kt
- `life: smoother repository dashboard seeding (fixes #15521)`
  ← base/BaseDashboardFragment.kt, repository/LifeRepositoryImpl.kt
- `life: smoother health repository testing (fixes #15491)`
  ← test/repository/HealthRepositoryImplTest.kt

## login (23)

- `login: smoother configurations repository server availability checking (fixes #16538)`
  ← repository/ConfigurationsRepositoryImpl.kt, test/repository/ConfigurationsRepositoryImplTest.kt
- `login: smoother achievements payload handling (fixes #16523)`
  ← ui/user/AchievementsAdapter.kt, test/ui/user/AchievementsAdapterTest.kt
- `login: smoother activities repository bulk inserting (fixes #16511)`
  ← repository/ActivitiesRepositoryImpl.kt, test/repository/ActivitiesRepositoryImplTest.kt
- `login: smoother achievements editing (fixes #16407)`
  ← ui/user/EditAchievementFragment.kt
- `login: smoother sync back press handling (fixes #16273)`
  ← ui/sync/SyncActivity.kt, res/values-ar/strings.xml, res/values-es/strings.xml, res/values-fr/strings.xml, res/values-ne/strings.xml, +2 more
- `login: smoother activities repository serializing (fixes #16281)`
  ← repository/ActivitiesRepositoryImpl.kt
- `login: smoother form submitting (fixes #16267)`
  ← ui/sync/LoginActivity.kt
- `login: smoother settings text capitalizing (fixes #16130)`
  ← res/values/strings.xml
- `login: smoother teams members view modelling (fixes #16243)`
  ← ui/sync/LoginViewModel.kt
- `login: smoother url utils handling (fixes #16237)`
  ← services/sync/LoginSyncManager.kt, utils/UrlUtils.kt
- `login: smoother onboarding (fixes #16232)`
  ← ui/onboarding/OnboardingActivity.kt
- `login: smoother auth session updating (fixes #16222)`
  ← data/auth/AuthSessionUpdater.kt, test/data/auth/AuthSessionUpdaterTest.kt
- `login: smoother server dialog extensions url handling (fixes #16075)`
  ← ui/sync/ServerDialogExtensions.kt
- `login: smoother settings shared preference managing (fixes #16030)`
  ← services/SharedPrefManager.kt, ui/settings/SettingsActivity.kt
- `login: smoother storage breakdown indexing (fixes #16026)`
  ← ui/settings/StorageBreakdownFragment.kt
- `login: smoother storage category view modelling (fixes #16004)`
  ← ui/settings/StorageCategoryDetailFragment.kt, ui/settings/StorageCategoryViewModel.kt
- `login: smoother learner registering (fixes #15556)`
  ← ui/user/BecomeMemberActivity.kt
- `login: smoother configurations repository provisioning (fixes #15811)`
  ← repository/ConfigurationsRepository.kt, repository/ConfigurationsRepositoryImpl.kt, ui/sync/SyncActivity.kt, test/repository/ConfigurationsRepositoryImplTest.kt
- `login: smoother user repository dao querying (fixes #15791)`
  ← data/room/dao/UserDao.kt, repository/UserRepositoryImpl.kt, test/data/room/dao/UserDaoTest.kt, test/repository/UserRepositoryBulkInsertTest.kt
- `login: smoother configurations repository io wrapping (fixes #15778)`
  ← repository/ConfigurationsRepositoryImpl.kt
- `login: smoother user profile landscaping (fixes #15551)`
  ← ui/user/UserProfileFragment.kt, res/layout-land/fragment_user_profile.xml, res/layout-large-land/fragment_user_profile.xml, res/layout-normal-land/fragment_user_profile.xml, res/layout/fragment_user_profile.xml, +2 more
- `login: smoother feedback flow collecting (fixes #15566)`
  ← ui/dictionary/DictionaryActivity.kt, ui/feedback/FeedbackDetailActivity.kt, ui/sync/LoginActivity.kt
- `login: less settings edges is more (fixes #15257)`
  ← ui/settings/SettingsActivity.kt, res/xml/pref.xml

## dashboard (17)

- `dashboard: smoother navigating (fixes #16613)`
  ← ui/dashboard/DashboardElementActivity.kt, test/ui/dashboard/DashboardElementActivityNavigationTest.kt
- `dashboard: smoother voice date count querying (fixes #16455)`
  ← data/room/dao/NewsDao.kt, repository/VoicesRepository.kt, repository/VoicesRepositoryImpl.kt, ui/dashboard/DashboardViewModel.kt, test/data/room/dao/NewsDaoTest.kt, +2 more
- `dashboard: smoother surveys text coloring (fixes #16522)`
  ← ui/dashboard/DashboardSurveysAdapter.kt, test/ui/dashboard/DashboardSurveysAdapterTest.kt
- `dashboard: smoother bell sync status refreshing (fixes #16272)`
  ← ui/dashboard/BellDashboardFragment.kt, ui/dashboard/DashboardActivity.kt
- `dashboard: smoother activities repository offline logins flowing (fixes #16215)`
  ← repository/ActivitiesRepository.kt, repository/ActivitiesRepositoryImpl.kt, ui/dashboard/ActivitiesFragment.kt, test/repository/ActivitiesRepositoryImplTest.kt, test/ui/dashboard/ActivitiesFragmentTest.kt, +1 more
- `dashboard: smoother courses shelf handling (fixes #15727)`
  ← base/BaseDashboardFragment.kt, ui/dashboard/BellDashboardFragment.kt
- `dashboard: smoother activities view modelling (fixes #16205)`
  ← ui/dashboard/ActivitiesFragment.kt, ui/dashboard/ActivitiesViewModel.kt, test/ui/dashboard/ActivitiesViewModelTest.kt
- `dashboard: smoother activities fragment date format caching (fixes #16054)`
  ← ui/dashboard/ActivitiesFragment.kt
- `dashboard: smoother activities monthly counting (fixes #16052)`
  ← ui/dashboard/ActivitiesFragment.kt
- `dashboard: smoother base resources navigating (fixes #15728)`
  ← base/BaseDashboardFragment.kt, ui/dashboard/BellDashboardFragment.kt, res/layout-sw600dp/home_card_library.xml, res/layout/home_card_library.xml, test/ui/resources/ResourcesViewModelTest.kt
- `dashboard: smoother bell view modelling (fixes #15744)`
  ← ui/dashboard/BellDashboardFragment.kt, ui/dashboard/BellDashboardViewModel.kt, test/ui/dashboard/BellDashboardViewModelTest.kt
- `dashboard: smoother activities chart landscaping (fixes #15552)`
  ← ui/dashboard/ActivitiesFragment.kt, res/layout-land/fragment_activities.xml, res/layout/fragment_activities.xml, test/ui/dashboard/ActivitiesFragmentTest.kt
- `dashboard: smoother responsive layout handling (fixes #15524)`
  ← app/src/main/AndroidManifest.xml, base/BaseDashboardFragment.kt, ui/dashboard/BellDashboardFragment.kt, ui/dashboard/DashboardActivity.kt, ui/dashboard/DashboardPluginFragment.kt, +41 more
- `dashboard: smoother sync message spacing (fixes #15122)`
  ← res/values/strings.xml
- `dashboard: smoother placeholder wording (fixes #15522)`
  ← res/values-ar/strings.xml, res/values-es/strings.xml, res/values-fr/strings.xml, res/values-ne/strings.xml, res/values-so/strings.xml, +1 more
- `dashboard: smoother user repository gson injecting (fixes #15539)`
  ← repository/UserRepositoryImpl.kt, test/repository/EventsRepositoryImplTest.kt
- `dashboard: smoother guest offline visiting (fixes #15213)`
  ← ui/dashboard/DashboardActivity.kt, res/layout/banner_offline_visit_warning.xml, res/values-ar/strings.xml, res/values-es/strings.xml, res/values-fr/strings.xml, +3 more

## enterprises (14)

- `enterprises: smoother finances totals view modelling (fixes #16586)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt, ui/enterprises/EnterprisesFinancesViewModel.kt, test/ui/enterprises/EnterprisesFinancesViewModelTest.kt
- `enterprises: smoother repository reports csv view modelling (fixes #16374)`
  ← repository/EnterprisesRepository.kt, repository/EnterprisesRepositoryImpl.kt, ui/enterprises/EnterprisesReportsFragment.kt, ui/enterprises/EnterprisesViewModel.kt, test/repository/EnterprisesRepositoryImplTest.kt
- `enterprises: smoother repository report flowing (fixes #16354)`
  ← repository/EnterprisesRepositoryImpl.kt, test/repository/EnterprisesRepositoryImplTest.kt
- `enterprises: smoother finances string comparisons handling (fixes #16285)`
  ← ui/enterprises/EnterprisesFinancesAdapter.kt, ui/enterprises/EnterprisesFinancesFragment.kt
- `enterprises: smoother teams repositories view modelling (fixes #16212)`
  ← di/RepositoryModule.kt, repository/EnterprisesRepository.kt, repository/EnterprisesRepositoryImpl.kt, repository/TeamsFinancesRepository.kt, repository/TeamsRepositoryImpl.kt, +2 more
- `enterprises: smoother finances transaction view modelling (fixes #16145)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt, ui/enterprises/EnterprisesFinancesViewModel.kt, test/ui/enterprises/EnterprisesFinancesViewModelTest.kt
- `enterprises: smoother finances view binding (fixes #16142)`
  ← ui/enterprises/EnterprisesFinancesAdapter.kt
- `enterprises: smoother finances landscaping (fixes #15577)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt, res/layout/add_transaction.xml, res/layout/dialog_add_transaction.xml, res/layout/fragment_finance.xml, res/layout/header_finance.xml, +6 more
- `enterprises: smoother finances date filter resetting (fixes #15767)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt
- `enterprises: smoother finances date filtering (fixes #15766)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt
- `enterprises: smoother glide request managing (fixes #15774)`
  ← ui/courses/CoursesAdapter.kt, ui/enterprises/EnterprisesFinancesAdapter.kt, ui/enterprises/EnterprisesReportsAdapter.kt
- `enterprises: smoother members reports payload diffing (fixes #15737)`
  ← ui/enterprises/EnterprisesReportsAdapter.kt, ui/teams/members/MembersAdapter.kt, test/ui/enterprises/EnterprisesReportsAdapterTest.kt, test/ui/teams/members/MembersAdapterTest.kt
- `enterprises: smoother finances date picking (fixes #15518)`
  ← ui/enterprises/EnterprisesFinancesFragment.kt
- `enterprises: smoother csv export date caching (fixes #15501)`
  ← ui/enterprises/EnterprisesReportsFragment.kt

## community (8)

- `community: smoother configurations repository tab views modelling (fixes #16326)`
  ← repository/ConfigurationsRepository.kt, repository/ConfigurationsRepositoryImpl.kt, ui/community/CommunityTabViewModel.kt, ui/community/HomeCommunityDialogFragment.kt, ui/community/LeadersViewModel.kt, +5 more
- `community : smoother tab pager adapting (fixes #16308)`
  ← ui/community/CommunityPagerAdapter.kt, ui/community/CommunityTabFragment.kt, ui/community/HomeCommunityDialogFragment.kt
- `community: smoother voices view modelling (fixes #16165)`
  ← ui/voices/VoicesViewModel.kt
- `community: smoother tab view modelling (fixes #16066)`
  ← ui/community/CommunityTabFragment.kt, ui/community/CommunityTabViewModel.kt
- `community: smoother leaders view modelling (fixes #16037)`
  ← ui/community/LeadersFragment.kt, ui/community/LeadersViewModel.kt
- `community: smoother home dialog handling (fixes #16024)`
  ← ui/community/HomeCommunityDialogFragment.kt
- `community: smoother voices showing (fixes #15695)`
  ← repository/VoicesRepositoryImpl.kt, ui/voices/VoicesFragment.kt, test/repository/VoicesRepositoryImplTest.kt
- `community: smoother type shared preferences handling (fixes #15474)`
  ← repository/ConfigurationsRepository.kt, repository/ConfigurationsRepositoryImpl.kt, repository/TeamsRepository.kt, repository/TeamsRepositoryImpl.kt, ui/community/CommunityPagerAdapter.kt, +4 more

## chat (8)

- `chat: smoother history caching (fixes #16448)`
  ← ui/chat/ChatHistoryAdapter.kt
- `chat: smoother history view binding (fixes #16415)`
  ← ui/chat/ChatHistoryAdapter.kt, test/ui/chat/ChatHistoryAdapterTest.kt
- `chat: smoother history view modelling (fixes #16319)`
  ← ui/chat/ChatHistoryFragment.kt, ui/chat/ChatViewModel.kt, test/ui/chat/ChatViewModelTest.kt
- `chat: smoother clipboard caching (fixes #16518)`
  ← ui/chat/ChatAdapter.kt, test/ui/chat/ChatAdapterTest.kt
- `chat: smoother repository search view modelling (fixes #16084)`
  ← repository/ChatRepository.kt, repository/ChatRepositoryImpl.kt, ui/chat/ChatViewModel.kt, test/repository/ChatRepositoryImplTest.kt, test/repository/ChatRepositoryTest.kt, +1 more
- `chat: smoother api dispatcher providing (fixes #16050)`
  ← data/api/ChatApiService.kt, test/data/api/ChatApiServiceTest.kt
- `chat: smoother history ai provider view modelling (fixes #15999)`
  ← ui/chat/ChatDetailFragment.kt, ui/chat/ChatHistoryFragment.kt, ui/chat/ChatViewModel.kt, test/ui/chat/ChatViewModelTest.kt
- `chat: smoother detail ui state view modelling (fixes #15776)`
  ← ui/chat/ChatDetailFragment.kt, ui/chat/ChatViewModel.kt, test/ui/chat/ChatViewModelTest.kt

## lifel (1)

- `lifel: smoother personals repository device name providing (fixes #16433)`
  ← repository/PersonalsRepositoryImpl.kt, utils/DeviceNameProvider.kt, test/repository/PersonalsRepositoryImplTest.kt

