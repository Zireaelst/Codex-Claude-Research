**Build a creator-community launchpad whose defining feature is what happens after launch: trading fees become a visible community budget, that budget funds specific work, and completed work becomes part of the token’s public history.**

Start with a complete **instant-launch v3 product**, then add the **curve-to-v4 path**. Both launch mechanisms already have direct Arc competitors. A longer list of hooks will not distinguish us; a better creator and contributor experience might.

Sources were checked on **October 22, 2026**. Below, **verified** means supported by official documentation or directly inspected tooling; **project claim** means documented by the project but not independently established onchain; **proposal** means my recommended design. No app was created, no product code was written, and no transaction was sent.

---

**The competitive evidence changes the positioning.**

| Arc product | What the inspected material supports | Implication for us |
|---|---|---|
| [ArcPad](https://arcpad.meme/docs) | Documents immediate v3 launches, fixed supply, a permanent fee locker, creator/holder rewards, charts and public APIs. Its launcher example identifies `0x24196CD6e534cfCE8F480B53E70809b68Ea86F29`. **Project claims**, not an independently verified deployment in this pass. | Instant v3 launch and locked LP are already offered. Documentation also contains inconsistent descriptions of transfer restrictions and fee treatment; implementation must determine actual behavior. |
| [Arcfun](https://arcfun.app/docs) | Documents a USDC curve graduating into a locked v4 pool, a hook, router and indexer. Factory: `0xBBf81Fd835B471C86d094eAaD35BB10068a987f8`. | Direct competitor to our programmable path. Graduation alone is not differentiation. |
| [moon](https://moon.family/docs) | Describes itself as a PONS v2 port: curve launches, v4 graduation, creator-fee or holder-reward modes, and burns. Documents a 1 USDC launch fee and 10,000 USDC graduation threshold for USDC launches. | Much of the requested feature set is already documented on Arc. Adoption and security remain separate questions. |
| [Arcade](https://www.arcade.trading/docs) | Publishes an [integration repository](https://github.com/obseasd/arcade-integrations) and [deployment manifest](https://www.arcade.trading/deployments.json), including curve and instant-launch modes. Current hook: `0x7706d261f0C370e8f0E273164A603E885C89beC2`. | A broad trading terminal is a crowded position. Its documented inactivity-based liquidity recovery also shows why “permanently locked” needs precise qualification. |
| [TOLLY](https://tollylabs.com/guide) | Publishes extensive launch, trading, fee-routing and rewards documentation, with a contract-source verification package. Listed launcher: `0xcad7ee36ac193bf2eddb7b3e2736c5bdb8269c8b`. Distinguishes calculated rewards from claimable rewards. | Strongest warning against competing on dashboards, fee splits or feature count alone. Borrow its evidence discipline. |
| [Parabola](https://parabola.meme/) | Public material describes USDC curves and graduation; inspected evidence did not establish a functioning launch/trade lifecycle or verified deployment. | Treat as announced competition, not proven adoption and not nonexistent. |

I attempted independent bytecode checks against Arc’s public RPC. Those requests returned access errors; explorer pages did not expose sufficient machine-readable evidence. **The addresses above are published identifiers, not deployment or security attestations.** I have not established organic trading volume, retained creators or revenue for these competitors.

The most useful cross-chain comparisons are:

| Reference | Mechanics and growth loop worth learning | Revenue, liquidity and protection | Weakness or constraint |
|---|---|---|---|
| [Pump.fun](https://pump.fun/docs/fees) | Extremely short creation flow, discovery, live activity and repeated creator launches. | Curve → PumpSwap; documented curve fee currently 1.25%, with separate post-graduation schedules and interface fees. | Distribution is the advantage; copying the curve does not reproduce the audience. Incentives can reward churn rather than enduring communities. |
| [PONS v1](https://docs.ponsfamily.com/) / [v2](https://docs.ponsfamily.com/v2) | Simple launch choices and persistent creator economics. | v1 documents direct v3 launches; v2 documents curve graduation and hook-based fees, with optional creator tax/buybacks. | Versions differ materially. Quote-asset fee claims require inspecting conversion paths, permissions and execution assumptions. |
| [Hookr](https://hookr.fun/docs/pools/core-blocks) | Understandable rule blocks, fixed launch configuration, reusable launcher infrastructure. | Anti-snipe, dynamic fees, burn and LP-reward mechanisms; some additional blocks explicitly remain “deploying soon.” | Permitted fee bounds can be extreme. More configurability expands the attack surface and makes comparison harder. The older AvaxHook reference should not be assumed identical to every current Hookr release. |
| [Flaunch](https://docs.flaunch.gg/protocol/frequently-asked-questions) | Creator economics plus community-managed revenue, rather than launch-only engagement. | Fixed-price opening period, subsequent price discovery, revenue rights and community buyback/treasury options. | Closest conceptual competitor. “Fees fund the community” is not our invention; our differentiation must be funded work, contributor coordination and transparent spending. |
| [Clanker](https://github.com/clanker-devco/v4-contracts) | Distribution through social creation workflows; modular deployment, rewards and launch protection. | Public v4 contracts include static/dynamic hooks, lockers and sniper-auction components. | Creator revenue belongs to particular positions and pools, not every market for the token. Existing social distribution is difficult to recreate. |
| [Zora](https://support.zora.co/en/articles/2509953) | Content itself becomes discovery inventory; creator, referral and trading loops reinforce each other. | Documents creator/content pool fees and additional interface transaction fees. | Tokenizing content does not automatically grant IP rights or create sustainable demand. Fee stacking needs clear presentation. |
| [Four.meme](https://four-meme.gitbook.io/four.meme/guide/how-it-works) | Familiar curve progression, ecosystem distribution, straightforward graduation. | Documents curve trading, reserved LP supply and migration to PancakeSwap. | Graduation targets and product versions change. The transferable lesson is predictable lifecycle presentation, not copying an old numeric threshold. |

These sources establish documented mechanics and inspectable implementations where linked. They do not establish comparative security or prove that a particular mechanism caused adoption.

---

**Three plausible positions emerge; only one is attractive enough to pursue first.**

| Position | First audience | Why they might choose it | Assessment |
|---|---|---|---|
| “The fastest Arc meme launcher” | Speculative launchers | Speed, low friction, discovery | Weak: ArcPad, moon, Arcfun and others already address this. |
| “The programmable launch laboratory” | Sophisticated creators and traders | Bounded rule presets, visible simulations, unusual market behavior | Credible second-stage identity, but expensive to secure and easy to turn into a confusing settings panel. |
| **“Launch a community with an operating budget”** | Small meme-art collectives, recurring content teams and community managers already commissioning work | Launch, trade, earn, commission, review and publish outcomes in one place | **Recommended.** Specific recurring workflow; still a hypothesis requiring creator validation. |

The first users should be **existing teams that already publish weekly and pay artists, editors or moderators**, not anonymous creators hoping token trading will manufacture a community.

Arc improves this experience because budgets, payouts, trading quotes and gas can all be expressed in USDC. It removes a volatile gas-token requirement and reduces conversion work for contributors. It does **not** supply audience, liquidity or sustainable fee income.

A useful product promise is:

> Launch a community token, see exactly what its founding liquidity earns, and turn available USDC into completed community work.

Avoid promises of passive income, guaranteed price support or token-holder entitlement to business profits.

---

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

---

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

---

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

---

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

---

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

---

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

---

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

**Delivery should proceed through acceptance gates, not through accumulating features.**

| Stage | Deliverables | Acceptance criteria |
|---|---|---|
| **1. Validate the product and integration assumptions** | Clickable journey specification; verified dependency manifest; economic model; creator feedback. | At least three target teams identify real recurring work they would fund and accept the proposed liquidity/fee model. Canonical contracts and Arc USDC behavior are independently readable. |
| **2. Contract foundation** | Token/registry, v3 launcher/locker, fee accounting, treasury and work escrow; unit, fuzz and invariant tests. | Atomic launch; principal cannot leave locker; both fee assets reconcile; accepted work can be paid exactly once; no unresolved critical/high findings. |
| **3. Complete v3 MVP** | Working launch, buy/sell, charts, discovery, fee collection, funded assignment, submission, acceptance and claim. | A fresh user can complete each role’s journey without developer intervention. Restarting the indexer reconstructs the same state. Failed transactions remain recoverable. |
| **4. Production hardening** | Independent review, production deployment plan, monitoring, backups, support procedures and public hosting. | Pinned build matches deployment artifacts; release checklist below passes; small-value end-to-end checks reconcile. |
| **5. Curve and graduation** | Curve balances, quotes, expiry/refunds, v4 executor and locked position; corresponding UI. | Price continuity meets tolerance; failure/retry/refund paths pass adversarial tests; no funds are stranded if graduation fails. |
| **6. Programmable launch presets** | Standard/protected-opening presets, compatibility validation and public rule explanations. | Each preset works for supported swap directions, cannot exceed fee bounds and cannot modify launched configurations. |
| **7. Platform expansion** | Cross-chain funding, external LP incentives, richer creator tools and integrations. | Each addition addresses measured user friction and has separate security/operational acceptance criteria. |

The MVP is complete only when **launch → trade → collect fees → fund work → approve → pay** works. A factory and a token page are not enough.

---

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

**The following master brief and prompts are ready for a later authorized Studio build.**

Save the master brief as `product-brief.md`. Save the specification above as `specification.md`. These are suggested filenames; no files or Studio session have been created during this research.

```text
Build a creator-community token launchpad on Arc.

Primary user: an existing meme-art or content team that regularly commissions
artists, editors or moderators. The product connects launch and trading with
a visible USDC operating budget, funded assignments, review and payments.

Two immutable launch paths:
1. Start trading now: fixed-supply token, creator-seeded full-range Uniswap v3
   token/USDC pool, atomic permanent founding-LP lock.
2. Launch toward a community target: USDC curve balances, permissionless
   graduation into locked Uniswap v4 liquidity, reviewed immutable rule presets.

Build the complete v3 product first. Keep v4 interfaces and states in the design,
but do not enable incomplete paths.

Default policy: 1B tokens, 18 decimals, minted once; no creator allocation,
transfer tax, blacklist or subsequent minting. Fixed 1% v3 pool fee.
Collected founding-LP fees split 40% creator / 50% community / 10% protocol,
separately per asset. Token fees are not spendable USDC.
Launch fee 5 USDC. Pilot seed range 500–25,000 USDC, subject to validation.
No arbitrary creator-selected hooks, lottery, volume rewards or guaranteed yield.

Arc application accounting uses the USDC ERC-20 interface with 6 decimals.
Native USDC uses 18 decimals and shares the balance. Never double-count it.
Verify dependencies against official sources; missing verification is a gate.

Contracts separate launch, permanent LP custody, fee liabilities, community
budget and work escrow. Founding principal cannot be withdrawn, approved away,
upgraded away or swept. Work payments require explicit reviewer approval;
do not claim that creative quality is verified onchain.

Use the attached specification as the detailed requirements.
Develop contracts and adversarial tests before transaction UI.
Keep mocks and fixtures clearly separated from real chain data.

For every turn: report changed files, tests actually run, failures, assumptions
and unresolved gates. Do not invent deployment addresses or passing results.
Do not deploy, broadcast, spend funds, create wallets, provision credentials,
publish the app or expose secrets. Local tests and read-only inspection only.
Any later deployment requires a separate explicit instruction.
```

Use **one named session**, with each prompt saved to the indicated file. All prompts below are comfortably below the CLI’s 10,000-character limit. For manual use, attach the brief/specification once, then paste each prompt into the same Studio conversation in order.

**Turn 01 — `prompts/01-model.md`**

```text
Read product-brief.md and specification.md. Establish the requirements model
before implementing production contracts. Produce the exact v3 and v4 state
machines, authorization table, asset-flow table, immutable configuration
schema and invariant catalogue.

Identify contradictions or unsupported dependencies. Derive the illustrative
curve parameters independently and explain rounding and graduation continuity.
Specify property tests and their expected failure cases. Do not silently
change economics. Do not deploy or create wallets. Return the model and gates
for review; do not implement the application in this turn.
```

**Turn 02 — `prompts/02-token-registry.md`**

```text
Implement only the fixed-supply token factory and launch registry for the
approved model, with Foundry tests. Bind each token to one canonical launch
path and version. Mint once; prohibit owner minting, transfer taxes and
blacklists. Separate immutable economics from versioned social metadata.

Test unauthorized registration, duplicate launch identifiers, salt collisions,
supply conservation and metadata authorization. Use pinned dependencies.
Do not implement the launcher, frontend or deployment. Report actual tests.
```

**Turn 03 — `prompts/03-v3-launch-lock.md`**

```text
Implement the v3 launcher and permanent founding-liquidity locker. Launch
must atomically create the token, initialize the expected token/USDC pool,
mint full-range liquidity directly into custody, register its position and
fee policy, and return permitted USDC dust.

Use ERC-20 USDC accounting. Reject unexpected existing pool state and unintended
native value. Expose only narrowly scoped fee collection; prohibit position
transfers, approvals, principal decreases, upgrades and arbitrary execution.

Test token ordering, 6/18 decimal scaling, slippage, initialization griefing,
reverts at every step and all possible principal escape paths. Label local
Uniswap fixtures separately from canonical Arc integration tests. No deployment.
```

**Turn 04 — `prompts/04-fee-treasury.md`**

```text
Implement per-launch, per-asset fee accounting and the community treasury.
Apply the immutable 40/50/10 split to actual received fees. Support bounded
creator-team recipients and pull claims. Separate USDC cash, token balances,
uncollected estimates and committed budgets.

Recipient changes must preserve previously accrued entitlements. Permissionless
collection must not let callers redirect proceeds. A failing recipient must
not block other recipients. Treasury cannot access LP principal.

Test rounding, repeated collection, duplicate claims, asset isolation, launch
isolation, recipient transitions and malicious token/recipient callbacks.
Do not add token-fee conversion or general treasury execution.
```

**Turn 05 — `prompts/05-work-escrow.md`**

```text
Implement funded work assignments and contributor claims. Use explicit funded,
assigned, submitted, accepted, claimable, paid, rejected and expired states.
Record terms/content hashes and reviewer authority. Reserve the complete USDC
budget before an assignment becomes fundable in the UI.

Prevent unilateral amount or terms changes after assignment. Accepted claims
cannot be cancelled. Unused funds return only to the community treasury.
Managers judge work; do not claim trustless quality verification.

Test authorization, deadline boundaries, cancellation, reviewer changes,
reentrancy, double payment and blocked payout recipients. No UI or deployment.
```

**Turn 06 — `prompts/06-contract-adversarial.md`**

```text
Adversarially review the implemented v3 contract system. Attempt to violate
supply, principal custody, fee conservation, treasury solvency and work-payment
invariants using multi-user fuzz sequences and malicious callbacks.

Include wrong-network configuration, manipulated pool initialization,
unexpected transfers, dust accumulation and Arc native/ERC-20 balance aliasing.
Mocks do not establish Arc compatibility: mark missing real-fork tests as gates.

Produce reproducible findings with severity and failing tests. Fix findings
within the approved design and rerun relevant tests. Do not describe automated
review as an independent security audit. No deployment.
```

**Turn 07 — `prompts/07-app.md`**

```text
Build the v3 application screens against generated typed ABIs and explicit
data interfaces: discovery, launch wizard, token/trade page, creator dashboard,
community budget/workspace, contributor workspace and portfolio.

Use user-facing launch language. Show the v4 path as unavailable, not functional.
Implement wallet/network states, approval explanations, slippage controls,
transaction progress, retries and clear liquidity-lock disclosures.

Separate fixtures from real data. Never show invented TVL, trades, claims or
successful transactions. Make available USDC visibly different from estimated
or token-denominated fees. Do not deploy or publish.
```

**Turn 08 — `prompts/08-indexer.md`**

```text
Implement the indexer and read API required by the app. Index registered
launches, canonical pools, swaps, fee collection, credits, claims, treasury
commitments and work events. Use transaction hash/log index identity,
checkpointing, replay and rollback handling.

Provide paginated tokens, trades, candles, holders, fee ledger, treasury, work
and health endpoints. Include source block and staleness information. Store
public content separately from chain accounting.

Test duplicate delivery, restarts, missing blocks and complete reconstruction.
No private keys in the indexer. Do not provision hosted services or credentials.
```

**Turn 09 — `prompts/09-integration.md`**

```text
Integrate the v3 UI, indexer and contracts. Implement fresh onchain quote and
simulation checks before signatures; indexer prices are display-only.
Exercise launch, buy, sell, collect, fund work, submit, approve and claim using
local fixtures or an available read-only mainnet fork.

Test wallet rejection, wrong chain, insufficient gas, expired quotes, RPC
failure, stale indexer and page reload during a pending transaction. Confirm
every displayed financial state can be traced to contract state or receipts.
Do not send public-network transactions. Report untested integration gates.
```

**Turn 10 — `prompts/10-release-review.md`**

```text
Prepare the v3 project for export and independent review. Run the relevant
contract, integration, frontend and indexer tests. Produce an artifact manifest,
dependency versions/licenses, ABI hashes, compiler settings, configuration
schema, threat model and unresolved findings.

Prepare unsigned deployment and verification instructions for use outside
Studio, but do not execute them. Check that exported files contain no secrets
and that a clean environment can rebuild the project. Distinguish passing
tests from unavailable tests. Do not publish, deploy or claim production safety.
```

The next four turns are **later expansion work**, after the v3 release gate:

**Turn 11 — `prompts/11-curve.md`**

```text
Implement only the approved USDC curve and internal curve balances, with a
separate reference model. Derive pricing, backing reserve and graduation
parameters together. Separate trading fees from backing. Support buy/sell
slippage, exact target partial fills, expiry and pro-rata refund snapshots.

Curve balances are not transferable ERC-20 tokens; expose that distinction.
No privileged creator buys. Test dust cycling, reserve solvency, arbitrary
buy/sell sequences, expiry boundaries and refund conservation. Keep graduation
behind an interface until its implementation is reviewed. No deployment.
```

**Turn 12 — `prompts/12-v4-graduation.md`**

```text
Implement permissionless v4 graduation and the v4 founding-position locker.
Authenticate canonical pool initialization to the registered executor.
Atomically deposit backing and reserved tokens, lock the position, finalize
graduation and enable 1:1 token claims.

Permit retries after failed graduation and the specified timeout-to-refund
path. Restrict fee collection to the exact zero-liquidity action sequence;
prohibit principal withdrawal and arbitrary PositionManager commands.

Test pool initialization attacks, both currency orders, rounding, price
continuity, incomplete settlement, repeated graduation and failed token claims.
No deployment.
```

**Turn 13 — `prompts/13-hook-presets.md`**

```text
Implement the reviewed hook registry and two fixed composite presets:
standard 1% and protected opening with at most 3% declining to 1% within
120 seconds. Existing launches cannot change preset or parameters.
No arbitrary modules, delegatecall, extra swap taxes, lottery or volume rewards.

Validate hook address permission bits, PoolManager-only callbacks, pool
registration, supported exact-input/exact-output behavior and fee bounds.
Test direct routers, malicious hook data, callback reentrancy and incompatible
configuration. Describe protection as a surcharge, not bot exclusion.
Leave more complex dynamic fees and LP incentives disabled.
```

**Turn 14 — `prompts/14-programmable-ui.md`**

```text
Extend the existing app and indexer for curve trading, target progress,
immutable rule summaries, graduation retries, token claims and refunds.
Keep curve balances visually distinct from transferable tokens.

Show price impact, fee treatment, target partial fills, expiry and the exact
meaning of pro-rata refunds before users sign. Display which rules apply
only to the canonical v4 pool. Add end-to-end tests covering successful
graduation, failed graduation recovery and expired-curve redemption.
Do not enable the path in production or deploy any contracts.
```

The corresponding commands are:

```bash
arc-studio run --session arc-creator-launchpad --output json --file product-brief.md --file specification.md --prompt-file prompts/01-model.md

arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/02-token-registry.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/03-v3-launch-lock.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/04-fee-treasury.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/05-work-escrow.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/06-contract-adversarial.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/07-app.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/08-indexer.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/09-integration.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/10-release-review.md

arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/11-curve.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/12-v4-graduation.md
arc-studio run --session arc-creator-launchpad --output json --skills uniswap --prompt-file prompts/13-hook-presets.md
arc-studio run --session arc-creator-launchpad --output json --prompt-file prompts/14-programmable-ui.md
```

These are **handoff commands, not commands executed during this research**. Inspect each JSON result before continuing. `needs_input`, `error` or `budget_exceeded` is not successful completion.

For manual execution, each numbered prompt is its own copy/paste turn; retain the same attached brief and specification. If authentication remains unavailable, that manual route avoids depending on the CLI.

For export, first inspect files:

```bash
arc-studio ls --session arc-creator-launchpad
arc-studio pull --session arc-creator-launchpad --out ./studio-export --dry-run
```

Then export reviewed source paths explicitly. For example:

```bash
arc-studio pull --session arc-creator-launchpad --out ./studio-export --paths "contracts/**"
```

Repeat for the actual frontend, indexer, test and configuration paths reported by `ls`. Include build manifests and lockfiles. Do not use a blanket secret-inclusive export.

---

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

**My recommendation is the v3-first creator-community launchpad, with the complete funded-work loop included in the MVP.** The strong alternative is a programmable v4 launch laboratory, but only if creator interviews reveal concrete demand for particular rules rather than enthusiasm for customization.

The evidence that would change my recommendation is straightforward: target teams do not want to seed liquidity, do not regularly commission work, or prefer an existing launcher plus a normal treasury tool. The cheapest next experiment is to walk three existing creator teams through one realistic token page containing a fee ledger, available budget and funded assignment—and ask them to bring an actual upcoming commission. That tests the product’s reason to exist before we invest in another launch mechanism.
