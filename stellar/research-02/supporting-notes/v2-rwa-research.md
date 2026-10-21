# V2 RWA and RWA/DeFi investigation — checked 20 October 2026

Research only: public documentation, repositories, ledger reads, venue APIs and unsigned quote requests. No wallet access, signing, transactions, outreach, deployments or grant research. Reopened the prior conclusion rather than treating the earlier operations candidate as the winner.

**New conclusion:** Stellar has real tradeable RWA inventory and some configured collateral markets, but much less observed secondary activity than tokenized value suggests. Current evidence favors testing a **professional RWA execution and cash-readiness product** over a new issuance platform, passive market-making pool or generic leveraged-yield app. It does not yet justify building that company: no independent buyer or repeat execution volume has been verified. A registered product, price feed, lending configuration, AMM TVL and eligible investor are five separate things.

Labels: **F** directly observed ledger/API/document/repository fact; **V** provider assertion or selected customer case; **I** inference; **H** unvalidated company, price or commercial proposition. A fact that a provider publishes a value is not independent verification that the value is complete or economically meaningful.

## 1. What was measured, and what was not

Public network reads were made with `curl` through sandbox escalation for read-only research. Plain sandbox networking failed. The first Python urllib attempt was rejected by the remote endpoint with HTTP403; the same public APIs worked through curl. All observations below are **single snapshots** around 19:28–19:33 UTC, 20 October 2026; they are not an organic-volume study or guarantees of future execution.

Saved raw evidence:

- `work/v2-usdy-asset.json`, `work/v2-benji-asset.json`: Horizon asset summaries.
- `work/v2-usdy-book.json`, `work/v2-benji-book.json`, `work/v2-usdy-trades.json`: Classic orderbook/trade data.
- `work/v2-ondo-stellar.toml`: identity from issuer's own domain.
- `work/v2-aqua-all.json`: all 37 pages, 366 operational-pool records, retrieval timestamp `2026-10-20T19:30:57Z`.
- `work/v2-aqua-tickers.json`: 369 public ticker rows, approximately 19:32 UTC.
- `work/v2-aqua-openapi.json`: venue's schema defining price/volume/TVL units and quote semantics.
- `work/v2-aqua-quotes.json`: six unsigned strict-send path estimates, 19:33:15–16 UTC, plus local request inputs.
- `work/v2-xoxno-{markets,spokes,oracle_feeds,hubs}.json`, `work/v2-xoxno-tree.json`: public repository mainnet configurations. Repository tree SHA `63de8f1d85eee7833919502158ef3dfdd9a5dc6e` observed. Raw files were fetched from main sequentially, so do not claim every downloaded blob was cryptographically pinned to that tree without comparing blobs.

