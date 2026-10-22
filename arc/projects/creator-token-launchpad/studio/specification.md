# Current detailed specification

Both v3 and v4 are mandatory for the complete initial product. The final decision below supersedes any historical v3-only release wording.

# Final product decision: both v3 and v4

**Authority:** user's final direction on October 22, 2026. [Original Turkish message](../../../research-06/decision-original.md).

The platform will offer **both launch paths**. The token creator selects one during creation. Each path exposes its own compatible feature set. This decision supersedes the historical v3-first-release recommendation, not the underlying security constraints.

| Choice | Canonical path | Creator-facing behavior | Path-specific features |
| --- | --- | --- | --- |
| Start trading now | Immediate Uniswap v3 token/USDC pool | Choose identity, reviewed initial liquidity and fee recipients; launch and lock founding LP atomically. | Immediate final market; fixed pool fee; no curve, migration or v4 hooks. |
| Launch toward a community target | USDC bonding curve, then locked Uniswap v4 pool | Choose identity and an approved bounded rule preset; users trade curve balances until graduation. | Curve progress, target/expiry, partial fills, recovery/refunds, graduation, pool-specific hook presets. |

## Shared product

Creator profiles, discovery, charts, wallet trading, transparent fee collection, creator claims, community USDC budget, funded assignments, submissions, review, contributor payments, portfolio and public completion history.

## Binding boundaries

- One token has one immutable canonical launch path; no later v3/v4 toggle.
- v4 pool hooks never apply to v3 pools. Neither path controls every external pool for its token.
- Contract implementation can proceed in dependency order, but the complete initial launchpad must allow a creator to select either working path. An internal v3 milestone is not the finished product.
- A placeholder, disabled selector or mock v4 flow does not satisfy the two-path release scope.
- Each path must independently pass its security and integration gates. Missing dependencies block that path and therefore the complete release; do not disguise them as implemented features.
- Different feature sets do not mean arbitrary creator code. Use bounded, reviewed presets with explicit compatibility rules.
- Initial v4 presets: standard fixed fee and protected opening surcharge. More advanced volatility fees, external LP incentive campaigns and automatic burns remain separately gated extensions, not claims of completed functionality.
- Proposed seed amounts, splits, curve parameters and fees remain design proposals requiring validation; the user confirmed the two-path scope, not every numeric parameter.
- The current task authorizes documentation and GitHub publication only. It does not authorize implementation, wallet creation, deployment or spending.


---

# Product journeys, launch choices and features

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The product should present two choices, with one permanent choice per token.**

| User-facing choice | Explanation | Underlying path |
|---|---|---|
| **Start trading now** | Seed a market, permanently lock its founding liquidity, and begin trading immediately. | Uniswap v3 |
| **Launch toward a community target** | Buy and sell against a published curve; reaching the target creates the permanent market with the selected rules. | Curve → Uniswap v4 |

The canonical path is recorded at creation and cannot be switched. External pools may still exist. “Canonical” identifies our supported launch market; it does not grant exclusive control over the token.

A **v4 hook** is an onchain callback attached to a particular v4 pool. A treasury spending rule is application logic. An offchain webhook is a notification mechanism. They are separate concepts.

The full user journeys should be:

| User | Complete journey and recurring loop |
|---|---|
| Creator | Connect → create a community profile → choose launch path → review immutable economics and risks → launch → publish the token page → monitor collected revenue → commission work → publish completed outcomes → return for the next budget cycle. |
| Buyer | Discover a community → inspect creator identity, actual liquidity, launch rules and spending history → fund wallet → review quote and fees → buy → track position and community updates → sell or participate. |
| Trader | Find an exact token/pool → inspect liquidity, fees and market phase → quote → approve exact spender → execute → inspect receipt and position history. No compulsory social participation. |
| Contributor | Discover **funded** work → read acceptance criteria and reviewer identity → submit or accept an assignment → deliver → receive approval → claim USDC → build a public completion history. Holding the token is unnecessary. |
| Community manager | Review available versus committed funds → publish bounded work budgets → assign reviewers → approve/reject with reasons → release payments → reconcile spending and publish updates. |

