# Roadmap to a complete dual-path launchpad

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

The initial complete release includes both v3 and v4. Milestones below are dependency-ordered engineering checkpoints, not a v3-only launch commitment.

| Stage | Deliverables | Acceptance criteria |
| --- | --- | --- |
| 1. Product and dependency validation | Creator feedback; exact integration manifest; curve reference model; both-path UX specification. | Three relevant teams bring recurring paid work; seed/fee tradeoffs are explicit; required Arc dependencies are independently verifiable. |
| 2. Shared contract foundation and v3 | Token factory/registry, v3 launcher/locker, fee accounting, treasury and funded-work escrow. | Atomic lock; no principal escape; supply and per-asset accounting invariants; approval and payment work. Internal checkpoint only. |
| 3. Curve and v4 foundation | Curve balances, expiry/refunds, graduation executor, v4 locker and reviewed standard/protected-opening presets. | Solvency, price continuity, exact target fills, retry/refund and hook-permission tests pass. Both directions and supported swap types work. |
| 4. Complete application and indexing | Both selectable launch flows; trading, discovery, charts, fees, budgets, assignments, submissions, approval and claims; phase-aware indexer. | Fresh creators can complete either path without developer intervention; no production mocks or fake readiness; replay reconstructs accounting. |
| 5. Independent review and release readiness | Reproducible export, independent contract review, external deployment/hosting plan, monitoring and recovery procedures. | Both paths pass the release checklist; no unresolved critical/high findings; missing dependencies block release. |
| 6. Separately authorized deployment and acceptance | Independently signed deployment, source verification and controlled small-value checks for each path. | Receipts, actual transfers, LP custody and fee/payout reconciliation confirmed separately for v3 and v4. Not authorized by this documentation task. |
| 7. Extensions | Advanced bounded dynamic fees, optional collected-fee burns, external LP incentives, cross-chain funding, richer creator integrations. | Each solves observed user friction and passes its own economic/security review. |

## Definition of a complete initial product

For each launch path, demonstrate the appropriate lifecycle plus trading, fee collection, funding work, submission, acceptance and USDC payment. The v4 path must additionally demonstrate graduation and failure/refund recovery. A token factory, landing page or disabled second path is insufficient.

Read [economic parameters](04-economics-and-lifecycles.md), [security gates](06-security-and-release-checklist.md) and [Studio handoff](studio/README.md) before implementation.
