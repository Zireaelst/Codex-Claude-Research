# EVM Launchpad Implementation Plan

> For agentic workers: use a task-by-task plan execution workflow with review gates; if available, `superpowers:executing-plans` may help. No particular agent platform or delegation is required.

**Goal:** implement the entire specified product in a new application repository.

**Architecture:** shared immutable launch primitives with separate v3/v4 paths, bounded rules, isolated vault accounting and network-specific verified manifests; web/API/indexer form one product. Reusable blueprints contain approved configurations, not arbitrary code.

**Tech stack:** Solidity/Foundry; pinned upstream Uniswap/Permit2; TypeScript, React, viem/wagmi; PostgreSQL; browser E2E runner. Exact compatible versions are pinned by WP01, not guessed from this research package.

## Global constraints

No Arc dependency. Both paths required. V4 first. Six modules maximum; exact bounds in economics/rules. No real-value transactions or deployment without separate permission. No invented interfaces, addresses or passing-test claims. All application paths below are proposed paths in the NEW repository, not files currently present in this archive. This plan specifies test behavior and deliverables; implementation code is intentionally not prewritten.

## Universal task cycle

For EACH package: [ ] select acceptance cases; [ ] write failing tests reproducing the intended behavior; [ ] run and record the expected failure; [ ] implement minimal coherent logic; [ ] run targeted and affected regression tests; [ ] compare against security invariants; [ ] update evidence/status; [ ] commit. Never weaken a test just to pass. Keep a reviewable contract+test or feature+test change together. The complete application is the cumulative result of all packages, not an optional later ambition.

### WP01 — Reproducible protocol harness and network schemas

Files: packages/contracts/foundry.toml, packages/contracts/test/integration/UpstreamHarness.t.sol, packages/config/src/network.ts, package lockfiles, docs/evidence/upstream.md.

Consumes: network specification, official upstream sources. Produces: pinned real v3/v4/Permit2 artifacts, validated NetworkManifest schema and local-chain setup. Compile differing exact upstream pragmas in isolated build jobs. Test CREATE2 permission-bit hook deployment without etch, real swap settlement and actual position fee harvest. Run `forge test --match-path 'test/integration/UpstreamHarness.t.sol'` from contracts package. Expected: real managers execute, balances reconcile, zero failures. Tests A07/A09/A30 foundation. If this cannot run, do not write a complete mock-based protocol on top.

### WP02 — Registry, tokens and authority boundaries

Files: packages/contracts/src/{LaunchRegistry,TokenFactory,StandardToken,AdvancedToken}.sol; test/unit/FactoryRegistry.t.sol; packages/sdk/src/config-schema.ts.

Consumes: shared LaunchConfig schema, manifest. Produces: deterministic launch identity, single-mint tokens, write-once records and authenticated lifecycle controller. Test arbitrary custodian, creator impersonation, wrong path, cross-launch mutation, supply increase and config changes all rejected. Test advanced profile sunset/partial claims/exemptions. A01/A11/A13; `forge test --match-path 'test/unit/FactoryRegistry.t.sol'`.

### WP03 — Curve accounting, fees and perpetual refund

Files: src/curve/{CurveMath,CurveFactory,CurveSale}.sol; src/fees/FeeVault.sol; test/{unit/CurveSale.t.sol,invariant/CurveAccounting.t.sol}; packages/sdk/src/curve-model.ts.

Consumes: WP02 token/registry, economics. Produces: buy/sell quotes and execution, entitlements, backed fee accrual, pending and expiry/refund states. Independent rational reference model must not reuse production math. Test final-buy cap, six/eighteen decimals, tiny trades, claim ordering and failed transfers. A02–A05/A10/A16. Run unit plus stateful accounting suite with recorded seed.

### WP04 — Real v4 graduation, hook registration and locked principal

Files: src/v4/{GraduationExecutor,V4Locker,CompositeHook,HookRegistry}.sol; src/vaults/DustVault.sol; test/integration/V4Lifecycle.t.sol.

Consumes: actual CurveSale and WP01 real artifacts. Produces: atomic pending → pool/locked LP → token claims; failed attempt rollbacks; exact config-bound initialization. Test real Permit2 settlement, both asset orientations, actual LP inventory transfer, attacker pre-init through genuine PositionManager, swap and repeated fee harvesting. A05–A09/A15/S01–S16 relevant invariants. No alternate mock path may satisfy this package.

### WP05 — Required v3 instant lane

Files: src/v3/{V3Launcher,V3Locker}.sol; test/integration/V3Lifecycle.t.sol.