Primary endpoints: [Horizon genuine USDY](https://horizon.stellar.org/assets?asset_code=USDY&asset_issuer=GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6), [Horizon BENJI](https://horizon.stellar.org/assets?asset_code=BENJI&asset_issuer=GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5), [Ondo TOML](https://ondo.finance/.well-known/stellar.toml), [Aquarius pool API](https://amm-api.aqua.network/api/external/v1/pools/), [tickers](https://amm-api.aqua.network/api/tickers/), [API schema](https://amm-api.aqua.network/api/schema/), [official API guide](https://docs.aqua.network/developers/code-examples/get-pools-info).

**What these reads cannot establish:** ultimate beneficial owners, verified legal eligibility, paid external customers, whether liquidity providers are issuer-supported, wash/self trading, actual obtainable redemption capacity, contract runtime parameters or reliable stress exits. Horizon Classic trades do not include all Soroban swaps. Aquarius statistics are its indexer's reports, not independently replayed swaps. No private OTC/dealer inventory or issuer redemption book was accessed.

## 2. Actual inventory, holders and access

| Asset | Direct observation F | Commercial interpretation I / missing evidence |
|---|---|---|
| Genuine USDY | Issuer `GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6`, confirmed by Ondo domain TOML. Horizon reports 3,203 authorized trustlines, 54 contract balances, 46 Classic liquidity-pool entries; `auth_required:false`, revocation/clawback enabled. | Trustline count includes zero balances and is not investor count or legal approval. Multiple entities can own multiple addresses; omnibus balances hide many holders. The ticker is not identity: other USDY issuers with imitative domains appeared in the public query. |
| BENJI | Genuine issuer summary: 1,382 authorized and 1,059 unauthorized trustlines, zero contract balances and zero Classic liquidity-pool balances. BENJI/USDC Classic orderbook empty at observation. | Strong direct evidence that large issuance is not open DeFi float. Does not exclude transfer-agent P2P or dealer/bank facilities outside this book. Unauthorized trustlines are not eligible investors awaiting a trade. |
| Etherfuse CETES/USTRY/TESOURO | Operational Aquarius pools found with issuer `GCRYUGD5NVARGXT56XEZI5CIFCQETYHAPQQTHO2O3IQZTHDH4LATMYWC`; published Etherfuse/Blend config has matching SAC contract addresses. Current redemption acceptance for that exact issuer was not exercised. | Mainnet pools exist, but availability of an asset does not authorize a new distributor, an investor or a liquidator to redeem it. Current ramp APIs instruct asset discovery because issuers can differ across environments/change. |
| Spiko fund tokens | Issuer publishes Soroban contracts, Permission Manager, Redemption Manager, source and a September 2025 Stellar audit. | Permissioned inventory; not automatically Classic DEX float. Current XOXNO configuration explicitly disables its Spiko spoke and assets. Neither issuer NAV nor a proposed listing establishes usable collateral. |

Access terms remain important after a token reaches mainnet:

- **BENJI F:** August 2026 SEC prospectus requires transfer-agent-permissioned wallets; P2P is not a public trading market and the fund does not find counterparties. Normal cash-redemption processing is business-day based, with potential delays up to seven days. [Prospectus](https://www.sec.gov/Archives/edgar/data/1786958/000165558926000970/c485bpos.htm).
- **USDY F:** current docs say qualifying non-US investors; Stellar mint/redemption requires support contact and a $5,000 minimum. Legal/backing details depend on issuance vintage. The issuer publishes no guaranteed Stellar per-day redemption capacity in the page reviewed. This is **not evidence capacity is zero**; it is unknown without terms/quotes. [Current basics](https://docs.ondo.finance/general-access-products/usdy/basics).
- **Spiko F:** shares held/transferred only among approved addresses. [Transfers](https://docs.spiko.io/documentation/tokenization/transfers/). [Contract/audit register](https://docs.spiko.io/documentation/tokenization/addresses/).
- **Spiko F:** explicit dealing cutoffs differ by fund; an order cannot be canceled after cutoff. T-Bills cutoff11:30Paris; SmartCash15:00; Cash&Carry11:00 one business day before execution. Unknown-versus-known NAV matters. [Orders lifecycle](https://docs.spiko.io/embedded/distributor_api_recipes/order_lifecycle/).
- **Etherfuse V/F:** product advertises NAV redemption any business day; API fee page identifies MXN as live and BRL/KRW/ARS as upcoming. A documented right/flow is not a committed firm-size redemption quote. [Product](https://etherfuse.com/products/stablebonds), [fees](https://docs.etherfuse.com/fees).
- **WisdomTree F/V:** 24/7 WTGXX access includes broker principal inventory, distinct from fund redemption and subject to pricing, inventory and possible pauses. [Issuer explanation and disclosures](https://www.wisdomtree.com/onchain/insights/blog/making-real-world-assets-move-like-crypto).

## 3. Secondary markets: depth and activity, not AUM

### Aquarius snapshot

The ticker schema defines `liquidity_in_usd` as pool TVL and `base_volume`/`target_volume` as 24-hour volume in token units. The following uses the USDC side of USDC pairs rather than assuming all tokens equal $1. TVL is **both sides**, not immediately sellable USDC. No LP concentration/incentive ownership analysis was performed. Etherfuse asset identifiers match published integration configurations; current primary redemption acceptance of that precise issuer was not independently exercised, so do not silently treat legacy and newly issued tokens as interchangeable.

| Observed RWA pair / pool | Reported TVL | 24-hour USDC-side volume | Implication |
|---|---:|---:|---|
| USDY/USDC CP `CAFHLH…ZHUSM` | $2,020,167.54 | 91.4301 USDC | Pool exists with material inventory, very little activity in this window. |
| USDY/USDC concentrated `CCV2X5…Y2OX6` | $13,970.39 | 91.2090 USDC | Additional venue; concentrated TVL is not uniformly available at all prices. |
| USTRY/USDC CP `CCX2TY…32MIA` | $2,200,737.65 | 0.7739 USDC | Capital sitting in a pool is not a market-making revenue opportunity by itself. |
| CETES/USDC main CP `CCKGQS…YL2AD` | $2,295,678.14 | 5,056.0529 USDC | More activity than other measured pairs; still needs longer-window and counterparty analysis. |
| CETES/USDC tiny CP `CBLPZU…AFTI5` | $21.55 | 0 | Counting pools inflates apparent venue choice. |
| TESOURO/USDC CP `CDPF7G…JOTD7` | $117,742.74 | 193.6858 USDC | Smaller depth; obligations in another currency add FX risk. |

Direct pool example: [USDY CP](https://aqua.network/pools/CAFHLHGZXOVNCGFJ7DOXL7JDNMBCEZKDI3LS5NRQH3GXC7CSIMQZHUSM/). Full identifiers and rows are preserved in raw snapshots.

Additional sUSD pools exist for USDY/CETES/USTRY/TESOURO. They introduce another issuer/peg/exit dependency; their token volume should not be naively added as dollars or assumed to provide an equivalent USDC exit. The total ticker TVL sums to $56,181,999.19 across369 ticker rows, consistent with root's roughly$56.2m UI observation. The operational registry returned366 rows. These are different API datasets, not proof of369 independent active markets. Root's DefiLlama total differs; not reconciled here.

**I:** Creating another passive AMM funded with millions to earn fees from this snapshot's very small flow is not an attractive default company. Low velocity can be normal for a cash-holding asset; it does not prove investors are dissatisfied. Demand for size may be episodic, but must be observed rather than inferred from AUM.

### Classic USDY/USDC book and recent trades

Horizon book at observation: best bid1.1326549 USDC/USDY; best ask1.1452698; approximately1.1076% spread relative to midpoint. Bid-side USDC within10bps of best bid:$1,593.07;50bps:$2,536.57;100bps:$3,292.38. These bands are from **best bid**, not NAV. Ask depth within100bps of best ask was942.01USDY. Quote-side amounts and asset orientation were retained in raw JSON.

The newest200 Classic trades span `2026-10-19T14:48:28Z` through `2026-10-20T19:26:58Z`, totaling224.5136505 USDC counter-amount, with34 distinct participating address strings. This is a page-bounded ~29hour sample, **not** an exact24hour total, all venues, independent humans or organic demand. It demonstrates real trades while revealing how misleading “trading supported” can be as a proxy for depth.

[Horizon orderbook](https://horizon.stellar.org/order_book?selling_asset_type=credit_alphanum4&selling_asset_code=USDY&selling_asset_issuer=GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6&buying_asset_type=credit_alphanum4&buying_asset_code=USDC&buying_asset_issuer=GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN&limit=200), [recent Classic trades](https://horizon.stellar.org/trades?base_asset_type=credit_alphanum4&base_asset_code=USDY&base_asset_issuer=GAJMPX5NBOG6TQFPQGRABJEEB2YE7RFRLUKJDZAZGAD5GFX4J7TADAZ6&counter_asset_type=credit_alphanum4&counter_asset_code=USDC&counter_asset_issuer=GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN&order=desc&limit=200).

### Unsigned Aquarius path estimates at different sizes

Read-only POST to `/api/external/v1/find-path/`, seven-decimal input units, max depth 4, slippage 0, provider fee 0. No transaction was submitted. API route estimates are not firm executable RFQs or simulation against a particular investor's permissions/balance. V1 searches a path; it does not establish globally optimal split execution across Classic+all Soroban venues.

| Sell USDY | Estimated USDC out | Shortfall versus1.13348723 marginal pool spot, including fee/impact | Returned path |
|---:|---:|---:|---|
| 1,000 | 1,132.1545 | 0.1176% | Concentrated pool |
| 10,000 | 11,198.3965 | 1.2040% | CP pool |
| 100,000 | 101,853.3670 | 10.1416% | CP pool |

Reverse:1,000USDC→881.2010USDY;10,000→8,727.4662;100,000→80,225.7440. All six returned success. Comparisons use pool spot, **not official issuer NAV**; the two may diverge. Quotes can change immediately, exclude gas/legal/bank costs, and do not establish maximum exit depth. This is the central finding: roughly$2m pool TVL did not yield a near-NAV$100k exit.

## 4. Oracles, permissioned collateral and production maturity

**F: usable interfaces exist.** SAC connects Classic assets to Soroban without issuing a bridge token; AUTH_REQUIRED assets require issuer approval of contract recipients. [SAC](https://developers.stellar.org/docs/tokens/stellar-asset-contract). OpenZeppelin has a modular Stellar RWA/identity/transfer-compliance framework. [OZ](https://docs.openzeppelin.com/stellar-contracts/tokens/rwa/rwa). These do not supply legal authority, investor approval, funding or liquidation bids.

**V/F: price-feed announcement.** RedStone's August 5, 2026 primary announcement provides USDY/USD and SEP-40 support. It says feed support makes listing possible; this is not proof Blend/Templar listed the asset or that a lender has cash. Pricing NAV is different from estimating immediately realizable sale proceeds. [RedStone USDY](https://www.redstone.finance/blog/redstone-brings-ondos-usdy-to-stellar-defi-with-sep-40-integration).

**F: XOXNO current repository configuration, not runtime read:**

| Inventory | Configured role/parameters | Oracle configuration | Maturity limit |
|---|---|---|---|
| USDY | Ondo spoke 7: collateral-only,80%LTV,85%liquidation threshold; its USDY/USDC LP at50%/60% | RedStone `USDY_FUNDAMENTAL/USD`; bounds$1.08–$1.32; max stale57,600 seconds | Config is not current cash, remaining caps, legal liquidator access or realized liquidation evidence. |
| CETES/USTRY | Etherfuse spoke 2: collateral-only60%LTV/70%threshold; USDC/EURC/XLM/PYUSD borrowing configurations | Reflector three-sample TWAP scaled by USDC plus RedStone fundamental feed; tolerance/sanity bounds | Local-currency FX and underlying redemption differences remain. |
| Spiko | Spoke 3 explicitly `enabled:false`; each listed fund also disabled | Custom XOXNO fundamental feed entries present, `oracle_feeds.json` marks Spiko feeds disabled | Do **not** describe Spiko as presently usable XOXNO collateral on the basis of its name/parameters. |
| Centrifuge wrappers | deJTRSY/deJAAA configurations in RWA spoke4 | RedStone fundamental feeds | Not independently verified enabled runtime holdings/borrows or end-user permissions here. |

Sources: [spokes](https://github.com/XOXNO/rs-lending-xlm/blob/main/configs/mainnet/spokes.json), [markets/oracles](https://github.com/XOXNO/rs-lending-xlm/blob/main/configs/mainnet/markets.json), [feed configuration](https://github.com/XOXNO/rs-lending-xlm/blob/main/configs/mainnet/oracle_feeds.json). Public [XOXNO SDK mainnet constants](https://docs.rs/xoxno-contract-sdk/latest/xoxno_contract_sdk/networks/mainnet/index.html) and provider's mainnet-beta announcement support production-deployment claims. This pass did not simulate borrowing or read every deployed parameter.

**F:** issuer's Etherfuse/Blend repository publishes mainnet Etherfuse pool `CDMAVJPFXPADND3YRL4BSM3AKZWCTFMX27GLLXCML3PD62HEQS5FPVAI`, oracle and SAC addresses. [Configuration](https://github.com/etherfuse/etherfuse-blend-pool-utils/blob/main/mainnet.contracts.json). This demonstrates integration artifacts, not current reserve liquidity/utilization. Root is separately investigating DeFi runtime/risk details.

**F/V:** Spiko NAV page publishes fund administrator NAV and EVM oracle links, but no Stellar oracle row on the retrieved table. Absence from that table is not proof no Stellar feed exists. [NAV sources](https://docs.spiko.io/documentation/tokenization/nav/).

**Competition / current-versus-future:**

- **RedStone Settle V:** April 28, 2026 launch describes auction-based distressed RWA exits through specialized KYC solvers, taking the underlying while repaying onchain. No independently verified Stellar deployment/filled bids were collected. It directly competes with a new “RWA liquidation network.” [Primary launch](https://www.redstone.finance/blog/redstone-settle-bringing-instant-settlement-to-real-world-assets-liquidations/).
- **Ascend V/F:** SDF$1m strategic investment and permissioned vault/distressed-disposal architecture; no live Stellar volumes independently established. [SDF](https://stellar.org/press/stellar-development-foundation-makes-strategic-investment-in-ascend-to-accelerate-compliant-rwa-infrastructure-development).
- **STBL F/V:** current [Stellar app](https://stellar.stbl.com/) labels mainnet and approved USDY collateral minting ofUSST; public extraction did not expose populated supply/collateral figures. A mainnet label is not validated borrowing demand or exit capacity.
- **Aave Horizon F:** issuer whitelist and eligible liquidation recipients are explicit in current [mWIN onboarding proposal](https://governance.aave.com/t/arfc-onboard-mwin-midas-wellington-management-to-aave-horizon/25536). Proposal status must not become “live listing.”

## 5. ETHGlobal prior art: awards versus actual company evidence

Award facts below are from showcase award sections; source links were inspected where specified. “No paid-user evidence found” means in the examined primary pages/repo, not proof that the team has no users anywhere. Finalist status is not inferred from a sponsor prize.

| Project | Verified award / network | What is actually evidenced | What it does not solve |
|---|---|---|---|
| [Bailiff](https://ethglobal.com/showcase/bailiff-368x0) | Tokyo2026, Uniswap Best Stack Contribution2nd | [Repo](https://github.com/eugenioclrc/bailiff) opened; Anvil/Sepolia fork, mock ERC3643-style asset. Keeper can trigger without holding RWA; preapproved LP supplies USDC. Known missing NAV floor and borrower-receipt blockage. | Expands trigger set, not eligible balance sheets. No mainnet issuer mandate, independent liquidity or paid users verified. |
| [Wafer](https://ethglobal.com/showcase/wafer-r4uab) | NY2026, Hedera Tokenization winner | [Repo](https://github.com/aiden-fianso/Wafer) explicitly Hedera testnet296; KYC-gated fund shares, claim NFTs, SaucerSwap market; reward stream simulated. Repo discloses local tests mirror arithmetic rather than deployed bytecode. | Does not prove controllable commercial DePIN cashflow, enforceable receivable or default recovery. No paid borrowers verified. |
| [DayTrader](https://ethglobal.com/showcase/daytrader-2mkp6) | Tokyo2026, Curvegrid Best RWA Tokenization | [Repo](https://github.com/ETHTokyo2026-MODY/project-tokyo) opened; rental-day tokens, bundles and atomic 1inchAqua settlement. Source/app demonstrates marketplace design. | No verified contracted hosts, booking-system integration, fulfilled stays/cars or paying traders. No production claim made here. |
| [Mand(ate)](https://ethglobal.com/showcase/mand-ate-3npu6) | HackMoney2026 ENS IntegrateENS **pool prize**; Arc settlement | [Repo](https://github.com/codebird-n4vnt/mandate) opened; borrower/lender intent discovery and99/1USDC settlement; compliance/underwriting explicitly offchain. “Live demo” links to Canva. | No bank distribution, licensed origination, funded legal loans or paid buyers verified. Source's3-of10lost-deal claim is founder anecdote. |
| [AssetSphere](https://ethglobal.com/showcase/assetsphere-0xcfo) | Cannes, ASI Innovator'sEdge1st | Showcase explicitly syncs appraisals across BaseSepolia/EthereumSepolia/PolygonAmoy testnets. | An AI score plus price API is not realizable collateral value, appraisal authority or lender acceptance. No paid underwriting verified. |
| [RWA Outlet](https://ethglobal.com/showcase/rwa-outlet-oq1j5) | ETHOnline2026; **no award shown** on examined page | [Repo](https://github.com/rwa-outlets/rwa-outlet-contracts-core) opened; Sepolia mocked assets/KYC faucet, NAV-spread/Dutch/AMM routes and async redemption queues. | Strong technical prior art. Fixed “instant-versus-patient” spread is not a verified real arbitrage; legal redemption rights and funded makers remain missing. USDe labeled as a credit twin is not private-credit evidence. |
| [Unison](https://ethglobal.com/showcase/unison-qmt6t) | Tokyo2026; **no award shown** | UnichainSepolia and Sui testnet; wrapper-parity conversions, batch crossing and Seal/Walrus confidential send; showcase reports simulations. | A conversion between different issuer liabilities need not be legally/tax equivalent; market-maker inventory is assumed. Do not repeat “no tax event” as fact. |
| [BaseAgentX](https://ethglobal.com/showcase/baseagentx-tsn9r) | AgenticEthereum CDP AgentKit **pool prize** | Carbon-credit agent/verification/trading architecture described onBase. | Network name and award do not verify legal credits, attributable carbon retirement, valuable trading, mainnet addresses or paid users. |

Coverage caveat: a credible Solana RWA-specific ETHGlobal winner with verifiable primary award+deployment+buyer evidence was not located in this bounded pass; this is not a claim none exists. Use real Solana product competition instead: [BUIDL Solana issuer release](https://investors.securitize.io/news/news-details/2025/BlackRock-and-Securitize-Debut-New-BUIDL-Share-Class-on-Solana-Network-03-25-2025/default.aspx), and WisdomTree's documented multichain products. Do not fill a chain checklist with an invented winner.

## 6. Four distinct full-company theses, evaluated afresh

All products, prices and acquisition routes below are **H**, not customer requests. Each describes a repeated experience rather than an issuance demo.

### R1. Professional RWA execution and cash-readiness workstation — strongest to test

**Exact buyer/user:** Head of Treasury or COO at a licensed fintech, distributor or asset manager that already holds externally issued cash-fund tokens and must fund recurring USDC/fiat obligations. The treasury trader/controller is the user. Exclude passive holders with one issuer and no recurring cash decisions.

**Repeated experience and recovery:** consolidate eligible holdings and obligations; compare patient primary redemption, permitted dealer/RFQ, Classic/AMM exit and an approved credit bridge. Show net cash, date, price impact, permission, inventory and counterparty risk. Propose a schedule, obtain custody/human approval, execute through existing licensed providers, reconcile actual cash. When a quote expires, a redemption misses cutoff or a transfer is paused, preserve pending status and recompute the gap. Never double-sell or automatically borrow to conceal a missed obligation.

**Why standalone:** could own daily cash planning, policy, approvals, execution evidence and counterparties across issuers/chains. A quote comparison page or redemption-ticket screen is a feature. Recurring planning plus reusable integrations must justify purchase.

**Stellar advantage/multichain:** measured differences between same-rail USDC/RWA holdings and exits make Stellar useful first inventory. Real customers must already use it. Expand Base/Ethereum/Solana and banks because issuer/product access dominates chain loyalty. No new token is needed.

**Competition/unmet need:** Spiko Direct, WisdomTree Connect/Stable Sea, Securitize, TMSs, OTC desks and existing swap routers already supply parts. The proposed gap is independent cash-outcome planning across providers with a demonstrably better net result. Evidence proves differing terms/depth; it does not prove buyers need aggregation.

**Pricing/distribution:** test $12k–$36k/year plus implementation with the treasury budget owner. Any execution fees require an appropriate licensed arrangement and disclosure. Small trade volume cannot support take-rate-only revenue. Recruit through public product customers and treasury accountants; no founder channel is secured.

**Dependencies/legal:** issuer accounts and eligibility, custody/provider APIs, dealer permission, authoritative NAV/terms, current market quotes and liquidity. Start read-only. Recommendations, order transmission, routing, execution and credit facilitation require exact jurisdiction/legal analysis. Using USDC does not make the startup a broker.

**Evidence/confidence:** medium problem evidence from primary terms and direct depth; low independent demand. A historical replay is feasible without capital risk. Preferred for discovery, not a broad build commitment.

### R2. Permissioned RWA dealer and redemption-liquidity network

**Buyer/user:** issuer Head of Capital Markets or distributor treasurer requiring executable exits outside ordinary dealing windows. Eligible institutions supply funded market-making capacity.

**Repeated experience and recovery:** onboard seller and maker eligibility; solicit size/time-specific firm bids; compare discount with expected redemption cost; settle through controlled custody; redeem inventory and recycle cash. On pause/default or failed redemption, the funded maker bears genuine liquidity/asset risk and follows legal recovery procedures. The product includes RFQ, inventory limits, funding, settlement and customer reports, not merely a smart contract auction.

**Why standalone:** a recurring liquidity service can be a company when issuer retainers and genuine flow fund capital costs. Another emissions-funded pool without flow cannot. Funded competing quotes discover a clearing price; NAV is only an input.

**Stellar/multichain:** fast controlled transfers and atomic asset/USDC settlement help. The eligible dealer network must serve multiple chains. Same-fund deployments do not confer portable balances or legal eligibility.

**Competition:** established OTC/dealer desks, issuer inventory programs, RedStone Settle, Ascend and existing exchange makers. Measured low activity challenges passive LP economics. Need actual service contracts and redemption terms before raising LP capital.

**Pricing/distribution/legal:** hypothetical issuer retainer $3k–$10k/month plus permissible spread, backed by committed independent capital. Need relevant broker/dealer/venue structure, custody, issuer allowlists and enforceable redemption rights. Investor solicitation and pooled capital create additional obligations. A founder with only possible DevRel introductions lacks this commercial network today.

**Evidence:** structural size/stress constraint is clear; observed customer willingness to pay and committed capital are not. Regulated-partner-led or future candidate.

### R3. RWA-backed working-capital brokerage for fintech treasuries

**Buyer/user:** CFO of a fintech/asset manager holding eligible yield assets but needing short-duration stablecoin liquidity. Product combines borrower onboarding, collateral permission/custody, term comparison, credit agreement, drawdown, monitoring, margin notices, repayment and release.

**Repeated experience and recovery:** the borrower compares an outright sale with retaining the asset and paying interest. If an oracle becomes stale, pool cash disappears, collateral is frozen or a margin call is unanswered, stop new draws and invoke agreed collateral/repayment procedures. Liquidation must route to an eligible holder with a real exit. A contract cannot manufacture cash or override an issuer.

**Why standalone:** commercial credit distribution/servicing with underwriting and lender relationships could be a company. A collateral adapter is a feature. Revenue comes from lawful origination/servicing, not token emissions. An illustrative 10–30bps facility fee must cover underwriting and support; small/short facilities may not.

**Stellar/multichain:** XOXNO configurations and Etherfuse/Blend artifacts support same-rail lending feasibility. Runtime cash/caps, customer permission and viable rates remain unverified. Expand by lender/asset relationship across chains.

**Competition/dependencies:** XOXNO/Blend, Aave Horizon, Morpho, Ascend, STBL and traditional securities-backed lending. Need an eligible lender, borrower, custodian, legally enforceable collateral, funded liquidators and robust oracles. Configured LTV is not commercial credit approval. No lender, capital or underwriting partner is secured for this founder.

**Evidence:** infrastructure feasibility is substantially stronger than a tokenization demo; unmet borrower need and net economic benefit remain unproven. Borrowing at or above fund yield can be useful liquidity insurance but is not free carry. Partner-led future candidate, not an immediate leveraged-yield app.

### R4. Embedded local-currency yield account inside a payroll/vertical platform

**Buyer/user:** payroll or vertical-software operator serving Mexican SMEs/workers with recurring MXN earnings and obligations. Users want temporary yield and predictable bill cash. The complete product includes eligibility, consent, holding/tax records, education, bill calendar, primary/secondary exit, cash-out and support.

**Repeated experience and recovery:** salary arrives, a user elects an allocation, sees NAV/risk and schedules a bill redemption. If a market exit is discounted or a cutoff missed, present approved alternatives and their costs. Resolve order, claimable-balance and provider failures through verified workflows. Never substitute leveraged DeFi while describing it as safe cash.

**Why standalone:** only credible if it owns a distribution channel and repeated user relationship. A generic wallet frontend over Etherfuse does not. A $500 average balance at a hypothetical 30bps/year produces $1.50 gross before support, acquisition and compliance.

**Stellar/multichain:** local ramp inventory and small transfers support one geography, but Etherfuse also operates on other chains. OpenTrade/Littio on Avalanche, Spiko Embedded and ordinary savings products are alternatives. An upcoming BRL rail cannot be sold as current banking access.

**Pricing/distribution/legal:** hypothetical B2B $500–$2k/month or a contracted revenue share, conditional on workflow value beyond balances. Requires securities/product-distribution agreement, local eligibility/KYC, payment/custody/tax partners and any promised liquidity commitment. No committed platform channel is secured. DevRel can introduce builders; that does not establish employer compliance/budget approval.

**Evidence:** existing product category and asset supply are real; entrant advantage is low. Eliminate now without a committed channel and eligible user cohort.

## 7. R1 finalist: one weekly journey and architecture

**H journey:** a treasurer holds externally issued cash-yield assets and has Friday USDC/fiat obligations. Monday she imports liabilities and reviews holdings, legal permissions and cash floors by entity. Tuesday she compares primary redemption timing with size-sensitive market quotes and any approved facility; she schedules patient redemption and retains an explicit cash buffer. Wednesday's order misses cutoff or its NAV arrives late. Expected cash becomes uncertain, is not counted twice, and triggers a confirmation request. Thursday she obtains a current firm quote from an authorized dealer or another approved alternative. Custody signs with size/price/time bounds. Friday actual cash and obligation funding reconcile. The weekly report measures realized price and cash date against the proposal. No step automatically adds leverage to hide a cash shortfall.

**Architecture and responsibility:**

1. Encrypted offchain tenant records contain legal investor/entity mappings, obligations, mandates, eligible products, term versions, cutoff calendars and accounting/bank/custody events. Issuer/TA registers remain authoritative; imports preserve source provenance.
2. Read-only Horizon/RPC/indexer connectors identify issuer plus code, SAC/contract IDs, trustline/authorization state, trades and contract events. Classic and Soroban data remain distinguishable. Decimals and asset identity must be explicit.
3. Separate official NAV and timestamp from secondary spot/TWAP and actual size quotes. Stale, disabled or missing input means unknown. A configured feed is not a read of its live value. Risk value should reflect conservative recoverable cash, not raw NAV when depth or permission fails.
4. The decision engine compares patient redemption, market exit and approved credit under customer policy. It distinguishes indicative quotes from firm commitments and expected proceeds from available cash. Deterministic eligibility, size and time constraints gate any agent-generated proposal.
5. Existing custody/licensed providers execute with human approval. A later approved Soroban atomic exchange could settle eligible asset/USDC with minimum output and expiry. It cannot atomically guarantee an external bank payment or override issuer dealing rules.
6. Failed/partial/pending orders retain explicit status. Check chain and provider records before resubmitting. Customer owns investment/liquidity decisions; issuer owns redemption/register permission; lender owns credit; custodian safeguards assets; startup owns contracted software and data-quality duties.

**Now:** retrospective cash-readiness audit, provider terms, permission checks, recurring indicative quotes, planning and post-trade evidence. **Requires commercial partners/future work:** firm dealer inventory, funded credit, regulated routing, discretionary execution or custody. **Not usable assumptions:** announced DTCC 1H2027 Stellar assets, disabled Spiko collateral, unaudited privacy wrappers or promised future third-party liquidity.

## 8. Recruiting 5–10 interviews without assuming access

No outreach sent. The following are targets, not verified multi-issuer buyers or available partners. Build 30 tailored contacts across about 20 organizations; pursue one thesis rather than all four simultaneously. DevRel/Ambassador introductions may accelerate access; direct professional outreach and public customer references are the fallback. No conversion rate is guaranteed.

| Target | Role and purpose | Route and qualification |
|---|---|---|
| Meru / Decaf | Treasury/operations lead; possible R1 buyer | Named in Ondo's Stellar launch integrations. Verify current multiple-issuer holdings and cash deadlines; otherwise classify as expert only. |
| LOBSTR | Product/operations lead; secondary-access expert | Issuer-listed integration and professional company contact. Integration does not establish customer-asset custody or treasury purchase intent. |
| Stable Sea | Treasury-product/operations lead; competitor/expert or possible channel | Public WisdomTree collaboration. Ask which cross-issuer decision remains outside existing product, including a satisfied incumbent baseline. |
| Conquest | Treasury/controller; customer reference | Spiko case identifies multi-entity cash placement. Contact through current professional management roles; already served, not an available pilot. Ask about residual provider fragmentation. |
| Ramify / Bitstack | Treasury/product operations; distribution experts | Public Spiko embedded-product cases. Verify current account, custody and provider model before calling them buyers. |
| Etherfuse | Institutional/integration operations expert | Official product/developer contact. Obtain precise size/redemption/SLA facts; support knowledge is not buyer willingness to pay. |
| Ondo / WisdomTree | Institutional servicing/capital-markets expert | Published product contacts; precise chain, product and country terms. No assumed partner permission. |
| XOXNO / Blend pool operator | Market/risk/treasury expert | Public protocol community to request the actual operating role. Validate runtime assets, cash, current borrowers and liquidators. |
| Fund administrator / digital-asset accountant | Controller/TA operator; expert or buyer | Relevant professional practice and firm contact. Identify authoritative ownership/cash records and residual work customers pay for. |

Target four current holder/distributor operators, two treasurers/controllers, two issuer operators and one market maker/lender. At least three should be actual independent budget roles. Request redacted last-month holdings, their last three consequential cash decisions, order/quote/receipt times, size, eligible issuer accounts, realized cash dates and existing tool costs. Include two satisfied incumbent users. A developer conversation or hypothetical willingness-to-pay answer cannot replace this evidence.

## 9. Three kill observations for R1

1. **No repeated material job:** after 5–10 qualified interviews, nobody can show at least three recent cross-provider cash/liquidity decisions, or holdings simply sit until issuer redemption. Large AUM and low turnover cannot rescue the business.
2. **No independent paid outcome:** issuer/TMS/dealer already provides adequate cash-date, net-price and permission handling; or buyers will not pay $1k+/month independently of product referral/yield revenue. This suggests an integration service or commodity quote API.
3. **No lawful actionable inventory:** buyers cannot transfer/redeem, cannot share authoritative data, or no funded eligible dealer/lender will commit access. A view without an approved actionable exit is not an execution company. If real buyers have no current Stellar holdings, reject the Stellar-core claim even if a general multichain version could work.

**Decision:** R1 warrants bounded discovery and replay against actual cash obligations. R2/R3 require counterparties and capital this founder does not yet have; R4 requires distribution. No RWA company presently clears an investment-ready evidence bar. This reopened evaluation follows secondary depth, activity and access rather than automatically inheriting the earlier operations winner.
