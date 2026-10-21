# RWA venture research — working evidence, 20 October 2026

Research only. No outreach, applications, transactions, wallet connections, deployments, or Instaward rules consulted. Current pages retrieved 20 October 2026. This is an opportunity screen, not a legal opinion or investment recommendation.

## Bottom-line research judgment

The strongest RWA *problem* evidence is recurring operations across fund, distributor, custody, bank, and blockchain records. It does **not** yet prove an independent software market that a new Stellar startup can win. Generic issuance, eligibility registries, RWA distribution, yield APIs, lending, and reconciliation all have relevant incumbent or funded competitors. Do not describe these as whitespace.

Conditional best company hypothesis: an operations system for **distributors already offering multiple tokenized cash products**, beginning with redemption/withdrawal exceptions and source-of-truth reconciliation. Its buyer is the distributor's Head of Operations or COO, not the asset issuer by default. Its value must be visible even when issuers already have transfer agents. The output is completed cases and trustworthy availability data across vendors, not a token minting UI. Stellar is the first supported production rail; the company's defensible asset would be cross-provider operating integrations and resolved-exception history. This is inherently a multichain business if successful. A requirement that Stellar remain the only chain would weaken the commercial case.

No concept below has verified customer willingness to pay. The recommendation is to validate this operations hypothesis, not to claim product-market fit. Buyer interviews are essential before building a company around it.

## Evidence labels

- **Verified document fact:** what an issuer's current docs, source code, filed prospectus, current job posting, or grant database actually says. Does not imply independent verification of all marketing claims in that document.
- **Vendor claim:** issuer/platform assertions about benefits, scale, adoption, safety, or service quality.
- **Attributed customer evidence:** a named customer statement published by a vendor. Stronger than a generic TAM claim, but selected testimony, not independent research.
- **Inference:** analytical implication drawn from facts.
- **Hypothesis:** proposed buyer, price, economics, workflow, or market gap not established by the evidence.
- **Unverified status:** no direct independent mainnet/RPC evidence collected in this pass. Issuer documentation may establish a credible production claim without independently proving current volume or accessibility.

## 1. Stellar RWA landscape: usable assets versus nominal issuance

| Issuer/infrastructure | Maturity classification as observed | Independent mainnet verification in this pass | Access constraint / uncertainty |
|---|---|---|---|
| Franklin / BENJI | Current registered production fund, supported by dated prospectus and five-year issuer history | Not completed | Transfer-agent permission; fund redemption clock differs from transfers |
| Spiko | Production availability documented; addresses, code and Stellar audit published | Not completed; explorer extraction failed | Allowlisted wallets; Soroban contracts |
| Ondo / USDY | Explicit Stellar live launch September 2025; current docs include Stellar | Not completed | Investor eligibility and supported redemption process |
| Etherfuse | Current production API docs expressly support Stellar operations | Not completed | Quote/discovered asset identity and customer/rail approval |
| WisdomTree | Current issuer materials list Stellar production products | Not completed | Product/channel details need resolving against stale FAQ |
| RedSwan | Issuer/ecosystem tokenization announcement | Not completed | Tokenized gross value does not establish sold shares or liquidity |
| Liqvid Stellar | Awarded deployment plan; prior Base traction claimed | Not completed | No collected proof Stellar roadmap completed |
| Ascend Stellar | Funded strategic extension/infrastructure announcement | Not completed | No collected proof live funded Stellar credit market |
| DTC/DTCC Stellar | Announced future integration, expected 1H2027 | Not applicable as live inventory | Exclude from current accessible product claims |

Sources and exact qualifications appear in issuer entries below. Production in this table describes the strength of issuer documentation, not an independently reproduced onchain census.

### BENJI / Franklin OnChain U.S. Government Money Fund

**Verified document fact:** August 1, 2026 prospectus, filed July 27, describes permissioned wallets controlled by the transfer agent. Initial minima are Stellar $20; Base/Solana/Aptos $100; Polygon/Arbitrum $1,000; Avalanche $20,000; Ethereum $5m. Transfer participants must be whitelisted. P2P transfers can occur any time, but are not a public trading market. The issuer does not connect counterparties. Redemptions typically process by the next business day, potentially up to seven days. Annual operating expense after waiver is 0.20% through July 31, 2027.

**Inference:** cheap transfers do not create a liquid redeemable cash instrument for arbitrary wallet users. A permissionless vault cannot assume BENJI eligibility. P2P token finality is distinct from bank redemption settlement.

