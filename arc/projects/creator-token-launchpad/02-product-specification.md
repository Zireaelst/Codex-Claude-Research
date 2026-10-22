# Product journeys, launch choices and features

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

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
