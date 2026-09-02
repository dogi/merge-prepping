# Title corpus — planet, the last 500 merged PRs

Generated from the 500 most recent squash commits on `master` (`bef1977`, PR #10363 / issue #10362, back to `cea7e5a`, PR #8777 / issue #8776).
Each line pairs the landed title with the changed files that produced it — **the changed files are the primary input to the title**. Skim for the nearest precedent by scope, then by the area of the files you changed.

Path shorthand: bare paths are under `src/app/`; everything else is written from the repo root.
Omitted from every entry: `package-lock.json`, `package.json` — the per-PR version bump, present in nearly every diff.

The trailing `(#NNNN)` GitHub appends at squash time is stripped: what you see here is what the PR title was.

Regenerate with:

```
scripts/build-corpus.py --repo <checkout> --name planet --strip src/app/ --skip package.json --skip package-lock.json
```

## Shape of the window

- **Shape shares:** `smoother` 458/500 (91%), `less … is more` 32, `bump` 9, other 1.
- **Scope league table:** `all` 148 · `teams` 91 · `manager` 72 · `courses` 57 · `community` 25 · `dashboard` 22 · `actions` 20 · `resources` 20 · `chat` 16 · `life` 12 · `login` 10 · `mylife` 4 · `enterprises` 3.
- **Gerund league table:** handling 91 · navigating 12 · filtering 11 · linting 10 · aligning 10 · formatting 9 · styling 8 · loading 8 · showing 7 · paginating 7 · linking 7 · creating 7 · building 7 · validating 6 · testing 5 · selecting 5 · hovering 4 · padding 4 · viewing 4 · spacing 4 · reporting 4 · routing 4 · removing 3 · confirming 3.
- **Issue link:** `fixes` 468, `connects` 27, well-formed 494/500.
- **Diff size:** 166/500 diffs touch a single file beyond the version bump, 329/500 touch three or fewer.
- **⚠️ The gerund era starts 2025-10-14.** The trailing gerund is not uniform across this window: of the 350 `smoother` titles from 2025-10-14 onward, 343 end in one (98%) — but of the 108 before it, only 23 do (21%). Older titles stop at a bare noun phrase. **Take precedent from the recent half.** The older entries are kept because their scope and noun-phrase choices are still good evidence; their missing gerunds are not.
- **Malformed or link-less titles in this window:**
  - `teams: smoother voices icon aligning (#9787)`
  - `login: smoother dialogs handling (#9796)`
  - `all: smoother typed forms handling (closes #9047)`
  - `all: less material legacy core is more (closes #9166)`
  - `all: smoother profile image styling (fixes: #9423)`
  - `all: smoother linting (fixes 9105)`

## all (148)

- `all: smoother arrow body style linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, community/community.component.ts, configuration/configuration.component.ts, configuration/configuration.service.ts, +47 more
- `all: smoother quote props linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, app.component.ts, chat/chat-sidebar/chat-sidebar.component.ts, chat/chat-window/chat-window.component.ts, +87 more
- `all: smoother configuration patching (fixes #10341)`
  ← configuration/configuration.component.ts, configuration/configuration.service.spec.ts, configuration/configuration.service.ts, manager-dashboard/manager-aiservices.component.ts, manager-dashboard/manager-currency.component.ts, +2 more
- `all: smoother collections truncating (fixes #10343)`
  ← shared/forms/planet-tag-input-dialog.component.html, shared/forms/planet-tag-input-dialog.component.ts, shared/forms/planet-tag-input-dialog.scss
- `all: smoother collection title handling (fixes #10325)`
  ← shared/forms/planet-tag-input.component.html, shared/forms/planet-tag-input.scss, src/styles.scss
- `all: smoother notifications unread indicating (fixes #10284)`
  ← notifications/notifications.component.html, notifications/notifications.component.scss, notifications/notifications.component.ts
- `all: smoother search clearing (fixes #10199) (fixes #10200)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.component.ts, community/community.component.html, community/community.component.ts, courses/courses.component.html, +23 more
- `all: smoother coderabbit reviewing (fixes #10348)`
  ← .coderabbit.yaml
- `all: smoother user profile dialog focusing (fixes #10184)`
  ← courses/progress-courses/courses-progress-leader.component.ts, manager-dashboard/reports/reports-detail.component.ts, meetups/view-meetups/meetups-view.component.ts, news/news-list-item.component.ts, tasks/tasks.component.spec.ts, +6 more
- `all: smoother members deactivation confirming (fixes #10292)`
  ← shared/dialogs/dialogs-prompt.component.html, users/users-table.component.html, users/users-table.component.spec.ts, users/users-table.component.ts, users/users.service.ts
- `all: smoother prefer arrow const linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, dashboard/dashboard.component.spec.ts, home/home-router.module.ts, resources/resources-add.component.ts, +7 more
- `all: smoother one var linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, courses/courses.component.ts, home/home.component.spec.ts, login/login.component.spec.ts, +4 more
- `all: smoother object shorthand linting (connects #9082)`
  ← eslint.config.mjs, chat/chat-sidebar/chat-sidebar.component.ts, community/community.component.ts, courses/courses.service.ts, courses/progress-courses/courses-progress-leader.component.ts, +16 more
- `all: smoother requests table column sizing (fixes #10229)`
  ← _mixins.scss, courses/courses.scss, manager-dashboard/requests/requests-table.component.html, manager-dashboard/requests/requests-table.component.scss, manager-dashboard/requests/requests-table.component.ts, +8 more
- `all: smoother notification planet scoping (fixes #10205)`
  ← home/home.component.ts, news/news-list-item.component.spec.ts, news/news-list-item.component.ts, notifications/notifications.component.ts, notifications/notifications.service.spec.ts, +3 more
- `all: smoother eqeqeq less underscore linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, chat/chat-sidebar/chat-sidebar.component.ts, courses/add-courses/courses-add.component.ts, courses/courses.component.html, +21 more
- `all: smoother markdown read only rendering (fixes #10162)`
  ← exams/exams-view.component.html, exams/exams-view.component.ts, exams/public-surveys/public-survey.component.html, exams/public-surveys/public-survey.component.ts, health/health-event-dialog.component.html, +22 more
- `all: smoother auto side navigating (fixes #10222)`
  ← home/home.component.html, home/home.component.spec.ts, home/home.component.ts
- `all: smoother feedback forms saving (fixes #10201)`
  ← feedback/feedback.directive.ts, shared/dialogs/dialogs-form.component.html, shared/dialogs/dialogs-form.component.ts, shared/dialogs/dialogs-form.service.ts
- `all: smoother profiles keyboard navigating (fixes #10168)`
  ← courses/progress-courses/courses-progress-chart.component.html, courses/progress-courses/courses-progress-chart.component.ts, manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.component.ts, meetups/view-meetups/meetups-view.component.html, +9 more
- `all: smoother agents assisting (fixes #10270)`
  ← .agents/skills/merge-prepping, .claude/settings.json, .github/copilot-instructions.md, .github/workflows/automerge.yml, .gitmodules, +4 more
- `all: smoother delete buttons styling (fixes #10170)`
  ← manager-dashboard/certifications/certifications.component.html, manager-dashboard/reports/pending-table.component.html, shared/forms/planet-step-list.component.html, shared/forms/planet-tag-input-dialog.component.html, teams/teams-view.component.html, +3 more
- `all: smoother user profile language handling (fixes #10157)`
  ← home/home.component.html
- `all: smoother markdown fullscreen handling (fixes #10145)`
  ← shared/forms/planet-markdown-textbox.component.spec.ts, shared/forms/planet-markdown-textbox.component.ts, shared/forms/planet-markdown-textbox.scss
- `all: smoother android app promoting (fixes #10221)`
  ← exams/public-surveys/public-survey.component.ts, home/home.component.html, home/home.component.ts, home/home.scss, shared/android-app-prompt.service.spec.ts, +8 more
- `all: smoother profile picture uploading (fixes #10136)`
  ← users/users-update/users-update.component.html
- `all: smoother users role selecting (fixes #10069)`
  ← users/users.component.html, users/users.component.scss, users/users.component.ts, src/styles.scss
- `all: smoother markdown form textbox handling (fixes #10074)`
  ← shared/forms/planet-markdown-textbox.component.ts, shared/forms/planet-markdown-textbox.scss
- `all: smoother system variables handling (fixes #10057)`
  ← _variables.scss, chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.scss, chat/chat-window/chat-window.scss, community/community.scss, +25 more
- `all: smoother chat navigating (fixes #10128)`
  ← home/home.component.html
- `all: smoother pouchdb git ignoring (fixes #10121)`
  ← .gitignore
- `all: smoother package json locking (fixes #9991)`
  ← .github/workflows/planet.yml, .gitignore, docker/gateway/Dockerfile, docker/planet/pre-builder-Dockerfile, docker/planet/scripts/check_dependencies.sh, +1 more
- `all: smoother translating (fixes #9451)`
  ← AGENTS.md, README.md, angular.json, scripts/dev-env.sh, scripts/i18n-normalize.mjs, +79 more
- `all: smoother feedback page parameters handling (fixes #10034)`
  ← feedback/feedback.directive.spec.ts, feedback/feedback.directive.ts
- `all: smoother linting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, app.component.ts, resources/resources-add.component.ts
- `all: smoother install configuration viewing (fixes #10024)`
  ← configuration/configuration.component.ts
- `all: smoother agents assisting (fixes #10027)`
  ← AGENTS.md, CLAUDE.md
- `all: smoother spanish developing (fixes #9957)`
  ← README.md, dev-env.sh
- `all: smoother database testing (fixes #10012)`
  ← courses/add-courses/courses-add.component.spec.ts, resources/view-resources/resources-view.component.spec.ts, users/users-update/users-update.component.spec.ts, users/users-update/users-update.component.ts, users/users.component.spec.ts
- `all: smoother testing (fixes #9996)`
  ← __snapshots__/app.component.spec.ts.snap
- `all: smoother feedback details username truncating (fixes #9993)`
  ← feedback/feedback-view.component.html, feedback/feedback-view.component.ts, feedback/feedback-view.scss
- `all: smoother form changing (fixes #9989)`
  ← meetups/add-meetups/meetups-add.component.ts, users/users-achievements/users-achievements-update.component.ts
- `all: smoother syntax formatting (fixes #9927)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.component.ts, chat/chat-window/chat-window.component.html, chat/chat-window/chat-window.component.ts, chat/chat.component.html, +200 more
- `all: smoother testing (fixes #9988)`
  ← .gitignore, README.md, angular.json, __snapshots__/app.component.spec.ts.snap, app.component.spec.ts, +20 more
- `all: smoother image file selector placing (fixes #9979)`
  ← shared/dialogs/dialogs-images.component.html
- `all: less const export material icons is more (fixes #9985)`
  ← manager-dashboard/reports/myplanet/filter.base.ts, shared/table-helpers.ts, shared/utils.ts, teams/teams.utils.ts
- `all: bump `angular` to 20 (fixes #9926)`
  ← .github/workflows/gateway.yml, docker/db-init/Dockerfile, docker/gateway/Dockerfile, docker/planet/builder-Dockerfile, docker/planet/pre-builder-Dockerfile
- `all: smoother challenge handling (fixes #9959)`
  ← community/community.component.ts, courses/step-view-courses/courses-step-view.component.ts, exams/exams-view.component.ts, home/home.component.ts, notifications/notifications.component.html, +6 more
- `all: smoother announcements dialog filtering (fixes #9961)`
  ← shared/dialogs/dialogs-announcement.component.ts
- `all: smoother feedback titles translating (fixes #9566)`
  ← feedback/feedback-view.component.html, feedback/feedback-view.component.ts, feedback/feedback.component.html, feedback/feedback.component.ts, feedback/feedback.directive.ts, +4 more
- `all: smoother sorting (fixes #9929)`
  ← courses/courses.component.ts, manager-dashboard/manager-fetch.component.ts, meetups/meetups.component.ts, resources/resources.component.ts, surveys/surveys.component.html, +1 more
- `all: smoother page breakpoints handling (fixes #9937)`
  ← chat/chat-sidebar/chat-sidebar.component.ts, community/community.component.ts, courses/courses.component.ts, courses/progress-courses/courses-progress-leader.component.ts, courses/view-courses/courses-view.component.ts, +29 more
- `all: smoother table filtering (fixes #9922)`
  ← shared/table-helpers.ts
- `all: smoother documenting (fixes #9913)`
  ← CLAUDE.md, README.md, couchdb-setup.sh, design/courses/README.md
- `all: smoother version bumping (fixes #9890)`
  ← chatapi/package.json
- `all: smoother dialogs guarding (fixes #9863)`
  ← courses/courses.component.html, courses/courses.component.ts, manager-dashboard/manager-dashboard.component.ts, manager-dashboard/requests/requests-table.component.ts, meetups/view-meetups/meetups-view.component.ts, +6 more
- `all: smoother feedback list viewing (fixes #9868)`
  ← feedback/feedback.component.html, feedback/feedback.component.ts
- `all: smoother claude assisting (fixes #9883)`
  ← CLAUDE.md
- `all: smoother notifications responsive controls paginating (fixes #9851)`
  ← notifications/notifications.component.html, src/styles.scss
- `all: smoother tables responsive layout handling (fixes #9777)`
  ← feedback/feedback.component.html, health/health.component.html, manager-dashboard/reports/myplanet/logs-myplanet.component.html, manager-dashboard/reports/myplanet/reports-myplanet.component.html, manager-dashboard/reports/reports-detail-activities.component.html, +17 more
- `all: smoother navigation responsive closing (fixes #9843)`
  ← home/home.component.html, home/home.component.ts
- `all: smoother rule consistent type asserting (connects #9082)`
  ← .eslintrc.json, eslint.config.mjs, exams/exams-add.component.ts, shared/forms/planet-markdown-textbox.component.ts, submissions/submissions.service.ts, +1 more
- `all: smoother components standalone handling (fixes #9829)`
  ← app.component.spec.ts, app.component.ts, app.module.ts, chat/chat-sidebar/chat-sidebar.component.ts, chat/chat-window/chat-window.component.ts, +188 more
- `all: smoother linting (connects #9082)`
  ← .eslintrc.json, chatapi/package.json, eslint.config.mjs, community/community.component.ts, manager-dashboard/manager-dashboard.component.ts, +8 more
- `all: smoother feedback username overflow handling (fixes #9685)`
  ← feedback/feedback.component.html
- `all: smoother notifications selector aligning (fixes #9828)`
  ← notifications/notifications.component.html, src/styles.scss
- `all: smoother couchdb url handling (fixes #9807)`
  ← shared/couchdb.service.ts, src/environments/environment.prod.ts, src/environments/environment.template, src/environments/environment.test.ts, src/environments/environment.ts
- `all: smoother feedback fallback redirecting (fixes #9770)`
  ← feedback/feedback-view.component.ts, feedback/feedback.directive.ts
- `all: smoother js zip handling (fixes #9790)`
  ← resources/resources-add.component.ts
- `all: smoother angular building (fixes #9797)`
  ← docker/planet/scripts/docker-entrypoint.sh, shared/couchdb.service.ts, src/environments/environment.prod.ts, src/environments/environment.template, src/environments/environment.test.ts, +1 more
- `all: bump `angular` to 19 (fixes #9749)`
  ← .eslintrc.json, app.component.ts, chat/chat-sidebar/chat-sidebar.component.ts, chat/chat-window/chat-window.component.ts, chat/chat.component.ts, +154 more
- `all: smoother authentication code archiving (fixes #9533)`
  ← shared/beta-then-auth-guard-service.ts
- `all: smoother letter spacing (fixes #9771)`
  ← src/styles.scss
- `all: smoother notification marking (fixes #9713)`
  ← notifications/notifications.component.scss
- `all: smoother planet building (fixes #9739)`
  ← angular.json, docker/planet/scripts/compile_planet.sh, health/health-event-dialog.component.ts, shared/utils.ts, submissions/submissions.service.ts, +3 more
- `all: smoother material density styling (fixes #9621)`
  ← src/planet-mat-theme.scss
- `all: smoother feedback button handling (fixes #9674)`
  ← feedback/feedback-view.component.html, feedback/feedback-view.component.ts
- `all: smoother linting (connects #9082)`
  ← .eslintrc.json, app.component.ts, chat/chat-window/chat-window.component.ts, community/community.component.ts, feedback/feedback.directive.ts, +8 more
- `all: less protractor e2e is more (fixes #9721)`
  ← .eslintrc.json, .gitignore, README.md, angular.json, e2e/login.e2e-spec.ts, +4 more
- `all: smoother general sass modules handling (fixes #9701)`
  ← _variables.scss, src/planet-mat-theme.scss, src/styles.scss
- `all: smoother shared components sass handling (fixes #9704)`
  ← home/home.scss, shared/dialogs/dialogs-announcement.component.scss, shared/forms/planet-markdown-textbox.scss, src/styles/calendar.scss
- `all: smoother lint ruling (fixes #9730)`
  ← .eslintrc.json, shared/table-helpers.ts
- `all: bump `angular` to 18 (fixes #9720)`
  ← README.md, _variables.scss, app.module.ts, configuration/configuration.component.spec.ts, courses/add-courses/courses-add.component.spec.ts, +18 more
- `all: smoother brace style indent ruling (connects #9082)`
  ← .eslintrc.json, chat/chat-sidebar/chat-sidebar.component.ts, community/community.component.ts, configuration/configuration.component.ts, configuration/migration.component.ts, +79 more
- `all: bump `angular` to 17 (fixes #9661)`
  ← angular.json, docker/planet/builder-Dockerfile, docker/planet/pre-builder-Dockerfile, _variables.scss, shared/material.module.ts, +3 more
- `all: smoother style variables coloring (fixes #9670)`
  ← shared/utils.ts
- `all: bump `angular` to 16 (fixes #9635)`
  ← app.module.ts, configuration/configuration.component.html, configuration/configuration.component.ts, dashboard/dashboard-tile.component.ts, shared/unsaved-changes.guard.ts, +4 more
- `all: smoother typed forms handling (closes #9047)`
  ← exams/exams-add.component.ts, login/login-form.component.ts, manager-dashboard/manager-aiservices.component.ts, shared/dialogs/dialogs-form.component.ts, shared/dialogs/dialogs-form.service.ts
- `all: smoother planet step list form handling (fixes #9296)`
  ← shared/forms/planet-step-list.component.ts
- `all: less material legacy core is more (closes #9166)`
  ← _variables.scss, dashboard/dashboard.component.html, home/home.scss, manager-dashboard/reports/reports-detail.scss, tasks/tasks.scss, +2 more
- `all: smoother typed forms control standardizing (fixes #9582)`
  ← chat/chat-sidebar/chat-sidebar.component.ts, community/community.component.ts, configuration/configuration.component.ts, configuration/migration.component.ts, exams/exams.service.ts, +8 more
- `all: smoother table material handling (connects #9166)`
  ← courses/courses.component.ts, courses/courses.scss, feedback/feedback.component.ts, health/health.component.ts, manager-dashboard/certifications/certifications.component.ts, +24 more
- `all: smoother dialog material handling (connects #9166)`
  ← chat/chat-sidebar/chat-sidebar.component.ts, community/community-link-dialog.component.ts, community/community-list-dialog.component.ts, community/community.component.ts, courses/add-courses/courses-step.component.ts, +81 more
- `all: smoother input forms material autocompleting (connects #9166)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-window/chat-window.component.html, chat/chat-window/chat-window.scss, chat/chat.component.html, community/community-link-dialog.component.html, +53 more
- `all: smoother tabs material handling (connects #9166)`
  ← shared/material.module.ts, teams/teams-view.component.ts, src/styles.scss
- `all: smoother checkbox material handling (connects #9166)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.scss, courses/courses.scss, exams/exams-add.component.html, exams/exams-question.scss, +11 more
- `all: smoother chips material handling (connects #9166)`
  ← courses/add-courses/courses-step.component.html, courses/add-courses/courses-step.scss, courses/courses.component.html, courses/courses.scss, feedback/feedback.component.html, +10 more
- `all: smoother slide toggle radio material handling (connects #9166)`
  ← shared/dialogs/dialogs-form.component.ts, shared/material.module.ts
- `all: smoother cards material handling (connects #9166)`
  ← feedback/feedback-view.component.html, manager-dashboard/manager-aiservices.component.html, manager-dashboard/manager-currency.component.html, manager-dashboard/manager-dashboard.component.html, news/news-list-item.component.html, +11 more
- `all: smoother planet spinner loading (fixes #9562)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.component.ts, community/community-list.component.html, community/community-list.component.ts, community/community.component.html, +43 more
- `all: smoother menu material handling (connects #9166)`
  ← courses/step-view-courses/courses-step-view.component.ts, courses/view-courses/courses-view.component.ts, exams/exams-add.component.html, exams/exams-question.component.html, home/home.scss, +4 more
- `all: smoother list material handling (connects #9166)`
  ← community/community-list.component.html, community/community.component.html, courses/add-courses/courses-step.component.html, courses/add-courses/courses-step.scss, courses/search-courses/courses-search.component.ts, +26 more
- `all: less planet stacked bar component is more (fixes #9535)`
  ← shared/forms/planet-forms.module.ts
- `all: smoother material paginating (connects #9166)`
  ← courses/courses.component.ts, feedback/feedback.component.ts, manager-dashboard/certifications/certifications.component.ts, manager-dashboard/manager-fetch.component.ts, manager-dashboard/reports/myplanet/myplanet-table.component.ts, +15 more
- `all: less debug operator is more (fixes #9508)`
  ← app.component.spec.ts, courses/courses.component.ts, debug-operator.ts, feedback/feedback-view.component.ts, feedback/feedback.component.ts, +11 more
- `all: smoother snack progress bar spinning (connects #9166)`
  ← resources/resources.scss, shared/material.module.ts, shared/planet-filtered-amount.component.ts, shared/planet-message.service.ts, teams/teams-reports-dialog.component.html, +1 more
- `all: smoother profile image styling (fixes: #9423)`
  ← home/home.scss
- `all: smoother angular typed form validating (fixes #9358)`
  ← validators/custom-validators.ts
- `all: smoother design doc creating (fixes #9369)`
  ← design/create-design-docs.js
- `all: smoother dialogs form handling (fixes #9314)`
  ← shared/dialogs/dialogs-form.component.ts, shared/dialogs/dialogs-form.service.ts, surveys/surveys.component.ts
- `all: smoother planet form validating (fixes #9299)`
  ← shared/forms/planet-number-validator.directive.ts
- `all: smoother material buttons designing (connects #9166)`
  ← chat/chat-sidebar/chat-sidebar.component.html, configuration/configuration.component.ts, configuration/migration.component.ts, courses/view-courses/courses-view.component.html, dashboard/dashboard-tile.component.ts, +36 more
- `all: less dependencies is more (fixes #9338)`
  ← (no files)
- `all: smoother tag form inputting (fixes #9304)`
  ← shared/forms/planet-tag-input.component.ts
- `all: bump `planet` to 0.20.75 (fixes #9317)`
  ← (no files)
- `all: less planet docker cross compile is more (fixes #9306)`
  ← docker/planet/scripts/crosscompile_planet.sh
- `all: smoother docker entry fs directory creating (fixes #9302)`
  ← docker/planet/scripts/docker-entrypoint.sh
- `all: smoother utils sharing (fixes #9287)`
  ← courses/courses.component.ts, manager-dashboard/manager-fetch.component.ts, meetups/meetups.component.ts, resources/resources.component.ts, shared/utils.ts, +1 more
- `all: less pre push hook is more (fixes #9283)`
  ← git-hooks/pre-push

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `all: smoother spanish translations (fixes #9086)`
  ← angular.json, chat/chat-sidebar/chat-sidebar.component.html, chat/chat-window/chat-window.component.html, courses/enroll-courses/courses-enroll.component.ts, courses/progress-courses/courses-progress-leader.component.ts, +33 more
- `all: smoother planet build dockerfile (fixes #9188)`
  ← docker/planet/builder-Dockerfile
- `all: smoother custom fonts swapping (fixes #9178)`
  ← angular.json, src/styles/_mixins.scss
- `all: less planet component is more (fixes #9168)`
  ← home/home.module.ts, home/planet.component.html, home/planet.component.ts
- `all: less mango helpers is more (fixes #9167)`
  ← shared/mangoQueries.ts
- `all: smoother `README.md` (fixes #9125)`
  ← README.md
- `all: bump `angular` to 15 (fixes #9123)`
  ← angular.json, docker/planet/pre-builder-Dockerfile, _export.module.scss, app-router.module.ts, chat/chat-sidebar/chat-sidebar.component.ts, +93 more
- `all: smoother linting (fixes 9105)`
  ← manager-dashboard/reports/reports-detail.component.ts, manager-dashboard/reports/reports.utils.ts, submissions/submissions.service.ts
- `all: less `README.md` is more (fixes #9034)`
  ← README.md
- `all: smoother formatting (fixes #9080)`
  ← .eslintrc.json, configuration/configuration.component.ts, courses/add-courses/courses-add.component.ts, courses/courses.component.ts, courses/search-courses/courses-search.component.ts, +21 more
- `all: smoother markdown editor (fixes #9024)`
  ← shared/forms/planet-markdown-textbox.scss
- `all: smoother `npm run dev` (fixes #9055)`
  ← dev-env.sh, src/environments/environment.template
- `all: smoother `package.json` (fixes #8999)(fixes #9013)`
  ← (no files)
- `all: smoother spanish translations (fixes #8942)`
  ← courses/add-courses/courses-add.component.html, health/health-update.scss, manager-dashboard/certifications/certifications-view.component.html, manager-dashboard/manager-dashboard.component.html, manager-dashboard/requests/requests-table.component.html, +8 more
- `all: bump `angular` to 14 (fixes #8994)(connects #8752)`
  ← angular.json, _export.module.scss, _variables.scss, app.module.ts, chat/chat-sidebar/chat-sidebar.component.ts, +41 more
- `all: smoother navigation small screens (fixes #8957)`
  ← home/home.component.html, home/home.component.ts, home/home.scss
- `all: smoother lists with trackBy (fixes #8954)`
  ← courses/add-courses/courses-add.component.ts, courses/courses.component.ts, courses/search-courses/courses-search.component.ts, courses/view-courses/courses-view.component.html, courses/view-courses/courses-view.component.ts, +12 more
- `all: less video dialog is more (fixes #8947)`
  ← shared/dialogs/dialogs-video.component.ts, shared/dialogs/planet-dialogs.module.ts
- `all: smoother unsaved changes dialog (fixes #8944)`
  ← app-router.module.ts, courses/add-courses/courses-add.component.ts, courses/courses-router.module.ts, health/health-event.component.ts, health/health-update.component.ts, +15 more
- `all: smoother dev environment (fixes #8901)`
  ← angular.json
- `all: bump `angular` to 13 (connects #8752)`
  ← .eslintrc.json, .gitignore, README.md, angular.json, docker/planet/pre-builder-Dockerfile, +28 more
- `all: smoother navigation community (fixes #8884)`
  ← home/home.component.ts
- `all: smoother spanish translations (fixes #7831)`
  ← community/community-link-dialog.component.ts, community/community.component.html, community/community.component.ts, courses/add-courses/courses-step.component.html, courses/add-courses/courses-step.component.ts, +25 more
- `all: smoother notification buttons (fixes #8824)`
  ← notifications/notifications.component.scss
- `all: smoother active svg icon colors (fixes #8849)`
  ← home/home.component.html, home/home.scss, src/styles.scss
- `all: less images is more (fixes #8831)`
  ← app.component.ts, src/assets/BELL_invision_artboard-V-LeonardSnapsSplash-Screen.png.png, src/assets/flags/en.png, src/assets/flags/es-ES.png, src/assets/flags/fr.png, +8 more
- `all: smoother icons permissions (fixes #8827)`
  ← home/home.component.html, home/home.component.ts
- `all: smoother `README.md` (fixes #8819)`
  ← README.md
- `all: smoother navigation changing language (fixes #8776)`
  ← home/home.component.html, home/home.component.ts, shared/planet-language.component.ts

## teams (91)

- `teams: smoother join requests alerting (fixes #10307)`
  ← dashboard/dashboard-tile.component.html, dashboard/dashboard-tile.component.ts, home/home.component.html, home/home.component.ts, teams/teams-view.component.html, +1 more
- `teams: smoother meetups actions buttons hovering (fixes #10295)`
  ← meetups/view-meetups/meetups-view.component.html
- `teams: smoother resources removing (fixes #10280)`
  ← teams/teams-view.component.html
- `teams: smoother member profile cards styling (fixes #10182)`
  ← _variables.scss, community/community.component.html, community/community.component.ts, community/community.scss, resources/resources-add.scss, +10 more
- `teams: smoother member name formatting (fixes #10299)`
  ← dashboard/dashboard.component.spec.ts, dashboard/dashboard.component.ts, dashboard/dashboard.scss, health/health.component.html, health/health.component.ts, +15 more
- `teams: smoother surveys adopt view filtering (fixes #10239)`
  ← surveys/surveys.component.spec.ts, surveys/surveys.component.ts
- `teams: smoother names keyboard navigating (fixes #10249)`
  ← teams/teams.component.html, teams/teams.scss
- `teams: smoother calendar events handling (fixes #10223)`
  ← meetups/meetups.component.html, meetups/view-meetups/meetups-view.component.html, shared/calendar.component.spec.ts, shared/calendar.component.ts
- `teams: smoother calendar task closing (fixes #10219)`
  ← shared/calendar.component.ts, shared/dialogs/dialogs-add-meetups.component.spec.ts, shared/dialogs/dialogs-add-meetups.component.ts
- `teams: smoother surveys adopt button hovering (fixes #10212)`
  ← surveys/surveys.component.html, surveys/surveys.component.ts
- `teams: smoother tasks assignee avatar refreshing (fixes #4735)`
  ← tasks/tasks.component.html, tasks/tasks.component.spec.ts, tasks/tasks.component.ts
- `teams: smoother membership validating (fixes #10208)`
  ← teams/teams-view.component.ts, teams/teams.component.ts, teams/teams.service.spec.ts, teams/teams.service.ts
- `teams: smoother finances reports buttons hovering (fixes #10190)`
  ← teams/teams-reports.component.html, teams/teams-reports.component.ts, teams/teams-view-finances.component.html, teams/teams-view-finances.component.ts
- `teams: smoother voices text hovering (fixes #10176)`
  ← community/community.component.html, community/community.component.ts, news/news-list-item.component.html
- `teams: smoother surveys handling (fixes #10172)`
  ← _mixins.scss, surveys/surveys.component.html, surveys/surveys.component.scss, surveys/surveys.component.ts, teams/teams.scss, +1 more
- `teams: smoother join request canceling (fixes #10138)`
  ← teams/teams-view.component.html, teams/teams-view.component.ts, teams/teams.component.html, teams/teams.component.ts, teams/teams.service.ts
- `teams: smoother list action buttons padding (fixes #10126)`
  ← surveys/surveys.component.html, surveys/surveys.component.scss, src/styles.scss
- `teams: smoother surveys record loading (fixes #9347)`
  ← surveys/surveys.component.spec.ts, surveys/surveys.component.ts
- `teams: smoother surveys table style handling (fixes #10095)`
  ← surveys/surveys.component.html, surveys/surveys.component.scss, teams/teams.component.html, teams/teams.scss, users/users-table.component.html, +2 more
- `teams: smoother courses deleting (fixes #10111)`
  ← teams/teams-view.component.html, teams/teams-view.component.ts
- `teams: smoother calendar events dialog handling (fixes #10066)`
  ← shared/calendar.component.ts, shared/forms/planet-tag-input-dialog.scss, shared/forms/planet-tag-input.component.ts, teams/teams-view.component.ts, src/styles.scss
- `teams: smoother members paginating (fixes #10106)`
  ← users/users-table.component.html
- `teams: smoother finances reports pdf exporting (fixes #10032)`
  ← health/health-event-dialog.component.ts, shared/pdf.service.spec.ts, shared/pdf.service.ts, submissions/submissions.service.ts, teams/teams-attachments.service.ts, +7 more
- `teams: smoother events detail url linking (fixes #9419)`
  ← meetups/view-meetups/meetups-view.component.html, meetups/view-meetups/meetups-view.scss
- `teams: smoother finances date button size handling (fixes #10061)`
  ← teams/teams-view-finances.scss
- `teams: smoother surveys button size handling (fixes #10071)`
  ← surveys/surveys.component.scss
- `teams: smoother button size handlng (fixes #10065)`
  ← teams/teams.scss
- `teams: smoother surveys question options spacing (fixes #10049)`
  ← exams/exams-question.scss
- `teams: less submissions service import is more (fixes #10038)`
  ← submissions/submissions.service.ts
- `teams: smoother header name button handling (fixes #10021)`
  ← teams/teams-view.component.html, teams/teams-view.scss
- `teams: smoother surveys button resizing (fixes #10023)`
  ← surveys/surveys.component.html, surveys/surveys.component.scss, surveys/surveys.component.ts
- `teams: smoother meetups time picking (fixes #9109)`
  ← meetups/add-meetups/meetups-add.component.html, meetups/add-meetups/meetups-add.component.ts
- `teams: smoother task time picking (fixes #9110)`
  ← shared/dialogs/dialogs-form.component.html, shared/dialogs/dialogs-form.component.ts
- `teams: smoother meetups spinner handling (fixes #9981)`
  ← shared/dialogs/dialogs-add-meetups.component.spec.ts, shared/dialogs/dialogs-add-meetups.component.ts
- `teams: smoother survey question error aligning (fixes #10016)`
  ← exams/exams-question-frame.component.scss, exams/exams-view.component.html
- `teams: smoother survey demographics handling (fixes #9983)`
  ← gateway/src/modules/public/services/surveys.service.ts, exams/public-surveys/public-survey.component.html, exams/public-surveys/public-survey.component.scss, exams/public-surveys/public-survey.component.ts, exams/public-surveys/public-surveys.service.ts
- `teams: smoother reports toolbar handling (fixes #9992)`
  ← teams/teams-reports.scss
- `teams: smoother tasks aligning (fixes #9994)`
  ← tasks/tasks.scss
- `teams: smoother reporting (fixes #9919)`
  ← _variables.scss, teams/teams-reports-detail.component.html, teams/teams-reports-detail.component.ts, teams/teams-reports-detail.scss, teams/teams-reports.component.html, +2 more
- `teams: smoother surveys public displaying (fixes #9934)`
  ← exams/exams-question-frame.component.html, exams/exams-question-frame.component.scss, exams/exams-question-frame.component.ts, exams/exams-take/exam-answer.helpers.ts, exams/exams-take/exams-take-widget.component.html, +14 more
- `teams: smoother join requests sorting (fixes #9958)`
  ← teams/teams-view.component.ts, teams/teams.service.ts, teams/teams.utils.ts
- `teams: smoother survey rating scaling (fixes #9906)`
  ← exams/exams-add.component.html, exams/exams-question.component.html, exams/exams-question.component.ts, exams/exams-question.scss, exams/exams-view.component.html, +5 more
- `teams: smoother list default sorting (fixes #9931)`
  ← teams/teams.component.html, teams/teams.component.ts
- `teams: smoother members comparing (fixes #9910)`
  ← teams/teams.utils.ts
- `teams: smoother survey chart exporting (fixes #9898)`
  ← shared/chart-utils.ts, submissions/submissions.service.ts
- `teams: less rxjs imports is more (fixes #9899)`
  ← teams/teams.service.ts
- `teams: smoother members name comparing (fixes #9869)`
  ← teams/teams.utils.ts
- `teams: smoother member list task status toggling (fixes #9496)`
  ← teams/teams-member.component.ts
- `teams: smoother voices routing (fixes #9809)`
  ← news/news-list.component.ts
- `teams: smoother voices button sizing (fixes #9791)`
  ← teams/teams-view.component.html
- `teams: smoother voices icon aligning (#9787)`
  ← community/community.scss
- `teams: smoother submissions normalizing (fixes #9819)`
  ← submissions/submissions.component.ts
- `teams: smoother list paginating (fixes #9767)`
  ← teams/teams.component.html, teams/teams.scss
- `teams: smoother voices paginating (fixes #9773)`
  ← community/community.component.html, community/community.scss, news/news-list.component.html, news/news-list.component.scss, news/news-list.component.ts, +2 more
- `teams: smoother events error reporting (fixes #9736)`
  ← meetups/add-meetups/meetups-add.component.ts
- `teams: smoother sass modules handling (fixes #9714)`
  ← meetups/view-meetups/meetups-view.scss, news/news-list-item.scss, tasks/tasks.scss, teams/teams-view.scss, teams/teams.scss, +4 more
- `teams: smoother surveys canceling (fixes #9414)`
  ← exams/exams-add.component.ts, shared/unsaved-changes.guard.ts, surveys/surveys-router.module.ts
- `teams: smoother voices username shortening (fixes #9476)`
  ← news/news-list-item.scss
- `teams: smoother join all user selecting (fixes #9592)`
  ← users/users-table.component.html, users/users-table.component.ts
- `teams: smoother resources visibility handling (fixes #9626)`
  ← _variables.scss, news/news-list-item.scss, teams/teams-view.component.html, teams/teams-view.scss, src/styles.scss
- `teams: smoother calendar events adding (fixes #9550)`
  ← meetups/add-meetups/meetups-add.component.html
- `teams: smoother calendar events handling (fixes #9580)`
  ← chat/chat-window/chat-window.scss, chat/chat.scss, dashboard/dashboard-tile.scss, login/login.scss, manager-dashboard/manager-dashboard.scss, +7 more
- `teams: smoother finances transacting (fixes #9531)`
  ← teams/teams-view-finances.component.html
- `teams: smoother tasks status coloring (fixes #9536)`
  ← tasks/tasks.scss
- `teams: smoother survey counting (fixes #9354)`
  ← surveys/surveys.component.ts
- `teams: smoother survey formatting (fixes #9235)`
  ← exams/exams-add.component.ts, exams/exams.service.ts, submissions/submissions.component.html, submissions/submissions.component.ts, submissions/submissions.service.ts, +3 more
- `teams: smoother calendar event inputting (fixes #9322)`
  ← meetups/add-meetups/meetups-add.component.ts
- `teams: smoother resources navigating (fixes #8875)`
  ← teams/teams-view.component.html
- `teams: smother surveys lazy loading (fixes #9262)`
  ← teams/teams-view.component.html
- `teams: smoother list button spacing (fixes #9199)`
  ← teams/teams.component.html, teams/teams.scss
- `teams: smoother survey navigating (fixes #9130)`
  ← surveys/surveys.component.html

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `teams: smoother survey title handling (fixes #9161)`
  ← exams/exams-view.component.ts, users/users-update/users-update.component.html, users/users-update/users-update.component.ts
- `teams: smoother voices markdown whitespacing (fixes #9135)`
  ← shared/planet-markdown.component.ts
- `teams: smoother survey birthyear input (fixes #9119)`
  ← users/users-update/users-update.component.html, users/users-update/users-update.component.ts
- `teams: smoother finance notes formatting (fixes #9113)`
  ← teams/teams-view-finances.component.html, teams/teams-view-finances.scss
- `teams: smoother finances loading message (fixes #9085)`
  ← community/community.component.html, community/community.component.ts, teams/teams-view-finances.component.html, teams/teams-view-finances.component.ts, teams/teams-view.component.html, +1 more
- `teams: less voices response is more (fixes #9063)`
  ← news/news-list-item.component.ts, news/news-list.component.ts
- `teams: smoother voices markdowning (fixes #8940)`
  ← news/news-list-item.component.ts, news/news-list.component.ts
- `teams: smoother voices checks (fixes #9023)`
  ← news/news-list-item.component.ts
- `teams: smoother survey submission questions (fixes #8845)`
  ← exams/exams-view.component.html, exams/exams-view.component.ts, submissions/submissions.component.ts
- `teams: smoother joining notifications (fixes #8992)`
  ← teams/teams.service.ts
- `teams: smoother voices names (fixes #8967)`
  ← news/news-list-item.component.html, news/news-list-item.component.ts, news/news-list-item.scss, src/styles.scss
- `teams: smoother member cards (fixes #8913)`
  ← teams/teams-member.component.html, teams/teams-member.component.ts
- `teams: smoother survey submissions (fixes #8959)`
  ← users/users-update/users-update.component.ts
- `teams: smoother survey views (fixes #8823)`
  ← exams/exams-view.component.html
- `teams: smoother list view (fixes #8778)`
  ← courses/courses.scss, resources/resources.scss, teams/teams.component.html, teams/teams.scss
- `teams: smoother voices expansion (fixes #8883)`
  ← news/news-list-item.component.ts
- `teams: smoother courses list (fixes #8629)`
  ← courses/courses.component.html, courses/courses.component.ts
- `teams: smoother courses linking (fixes #8860)`
  ← courses/view-courses/courses-view-detail.component.ts, courses/view-courses/courses-view.component.ts, resources/view-resources/resources-view.component.ts, shared/dialogs/dialogs-resources-viewer.component.ts, teams/teams-view.component.ts
- `teams: smoother voices show replies (fixes #8724)`
  ← news/news-list.component.html, news/news-list.component.ts
- `teams: smoother survey choice other (fixes #8798)`
  ← exams/exams-view.component.html, exams/exams-view.component.ts, exams/exams-view.scss

## manager (72)

- `manager: smoother certifications search filtering (fixes #10080)`
  ← manager-dashboard/certifications/certifications.component.html, teams/teams.component.html, src/styles.scss
- `manager: smoother reports toolbar navigating (fixes #10031)`
  ← manager-dashboard/reports/myplanet/myplanet-toolbar.component.html, manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.scss, submissions/submissions.component.html
- `manager: less reports chart button top margin is more (fixes #10131)`
  ← manager-dashboard/reports/reports-detail.scss
- `manager: smoother report date filtering (fixes #9956)`
  ← manager-dashboard/reports/myplanet/reports-myplanet.component.ts, manager-dashboard/reports/reports.utils.ts, teams/teams-view-finances.component.ts
- `manager: less reports chart module is more (fixes #9946)`
  ← manager-dashboard/reports/reports-detail.component.ts
- `manager: smoother reporting (fixes #9911)`
  ← manager-dashboard/reports/reports.utils.ts
- `manager: smoother report health charting (fixes #9896)`
  ← manager-dashboard/reports/reports-health.component.ts, manager-dashboard/reports/reports.utils.ts
- `manager: less filter by date import is more (fixes #9903)`
  ← manager-dashboard/reports/myplanet/reports-myplanet.component.ts
- `manager: less host listener import is more (fixes #9902)`
  ← manager-dashboard/manager-dashboard.component.ts
- `manager: less report empty constructor is more (fixes #9879)`
  ← manager-dashboard/reports/reports-detail-activities.component.ts
- `manager: smoother reports timeframe selecting (fixes #9858)`
  ← manager-dashboard/reports/reports-detail.component.html
- `manager: smoother reports paginating (fixes #9811)`
  ← manager-dashboard/reports/reports-detail-activities.component.ts, manager-dashboard/reports/reports-detail.component.html
- `manager: smoother settings responsive styling  (fixes #9775)`
  ← manager-dashboard/manager-settings.shared.scss
- `manager: smoother password validating (fixes #9794)`
  ← validators/validator.service.ts
- `manager: smoother courses resources sent filtering (fixes #9570)`
  ← manager-dashboard/manager-fetch.component.html, manager-dashboard/manager-fetch.component.ts
- `manager: smoother configuration form handling (fixes #9692)`
  ← configuration/configuration.component.ts
- `manager: smoother sass modules handling (fixes #9718)`
  ← manager-dashboard/manager-dashboard.scss, manager-dashboard/manager-settings.shared.scss, manager-dashboard/reports/myplanet/myplanet.scss, manager-dashboard/reports/reports-detail.scss, manager-dashboard/reports/reports.components.scss, +1 more
- `manager: smoother send on accept buttons aligning (fixes #9628)`
  ← manager-dashboard/manager-dashboard.component.ts, manager-dashboard/manager-dashboard.scss
- `manager: less showdown export is more (fixes #9655)`
  ← shared/utils.ts
- `manager: smoother reports charting (fixes #9529)`
  ← manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.component.ts
- `manager: smoother surveys filtering (fixes #9565)`
  ← manager-dashboard/certifications/certifications.component.html, manager-dashboard/certifications/certifications.component.ts, manager-dashboard/manager-fetch.component.html, shared/planet-loading-spinner.component.ts, surveys/surveys.component.html, +3 more
- `manager: smoother reports form filtering (fixes #9504)`
  ← manager-dashboard/reports/reports-detail.component.ts, manager-dashboard/reports/reports.service.ts
- `manager: smoother submissions counting (fixes #9448)`
  ← submissions/submissions.component.ts
- `manager: smoother configuration angular form handling (fixes #9365)`
  ← configuration/configuration.component.ts
- `manager: smoother survey submissions viewing (fixes #9353)`
  ← couchdb-setup.sh, design/submissions/submissions-design.js, design/submissions/submissions-design.json, surveys/surveys.component.ts
- `manager: smoother survey subscriptions handling (fixes #9408)`
  ← surveys/surveys.component.ts
- `manager: smoother reports form handling (fixes #9327)`
  ← manager-dashboard/reports/reports-detail.component.ts, manager-dashboard/requests/requests-table.component.ts
- `manager: smoother report charts loading (fixes #9345)`
  ← manager-dashboard/reports/reports-detail.component.ts
- `manager: smoother configuration formatting (fixes #8975)`
  ← configuration/configuration.component.html, configuration/configuration.component.ts
- `manager: smoother report charts downloading (fixes #9339)`
  ← manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.component.ts, manager-dashboard/reports/reports-detail.scss
- `manager: smoother myplanet logs filtering (fixes #9346)`
  ← manager-dashboard/reports/myplanet/filter.base.ts, manager-dashboard/reports/myplanet/logs-myplanet.component.ts, manager-dashboard/reports/myplanet/myplanet-toolbar.component.ts, manager-dashboard/reports/myplanet/reports-myplanet.component.ts
- `manager: smoother submissions sourcing (fixes #9355)`
  ← submissions/submissions.component.html, submissions/submissions.component.ts, surveys/surveys.component.html, surveys/surveys.component.ts
- `manager: smoother report trend comparison exporting (fixes #9340)`
  ← manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.component.ts
- `manager: less couch service is more (fixes #9334)`
  ← manager-dashboard/manager-aiservices.component.ts
- `manager: smoother reporting (fixes #9309)`
  ← shared/chart-utils.ts
- `manager: smoother server pin changing (fixes #9217)`
  ← manager-dashboard/manager-dashboard.component.html, manager-dashboard/manager-dashboard.component.ts, manager-dashboard/manager.service.ts, shared/dialogs/dialogs-prompt.component.html
- `manager: smoother ai services formatting (fixes #9265)`
  ← manager-dashboard/manager-aiservices.component.html, manager-dashboard/manager-aiservices.component.ts
- `manager: smoother myplanet reports naming (fixes #9200)`
  ← manager-dashboard/reports/myplanet/reports-myplanet.component.html
- `manager: smoother surveys navigating (fixes #9193)`
  ← surveys/surveys.component.ts
- `manager: smoother member searching (fixes #9224)`
  ← users/users.component.ts
- `manager: smoother members navigation (fixes #9198)`
  ← users/users.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `manager: smoother myplanet logs and reports (fixes #9021)`
  ← home/home.module.ts, manager-dashboard/manager-dashboard-router.module.ts, manager-dashboard/manager-dashboard.module.ts, manager-dashboard/reports/myplanet/filter.base.ts, manager-dashboard/reports/myplanet/logs-myplanet.component.html, +10 more
- `manager: smoother reports charts loading (fixes #9183)`
  ← manager-dashboard/reports/reports-detail.component.ts, shared/chart-utils.ts, submissions/submissions.service.ts
- `manager: smoother surveys error handling (fixes #9194)`
  ← submissions/submissions.component.html, submissions/submissions.service.ts, teams/teams.service.ts
- `manager: smoother currency configuring (fixes #9064)`
  ← manager-dashboard/manager-aiservices.component.scss, manager-dashboard/manager-aiservices.component.ts, manager-dashboard/manager-currency.component.html, manager-dashboard/manager-currency.component.ts, manager-dashboard/manager-dashboard-router.module.ts, +4 more
- `manager: smoother submission chart library loading (fixes #9179)`
  ← submissions/submissions.service.ts
- `manager: smoother survey list (fixes #9129)`
  ← surveys/surveys.component.scss
- `manager: smoother myplanet reports (fixes #9114)`
  ← home/home.module.ts, manager-dashboard/manager-dashboard-router.module.ts, manager-dashboard/manager-dashboard.module.ts, manager-dashboard/reports/myplanet/logs-myplanet.component.html, manager-dashboard/reports/myplanet/logs-myplanet.component.scss, +7 more
- `manager: smoother survey export pdf markdown (fixes #9071)`
  ← submissions/submissions.service.ts
- `manager: smoother survey list (fixes #8920)`
  ← surveys/surveys.component.scss
- `manager: smoother survey rating scale export (fixes #9083)`
  ← exams/exams-view.component.html, exams/exams-view.scss, submissions/submissions.service.ts
- `manager: smoother report comparison trends (fixes #9072)`
  ← manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.component.ts, manager-dashboard/reports/reports-detail.scss, manager-dashboard/reports/reports.utils.ts, submissions/submissions.service.ts
- `manager: smoother survey rating scale (fixes #9068)`
  ← exams/exams-add.component.html, exams/exams-question.component.html, exams/exams-view.component.html, exams/exams-view.component.ts, exams/exams-view.scss, +5 more
- `manager: smoother survey submissions team column (fixes #9066)`
  ← submissions/submissions.component.html, submissions/submissions.component.ts, submissions/submissions.service.ts, teams/teams.service.ts
- `manager: smoother voices summary export (fixes #9049)`
  ← manager-dashboard/reports/reports-detail.component.ts, shared/csv.service.ts
- `manager: smoother reports search filters (fixes #9039)`
  ← manager-dashboard/reports/logs-myplanet.component.ts, manager-dashboard/reports/reports-myplanet.component.ts
- `manager: smoother reports navigation filter clearing (fixes #9022)`
  ← manager-dashboard/reports/logs-myplanet.component.html, manager-dashboard/reports/logs-myplanet.component.ts, manager-dashboard/reports/reports-myplanet.component.html, manager-dashboard/reports/reports-myplanet.component.ts
- `manager: smoother report details navigation (fixes #9044)`
  ← manager-dashboard/reports/reports-detail.component.html, manager-dashboard/reports/reports-detail.scss
- `manager: smoother survey exports (fixes #9042)`
  ← surveys/surveys.component.ts
- `manager: smoother submissions analysis (fixes #8993)`
  ← submissions/submissions.service.ts
- `manager: smoother submissions list names (fixes #8980)`
  ← submissions/submission.scss, submissions/submissions.component.html, submissions/submissions.component.ts
- `manager: smoother myplanet logs (fixes #8962)`
  ← manager-dashboard/reports/logs-myplanet.component.html, manager-dashboard/reports/logs-myplanet.component.ts, src/i18n/messages.spa.xlf
- `manager: smoother spanish translations (fixes #8960)`
  ← src/i18n/messages.spa.xlf
- `manager: smoother report summary exports (fixes #7894)`
  ← manager-dashboard/reports/reports-detail.component.ts, shared/csv.service.ts, shared/utils.ts, users/users-achievements/users-achievements.component.ts
- `manager: smoother myplanet reports loading (fixes #8918)`
  ← manager-dashboard/reports/reports-myplanet.component.html, manager-dashboard/reports/reports-myplanet.component.ts, src/i18n/messages.spa.xlf, src/i18n/messages.xlf
- `manager: smoother myplanet log buttons (fixes #8922)`
  ← manager-dashboard/reports/logs-myplanet.component.html, manager-dashboard/reports/reports-myplanet.component.html
- `manager: smoother dashboard (fixes #8882)`
  ← manager-dashboard/manager-dashboard.component.html, manager-dashboard/manager-dashboard.component.ts, manager-dashboard/manager-dashboard.scss
- `manager: smoother survey submissions filter (fixes #8880)`
  ← submissions/submissions.component.ts
- `manager: smoother survey submissions view (fixes #8841)`
  ← exams/exams-view.component.ts, manager-dashboard/manager-dashboard-router.module.ts, submissions/submissions.component.html, submissions/submissions.component.ts, surveys/surveys.component.html, +1 more
- `manager: smoother survey export charts (fixes #8797)`
  ← submissions/submissions.service.ts
- `manager: smoother fetch list icons (fixes #8815)`
  ← manager-dashboard/manager-fetch.component.html, manager-dashboard/manager-fetch.component.ts
- `manager: smoother surveys submissions view (fixes #8816)`
  ← submissions/submissions.service.ts, surveys/surveys.component.ts

## courses (57)

- `courses: smoother buttons keyboard navigating (fixes #10288)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts, courses/courses.component.html, courses/progress-courses/courses-progress-leader.component.html, courses/progress-courses/courses-progress-leader.component.ts, +6 more
- `courses: smoother shelf changes confirming (fixes #10217)`
  ← courses/courses.component.spec.ts, courses/courses.component.ts, courses/courses.service.spec.ts, courses/courses.service.ts, courses/view-courses/courses-view-confirmation.spec.ts, +3 more
- `courses: smoother steps submitting (fixes #10193)`
  ← submissions/submissions.component.html, submissions/submissions.component.ts, submissions/submissions.service.ts
- `courses: smoother exams answers saving (fixes #10181)`
  ← courses/courses-router.module.ts, exams/exams-view.component.ts, shared/dialogs/dialogs-prompt.component.html, shared/dialogs/dialogs-prompt.component.ts, shared/unsaved-changes.component.ts, +2 more
- `courses: smoother creation steps deleting (fixes #10188)`
  ← courses/add-courses/courses-step.component.html, shared/forms/planet-step-list.component.spec.ts, shared/forms/planet-step-list.component.ts
- `courses: smoother draft discarding (fixes #10152)`
  ← courses/add-courses/courses-add.component.spec.ts, courses/add-courses/courses-add.component.ts, shared/dialogs/dialogs-prompt.component.html
- `courses: smoother steps survey adding (fixes #10047)`
  ← courses/add-courses/courses-add.component.spec.ts, courses/add-courses/courses-add.component.ts
- `courses: smoother creation overflow handling (fixes #10107)`
  ← courses/courses.component.html, courses/courses.scss
- `courses: smoother exams questions text handling (fixes #10053)`
  ← exams/exams-take/exams-take-widget.component.scss
- `courses: smoother cover image handling (fixes #10054)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts, courses/add-courses/courses-add.scss, courses/view-courses/courses-view-detail.component.html, courses/view-courses/courses-view-detail.component.ts, +5 more
- `courses: smoother exams survey creating (fixes #9662)`
  ← exams/exams-add.component.html
- `courses: smoother deleting (fixes #9418)`
  ← courses/courses.component.ts
- `courses: smoother creating (fixes #9977)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts, courses/add-courses/courses-add.scss, courses/add-courses/courses-step.component.html, courses/add-courses/courses-step.component.ts, +1 more
- `courses: smoother icons constants handling (fixes #10019)`
  ← courses/add-courses/courses-step.component.html, courses/add-courses/courses-step.component.ts, courses/courses-icon.component.ts, courses/view-courses/courses-view.component.html, courses/view-courses/courses-view.component.ts
- `courses: smoother exams question navigating (fixes #9867)`
  ← exams/exams-question-frame.component.html, exams/exams-question-frame.component.ts, exams/exams-view.component.html, exams/exams-view.component.ts, exams/public-surveys/public-survey.component.ts, +1 more
- `courses: smoother tags selecting (fixes #9765)`
  ← shared/forms/planet-tag-input.component.ts
- `courses: smoother steps toolbar buttons showing (fixes #9930)`
  ← courses/courses.component.html, courses/step-view-courses/courses-step-view.component.html, courses/step-view-courses/courses-step-view.component.ts
- `courses: smoother collection counting (fixes #9639)`
  ← shared/forms/planet-tag-input-dialog.component.html, shared/forms/planet-tag-input-dialog.scss
- `courses: smoother nation upload dialog spacing (fixes #9579)`
  ← courses/courses.scss, shared/dialogs/dialogs-list.component.html
- `courses: smoother toolbar color styling (fixes #9855)`
  ← courses/step-view-courses/courses-step-view.component.html, courses/step-view-courses/courses-step-view.scss
- `courses: smoother card stack styling (fixes #9847)`
  ← courses/courses.component.html, courses/courses.component.ts, courses/courses.scss, resources/resources.component.html, resources/resources.component.ts, +2 more
- `courses: smoother creation error logging (fixes #9842)`
  ← courses/add-courses/courses-add.component.ts
- `courses: smoother collection creating (fixes #9563)`
  ← courses/courses.component.ts, resources/resources.component.ts
- `courses: smoother progress handling (fixes #9815)`
  ← courses/courses.module.ts, courses/progress-courses/courses-progress.module.ts, home/home.module.ts
- `courses: smoother path routing (fixes #9650)`
  ← courses/courses-router.module.ts
- `courses: smoother row sizing (fixes #9725)`
  ← courses/courses.component.html, courses/courses.component.ts, courses/courses.scss, resources/resources.component.html, resources/resources.component.ts, +6 more
- `courses: smoother submissions table showing (fixes #9686)`
  ← courses/step-view-courses/courses-step-view.component.ts, submissions/submission.scss
- `courses: smoother rating number aligning (fixes #9623)`
  ← shared/forms/planet-stacked-bar.component.ts
- `courses: smoother exams margin handling (fixes #9675)`
  ← exams/exams-add.scss
- `courses: smoother exams sass modules handling (fixes #9716)`
  ← exams/exams-add.scss, exams/exams-question.scss, exams/exams-view.scss, health/health-update.scss, submissions/submission.scss, +1 more
- `courses: smoother sass modules handling (fixes #9711)`
  ← courses/_courses-shared.scss, courses/add-courses/courses-add.scss, courses/courses.scss, courses/progress-courses/courses-progress-bar.scss, courses/progress-courses/courses-progress-chart.scss, +3 more
- `courses: smoother description expanding (fixes #9564)`
  ← courses/courses.component.html, courses/courses.component.ts, resources/resources.component.html, resources/resources.component.spec.ts, resources/resources.component.ts
- `courses: smoother collection buttons aligning (fixes #9640)`
  ← shared/forms/planet-tag-input-dialog.component.html, shared/forms/planet-tag-input-dialog.scss
- `courses: smoother collections scrollbar handling (fixes #9638)`
  ← shared/forms/planet-tag-input-dialog.scss, shared/forms/planet-tag-input.component.ts
- `courses: less collections sub tag ids is more (fixes #9656)`
  ← shared/forms/planet-tag-input-dialog.component.ts
- `courses: less current params is more (fixes #9657)`
  ← courses/courses.service.ts
- `courses: smoother steps buttons aligning (fixes #9532)`
  ← courses/add-courses/courses-add.scss, shared/forms/planet-step-list.scss
- `courses: smoother toolbar button aligning (fixes #9555)`
  ← courses/step-view-courses/courses-step-view.component.html, courses/step-view-courses/courses-step-view.scss
- `courses: less submission state is more (fixes #9646)`
  ← courses/courses.service.ts
- `courses: smoother collections handling (fixes #9557)(fixes #9512)`
  ← shared/forms/planet-tag-input-dialog.component.html
- `courses: smoother translating (fixes #9469)`
  ← src/i18n/messages.spa.xlf
- `courses: smoother exams form handling (fixes #9377)`
  ← exams/exams-view.component.ts
- `courses: smoother create form handling (fixes #9404)`
  ← courses/add-courses/courses-add.component.ts, courses/add-courses/courses-step.component.ts, courses/courses.component.ts, shared/table-helpers.ts
- `courses: smoother survey quesitions title aligning (fixes #9444)`
  ← exams/exams-view.component.html, exams/exams-view.scss
- `courses: smoother tags angular form handling (fixes #9291)`
  ← shared/forms/planet-tag-input-dialog.component.ts, shared/forms/tags.service.ts
- `courses: smoother open grade levelling (fixes #9427)`
  ← courses/constants.ts
- `courses: smoother exams angular form handling (fixes #9371)`
  ← .github/workflows/planet-chat.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml, exams/exams-add.component.ts, exams/exams-question.component.ts, +1 more
- `courses: smoother step resources draft removing (fixes #9435)`
  ← courses/add-courses/courses-step.component.ts
- `courses: smoother grade level open creating (fixes #9331)`
  ← courses/constants.ts
- `courses: smoother steps form handling (fixes #9397)`
  ← courses/add-courses/courses-step.component.ts
- `courses: smoother ratings form handling (fixes #9297)`
  ← shared/forms/planet-rating.component.ts
- `courses: smoother list level filtering (fixes #9257)`
  ← shared/table-helpers.ts
- `courses: smoother checkbox display state (fixes #9143)`
  ← courses/search-courses/courses-search.component.ts, resources/search-resources/resources-search.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `courses: smoother list small screen (fixes #8971)`
  ← courses/courses.scss, resources/resources.scss
- `courses: smoother creation translations (fixes #8978)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts, src/i18n/messages.spa.xlf, src/i18n/messages.xlf
- `courses: smoother creation draft automatic saving (fixes #8976)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts
- `courses: smoother creation workflow (fixes #8952)`
  ← courses/add-courses/courses-add.component.html, courses/add-courses/courses-add.component.ts, courses/add-courses/courses-add.scss, courses/add-courses/courses-step.component.ts

## community (25)

- `community: smoother finances displaying (fixes #9916)`
  ← teams/teams-view-finances.component.html, teams/teams-view-finances.component.ts, teams/teams-view-finances.scss
- `community: smoother reports buttons handling (fixes #9588)`
  ← community/community.component.ts
- `community: smoother button css handling (fixes #9478)`
  ← community/community.component.html, community/community.scss
- `community: smoother sass modules handling (fixes #9707)`
  ← chat/chat-sidebar/chat-sidebar.scss, chat/chat-window/chat-window.scss, chat/chat.scss, community/community.scss, dashboard/dashboard-notifications-dialog.component.scss, +4 more
- `community: smoother services icon linking (fixes #9671)(fixes #9691)`
  ← community/community-link-dialog.component.html, community/community-link-dialog.component.ts, community/community.component.html, community/community.component.ts, community/community.scss
- `community: smoother voices bar handling (fixes #9693)`
  ← community/community.component.html, community/community.scss
- `community: smoother dialog padding (fixes #9672)`
  ← community/community-link-dialog.component.html, shared/dialogs/dialogs-ratings.component.html
- `community: smoother services linking (fixes #9481)`
  ← community/community-link-dialog.component.ts
- `community: smoother services forms linking (fixes #9413)`
  ← community/community-link-dialog.component.ts
- `community: smoother services form handling (fixes #9412)`
  ← community/community.component.ts
- `community: smoother services navigating (fixes #9420)`
  ← community/community.scss
- `community: smoother services buttons formatting (fixes #9137)`
  ← community/community.component.html, community/community.scss
- `community: smoother services linking (fixes #9084)`
  ← app.component.ts, community/community-link-dialog.component.html, community/community-link-dialog.component.ts, community/community.component.html, community/community.component.ts, +10 more
- `community: smoother voices paginating (fixes #9223)`
  ← news/news-list.component.html, news/news-list.component.scss, news/news-list.component.ts
- `community: smoother center landing (fixes #9077)`
  ← home/home-router.module.ts, home/home.component.ts, shared/auth-guard.service.ts, shared/state.service.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `community: smoother voices (fixes #9185)`
  ← community/community.component.ts, news/news-list.component.ts, news/news.service.ts, shared/couchdb.service.ts
- `community: smoother services description removing (fixes #9095)`
  ← community/community.component.html
- `community: smoother navigation style (fixes #9015)`
  ← community/community.scss
- `community: smoother voices searching (fixes #8982)`
  ← community/community.component.html, community/community.component.ts
- `community: smoother voices filtering (fixes #8983)`
  ← community/community.component.html, community/community.component.ts
- `community: smoother voices searching pin (fixes #8903)`
  ← app.component.ts, community/community.component.html, community/community.component.ts, community/community.scss, src/assets/icons/pin.svg, +1 more
- `community: smoother voices shared (fixes #8938)`
  ← community/community.component.html, community/community.component.ts, news/news-list-item.component.html, news/news-list-item.component.ts, news/news-list-item.scss, +1 more
- `community: smoother voices reply (fixes #8931)`
  ← community/community.component.html, community/community.component.ts
- `community: smoother voices filter (fixes #8870)`
  ← community/community.component.html, community/community.component.ts, community/community.scss
- `community: smoother description editing (fixes #8848)`
  ← community/community.component.html

## dashboard (22)

- `dashboard: smoother profile back button navigating (fixes #10287)`
  ← users/users-profile/users-profile.component.html, users/users-profile/users-profile.component.spec.ts
- `dashboard: smoother courses title shelfing (fixes #10257)`
  ← dashboard/dashboard-tile.component.html, dashboard/dashboard-tile.component.spec.ts, dashboard/dashboard-tile.component.ts, dashboard/dashboard-tile.scss
- `dashboard: smoother tiles keyboard handling (fixes #10248)`
  ← dashboard/dashboard-tile.component.html, dashboard/dashboard-tile.component.ts, dashboard/dashboard-tile.scss
- `dashboard: smoother unit testing (fixes #10235)`
  ← dashboard/dashboard.component.spec.ts, dashboard/dashboard.component.ts, vite.config.mts
- `dashboard: less grid is more (fixes #10084)`
  ← dashboard/dashboard.scss
- `dashboard: smoother chat linking (fixes #10014)`
  ← chat/chat.component.ts, dashboard/dashboard-tile.component.html, dashboard/dashboard.component.ts
- `dashboard: smoother button background handling (fixes #10000)`
  ← dashboard/dashboard-tile.scss, src/planet-mat-theme.scss, src/styles.scss
- `dashboard: smoother path routing (fixes #9901)`
  ← home/home-router.module.ts
- `dashboard: smoother surveys reminding (fixes #8876)`
  ← dashboard/dashboard-notifications-dialog.component.html, dashboard/dashboard-notifications-dialog.component.scss, dashboard/dashboard-notifications-dialog.component.ts, login/login-form.component.ts
- `dashboard: smoother profile user archiving (fixes #9392)`
  ← shared/table-helpers.ts, users/users-archive/users-archive.component.ts
- `dashboard: smoother teams icon showing (fixes #9402)`
  ← app.component.ts, home/home.component.html, src/assets/icons/group.svg
- `dashboard: smoother health icon showing (fixes #9343)`
  ← home/home.component.html
- `dashboard: smoother certifications component form handling (fixes #9336)`
  ← manager-dashboard/certifications/certifications-add.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `dashboard: smoother mychat link (fixes #8910)`
  ← dashboard/dashboard.component.ts
- `dashboard: smoother profile name (fixes #8894)`
  ← dashboard/dashboard.component.html
- `dashboard: smoother feedback reply button (fixes #8914)`
  ← feedback/feedback-view.component.html
- `dashboard: smoother spanish translation (fixes #8911)`
  ← dashboard/dashboard.component.ts
- `dashboard: smoother courses routing (fixes #8872)`
  ← courses/view-courses/courses-view.component.ts, dashboard/dashboard.component.ts, resources/view-resources/resources-view.component.ts, teams/teams-view.component.ts
- `dashboard: smoother view small screens (fixes #8842)`
  ← dashboard/dashboard-tile.component.ts, dashboard/dashboard.component.ts
- `dashboard: smoother profile image editing (fixes #8757)`
  ← users/users-update/users-update.component.html, users/users-update/users-update.component.ts, users/users-update/users-update.scss
- `dashboard: smoother profile image reset (fixes #8837)`
  ← users/users-update/users-update.component.html, users/users-update/users-update.component.ts
- `dashboard: smoother layout accordion style (fixes #7417)`
  ← dashboard/dashboard-tile.component.html, dashboard/dashboard-tile.component.ts, dashboard/dashboard-tile.scss, dashboard/dashboard.component.ts, dashboard/dashboard.scss

## actions (20)

- `actions: smoother workflows base image checking (fixes #10362)`
  ← .github/workflows/gateway.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml
- `actions: smoother workflow gateway docker npm caching (fixes #10242)`
  ← .github/workflows/gateway.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml, docker/gateway/Dockerfile
- `actions: smoother workflow automerging (fixes #10312)`
  ← .github/scripts/automerge.sh, .github/scripts/coauthors.sh, .github/scripts/version.sh, .github/workflows/automerge.yml
- `actions: smoother testing (fixes #10117)`
  ← .github/workflows/planet.yml, karma.conf.js, src/test.ts
- `actions: smoother workflows qemu node handling (fixes #10092)`
  ← .github/workflows/gateway.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml, AGENTS.md, README.md
- `actions: smoother docker gateway building (connects #9934)`
  ← .github/workflows/gateway.yml, CLAUDE.md, README.md, chatapi/README.md, chatapi/src/config/nano.config.ts, +27 more
- `actions: less claude workflow is more (fixes #9139)`
  ← .github/workflows/claude.yml
- `actions: smoother docker tagging (fixes #9940)`
  ← .github/workflows/planet-chat.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml
- `actions: smoother db init dockerfile building (fixes #9870)`
  ← .github/workflows/planet-db.yml, docker/db-init/Dockerfile
- `actions: smoother db init buildx multiarch building (fixes #9917)`
  ← .github/workflows/planet-db.yml, docker/db-init/crosscompile-Dockerfile, docker/db-init/crosscompile_db-init.sh
- `actions: less couchdb setup is more (fixes #9912)`
  ← couchdb-setup.sh
- `actions: smoother docker containers building (fixes #9743)`
  ← .github/workflows/planet-chat.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml, docker/chatapi/Dockerfile, docker/chatapi/amd64-Dockerfile, +8 more
- `actions: smoother docker volumes including (fixes #9727)`
  ← docker/README.md, docker/hub.yml, docker/planet.yml, docker/volumes.yml, docker/volumes_hub.yml
- `actions: smoother chatapi nginx upgrading (fixes #9741)`
  ← docker/planet/nginx/credentials.sh, docker/planet/nginx/latest.sh
- `actions: less install deployment workflow is more (fixes #9728)`
  ← couchdb-setup.sh, design/courses/courses-mockup.json, design/meetups/meetups-mockup.json, design/resources/attachments/document.doc, design/resources/attachments/github.txt, +8 more
- `actions: less build planet script is more (fixes #9600)`
  ← docker/planet/builder-Dockerfile, docker/planet/scripts/build_planet.sh, docker/planet/scripts/compile_planet.sh
- `actions: smoother docker manifest uploading (fixes #9597)`
  ← .github/workflows/planet-chat.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml
- `actions: smoother db init container building (fixes #9502)`
  ← docker/db-init/crosscompile_db-init.sh

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `actions: smoother claude workflow (fixes #9117)`
  ← .github/workflows/claude.yml
- `actions: smoother workflows for codex (fixes #8907)`
  ← .github/workflows/deploy.yml, .github/workflows/planet-chat.yml, .github/workflows/planet-db.yml, .github/workflows/planet.yml

## resources (20)

- `resources: smoother creation needs describing (fixes #10329)`
  ← resources/resources-add.component.html, resources/resources-add.scss
- `resources: smoother csv details previewing (fixes #10328)`
  ← courses/step-view-courses/courses-step-view.scss, resources/view-resources/resources-view.component.html, resources/view-resources/resources-view.scss, resources/view-resources/resources-viewer.scss
- `resources: smoother creation year validating (fixes #10314)`
  ← resources/resources-add.component.html, resources/resources-add.component.ts, validators/custom-validators.spec.ts, validators/custom-validators.ts
- `resources: smoother file size showing (fixes #10317)`
  ← resources/resources.component.html, resources/resources.component.ts, resources/resources.utils.spec.ts, resources/resources.utils.ts, resources/view-resources/resources-view.component.html, +7 more
- `resources: smoother shelf removal confirming (fixes #10236)`
  ← dashboard/dashboard-tile.component.ts, resources/resources.component.ts, resources/view-resources/resources-view.component.ts
- `resources: smoother viewer fullscreen button handling (fixes #10166)`
  ← resources/view-resources/resources-viewer.component.html, resources/view-resources/resources-viewer.scss
- `resources: smoother csv viewing (fixes #8368)`
  ← resources/view-resources/resources-menu.component.ts, resources/view-resources/resources-viewer.component.html, resources/view-resources/resources-viewer.component.spec.ts, resources/view-resources/resources-viewer.component.ts, resources/view-resources/resources-viewer.scss, +4 more
- `resources: smoother pdf making (fixes #10091)`
  ← resources/resources-add.component.ts, shared/pdf.service.spec.ts, shared/pdf.service.ts, shared/zip-utils.ts, submissions/submissions.service.ts
- `resources: smoother downloading (fixes #10043)`
  ← resources/view-resources/resources-view.component.html
- `resources: smoother creating (fixes #9967)`
  ← resources/resources-add.component.html, resources/resources-add.component.ts, resources/resources-add.scss, shared/forms/planet-tag-input.component.html, shared/forms/planet-tag-input.component.ts, +1 more
- `resources: smoother file selecting (fixes #9972)`
  ← resources/resources-add.component.html, resources/resources-add.component.ts, resources/resources.service.ts, shared/dialogs/dialogs-images.component.html, shared/dialogs/dialogs-images.component.scss, +11 more
- `resources: smoother zip filename uploading (fixes #9923)`
  ← resources/resources-add.component.ts
- `resources: smoother markdown form previewing (fixes #9908)`
  ← resources/resources-add.component.html, resources/resources-add.scss, shared/forms/planet-markdown-textbox.component.ts, shared/forms/planet-markdown-textbox.scss
- `resources: smoother open level listing (fixes #9470)`
  ← resources/resources-constants.ts, resources/resources.component.ts
- `resources: smoother unzipping (fixes #9784)`
  ← resources/resources-add.component.ts, shared/user.service.ts
- `resources: smoother sass modules handling (fixes #9709)`
  ← resources/_resources-shared.scss, resources/resources-add.scss, resources/resources.scss, resources/search-resources/resources-search.scss, resources/view-resources/resources-view.scss, +1 more
- `resources: smoother icon downloading (fixes #9307)`
  ← resources/resources-add.component.html, resources/resources-add.component.ts
- `resources: smoother creation angular form handling (fixes #9370)`
  ← resources/resources-add.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `resources: smoother rating stars (fixes #9002)`
  ← src/styles.scss
- `resources: smoother creation (fixes #8852)`
  ← resources/resources-add.scss

## chat (16)

- `chat: smoother api assistant mode providing (fixes #9924)`
  ← chat/chat-window/chat-window.component.ts
- `chat: smoother sidebar form handling (fixes #9430)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.component.ts, chat/chat.model.ts
- `chat: smoother angular form handling (fixes #9429)`
  ← chat/chat-window/chat-window.component.ts
- `chat: smoother forms handling (fixes #9319)`
  ← shared/dialogs/dialogs-chat-share.component.ts
- `chat: smoother provider naming (fixes #9329)`
  ← chatapi/src/models/chat.model.ts, chatapi/src/models/db-doc.model.ts, chat/chat.component.ts, chat/chat.model.ts, shared/chat.service.ts
- `chat: smoother servicing (fixes #9310)`
  ← chatapi/src/index.ts, chatapi/src/services/chat.service.ts
- `chat: less assistant message is more (fixes #9294)`
  ← chatapi/src/services/chat.service.ts
- `chat: smoother missing docs error handling (fixes #9292)`
  ← chatapi/src/index.ts, chatapi/src/utils/db.utils.ts
- `chat: smoother global default context (fixes #9203)`
  ← chat/chat-window/chat-window.component.ts, shared/ai-prompts.constants.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `chat: smoother textarea padding (fixes #9111)`
  ← chat/chat-window/chat-window.scss
- `chat: smoother prompt inputs (fixes #9058)`
  ← chat/chat-sidebar/chat-sidebar.component.ts, chat/chat-window/chat-window.component.ts
- `chat: smoother unique ids (fixes #9008)`
  ← chatapi/src/models/chat.model.ts, chatapi/src/models/db-doc.model.ts, chatapi/src/services/chat.service.ts, chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.component.ts, +5 more
- `chat: smoother team sharing (fixes #7829)`
  ← chat/chat.module.ts, shared/dialogs/dialogs-chat-share.component.html, shared/dialogs/dialogs-chat-share.component.ts, shared/dialogs/dialogs-chat-share.module.ts, shared/dialogs/planet-dialogs.module.ts
- `chat: smoother siderbar (fixes #8932)`
  ← chat/chat-sidebar/chat-sidebar.component.html, chat/chat-sidebar/chat-sidebar.scss
- `chat: smoother provider toggle (fixes #8836)`
  ← chat/chat.component.html, chat/chat.scss
- `chat: smoother dev port (fixes #8760)`
  ← .gitignore, README.md, angular.json, chatapi/README.md, dev-env.sh, +2 more

## life (12)

- `life: smoother health blood pressuring (fixes #10305)`
  ← health/health-event.component.html
- `life: smoother health name overflow handling (fixes #10271)`
  ← health/health.component.html, health/health.scss
- `life: smoother achievements member date showing (fixes #10192)`
  ← users/users-achievements/users-achievements.component.html, users/users-achievements/users-achievements.component.ts
- `life: smoother achievements avatar handling (fixes #10238)`
  ← shared/avatar.component.spec.ts, shared/avatar.component.ts, users/users-achievements/users-achievements.component.html, users/users-achievements/users-achievements.component.ts, users/users-profile/users-profile.component.html, +2 more
- `life: smoother personals resources title padding (fixes #10137)`
  ← resources/resources.component.html, resources/resources.scss
- `life: smoother achievements resume attaching (fixes #9782)`
  ← shared/couchdb.service.ts, shared/forms/file-input.component.ts, users/users-achievements/users-achievements-update.component.html, users/users-achievements/users-achievements-update.component.ts, users/users-achievements/users-achievements-update.scss, +4 more
- `life: smoother achievements loading (fixes #8937)`
  ← users/users-achievements/users-achievements.component.ts, users/users-profile/users-profile.component.html
- `life: smoother health profile showing (fixes #9859)`
  ← health/health.scss
- `life: smoother achievements username overflow handling (fixes #9681)`
  ← users/users-achievements/users-achievements-update.component.html
- `life: smoother achievements forms handling (fixes #9393)`
  ← users/users-achievements/users-achievements-update.component.html, users/users-achievements/users-achievements-update.component.ts
- `life: smoother achievements form array handling (fixes #9393)`
  ← users/users-achievements/users-achievements-update.component.ts
- `life: smoother health info form handling (fixes #9288)`
  ← health/health-update.component.ts

## login (10)

- `login: smoother profile form aligning (fixes #9944)`
  ← users/users-update/users-update.component.html, users/users-update/users-update.scss
- `login: smoother profile username overflow handling (fixes #9684)`
  ← users/users-profile/users-profile.component.html
- `login: smoother dialogs handling (#9796)`
  ← dashboard/dashboard-notifications-dialog.component.ts, login/login-dialog.component.ts, login/login-form.component.ts, login/login.module.ts
- `login: smoother speed optimizing (fixes #9763)`
  ← login/login-form.component.ts, login/login-tasks.service.ts
- `login: smoother sass module handling (fixes #9703)`
  ← login/login.scss
- `login: smoother form handling (fixes #9528)`
  ← login/login-form.component.html, login/login-form.component.ts
- `login: smoother color styling (fixes #9488)`
  ← login/login.scss, shared/planet-language.scss
- `login: smoother profile form updating (fixes #9383)`
  ← resources/resources-add.component.ts, shared/table-helpers.ts, users/users-update/users-update.component.ts, users/users-update/users-update.model.ts
- `login: smoother migration form handling (fixes #9366)`
  ← configuration/migration.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `login: smoother typed forms (fixes #9059)`
  ← login/login-form.component.ts

## mylife (4)

- `mylife: smoother myhealth emergency contact validating (fixes #9390)`
  ← health/health-update.component.ts
- `mylife: smoother myhealth event form handling (fixes #9290)`
  ← health/health-event.component.ts

*— below here predates the gerund era (2025-10-14); take
scope and noun-phrase precedent only, not the ending. —*

- `mylife: smoother mysubmissions cursor (fixes #9001)`
  ← submissions/submissions.component.html
- `mylife: smoother achievement toolbar (fixes #8874)`
  ← users/users-achievements/users-achievements.component.ts

## enterprises (3)

- `enterprises: smoother reports formatting (fixes #10301)`
  ← teams/teams-reports.component.ts
- `enterprises: smoother joining (fixes #10154)`
  ← shared/dialogs/dialogs-prompt.component.html, shared/dialogs/dialogs-prompt.component.ts, teams/teams-view.component.ts, teams/teams.component.html, teams/teams.component.ts, +1 more
- `enterprises: smoother finances pictures attaching (fixes #9966)`
  ← shared/couchdb.service.ts, shared/dialogs/dialogs-form.component.html, shared/dialogs/dialogs-form.component.ts, shared/dialogs/dialogs-form.service.ts, teams/teams-attachments.service.ts, +9 more