The strongest social loop is **completed work → shareable attribution → new contributors and audience → continued community activity**. Trading-volume leaderboards and wash-trade incentives are not substitutes.



**The feature boundary should remain visible in the product.**

| Feature | Shared | Instant v3 | Curve → v4 | Later |
|---|---:|---:|---:|---:|
| Creator profiles, token pages, charts, watchlists | ✓ | | | |
| Fixed supply and permanent founding LP custody | ✓ | | | |
| Treasury, funded work, claims and spending history | ✓ | | | |
| Immediate final pool | | ✓ | | |
| Fixed pool fee | | ✓ | ✓ | |
| Curve progress, expiry and refund state | | | ✓ | |
| Pool-level opening protection | | | ✓ | |
| Bounded dynamic pool fees | | | ✓ | |
| Burn collected token fees | ✓ | | | Separate reviewed release |
| External LP incentive campaigns | | | | ✓ |
| Cross-chain USDC onboarding | | | | ✓ |
| Embedded wallets and gas sponsorship | | | | ✓ |
| Creator subscriptions, merchandise integrations | | | | ✓ |
| Community governance or takeover | | | | Separate governance design |
| Lottery / every-Nth-buy prize | | | | **Excluded** |

For v4 rules, begin with only two choices:

- **Standard:** fixed 1% pool fee.
- **Protected opening:** a deterministic, disclosed fee declining from at most 3% to 1% over at most 120 seconds after graduation.

This is an **early-trading surcharge**, not proof of bot exclusion. A later volatility-sensitive preset could operate within a 0.3–2% band, but requires manipulation analysis of its reference price.

Do not combine arbitrary percentage fees independently. Define one maximum effective swap charge and test every allowed combination.

“Burns” should initially mean burning a share of collected token fees outside swap execution. “Community rewards” should mean funded contributions. “LP rewards” should mean a separately funded incentive campaign with explicit eligibility—not redistributing other LPs’ principal or implying all pool fees belong to the founder.



**The frontend needs to make community activity as tangible as trading.**

The first complete app should include:

- **Discover:** communities, active work, recent launches, liquidity and activity filters; no fake popularity.
- **Launch wizard:** path comparison, supply, initial liquidity, fee policy, manager identity and an immutable-settings receipt.
- **Token page:** chart, trade panel, holdings, founding LP evidence, fee rules, treasury, funded work and completed contributions.
- **Creator dashboard:** launches, uncollected versus claimable fees, team recipients and metadata history.
- **Community workspace:** available budget, commitments, reviewer queue, spending log and published updates.
- **Contributor workspace:** assignments, submissions, decisions and USDC claims.
- **Portfolio:** balances, transactions, cost basis only where history is complete, and outstanding claims.
- **Recovery views:** failed transaction, stale indexer, wrong network, insufficient gas, curve refund and graduation retry.
- **Share cards:** token identity, exact address, funded assignment or completed contribution; no fabricated returns or guaranteed-income language.

Index launches, pools, swaps, LP ownership, collections, fee credits, claims, treasury commitments and work outcomes. Use block number, transaction hash and log index for idempotency, with rollback/replay support.

Expose paginated endpoints for tokens, candles, trades, holders, launch rules, fees, treasury ledger, work and indexer health. Read execution-critical state directly from contracts before signatures.

A practical runtime stack is Vite/React, viem/wagmi, pinned Uniswap SDKs, a PostgreSQL-backed event indexer, object storage/IPFS for public assets, and a notification worker. Secrets stay server-side. Circle wallets or CCTP can be added when they solve a demonstrated onboarding problem; neither is necessary to prove the core product.


---

# Arc, Uniswap and Studio: verified scope and gates

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The infrastructure is sufficiently documented to design against, but several deployment gates remain.**

Official Uniswap documentation lists the following **Arc mainnet, chain 5042** deployments:

| Component | Officially listed address |
|---|---|
| v3 Factory | `0xf0db7b58379503491d857dB50AC9ece64c653918` |
| v3 Position Manager | `0x39654A85A4C05127f5Fd6ED22CAeC077A0fB1377` |
| v3 SwapRouter02 | `0x53BF6B0684Ec7eF91e1387Da3D1a1769bC5A6F77` |
| v4 PoolManager | `0x8366a39CC670B4001A1121B8F6A443A643e40951` |
| v4 PositionManager | `0x6049c9a0e26405C0985f9E3685C87d0aE917f82B` |
| Universal Router 2.1.2 | `0x8702463e73f74d0b6765aBceb314Ef07aCb92650` |

Source: [Uniswap deployment registry](https://developers.uniswap.org/deployments.json) and [v4 deployment documentation](https://developers.uniswap.org/docs/protocols/v4/deployments). The registry also lists launch infrastructure on Arc, further weakening any claim that basic issuance is missing.

Before implementation targets these addresses, verify chain ID, runtime bytecode, implementation/version, factory relationships and relevant immutable values. Do not paste deployment addresses from competitor documentation into production configuration.

Arc’s USDC ERC-20 interface is `0x3600000000000000000000000000000000000000`, using **6 decimals**. Native USDC uses **18 decimals**, but represents the same underlying balance. Arc recommends the ERC-20 interface for application balance reads and transfers. Use it consistently for pools, fees and treasuries; do not invent wrapped USDC or count native and ERC-20 balances as separate assets. [Arc contract documentation](https://docs.arc.io/arc/references/contract-addresses)

| Capability | Design status |
|---|---|
| Mainnet EVM, USDC gas, wallet configuration | Officially documented; mainnet 5042, testnet 5042002. [Network documentation](https://docs.arc.io/arc/references/connect-to-arc) |
| Official mainnet v3/v4 | Listed by Uniswap; independent runtime verification remains a release gate. |
| Canonical Arc **testnet** v3/v4 deployments | Not established in this research. Use a clearly labelled test deployment or local fork; never present it as canonical. |
| CCTP/Gateway funding | Official Arc addresses are documented; useful later for onboarding, unnecessary for the first launch/trade loop. |
| Custom v4 hook | Must be built, reviewed and deployed separately. Existing v4 infrastructure does not certify our hook. |
| Charts, treasury accounting, discovery | Require our indexer and application backend; not supplied automatically by Arc or Uniswap. |
| Embedded wallets | Optional later integration, subject to current provider support and recovery model. Wallet connection is sufficient initially. |
| Studio mainnet deployment/public hosting | Not supported by the inspected terms; use independent tooling and hosting. |

The local CLI was available. `whoami` returned **not authenticated**. `agent-guide`, `skills --json` and command help were readable. The guide describes a Vite/Foundry workspace, named sessions, file export and a **10,000-character prompt limit**. Its Uniswap skill says “Arc mainnet only,” but that describes integration context—not permission for Studio to broadcast.

Studio’s terms explicitly place mainnet review, testing, deployment and operation outside Studio, and say Studio does not host apps. Mainnet references in a preview are not a deployment. [Studio terms, §§1.2, 4.1, 4.8](https://studio.arc.io/terms-of-use)



**Studio should be the build workspace; export and independent review should be the release boundary.**

Use Studio to generate and iterate on contracts, tests, frontend, indexer code, schemas and integration tests. Its preview can demonstrate UI behavior, but must not be presented as production hosting.

Export the source, lockfiles, compiler settings, ABIs, test suites and configuration. Outside Studio:

1. Rebuild in a clean environment and inspect dependencies/licenses.
2. Verify canonical Arc contracts and runtime behavior.
3. Run local/fork tests and separately authorized testnet tests.
4. Obtain independent review of custody, accounting and any curve/hook.
5. Prepare exact mainnet deployment transactions with your own tooling and signer.
6. Deploy only after approval; verify source and configuration.
7. Host frontend/API/indexer independently.
8. Run a small-value production acceptance check.

A later controlled acceptance check could use an explicitly labelled team-owned launch, a **1 USDC buy**, a small sell, fee collection and a **0.01 USDC contributor payment**. The treasury can receive an explicitly labelled test top-up if actual collected fees are insufficient. Seed liquidity, launch fees and gas are additional costs. Do not imply that a 1 USDC trade finances the whole test or proves organic demand.

The records must show successful transaction receipts, the actual transfer events, pool/locker identity, fee allocation and the contributor’s received amount. None of this has been executed.


---

# Economics, v3 lifecycle, curve and v4 graduation

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The initial economics should be deliberately constrained.**

The following are **proposed defaults**, not established optimal parameters.

| Parameter | Recommended initial policy |
|---|---|
| Supply | 1 billion tokens, 18 decimals, minted once. No creator allocation, future minting, transfer tax or blacklist. |
| Instant-launch liquidity | Creator-funded, two-sided, full-range v3 position. Pilot UI accepts 500–25,000 USDC; exact supported bounds must follow simulation. All issued tokens enter the position except explicitly bounded rounding residue. |
| Opening price | Derived from supplied USDC and tokens, with correct decimal scaling. With essentially all supply deposited, opening FDV is approximately the USDC seed—not an independently selectable valuation. |
| v3 pool fee | Fixed 1%; no additional interface trading fee initially. |
| Collected founding-LP fee split | **40% creator team / 50% community treasury / 10% protocol**, applied separately to each received asset. Immutable per launch. |
| Creator team | Up to five recipients; fixed percentages at launch. Recipient changes require the existing recipient’s consent and settle prior accrual first. |
| Launch fee | 5 USDC, charged only on successful creation. Separate from seed liquidity. |
| Curve fee | 1% on buys and sells, explicitly excluded from backing reserves. |
| Curve graduation | One reviewed preset initially; illustrative net reserve target of 6,000 USDC, 80% sold and 20% reserved for LP. |
| Curve expiry | Fixed at creation; initially 30 days. No discretionary creator extension. |
| v4 base fee | Fixed 1% first; bounded dynamic presets introduced only after separate review. |
| Community rewards | Funded work payments first. No automatic rewards for trading volume or wallet count. |
| Burns | Disabled initially. Later, an immutable option may burn a bounded share of collected token fees, never principal. |
| Bounty budgets | Fully funded from available USDC before publication. No spending against estimated future fees. |

**The seeded v3 choice has a real cost:** creators need starting capital, unlike single-sided launchpads. In return, the app can show an actual USDC reserve from the start. If target creators reject that tradeoff, evaluate a separately specified single-sided v3 preset before building; do not silently replace the liquidity model.

Full-range LP is less capital-efficient than a concentrated launch range. That is an acceptable initial tradeoff for simpler custody and fewer range-management assumptions.

Crucially, **v3 fees arrive in the input asset**. Buys commonly generate USDC fees; sells commonly generate token fees. The treasury must display:

- Available USDC.
- USDC committed to work.
- Uncollected estimated USDC fees.
- Token-denominated fees, separately.
- Completed USDC payments.

Do not mark token fees to a manipulable spot price and present the result as spendable dollars. Uniswap’s collection interface explicitly returns both assets. [v3 fee collection](https://developers.uniswap.org/docs/protocols/v3/guides/managing-liquidity/collect-fees)



**The two lifecycles need different failure semantics.**

For **Start trading now**:

```text
DRAFT → VALIDATED → SUBMITTED → ACTIVE_LOCKED
                         └── transaction reverts → retryable draft
```

Creation is atomic: deploy token → register canonical path → initialize pool at the committed price → mint LP directly to the locker → register fee policy and treasury → emit launch record.

There must never be a successful “token created, LP will be locked later” state.

- A failed transaction returns transferred assets through EVM rollback; gas is not refunded.
- An existing unexpected pool or price causes a revert, not opportunistic reuse.
- Unused USDC is returned; token rounding residue follows a predefined locked-residue policy.
- Successful launch is irreversible. The seed cannot be reclaimed by the creator.
- Selling occurs through the pool, not through a launch refund function.
- Founding LP principal cannot be decreased, transferred, approved away or rescued.
- Fee collection is permissionless, but proceeds can only enter the fixed accounting path.
- An app moderation flag may hide a token from discovery; it cannot freeze token transfers or seize LP.

For **Launch toward a community target**:

```text
DRAFT → CURVE_ACTIVE → READY_TO_GRADUATE → GRADUATED
              │                │
              │ expiry         │ unresolved migration failure
              ▼                ▼
          REFUNDABLE ← fixed timeout
              │
              ▼
            CLOSED
```

To prevent pre-graduation transfers from undermining the curve, I recommend **internal curve balances redeemable for the eventual token**, rather than introducing permanent restrictions into the ERC-20.

During the curve:

- Users buy and sell curve balances.
- The UI explicitly says these are claimable launch balances, not transferable ERC-20 holdings.
- The fixed token supply remains in contract custody.
- No creator-only first-buy privilege.
- Buys and sells use the same published pricing function and explicit slippage limits.

At the target:

- The final buy is capped to remaining capacity; excess USDC is returned.
- Curve trading closes.
- Graduation is attempted permissionlessly and atomically.
- Net backing USDC plus reserved tokens form the v4 LP.
- The LP is locked before graduation is recorded.
- Curve balances become redeemable 1:1 for tokens.
- Token claims do not depend on the website or indexer.

If graduation fails, reserves and balances remain intact. Anyone can retry. After a fixed recovery timeout—proposed **72 hours**—users can trigger the predefined refund state.

If the curve expires or migration becomes unrecoverable, redeem balances against a fixed pro-rata snapshot of remaining backing reserves. **This is not a refund of each user’s original purchase price.** Earlier buys, later buys, sells and trading fees make that promise impossible without separate insurance. Unclaimed refunds must not become an owner sweep.

An immutable hook initialization guard should permit only the registered graduation executor to initialize the canonical pool. Otherwise an attacker can initialize the future pool at a hostile price before migration.



**Curve continuity must be derived, not approximated by marketing numbers.**

A workable research model uses virtual constant-product reserves. Let:

- \(S\): total supply;
- \(q\): curve tokens sold;
- \(A\): virtual initial USDC;
- \(B\): virtual initial token reserve.

Then:

\[
R(q)=\frac{Aq}{B-q},
\qquad
p(q)=\frac{AB}{(B-q)^2}
\]

Here \(R\) is net backing USDC, excluding fees. To graduate with remaining tokens \(S-q_g\), require approximately:

\[
p(q_g)=\frac{R(q_g)}{S-q_g}
\]

For an 80% sale, this gives \(B=\frac{16}{15}S\). With \(A=2{,}000\) USDC:

- Graduation reserve: 6,000 USDC.
- Tokens for LP: 200 million.
- Terminal marginal price: 0.00003 USDC.
- Initial marginal price: approximately 0.000001875 USDC.

These are **analytical parameters, not production-ready Solidity constants**. Integer rounding, token ordering, finite v4 tick bounds and minting dust must be reconciled against actual pool mathematics. Require a documented continuity tolerance, proposed at most one basis point before trading fees, backed by differential tests.

A marginal-price match does not mean a large trade has identical execution before and after graduation: liquidity depth also changes.


---

# Contract boundaries and data flow

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

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


---

# Security, failure recovery and release gates

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**Security review must focus on the following failure modes.**

| Risk | Required design and test |
|---|---|
| Curve rounding and reserve insolvency | Integer-only arithmetic; explicit rounding direction; differential model; repeated dust trades cannot extract value; reserve accounting survives arbitrary buy/sell sequences. |
| Graduation discontinuity | Derive parameters together; compare actual initialized pool price and depth; prevent reserve deductions disguised as graduation fees. |
| Slippage and stale quotes | Every swap has minimum output/maximum input and expiry. Never use indexer prices as execution authority. |
| First buys and MEV | Atomic initialization; no hidden creator allocation or privileged curve price. v3 offers no hook-based protection. Private submission is optional only if actual Arc support is verified. |
| Pool initialization griefing | Reject unexpected v3 pool state; caller-bound launch salts reduce copying but are not complete protection. v4 initialization must require the registered executor. |
| External pools | Display rule scope. External trading can avoid our hook and creator fees. Additional LPs in the same pool earn their own share. |
| Locker escape routes | No generic execution, NFT approval, upgrade, rescue, migration or inactivity sweep affecting principal. Inspect inherited and callback paths. |
| Fee accounting | Credit actual received amounts; separate assets and launches; settle accrued fees before recipient changes; prevent duplicate claims and dust leakage. |
| Arc USDC representation | Use ERC-20 units consistently; reject unintended native value; test shared-balance behavior and gas budgeting on Arc. A mock ERC-20 is insufficient proof. |
| Hook permissions | Validate callback address flags, PoolManager caller, registered pool key and supported swap directions. Disabled callbacks cannot be invoked successfully. |
| Reentrancy and malicious recipients | Update state before external transfers; use pull claims; a blocked recipient must not halt all fee collection or other beneficiaries. |
| Treasury abuse | Manager authority is explicit. A manager can make poor or collusive awards; the contract cannot judge artistic quality. No arbitrary treasury call execution initially. |
| Sybil behavior | No “one wallet equals one person” claims; no volume mining, first-buy rewards or wallet-count rewards. |
| Metadata and social impersonation | Content hashes, edit history, signed creator linkage and moderation. A verified social link is not a safety endorsement. |
| Operational dependency | Indexer outages must not block claims/refunds. Stale data is labelled stale, never substituted with zero. |
| Licensing and legal exposure | Review copied code licenses, operating jurisdictions, token promotion and paid-contribution terms before release. Avoid implying token ownership conveys IP or financial rights. |

For work payments, use explicit states:

```text
FUNDED → ASSIGNED → SUBMITTED → ACCEPTED → CLAIMABLE → PAID
             └──────────────→ REJECTED / EXPIRED
```

A manager may cancel unassigned work. Once assigned, the agreed amount and acceptance terms cannot change unilaterally. Rejected or expired funds return to the **community treasury**, not the creator’s personal wallet. Accepted claims cannot be cancelled. Public rejection reasons and reviewer identities make discretionary trust visible.

**Exclude “every Nth buy wins the pot.”** The counter is predictable. Bots can split purchases, fill the remaining positions, bundle transactions or compete on ordering when the pot exceeds fees and price impact. Minimum buys and wallet caps do not solve this.

Randomness changes the mechanism but introduces oracle, entry-allocation, Sybil and potentially gambling issues. For this product, a fixed-budget creative commission or judged contest has a clearer purpose. Do not reward manufactured volume.



**Before any mainnet launch, every applicable release criterion must pass.**

| Check | Pass criterion |
|---|---|
| Network/dependencies | Correct chain ID; independently verified canonical contracts, versions and runtime code; no placeholders. |
| Reproducibility | Clean build reproduces release artifacts with pinned settings and dependencies. |
| Supply/path | Exactly one issuance and canonical path; no hidden allocation or mutable economics. |
| Liquidity custody | No reachable principal withdrawal, approval, transfer, upgrade or recovery escape path. |
| USDC accounting | Native/ERC-20 aliasing and decimal behavior tested on Arc; gas is not double-counted as spendable balance. |
| Fees | Collected amounts reconcile by asset and beneficiary; UI never labels token fees as USDC cash. |
| Trading | Correct quoting, slippage, expiry, approvals and receipt handling; buys and sells tested. |
| Work payments | Fully backed commitments; accepted payments cannot be cancelled or paid twice. |
| Curve/v4, when enabled | Solvency, continuity, initialization protection, retries, claims and refunds pass adversarial tests. |
| Hooks, when enabled | Permission bits and callback authentication verified; bounds hold across every enabled configuration. |
| Indexer | Replay produces matching accounting; stale or incomplete data is labelled; claims work without it. |
| Security review | No unresolved critical/high findings; independent reviewer has examined custody and accounting. |
| Operational control | No production keys in Studio, browser bundles, repositories or logs; monitoring and recovery procedures tested. |
| Product honesty | Lock, fee, refund, manager authority and external-pool limitations are visible before signing. |
| Production acceptance | Small-value receipts and balance changes reconcile end to end; no simulated success presented as real. |


---

# Roadmap to a complete dual-path launchpad

> Current planning document, organized from [the complete original report](../../../research-06/result.md). The [final user decision](../00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

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

Read [economic parameters](../04-economics-and-lifecycles.md), [security gates](../06-security-and-release-checklist.md) and [Studio handoff](README.md) before implementation.