Consumes: WP02 and real v3 artifact harness. Produces: immediate pool, full-range founding NFT custody, fee claims and dust accounting. Test seeded and conflicting initialized pools, bounded price/liquidity, recipient failure and impossible principal withdrawal. A12/A16. No v4 module can be attached to this lane.

### WP06 — Rule composition and trading router

Files: src/rules/{RuleValidator,OpeningRules,DynamicFee,BurnRule,ReferralRule}.sol; src/router/{LaunchRouter,QuoteLens}.sol; test/integration/RulesAndRoutes.t.sol; packages/sdk/src/rule-schema.ts.

Consumes: config registry and real pools. Produces: validated presets, authenticated TradeContext, executable quote schema and exact-input router. Test all allowed combinations, all conflicts, maximum aggregate cost, repeated swaps in one transaction, spoofed actor and unsupported aggregator routes. A14/A15/A22. Burn only in pool; no curve entitlement burn. Test timestamp boundaries without assuming fixed block time.

### WP07 — Existing-token markets and positions

Files: src/existing/ExistingPoolFactory.sol; test/integration/ExistingPools.t.sol; packages/sdk/src/pool-identity.ts.

Consumes: WP04/WP06 pool rules. Produces: distinct pool key/config, two-sided seed to opener-owned NFT, full-range LP operations. Test unsupported token behaviors, thin/empty pool, token-team impersonation and complete LP exit. A17/A18. No globally fixed token supply assumption or founding-lock badge.

### WP08 — Funded incentives and maintenance

Files: src/rewards/{RewardVault,LPRewardVault}.sol; src/maintenance/{MaintenanceVault,PriceObservations}.sol; test/invariant/RewardSolvency.t.sol; test/integration/Maintenance.t.sol.

Consumes: creator fee allocations and verified pool identity. Produces: backed time-weighted token/LP rewards, principal-safe withdrawals, protected auto-LP OR buyback. Test empty periods, late deposit, reward-token failure, stale/manipulated observations and funding exhaustion. A19/A21. No deterministic buy-count jackpot or newly invented platform token.

### WP09 — Community work and immutable blueprints

Files: src/community/{CommunityTreasury,WorkEscrow}.sol; src/blueprints/BlueprintRegistry.sol; test/unit/WorkLifecycle.t.sol; test/unit/Blueprints.t.sol.

Consumes: optional creator allocation and approved rule schema. Produces: funded assignments, independent review, deterministic timeouts, pull payments and reusable immutable templates. Test every deadline edge, revision, reviewer collusion boundary, duplicate payment and template hiding without old config mutation. A20/A28.

### WP10 — Read model, API and independent-agent interface

Files: packages/db/migrations/*; apps/indexer/src/{ingest,reorg,projection}.ts; apps/api/src/routes/{networks,launches,quotes,transactions,claims,jobs}.ts; packages/sdk/src/client.ts; apps/api/test/*.

Consumes: generated ABIs/events from completed contract packages. Produces: specified endpoints and versioned OpenAPI schema, indexer rollback, unsigned transaction planner. Test reorg/replay/duplicates, quote expiry, SSRF, fake token metadata instructions and target/spender validation. A22–A24/A29. Return real unavailable states instead of fabricated stats.

### WP11 — Complete web experience

Files: apps/web/src/routes/{board,launch,token,pool,portfolio,earnings,campaigns,community,blueprints,admin}; packages/ui/*; apps/web/e2e/*.

Consumes: SDK/API, contract manifests, wallet provider. Produces: all specified journeys, address-specific quotes and local-contract execution. Browser tests create v4 and v3 launches, cross graduation, trade, claim, fund work, stake rewards and exit external LP. A25–A29. Example fixtures explicitly isolated; cannot be the default proof of product completion.

### WP12 — Review, operations and network evidence

Files: docs/runbooks/{incident,indexer-recovery,restore,network-activation}.md; packages/config/networks/*; CI workflows; docs/evidence/acceptance.md.

Consumes: entire working product. Produces: clean-clone proof, fork evidence, security review findings, monitoring/restore drill, matrix of all A01–A32. Perform actual static analysis, fuzz/invariant suites and adversarial review; do not label them independent audit. Prepare deployment configuration but do not broadcast. Report all limitations and required external approvals. A30–A32 and all unresolved cases.

## Suggested standardized commands

Implement and document root commands `install:frozen`, `typecheck`, `lint`, `test:contracts`, `test:integration`, `test:api`, `test:e2e`, `build`, `dev:local` and `verify:manifests` in the new repo. None may secretly deploy to public networks. `dev:local` starts disposable local EVM, seeded real upstream contracts, DB/indexer/API/web. Root `check` runs deterministic validations and returns nonzero on any failure. Clean clone must work without internal-only packages from a hosted development environment.