Primary: [SEC prospectus](https://www.sec.gov/Archives/edgar/data/1786958/000165558926000970/c485bpos.htm), particularly “Use of Blockchain,” “Buying Shares,” “Selling Shares,” “Peer-to-Peer Transfer of Shares,” and “Account Policies.” Earlier issuer PDF search showed Avalanche $100k; current dated SEC filing is preferable. Do not blend the versions.

### Spiko

**Verified document facts:** issuer lists Stellar alongside Ethereum, Polygon, Arbitrum, Etherlink, Base, and Starknet; shares only held/transferred between allowlisted addresses. Documentation publishes Stellar fund, Permission Manager, and Redemption Manager contract links, source code, and a September 2025 Halborn audit. These are Soroban contract tokens; do not assume they are Stellar Classic DEX assets.

Sources: [Transfers & Redemptions](https://docs.spiko.io/documentation/tokenization/transfers/), [Addresses & Audits](https://docs.spiko.io/documentation/tokenization/addresses/), [Stellar code](https://github.com/spiko-tech/stellar-contracts), [Halborn report](https://www.halborn.com/audits/spiko/stellar-contracts-879885).

**Status:** strong issuer documentation of production availability and published deployments. The linked USTBL Stellar Expert page returned 404 through web extraction; independent RPC verification was not completed. This retrieval failure is not evidence that the contract does not exist. Shell access to Horizon failed DNS in sandbox. Do not report the contracts independently checked onchain.

### Ondo USDY

**Verified document facts:** issuer announced USDY live on Stellar September 17, 2025 and named LOBSTR, Aquarius, Meru, Soroswap, Decaf integrations. Current documentation restricts qualifying investors to non-US participants; mint/redeem on Stellar requires contacting support and a $5k minimum. Current docs also say legacy Ondo USDY LLC was folded under Ondo Stocks as of December 15, 2025; backing can depend on issuance date. An old description of a single unchanged USDY legal wrapper is unsafe.

**Inference:** a distributor needs to distinguish secondary exits, issuer redemption, and supported legal/product versions. “Permissionless” in a launch announcement should not be interpreted as unrestricted eligibility or instant bank redemption.

Sources: [Live launch](https://ondo.finance/blog/usdy-is-now-live-on-stellar), [current USDY basics](https://docs.ondo.finance/general-access-products/usdy/basics).

### Etherfuse Stablebonds

**Vendor claims:** issuer markets government-bond exposures CETES, TESOURO, EUROB, GILTS, USTRY; Stellar, Solana, Monad, Base, Polygon. Token value tracks NAV rather than a fixed unit of fiat. The product page says fiat redemption any business day. Treat “fully reserve-backed,” custody safety, and “no gates” as issuer claims until legal agreements and attestations are reviewed.

Source: [Stablebonds product](https://etherfuse.com/products/stablebonds).

**Verified technical/price facts:** official ramp documentation explicitly supports Stellar on/offramps and swaps and says use live asset discovery rather than hardcoded issuer addresses. Mexico MXN rails are live; BRL, KRW, ARS are “upcoming” in fee docs. MXN platform fees tier from 20 bps below $5m rolling volume to 5 bps above $100m. Partner fees can be added; these are not evidence partners can profitably charge the maximum permitted fee. These pages establish operational infrastructure, not legal permission for an arbitrary startup to distribute securities.

Sources: [Stellar integration](https://docs.etherfuse.com/guides/chains/stellar), [Ramp fees](https://docs.etherfuse.com/fees).

### WisdomTree

**Verified product-document facts:** Connect page offers permissioned institutional wallets, USD/USDC/PYUSD funding, API and on-receipt instructions, and advertises tokens on eight chains including Stellar. Its FAQ lower on the same page lists only five chains: this is an internal stale-content inconsistency. Confirm exact product/chain/channel availability through developer docs or the platform before promising an integration. No platform investment minimum is advertised. WTGXX primary dealing has trading-day cutoffs; separate instant liquidity uses broker-dealer inventory.

Source: [Connect product and FAQ](https://www.wisdomtreeconnect.com/).

**Vendor claims plus important qualification:** May 2026 issuer article describes 24/7 WTGXX liquidity, Stable Sea treasury distribution, full Solana expansion, and a Plume/Toku payroll **pilot**. Disclosures say bilateral principal transactions can pause, depend on inventory/pricing, carry commissions, and are not continuous fund redemption or an exchange/ATS. Thus “24/7 redemption” is a misleading simplification.

Source: [Making Real-World Assets Move Like Crypto](https://www.wisdomtree.com/onchain/insights/blog/making-real-world-assets-move-like-crypto).

### Pipeline should not be counted as live accessible inventory

- **DTCC:** May 27, 2026 primary release says DTC-tokenized assets on Stellar anticipated **first half 2027**. This is announced future integration, not live October 2026 inventory. [DTCC release](https://www.dtcc.com/press-releases/2026/tokenization-service-to-connect-with-stellar-public-blockchain-as-dtc-advances-multi-chain-strategy).
- **Ascend:** $1m SDF strategic investment, May 2026; permissioned credit vaults, identity-aware ERC-3643, oracle monitoring, Distressed Disposal Facility. Announcement language describes extending infrastructure; it does not independently establish live Stellar lending volume. [SDF primary release](https://stellar.org/press/stellar-development-foundation-makes-strategic-investment-in-ascend-to-accelerate-compliant-rwa-infrastructure-development), [Ascend dated blog](https://ascend.gl/blog/).
- **RedSwan:** public material describes $100m commercial real estate tokenization/plan; “asset value tokenized” is not sold equity, external investor deposits, liquid secondary float, or realized fundraising. No underlying current mainnet ownership/volume independently verified in this pass. [Stellar fireside summary](https://stellar.org/blog/ecosystem/tokenizing-real-estate-with-redswan).
- **Liqvid:** SCF #37 awarded $137.5k for Stellar deployment; page separates existing Base proof/claimed $12m first deal from a target Stellar $3m+ AUM and initial deal. Existing non-Stellar traction cannot establish completed Stellar deployment. [SCF submission](https://communityfund.stellar.org/submissions/rec2aZKPZ8SmvFoGS).

### What Stellar technically solves, and what it does not

**Verified technical fact:** Stellar Asset Contract allows Classic issued assets in Soroban without bridge/wrapper tokens. Account balances use trustlines; contract balances use contract storage. For AUTH_REQUIRED assets, a contract address must explicitly be issuer-authorized. SAC does not expose the Classic orderbook API. Therefore one cannot assume a generic lending pool/vault can hold every RWA or route every token through the native DEX. [SAC docs](https://developers.stellar.org/docs/tokens/stellar-asset-contract).

**Verified technical fact:** issuer flags provide required authorization, revocation/freeze, limited authorization, clawback. These are control primitives; they do not perform AML due diligence or establish beneficial ownership/legal entitlement. [Asset controls](https://developers.stellar.org/docs/tokens/control-asset-access).

**Verified technical fact:** OpenZeppelin already supplies a Stellar RWA framework modeled on ERC-3643/T-REX: modular identity verification, claim issuers, transfer compliance, freezing, recovery, forced transfer. A basic eligibility module or issuance wizard has weak technical defensibility. [OZ RWA docs](https://docs.openzeppelin.com/stellar-contracts/tokens/rwa/rwa).

**Inference:** Stellar is appealing when customers already hold native Stellar assets or need small-value distribution/settlement to Stellar wallets. It is much less decisive for software whose entire value is reading balances, scoring eligibility, or recording offchain PDFs; those can operate equally well on other chains. Asset issuer authorization, fund liquidity, banking hours, taxes, sanctions, custody arrangements, and local selling permissions remain business/legal constraints.

## 2. Concrete operational and buyer-demand evidence

### A. Paid operating labor survives inside a full-stack tokenization provider

**Verified current job-posting fact:** Securitize Capital is hiring an Associate, Fund Operations to work on NAV review, cash reconciliation, subscriptions/redemptions, discrepancy investigation, fund administrators/transfer agency coordination, procedures, audit requests, and operational escalation. This demonstrates a budgeted role, not SaaS purchase intent. It is notable precisely because Securitize already provides an extensive stack.

**Inference:** the residual problem is coordination, exception investigation and control evidence. **Counter-inference:** the work may require retained fiduciary judgment rather than software replacement. Securitize may be a sophisticated competitor/design-reference interview rather than the first customer.

Primary: [current job](https://job-boards.greenhouse.io/securitize/jobs/4411716009).

### B. A named portfolio manager paid the integration cost to remove treasury work

**Attributed customer evidence:** Spiko's Conquest case names a €500m infrastructure manager, 17 portfolio companies connected across three countries, several million euros placed, and a three-week API implementation. It describes prior multibank/multijurisdiction work selecting products, negotiating maturities, using different portals, and manual delays. Customer priorities included regulatory counterparties, permission management, tenant separation, and traceability. Plans to cover all 50 entities remain expansion plans.

**Inference:** multi-entity cash operations have a real buyer and repeated workflow. **Counterevidence:** Spiko already solved this account's stated problem quickly; an additional abstraction layer must justify itself.

Primary: [Conquest case, May 26 2026](https://www.spiko.io/blog/conquest-automated-cash-placement).

### C. A concrete Stellar support failure, not just a theoretical “UX problem”

**Verified vendor documentation:** Etherfuse says BYO wallets lacking required XLM/trustline can produce neither signing transaction nor webhook for swaps/offramps. The integration doc recommends preflight checks and repeated transaction regeneration because XDRs are short-lived. Embedded wallets absorb much setup already.

**Inference:** a wallet can show an order pending while no executable next step exists. A customer-facing support team needs deterministic state and resolution ownership. **Counterevidence:** this might be fixed by a free SDK/update, and most integration burden may be one-time rather than monthly software value.

Primary: [Stellar guide](https://docs.etherfuse.com/guides/chains/stellar), sections “Offramps and swaps” and “Transaction expiry.”

### D. Fund cash does not become instant just because shares are tokenized

**Verified vendor operational description:** Spiko SAFO daily cycle includes 3pm order cutoff, collection notice to Amundi, fund accounting by CACEIS, NAV validation/publication, 6pm unit issuance/cancellation, next-morning bank transfers; March 24 example shows 201 deposits and eight withdrawals. This is an actual repeated multi-party workflow, not demonstrated brokenness. Retail-facing instant withdrawal services may front liquidity; do not confuse the fund's standard cycle with those services.

**Inference:** product teams need a precise availability model and support handoff, not simply chain confirmation. **Counterevidence:** these responsibilities are already delegated/contracted to specialist parties.

Primary: [Daily operations, May 15 2026](https://www.spiko.io/blog/spiko-smart-cash-daily-operations).

### E. Permissioned collateral requires operational counterparties

**Verified primary governance analysis, proposed asset rather than completed listing:** Aave Horizon mWIN onboarding analysis says pool and liquidation destinations require whitelisting; non-whitelisted liquidation transfers revert, and redemptions have business-day cutoffs. HINC proposal similarly requires preapproved liquidators. These demonstrate a structural integration requirement, not demand for an unlicensed startup's lending marketplace.

Sources: [mWIN ARFC](https://governance.aave.com/t/arfc-onboard-mwin-midas-wellington-management-to-aave-horizon/25536), [HINC ARFC](https://governance.aave.com/t/arfc-onboard-hinc-neuberger-securitize-high-income-tokenized-fund-to-aave-horizon/25500).

### F. Adjacent customers already buy financial-data operations software

**Vendor-published customer testimony:** TRES homepage attributes time savings to named financial-operations/finance leaders at Alchemy, Starkware, OP Labs, Finoa and others. Its product includes multi-source reconciliation, accounting, alerting, banking inputs and tokenized securities. This supports the category's paid buyer, but also proves substantial competition. General crypto accounting success is not proof of a separate Stellar RWA wedge.

Primary: [TRES product/customers](https://tres.finance/).

## 3. Competitor map, funding, pricing and status

| Provider/project | Relevant offering and verified evidence | Implication/status caution |
|---|---|---|
| Spiko Embedded | Unlicensed integrator can act as business introducer; Spiko handles regulated service, brokerage, compliance, settlement. API handles user onboarding, regulatory disclosure, virtual IBAN deposit, withdrawal orders. [Docs](https://docs.spiko.io/embedded/distribute_with_spiko_license/overview/) | Generic “yield API for fintechs” already exists. Commercial partnership/country scope must be confirmed. |
| Spiko Direct | Portfolio/NAV, deposits/withdrawals/transfers/accruals, programmatic orders, accounting exports. [Docs](https://docs.spiko.io/direct/intro/welcome/) | Issuer's existing API undercuts a thin dashboard/API wrapper. |
| Spiko licensed distribution | Named/omnibus structures; omnibus requires relevant safekeeping/administration authorization. [Docs](https://docs.spiko.io/embedded/distribute_with_your_license/overview/) | “Aggregate tiny investors in our wallet” is not a free compliance workaround. |
| WisdomTree Connect + Stable Sea | Stablecoin-to-fund treasury, existing B2B distribution and APIs. [Issuer description](https://www.wisdomtree.com/onchain/insights/blog/making-real-world-assets-move-like-crypto), [Stable Sea API](https://docs.stablesea.com/api/index.html) | Generic treasury sweep/cash-yield company faces integrated competitors. |
| Etherfuse | Asset, fiat ramp, KYC/KYB, embedded-wallet, fees, transaction/webhook APIs. [Documentation](https://docs.etherfuse.com/) | Possible partner and competitor. Avoid “we integrate Etherfuse” as whole company. |
| Securitize | Tokenized funds, compliance/TA/admin/broker distribution; BUIDL launched across Ethereum, Avalanche, Solana etc.; published app integration examples. [BUIDL release](https://investors.securitize.io/news/news-details/2025/BlackRock-and-Securitize-Debut-New-BUIDL-Share-Class-on-Solana-Network-03-25-2025/default.aspx), [developer sample](https://github.com/securitize-io/securitize-dapp-sample/blob/main/docs/SECURITIZE_SKILL.md) | Full-stack leader; no evidence that generic middleware displaces it. |
| Tokeny | T-REX platform/API, issuance/servicing/investor tools; public standard €3k/month and advanced €5k/month, minimum 12 months; €1 additional event outside bundles. [Pricing](https://tokeny.com/pricing/) | Concrete enterprise software price benchmark, not what a new startup can charge. |
| Tokenistry | Independent lot/ownership lineage reconciliation over existing token books; consumes wallet-to-investor mappings, no keys; sold as part of Core, not separate purchase. [Reconciliation product](https://tokenistry.com/reconciliation/) | Closest positioning competitor to an “independent assurance layer.” No published customer/revenue proof verified here; still kills novelty claim. |
| TRES, Bitwave, Kryptos | Accounting/reconciliation/compliance; Bitwave broad enterprise suite. [Bitwave](https://www.bitwave.io/), [TRES](https://tres.finance/) | Integrate with established accounting tools instead of attempting generic replacement. |
| Ascend | SDF $1m investment, permissioned credit plus disposal facility. See above. | Stellar RWA collateral/lending is already institutionally funded. Production status needs separate proof. |
| Spydra | SCF #31 $132k **Awarded**, low-code RWA issuance. Earlier SCF #30 $150k **Not Awarded** should not be included as funding. [Project](https://communityfund.stellar.org/project/spydra-low-code-rwa-tokenization-engine-k2y) | Issuance tooling occupied; grant does not prove live paying customers. |
| Amber | SCF #20 $50k awarded for RWA tokenization. [Project](https://communityfund.stellar.org/project/amber-rwa-tokenization-on-stellar-sku) | Older funded concept, operational traction unverified. |
| Neovestor | SCF #28 $50k awarded. Grant self-reports RWA investor survey/waitlist and planned emerging-market launch. [Submission](https://communityfund.stellar.org/submissions/recUcnDR8rtlntavE) | Generic retail RWA launchpad occupied; claimed survey/waitlist is not verified retained funded investors. |
| Liqvid | SCF #37 $137.5k awarded, private-market RWA fundraising, access controls, secondary liquidity. See above. | Differentiate Base traction from Stellar roadmap. |
| TokenOps | SCF #30 $60k awarded; vesting, airdrops, staking, onchain salaries. [Project](https://communityfund.stellar.org/project/tokenops-hv6) | Token distribution management occupied; not all distribution is securities placement. |
| Kryptos | SCF #30 $35k awarded for PMS/accounting/tax integration. [Awards record](https://communityfund.stellar.org/awards/recYtZ5R17u4bxSrS) | Stellar accounting integration is not whitespace. |
| Tigerblocks KYC Token & UI | Present in official SCF project index; $45k reported in Stellar Community SCF #22 recap. [Project index](https://communityfund.stellar.org/projects), [community recap](https://medium.com/stellar-community/scf-22-recap-0d4a4c2b3655) | Treat amount as recap evidence; primary individual grant record not located. No independently checked production deployment. |

The [SCF database](https://communityfund.stellar.org/projects) also includes additional real estate, lending, and RWA projects. This is a relevant competitive sample, not an exhaustive census.

## 4. Ethereum/Base/Solana/Avalanche and traditional alternatives

Do not use a generic chain-speed table to decide the company. The customer buys a supported asset, eligible holding structure, reliable cash exit, and integrated workflow. Same-fund network terms provide more useful evidence than theoretical TPS.

| Alternative | Concrete evidence | What a Stellar company must beat |
|---|---|---|
| Ethereum | BENJI higher issuer minimum and BUIDL availability; Tokeny supports enterprise EVM servicing, Aave Horizon permissioned collateral. | Liquidity/provider access and mature integrations can outweigh gas. Need current actual customer costs rather than gas anecdotes. |
| Base | BENJI $100 documented minimum, Spiko deployment links, Etherfuse API support. | “Low fees + RWA” is insufficient differentiation from Base. Stellar advantage must be customer's existing rail/asset footprint. |
| Solana | BUIDL share class March 2025 and full WisdomTree suite per January/May 2026 issuer materials; BENJI $100. | Existing distribution and supported custody. Stellar cannot claim exclusive regulated yield. |
| Avalanche | BUIDL, BENJI, OpenTrade/Littio embedded yields. | For LATAM savings wallets, an incumbent comparable service exists. [Littio's own product explanation](https://littio.co/blog/como-crecen-tus-recursos-en-littio), [Avalanche/OpenTrade case](https://assets.ctfassets.net/voq4a5ue459o/5pSosqN6W8itlUrj0pjjnk/076e05a8a28febc3023f51e1efbf24ca/OpenTrade_%C3%83__Avalanche.pdf). |
| Traditional broker MMF | Schwab advertises minimums as low as $0; mutual funds already yield and provide familiar reports. [Schwab](https://www.schwab.com/money-market-funds) | Access to yield alone is not novel. Onchain mobility and workflow may matter only to certain customers. |
| Fintech treasury | Mercury Treasury advertises $250k qualification balance; automatic balance-based transfers already exist. [Treasury](https://mercury.com/treasury), [rules](https://support.mercury.com/hc/en-us/articles/28768212621332-Setting-up-auto-transfer-rules) | Existing banking integration, trust, and automatic treasury workflow. Check current fee quote rather than carrying forward an old ADV. |
| Existing fund services | Spiko uses CACEIS/Amundi, BENJI proprietary transfer agent; Securitize offers admin/TA. | A new ops company must show work that these contracted providers explicitly do not own. “The industry has a back office” is not a wedge. |

**ETHGlobal inspection:** [Treasury Anchor](https://ethglobal.com/showcase/treasury-anchor-k1825) demonstrates roles/policies and intent execution on Safe; [YieldProof](https://ethglobal.com/showcase/yieldproof-23srq) is a hackathon RWA-yield attestation protocol; [RWA Marketplace](https://ethglobal.com/showcase/rwa-marketplace-o3hoh) is a synthetic RWA market concept. [Bailiff](https://ethglobal.com/showcase/bailiff-368x0) won a Uniswap prize for permission-preserving liquidation routing, but explicitly runs a Sepolia/Anvil fork demo. These establish buildability/idea competition, **not** current regulated products, mainnet usage, paying buyers, or legal authority. Hackathon attestations do not establish economically recoverable asset claims.

## 5. Five distinct full-company hypotheses

All suggested prices, go-to-market routes and economics here are hypotheses, not verified offers or revenue forecasts. Do not apply market multiples to tokenized AUM and call it obtainable revenue.

### 1. Distributor redemption operations system — conditional first choice

**Buyer / user:** Head of Operations/COO at a wallet, neobank, investment app, or licensed distributor with two or more externally issued cash-yield products. Support lead, treasury/finance controller, and integration engineering use it daily. Avoid choosing giant issuer procurement as the first route.

**Repeat workflow:** ingest order + bank/issuer/custody + chain state; track eligibility, transfer permission, cutoff, quote expiry, token receipt, redemption acceptance, stablecoin/fiat payout; identify missing/out-of-order events; assign owner and action; reconcile closure; export evidence and accountant-ready records. Sell one operating console with working connectors and case resolution, not an asset comparison site.

**Revenue / expansion:** annual software subscription plus connectors/transaction volume; initial pricing test $1k–$3k/month only if it replaces expensive recurring investigations. Setup fees cover implementation but should not be the business. Expand into treasury inventory availability and issuer/distributor service-level reporting after evidence of retention.

**Distribution:** cold-reach the eight named wallet/distributor operators in current issuer integration lists and embedded-yield public cases. Ask DevRel/ambassadors only for relevant introductions, not purchase intent. Sell a redacted historical-order audit first, no funds moved. Need direct Head of Ops sponsorship.

**Partners/legal requirements:** read-only issuer/custody/bank APIs, data-processing/security arrangements, customer-approved account mappings. Human-approved resolution instructions initially; no custody, investment choice or security solicitation. Actual implementation needs counsel on whether any order transmission/execution/recommendation crosses regulated service boundaries. APIs and privacy controls are technical prerequisites, not a blanket legal safe harbor.

**Stellar reason:** real Stellar product/ramp inventory and asset-specific failure modes allow a precise initial connector set. Critical: non-native Soroban tokens, Classic SAC assets and bank redemptions require different state machines. If first customers use Base/Solana, economic reality should win.

**Failure case:** providers already deliver reliable end-to-end state and all residual support costs are small; operational exceptions are one-time integration problems; customers only use one provider; incumbents add the screen; security review exceeds expected ACV. Stronger substitute: a free preflight library plus existing Zendesk.

**Independent payer test:** customer must show at least three recent cases that required action across providers and cannot be closed from its TA/issuer dashboard. If no budget holder would pay for resolution reliability independent of choosing an issuer, reject.

### 2. Multi-entity cash operating system for private-market portfolio companies

**Buyer / user:** CFO/Head of Treasury at an infrastructure/private-equity holding group with 20–100 operating entities; local controllers execute. Selling point is coordinated working capital governance, not yield chasing.

**Repeat workflow:** forecast cash floors and obligations by legal entity/currency; enforce treasury policy and approvals; subscribe/redeem eligible fund positions; reconcile bank and fund records; roll up performance and audit evidence. Strongest concrete demand analogue is Conquest/Canary.

**Revenue / distribution:** per-entity monthly SaaS and group minimum. Sell through fund administration providers/accounting firms and CFO communities; begin with a buyer outside the named already-served case. Bootstrap service-assisted deployment may reveal recurring template. Unproven pricing test €15k–€50k yearly across a group.

**Partner/legal requirements:** licensed investment provider, local corporate eligibility, bank connectivity, approved custody and fund access; investment policies belong to customer/adviser. “We use Spiko's license” applies only under contracted approved business-introducer model.

**Stellar reason:** useful only when operating entities or payout destinations already use Stellar stablecoins/RWAs. Most traditional European groups have no compelling reason to select a blockchain. A Stellar-required company may lose the buyer.

**Failure case:** Spiko Direct and existing TMS/Canary solve the whole requirement. Treasury module becomes an issuer feature or custom systems integration. This has strongest demand evidence but weakest necessity of Stellar.

### 3. Local-currency yield-balance distribution for a specific worker/SME channel

**Buyer / customer:** a payroll/vertical software company wants sticky savings for its existing users; end-user holds local government-bond exposure rather than being offered risky tokenized private credit. Focus one Mexico segment with MXN obligations, not global retail.

**Repeat workflow:** receive wages/sales proceeds, opt-in allocation, show NAV/yield/tax data, redeem to local cash for bills; persist through salary cycles. Company must control acquisition or a valuable vertical workflow; generic “savings pots” is not enough.

**Revenue / distribution:** contracted platform fee/revenue share with regulated product and payments partners, plus employer/vertical software recurring SaaS. Economics must be calculated after ramp costs, support, compliance and balance persistence. Low balances cannot support high acquisition cost: illustrative $500 average balance × 30 bps = $1.50/year before costs.

**Partner/legal requirements:** explicit issuer distributor agreement, local eligibility/KYC, investment distribution/custody/payment structure, user consent, tax reporting, local redemption counterparties. MXN live ramp is documented; do not promise Brazil rails from an “upcoming” roadmap.

**Stellar reason:** local Stellar ramp and wallet footprint, low-value transfers. It is not exclusive: Etherfuse supports other chains, and OpenTrade/Littio already distribute yield on Avalanche.

**Failure case:** no exclusive channel, issuer owns distribution, users immediately cash out; regulated approvals and servicing overwhelm thin yield economics. Mark as commercially conditional, not a quick hackathon-to-company jump.

### 4. Permissioned collateral liquidity operations network

**Buyer / user:** RWA issuer, lending market operator, treasury lender; operations/risk teams. Company operates a verified network of eligible market makers and executable distressed-asset exit procedures.

**Repeat workflow:** maintain counterparties' eligibility, credit capacity and approved wallets; monitor NAV/collateral/cutoffs; route qualified liquidation and redemption; document settlement, run stress simulations and incident response. This is institutional counterparty operations, not merely an automated liquidation bot.

**Revenue / distribution:** market-operator retainer, onboarding/servicing fees, legally permitted execution or liquidity fees. Need signed mandates and committed capital; a speculative fee on future TVL is not initial revenue. Distribution through asset issuers/lending operators is relationship-heavy.

**Partner/legal requirements:** regulated broker/counterparties, issuer-approved contract/address permissions, risk provider, price oracle, custody, enforceable collateral and liquidation agreements, funded capital providers. Any guarantee creates balance-sheet risk. Exact requirements require jurisdiction-specific legal review.

**Stellar reason:** native controlled asset holding in Soroban plus same-rail stablecoin settlement. Strong technical relevance, weak founder accessibility without a dealer network.

**Failure case:** Ascend already funded on Stellar; Aave/Securitize/Morpho incumbents own counterparties elsewhere; no eligible buyer in a stress event; borrowers refuse rates; yields do not justify financing. Not recommended to a founder with no current network/capital/legal partner.

### 5. Independent ownership and entitlement assurance for transfer agents/auditors

**Buyer / user:** controller at tokenized fund/distributor, transfer-agent COO, auditor's digital-assets team. Pays for evidence of consistency across official investor book, chain wallets/contracts, custody and fund accounting records.

**Repeat workflow:** independent daily holdings and lot/entitlement reconstruction; wallet-to-legal-investor mapping; detect transfers, recoveries, freezes, accrual differences and unmapped holders; produce reconciliation file and signed reviewer trail for periodic close/audit. Avoid promising that blockchain alone proves legal ownership.

**Revenue / distribution:** recurring per-fund/per-entity SaaS with professional audit/adviser channel; pilot on a single completed reporting period. Pricing test $15k–$40k annually conditional on frequency and liability significance, not generic data-dashboard budget.

**Partners/legal requirements:** access to authoritative share register and accounting policies; reviewer/auditor acceptance; independent controls and data handling. Do not act as auditor or give assurance opinions without proper authorization. Software evidence and regulated assurance are different services.

**Stellar reason:** native asset-specific authorization changes and Soroban flows require capable indexing; but purely read-only assurance is not uniquely Stellar and should not manufacture onchain attestations to satisfy a rail constraint.

**Failure case:** Tokenistry directly markets this, TRES/Bitwave and TA systems overlap, investors never move outside the issuer's own platform, rare exceptions handled with a small script; auditor refuses reliance. Strongest potential budget is professional services, but risk of a bespoke consulting business.

## 6. Realistic interview access without an existing network

Target **5–10 completed interviews**, not “speak with institutional partners” as an assumed advantage. This is a proposed research process; no messages sent.

Build a 30–40-person contact list across 20 organizations using publicly visible current roles. Suggested mix:

1. **Four distributor operators:** Head of Ops/COO or Support Operations at Meru, Decaf, LOBSTR, or another issuer-listed wallet with actual RWA product. Validate product availability before outreach; integration announcement alone is not an operator roster.
2. **Three issuer/service operators:** fund operations or integrations at Etherfuse, Spiko, Ondo, WisdomTree. These are expert interviews and potential competitors; they need not be first buyers.
3. **Two controllers/administrators:** digital-assets fund controller or transfer-agency operations manager at a mid-sized provider, plus an accounting practice serving such clients. Securitize's job posting defines the workflow/persona even if Securitize itself is hard to access.
4. **One current treasury user:** CFO/controller of a multi-entity business using a tokenized MMF; reach via public case-study organization or financial-software community, with no assumption of a warm introduction.

Channel plan: individual cold email/LinkedIn to relevant public professional contact; builder/DevRel introductions as optional acceleration; product docs public support/developer forums only when appropriate, no mass marketing. A working hypothesis is 30–40 tailored requests may yield 5–10 discussions; it is not a guaranteed conversion rate. A DevRel conversation counts as an access lead, not customer validation. Allow two weeks; if access cannot be obtained, revise founder-market fit rather than invent feedback.

20-minute evidence-led interview:

- “Walk through the last redemption that did not complete on time. Which timestamp first looked wrong? Who owned each step?”
- “Show redacted order/ticket identifiers or your existing spreadsheet. How many similar cases in the last 30 days and how many person-hours?”
- “Which issuer/TA dashboard did you use? What was still missing? Which party was contractually responsible?”
- “How many products/providers/chains do you operate now, not on the roadmap?”
- “Who signs a software purchase? What do you already pay for accounting/reconciliation/support? What security review would a read-only tool face?”
- “If we deliver this one exception report from last month's anonymized data, what decision or work changes? Would you sponsor a paid four-week pilot?”

Do not ask “Would you use an RWA dashboard?” The next research artifact should be a table of incident counts, labor, counterparties, authoritative records and buyer authority.

## 7. Decision and strongest falsifiers

**Conditional recommendation:** prioritize hypothesis 1 for interviews because it tests a cross-company coordination job rather than rebuilding tokenization primitives. It can start without financial risk, licenses to custody assets, committed lending capital, or issuer replacement. Do not build a generalized platform first. First paid deliverable: reconstruct one distributor's past month of external redemptions/withdrawals from redacted exports, identify unresolved exceptions and confirm ownership/action. Then prove the same connector/rule resolves a second company's data.

**Predeclared go/no-go hypothesis:** proceed only if at least three genuinely independent target firms report repeated cross-provider exceptions and can supply redacted historical evidence; two budget owners sponsor a paid pilot; savings/reliability materially exceed subscription and integration burden; at least one buyer has a current Stellar workflow; and the solution adds material value after issuer/TA support is used. These numbers are decision thresholds, not established market facts.

**Strongest falsifier:** a distributor's existing issuer/TA provides sufficiently complete eligibility/order/settlement states and escalation, such that remaining work is under one person-day per month or handled by a free connector. If buyers will not pay independently of a yield/referral arrangement, the proposed operations company is a feature/integration service. Do not rescue it by adding a token, an AI agent, or an attestation protocol.

**Specific issuer SaaS falsifier:** Securitize/Spiko hiring and delegated fund operations do not prove external software demand. If issuer-side buyers say the pain is core fiduciary review, already funded in their administrator contract, or requires proprietary inputs they cannot share, issuer-only lifecycle SaaS should be rejected.

**Stellar falsifier:** if otherwise viable customers have no current Stellar flows and accept equivalent Base/Solana integrations, Stellar is a first connector or funding ecosystem, not the core reason the company exists. State that plainly in company selection.

## Research limitations

- No direct buyer interviews, paid pilots, security questionnaires, provider contracts, or legal opinions.
- Primary issuer documentation used for technical/product claims; vendor customer cases and hiring evidence distinguished from independent demand measurement.
- Mainnet independent volume/contract reads not completed; official deployment lists and source/audit evidence recorded without overclaiming.
- No fabricated future facts: DTCC first-half-2027 availability remains a plan; private credit fundraising targets remain targets; pilots remain pilots.
- Current aggregate AUM claims not used as obtainable TAM or revenue. SDF treasury page advertises $4bn/67 products and $605m BENJI as of Oct 6, 2026, but these are selected provider/aggregator claims rather than independently reconstructed assets or active investor counts. [SDF treasury page](https://stellar.org/solutions/treasury-management).
- No Instaward rules read. Company selection should precede any competition-format optimization.
