# Contract boundaries and data flow

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The contract system should separate market custody from community spending.**

```text
Creator / trader wallet
        │
        ├── LaunchFactory + LaunchRegistry
        │       ├── FixedSupplyToken
        │       ├── V3Launcher → v3 pool → V3LiquidityLocker
        │       └── CurveSale → GraduationExecutor
        │                           → v4 pool + fixed hook preset
        │                           → V4LiquidityLocker
        │
        └── Approved swap router / curve trading interface

Founding-LP fees → FeeAccounting
                      ├── Creator claims
                      ├── Protocol claims
                      └── CommunityTreasury → WorkEscrow → Contributor claims

Events → Indexer → API → Discovery, charts, budgets and work history
```

| Boundary | Responsibility and restriction |
|---|---|
| Token factory | Mint once; bind token to one launch ID/path. No arbitrary token implementation supplied by creators. |
| Launch registry | Canonical pool, path, deployment version, immutable economic configuration hash and metadata history. |
| v3 launcher | Atomic pool initialization, seed transfer and position creation. Cannot become a general-purpose execution proxy. |
| v3 locker | Hold founding NFT; collect fees only; no approvals, transfers, principal decreases or arbitrary calls. |
| Curve sale | Curve balances, reserves, quotes, fees, target and refund state. No treasury spending from reserves. |
| Graduation executor | Validate target and pool state; create and lock position; finalize claims atomically. |
| v4 locker | Hold position and collect fees through a narrowly constructed action sequence. |
| Hook registry | Approve reviewed versions and compatible parameter presets for **future launches**. Cannot replace an existing launch’s hook. |
| Composite hook | One fixed pool hook implementing the selected compatible rules; no creator-uploaded code or arbitrary `delegatecall`. |
| Fee accounting | Per-launch, per-asset liabilities and pull claims; no commingling of accounting between communities. |
| Community treasury | Available/committed balances, authorized work funding and public spending events. No access to pool principal. |
| Work escrow | Fully funded assignments, reviewer authorization, acceptance, deadlines and contributor claims. |
| Indexer/API | Search and derived data only. It never authorizes payments or determines balances used by contracts. |

A v4 pool has one hook address, although that hook may implement multiple callbacks and serve multiple pools. Selected modules therefore need a reviewed **composite implementation**, not independently attachable hook contracts. [Uniswap hook model](https://developers.uniswap.org/docs/protocols/v4/concepts/hooks)

For v4 fee collection, allow only the specific **zero-liquidity decrease** operation needed to realize fees. A blanket prohibition on every decrease action would trap fees; a general decrease function would endanger principal. [v4 PositionManager documentation](https://developers.uniswap.org/docs/protocols/v4/guides/position-manager)
