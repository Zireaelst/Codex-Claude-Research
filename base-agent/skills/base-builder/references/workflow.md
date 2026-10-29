# Work organization and agent handoff

## Single-agent loop

1. Read applicable source spec, repo instructions and current status. Pick one vertical slice with explicit acceptance; preserve final product scope.
2. Check dynamic dependencies before design commits: network activation, deployed code, compiler/upstream pins, venue capabilities and auth. Cite source/date/block where applicable.
3. For financial state transitions write meaningful failing tests first: conservation, replay, authorized recipient, partial execution and recovery. For UI changes use representative flows rather than assertion-only snapshots.
4. Implement the smallest coherent deliverable; run targeted tests and required affected checks. Use real upstream integration and fork evidence when testing protocol behavior.
5. Record actual command, revision, result, scope and blockers. A test name is not a passing result. Keep private data and credentials out of evidence.
6. Continue authorized independent work; ask only for missing decisions/access that block the next dependent step. Prepare concrete release artifacts before requesting any final action authorization not already supplied.

## When multiple agents are explicitly requested or authorized

Roles are responsibilities, not assumed installed agents:
- Coordinator: scope, contracts/API boundary, dependency graph, status and integration.
- Protocol worker: launchpad math, hooks, settlement, vaults and Foundry tests.
- App/data worker: generated clients, APIs, indexers or venue adapters.
- UX worker: mobile/desktop flows, state and accessibility tests.
- Reviewer: inspect delivered diffs and evidence independently; not an audit certification.

With four total slots, use coordinator + at most three workers; review can run after a worker completes. Do not imply a specific model or tool is mandatory. If delegation is unavailable, perform the same packages sequentially. Never create user-visible chats or message external services just to simulate subagents without the required authorization.

Freeze shared schema/ABI contracts before parallel consumers. Give each task file ownership, input revision, produced interface, acceptance tests and explicit non-goals. Avoid simultaneous edits to shared ABI/config/migrations; coordinator owns integration. Prefer isolated checkouts when supported. Worker completion must include files, commands/results, unresolved assumptions and status; coordinator reviews actual artifacts.

Dependency examples:
Launchpad harness → curve accounting → graduation/locked LP → rule/router → indexed/UI lifecycle → release preparation. UX prototypes can proceed from agreed schemas while protocol work runs.
Prediction capability spike → normalized market/domain → rooms/forecasts and order coordinator → positions/claims → E2E/reconciliation → pilot. Order types cannot be invented to unblock frontend.

## Persistent status in an application repo

Use `docs/agent/STATUS.md` with one row per work package: scope ID, state (not started/in progress/blocked/verified), current commit, evidence path, blocker and next action. Use `docs/agent/DECISIONS.md` for justified departures from source specs and `docs/agent/EVIDENCE.md` for executed checks. These are created only when implementation is requested; don't litter research-only tasks with scaffolds.

On context reset read status, decisions and relevant evidence, then inspect the actual working tree. Past passing checks apply to their recorded revision only. Report unfinished requirements as unfinished, not silently optional.
