# Bell / Protocol 30: company implications and investment decision

**Checked 21 October 2026. Research only.** No contracts were deployed, transactions sent, organizations contacted or applications submitted. This supplements the [20 October investigation](../research-02/report.md); it does not retrospectively change that report's evidence date.

**Verdict:** Bell strengthens a new challenger—**stablecoin collections and payment-exception operations for existing payment businesses**—but does not justify replacing the earlier discovery priorities: liquidity-aware DeFi risk/recovery operations, followed by RWA execution and cash readiness. CAP-84 is the clearest commercial improvement: it could make shared, programmable receipt accounts easier to integrate and operate. It does not establish demand for another account vendor. CAP-87 warrants institutional security discovery; CAP-88 warrants compatibility work and later performance measurement, not a faster-payments company today.

**Main reason this judgment could be wrong:** one existing ramp or fintech may have substantial customer-attribution and smart-account servicing costs that CAP-84 removes. Access to its records and a paid operational pilot could move collections ahead of the prior finalists. Conversely, existing providers may absorb the upgrade and leave little independent software budget.

Evidence labels: **F** verified documentation/code or the stated live observation; **V** vendor claim or vendor-described experiment; **A** public user anecdote; **I** inference; **H** unvalidated company, price, distribution or experiment hypothesis. Available code and vendor documentation do not establish production safety, customer adoption or willingness to pay. All proposed products below are H unless otherwise labeled.

## 1. Activation: released software is not an activated protocol

**F:** The [official announcement](https://stellar.org/blog/developers/introducing-bell-protocol-30-on-stellar) and [upgrade guide, updated 20 October](https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide) schedule validator votes for **3 November 2026, 17:00 UTC on testnet**, and **23 November 2026, 17:00 UTC on mainnet**. At this research cutoff these are future, conditional votes. Neither activation has occurred according to that schedule; no completed Protocol 30 vote was verified.

**F, narrow live observation:** the [public mainnet Horizon endpoint](https://horizon.stellar.org/) returned `current_protocol_version: 29`, with ledger **65,053,777**, closed **21 October 2026 at 03:51:08 UTC**. Its connected Core was **30.0.0**, with `core_supported_protocol_version: 30`. The distinction is observable: software can support 30 while the network runs 29. See the [saved response](evidence/bell-mainnet-root-2026-10-21.json). This is one public node's response, corroborated by the [official version history](https://developers.stellar.org/docs/networks/software-versions), not an independent quorum audit. The [Core 30 release](https://github.com/stellar/stellar-core/releases/tag/v30.0.0) alone would be insufficient activation evidence.

Dependency labels used throughout:

| Label | Meaning |
|---|---|
| **A — today** | The specified workflow is implementable using current mainnet mechanisms, subject to integration and security work. This does not mean the proposed company has built it. |
| **B — after activation** | The named Bell primitive requires successful Protocol 30 activation on the target network. Release binaries and a scheduled vote are insufficient. |
| **C — additional dependency** | Requires sender/wallet/issuer/custodian adoption, a commercial agreement, performance changes or further protocol/interface work. Activation alone is insufficient. |

## 2. CAP-84: the important opportunity is attributable receipts into programmable pooled accounts

### What changes, precisely

**F:** [CAP-84](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0084.md) adds a **W address: contract address plus a public unsigned 64-bit identifier**. SAC `transfer` accepts it as a destination; the balance belongs to the underlying contract and the receipt event carries `to_muxed_id`. Source multiplexing is excluded. Direct `mint` and `transfer_from` support is deferred; an issuer invoking SAC `transfer` has its special mint behavior. Classic Payment operations do not acquire W destinations. W is distinct from a normal contract `Address` and cannot itself be a storage key; store the decomposed contract and identifier where needed.

**F:** Current [SAC interfaces](https://developers.stellar.org/docs/tokens/stellar-asset-contract) distinguish transfer destinations from balance, authorization, allowance and other Address-based operations. **I:** W must therefore not be presented as an independently owned account, separate issuer authorization, separate balance or a universally supported token address. Custom tokens need their own compatible implementation; a token-interface convention does not update existing contracts automatically. [Token interface](https://developers.stellar.org/docs/tokens/token-interface).

**A, direct problem evidence:** a builder in the [muxed-contract discussion](https://github.com/orgs/stellar/discussions/1950) describes a smart-wallet/SEP-24 integration needing customer identifiers on inbound contract payments. The same discussion challenges whether programmable contracts already permit custom multiplexing and raises adoption concerns. This is a concrete integration need, not a named paying buyer or representative demand survey.

### Compare the real alternatives

| Design | Already possible? | Economic/operational advantage | What the comparison must include |
|---|---|---|---|
| Separate customer contract accounts | **A** | Distinct account state and authorization boundary; easier account-level attribution | Deployment, per-instance state, maintenance, recovery and operational overhead. Do not count one Wasm upload per customer: contract instances can share code. [Contract architecture](https://developers.stellar.org/docs/learn/encyclopedia/contract-development/stellar-contract). |
| Shared contract with explicit `deposit(customer_id, …)` | **A** | Shared treasury and programmable internal accounting today | Requires senders to call the app-specific interface. Bell does not invent multi-user contracts; its delta is standardized address-level receipt attribution. |
| Classic pooled G account with memo or M destinations | **A** | Existing customer-attributed pooled receipt model | Existing sender compatibility and custody controls may already solve the business problem; not equivalent to a custom contract authority model. [Muxed-address discussion](https://github.com/orgs/stellar/discussions/1950). |
| Shared contract receiving W transfers | **B**, ecosystem reach **C** | Address-level attribution into a programmable treasury without requiring one receiving contract per customer | Tenant liabilities, spending rights, recovery, indexer correctness, sender compatibility and aggregate treasury risk still require engineering. |

**I:** Bell's strongest fit is an operator that needs **both** address-based deposits and contract-enforced pooled spending policies. A business satisfied with current classic pooled custody may gain little. A business requiring genuinely separate customer accounts may still prefer separate contracts.

**F:** persistent state has rent and lifecycle costs; large shared entries also have access/contention implications. [Storage strategies](https://developers.stellar.org/docs/build/guides/storage/storage-strategies), [persistent-data layout](https://developers.stellar.org/docs/learn/fundamentals/contract-development/storage/persisting-data). **I:** pooling avoids some account-instance work, not customer state. Entitlements, mandates and journals still grow with users. Even separate tenant keys cannot remove contention on a single aggregate token-balance write. Partition by program or treasury where appropriate and benchmark under actual receipt/spend concurrency.

**H, measurement model:** compare avoided deployment, maintenance and applicable sweep work against additional ledgering, indexing, security review, support and contention costs. Measure total cost per active funded customer, successful receipt and resolved exception. There is no defensible percentage saving or universal break-even customer count yet. Savings against separate contracts are not savings against an already shared classic account.

### The hard mechanism: receipt attribution is not entitlement enforcement

The following is **I: architecture and failure analysis**, not additional protocol functionality.

An ordinary token transfer to W does not, merely by arriving, invoke the receiving application's accounting logic. Token balance/event changes and the application's tenant ledger are separate. Two credible designs have different trust models:

- **Operator ledger:** a regulated/payment operator credits an offchain double-entry customer ledger from successful committed receipts, reconciles it to chain assets and authorizes withdrawals. The operator remains trusted for entitlement correctness and release.
- **Onchain claims:** explicit deposit calls can combine transfer and claim accounting atomically. Accepting arbitrary direct W receipts and later granting onchain claims requires an authenticated credit mechanism. A backend attesting deposits adds trust; a contract cannot simply read arbitrary historical events. Any proof-based alternative needs its own design and audit.

Contracts can implement sophisticated authorization today. [Contract accounts](https://developers.stellar.org/docs/build/guides/contract-accounts), [advanced authorization patterns](https://developers.stellar.org/docs/build/guides/contract-accounts/advanced-patterns). **I:** for a shared treasury, bind each spend to the tenant's actual authority, asset identity, amount, destination, nonce, expiry and network/contract domain; check nested calls and allowances as well as top-level requests. W IDs are public labels, not credentials. Recovery/admin paths must not silently bypass the same separation. OpenZeppelin already supplies [smart-account rules](https://docs.openzeppelin.com/stellar-contracts/accounts/smart-account) and [policy mechanisms](https://docs.openzeppelin.com/stellar-contracts/accounts/policies); reuse and review them rather than claiming Bell newly enables spending limits.

| Failure | Required product behavior / limit — design recommendations |
|---|---|
| Unknown, missing or wrong customer ID | Quarantine unknown receipts. Treat missing ID separately from zero; never reuse identifiers. A syntactically valid W can identify the wrong customer. Bind network, full address, asset and order in authenticated payment instructions. A checksum cannot validate commercial intent. |
| Valid ID assigned to wrong customer | Hold release where detected; require reviewed compensating ledger entries and preserve evidence. If the wrong party has withdrawn funds, recovery may be impossible. No automatic protocol refund exists. |
| Duplicated, replayed or partially ingested receipt | Exactly-once application credit using a durable journal keyed by network/transaction/event position. Persist cursor and credit consistently; replay after downtime. Include successful issuer-transfer mint events where relevant. Monitor authoritative receipt events rather than assuming all transaction attempts succeeded. [Event ingestion](https://developers.stellar.org/docs/build/guides/transactions/send-and-receive-payments). |
| ID precision lost | Keep u64 values losslessly across SDKs, JSON, databases and exports; ordinary JavaScript Number is not sufficient for all u64 values. Test boundary identifiers. |
| Refund to original sending address | Original sender may be another pooled contract or exchange. Bind refund to the order and verified return instructions. An outgoing pooled payment does not automatically identify its beneficial customer. Track partial refunds and ambiguous retry outcomes. |
| Indexer or database loss | Rebuild receipts from retained chain history and checkpoints, but also preserve customer mappings, orders, internal transfers and spending journals. W deposit history alone is not a complete customer-ownership backup. |
| Issuer freezes/claws back pooled assets | Reconcile impaired assets against customer liabilities and stop inappropriate releases. W does not create separate issuer controls for every tenant. Verify actual asset configuration; pooling increases the impact of aggregate restrictions. [Asset controls](https://developers.stellar.org/docs/tokens/control-asset-access). |
| Shared contract fault or compromise | Independent review, bounded administration, recovery rehearsal and partitioned exposure. Shared code is already a common dependency across separate accounts; pooling additionally combines state and treasury consequences. |

**C, adoption boundary:** test W parsing, QR/payment-request creation, signing, simulation, transfer, event preservation and refund entry in each actual sender stack. Ordinary `Address` parameters are not automatically W-compatible, and updated SDKs do not establish app support. The [upgrade guide](https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide) calls for updated SDK/XDR handling. No checked evidence establishes end-to-end MetaMask, exchange, anchor or custodian W support today. Keep compatible existing receipt routes until the required partners demonstrate support.

### Privacy and RWA ownership boundaries

**I, threat model:** W routing supplies **no cryptographic confidentiality**. Public observers can see underlying contract, transfer sender, asset, amount, ID and timing in ordinary SAC flows. Reused IDs can expose customer-level links. A pooled contract balance remains public; a private offchain entitlement database may conceal its detailed allocation but does not make the chain payment private. The operator knows customer mappings; counterparties can reveal them; RPC/relayer providers can observe request metadata. Network/IP and cash-in/out links are unaffected. Instructions kept offchain remain confidential only against parties denied access to them, not through Bell cryptography. There is no anonymity set, viewing-key scheme or ZK privacy proof supplied by this address format.

**I:** issuer approval of a pooled C address also does not prove every beneficial holder is eligible or every tenant has legal title/redemption rights. Confirm the asset's contract-account, omnibus, transfer-agent and holder-record requirements. DeFi protocols recording a position at C do not automatically create a separate position per W customer. Allocation of collateral, yield, losses and liquidation proceeds remains a product obligation. Bell neither authorizes RWA pools nor creates their liquidity.

## 3. CAP-87: enforceable new authorization, conditional institutional business

**F:** [CAP-87](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0087.md) specifies pure ML-DSA-44/65/87 verification in contracts. Public keys are 1,312/1,952/2,592 bytes and signatures 2,420/3,309/4,627 bytes respectively; context is limited to 255 bytes. Final resource calibration is not established by prototype measurements. The primitive supports contract policies; **network transaction signatures remain Ed25519**. It supplies authenticity, not payment confidentiality.

**I:** a contract may require ML-DSA authorization even when a relayer submits an Ed25519 transaction envelope; these are different authorization layers. Conversely, contract PQ checks do not make consensus, issuers or every administrative authority quantum safe. An **ML-DSA OR classical key** spending rule retains a classical bypass. Requiring both closes that branch but adds availability and recovery dependencies. Review upgrade keys, guardians, recovery, issuer permissions, offchain attestations and policy modification—not merely the normal spend path. Long-lived agent mandates still need expiry, revocation and bounded permissions.

**F/V:** [AWS KMS offers ML-DSA](https://aws.amazon.com/about-aws/whats-new/2025/06/aws-kms-post-quantum-ml-dsa-digital-signatures/); precise message/context/signature compatibility still needs testing. [Fireblocks' October NEAR experiment](https://www.fireblocks.com/blog/post-quantum-key-rotation-ml-dsa-near) describes ML-DSA-65 key rotation using a software HSM, separating it from complete hardware, threshold, recovery and platform readiness. This is meaningful incumbent work, not verified Stellar production support. [BIS Project Leap](https://www.bis.org/project/leap) establishes institutional PQ payment experimentation, not a startup procurement budget. [SDF's preparedness plan](https://stellar.org/blog/foundation-news/introducing-the-quantum-preparedness-plan) treats classic-account PQ signers and consensus work separately; roadmap dates are not delivered capabilities.

**Business conclusion, I:** the plausible company is recurring **digital-asset authority and migration assurance**, not a wallet with one new signature algorithm. Buyer demand for migration evidence, downgrade monitoring and multi-custodian control might exist; no checked source proves a current Stellar RFP, buyer commitment or urgent deadline. Do not rank this above existing finalists without budget-owner evidence.

## 4. CAP-88: necessary timing groundwork, no demonstrated speed product

**F:** [CAP-88](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0088.md) adds millisecond ledger-close representation with a minimum increment of 1 ms; legacy seconds are the floor of the millisecond value. Transaction time bounds, minimum sequence age, claimable-balance timing, upgrade scheduling and Soroban `ledger_timestamp` retain whole-second semantics. New XDR union arms require compatible decoders. Bell does not itself deliver sub-second ledgers, millisecond contract expiry or faster customer settlement.

**I:** a timestamp's precision is not consensus latency, throughput, ordering fairness, quote freshness or a guaranteed execution deadline. Faster production service would require adopted interval/configuration choices and engineering that works under realistic consensus, execution, network and ingestion load. Depending on the target behavior, further protocol/interface changes may also be needed; it would be inaccurate to say every interval improvement requires a new CAP. Existing configuration already includes millisecond target/timeouts. [Configuration fields](https://developers.stellar.org/docs/data/analytics/hubble/data-catalog/data-dictionary/bronze/config-settings).

Before changing a payments or trading thesis, require observed loaded-mainnet p50/p95/p99 submission-to-finality and finality-to-usable-receipt times, failure/retry rates, congestion and outage behavior, wallet/RPC support and the actual fiat/redemption leg. A faster chain leg may be economically immaterial when a bank cutoff or inventory constraint dominates. Millisecond close telemetry could improve later execution diagnostics in the existing risk product; decoder compatibility is an integration feature. **Reject a standalone Bell high-frequency trading, millisecond escrow or instant-refund thesis today.**

## 5. Five product opportunities tested against Bell

All five are **H full-company hypotheses**, not existing products or customer commitments. The first four use different buyers/workflows despite sharing account infrastructure. The fifth is an institution-facing security business. No one needs all three CAPs to make a coherent product.

### B1. Stablecoin collections and payment-exception operations — strongest new challenger

**Buyer/job:** head of payment operations and controller at an existing ramp, cross-border PSP or fintech with actual Stellar receipts. Weekly journey: issue customer/invoice payment instructions, match receipts, credit liabilities, resolve missing/over/underpayments, approve refunds and reconcile provider/bank/chain records. The valuable product is reliable resolution and close-of-books evidence.

**Mechanism/flows:** integrate customer-controlled custody, committed events, partner statuses and a double-entry liability ledger. Produce an exception queue with evidence, dual-review adjustments and verified refund destinations. Start read-only; do not acquire spending authority just to reconcile. Later execution must use the operator's approved custody and payment policies.

**Bell delta:** shared contract deposit attribution can reduce custom deposit calls or separate receiving-contract management. **A:** current G/M/memo and explicit contract-deposit reconciliation. **B:** W receipt ingestion. **C:** actual senders and fiat partners preserving W and operational access to their records. No W-specific advantage if today's routes already work adequately.

**Competition/evidence:** [Anchor Platform](https://developers.stellar.org/docs/platforms/anchor-platform/sep-guide/sep24/integration) already documents payment/refund/error states, proving workflow complexity, not a missing software budget. [Bridge liquidation addresses](https://apidocs.bridge.xyz/platform/orchestration/liquidation_address/liquidation_address) already provide standing crypto-to-bank routes including Stellar G+memo examples. [Modern Treasury Ledgers](https://www.moderntreasury.com/products/ledgers) already sells pooled-balance/refund/reconciliation infrastructure. W issuance alone is not a company.

**Commercial H:** paid integration plus a subscription by supported operator, corridor or processing tier; test low-four-figure monthly pricing against measured labor and incident costs, not nominal gas savings. Provider adapters, resolved-case history and finance workflows might create switching costs. Expand across chains and bank rails while retaining Stellar receipt, asset and anchor integrations. Customer acquisition, provider access and support economics dominate early technical costs.

**First eight conversations:** three ramp/anchor ops leads, two payment-platform controllers, two payment engineers, one custody integration lead. Identify operators via public anchor/product directories; request specific role introductions through DevRel/Ambassadors, then use public business channels for interview requests. Introductions are not assured. Ask to reconstruct ten actual exceptions, tools used, resolution time, losses and budget ownership.

**Three kill observations:** no recurring costly exception; no two operators willing to share redacted histories; actual senders cannot support W and current receipt attribution is sufficient. Promote above the prior winner only with a credible paid pilot and a measured gap in existing tools.

### B2. Budget and recourse operations for agent-commerce platforms

**Buyer/job:** finance/risk owner at a platform already processing real third-party agent purchases. Weekly journey: fund customer budgets, approve supplier/counterparty rules, review unusual requests, reconcile delivery evidence, reclaim unused funds and handle refunds or compromised credentials. Customers buy control and accountability, not an agent wallet.

**Mechanism:** tenant entitlements plus enforced spending mandates, approval queue, seller/order records, receipt/billing exports and revocation/recovery. Separate “authorized to pay” from “seller delivered.” Neither signatures nor W IDs verify offchain fulfillment. Reuse [OpenZeppelin policies](https://docs.openzeppelin.com/stellar-contracts/accounts/policies); compare [Safe agent allowances](https://docs.safe.global/home/ai-agent-quickstarts/agent-with-spending-limit) and [Privy payments](https://www.privy.io/payments). Existing control stacks make a generic alternative easy to bundle away.

**Dependencies:** **A:** bounded smart-account spending, separate contracts or explicit pooled deposits, human approval workflows. **B:** W-funded pooled budgets; optional native ML-DSA check. **C:** paying agent marketplaces, sender support, compatible secure signers and participating sellers. Bell improves funding ergonomics, not the difficult procurement/recourse problem. Shared accounting is a security obligation rather than tenant isolation supplied by the protocol.

**Commercial H:** organization subscription and active funded budget tier; test whether a platform will pay an annual minimum before choosing per-operation pricing. Expand across agent runtimes, payment rails and chains. Domain-specific supplier performance, incident evidence and buyer workflows could defend the company; policy code alone cannot.

**First eight:** three platforms with recurring non-demo paid orders, two finance/risk owners, two wallet/payment integration leads, one procurement/security lead. Reach through public merchant/customer examples and ecosystem referrals; verify real purchase records before accepting “agent commerce” as demand. Learn whether deposit onboarding, spend control, fulfillment or demand generation is the bottleneck.

**Kill:** all prospects are demos/self-payments; incumbent policies suffice; no buyer will share a real incident or fund a controlled pilot. Keep A1's original recourse thesis conditional; do not promote a generic shared agent-account product.

### B3. Marketplace seller balances and resolution operations

**Buyer/job:** head of payments at one existing stablecoin-active marketplace vertical. Weekly journey: match buyer deposits to orders, allocate seller payables/fees, track partial delivery, adjudicate disputes under agreed rules, refund and produce seller statements. This is seller finance and resolution software, distinct from B1's operator-level payment exception queue.

**Mechanism:** order/evidence state machine, liability ledger, agreed release authority, payment adapters and recovery queue. Define who can release or reverse ledger claims; do not imply programmable escrow guarantees favorable dispute outcomes. Keep funds with an appropriate operator/escrow arrangement; legal responsibility depends on the actual custody and dispute service.

**Dependencies:** **A:** marketplace ledger/escrow workflows. **B:** tagged receipts into shared contract treasury. **C:** marketplace distribution, compliant escrow structure and compatible sender/token contracts. Bell neither establishes segregated escrow title nor enables automatic reversals.

**Competition:** [Trustless Work pricing](https://www.trustlesswork.com/pricing) advertises Stellar mainnet escrow infrastructure at 0.3% of successful releases; its [workflow](https://docs.trustlesswork.com/trustless-work/api-rest/deploy) includes approver and dispute roles. This is available infrastructure to reuse and a competitive floor, not proof the proposed vertical will pay. Modern Treasury is another ledger substitute.

**Commercial H:** subscription per marketplace plus justified resolution/workflow fees. Multichain expansion follows existing marketplace demand; seller integrations and accumulated case outcomes could compound. Without a vertical channel this is less founder-accessible than B1, because both software adoption and order distribution are missing.

**First eight:** three operators in one chosen vertical, two finance/payments leads, two dispute managers and one escrow provider. Source public marketplaces already accepting stablecoins, not hypothetical future merchants; request historical disputed-order walkthroughs. DevRel can identify providers but not supply a marketplace's purchasing authority.

**Kill:** transaction demand must be created from scratch; no two operators permit historical-case analysis; existing escrow/platform software already handles the costly workflow. Do not build a marketplace to manufacture customers for an account feature.

### B4. Customer treasury and RWA cash-servicing operations

**Buyer/job:** controller at a distributor/custodian already managing customer tokenized cash. Weekly journey: match subscriptions to eligible holder records, reconcile customer claims with aggregate assets, predict payout cash, track redemption cutoffs/acknowledgements, allocate income/fees and resolve shortfalls. This strengthens the existing R1/C2 work rather than creating another issuance dashboard.

**Mechanism:** reconciled cash/asset/liability model with issuer acknowledgements, permissions, redemption state and customer statements. Independent software can analyze records; distributing securities, holding assets, executing subscriptions or operating custody requires the relevant authorized entities and agreements. “The protocol” cannot own those obligations.

**Dependencies:** **A:** read-only cash readiness using existing accounts and provider APIs. **B:** W attribution for compatible SAC transfer paths. **C:** issuer/transfer-agent approval of the ownership model, customer eligibility, custody and redemption integrations. If individual registered holdings are required, pooling may be unsuitable. CAP-84 does not create a liquid secondary market or safe collateral.

**Competition/evidence:** the [Franklin Templeton case study](https://stellar.org/case-studies/franklin-templeton) describes established holder-management and subscription/redemption operations; it does not offer this founder a channel. [Zero Hash virtual accounts](https://docs.zerohash.com/docs/virtual-accounts) already combine customer accounting with fiat/stablecoin flows. A new entrant needs a demonstrable cross-provider cash-servicing gap.

**Commercial H:** annual software fee plus integrations/entities. Start with operational analysis, expand across issuers and chains; reliable historical reconciliations and embedded controls could create switching costs. Institutional procurement, data rights and partner access are the main delivery risks. Bell's account savings are secondary.

**First eight:** two issuer/distributor operations leads, two custodian/transfer-agent leads, two controllers already using tokenized cash, two fiat/wallet integration leads. Seek role-specific introductions through public issuer/provider ecosystems; map one real redemption into spendable cash, including every rejection and cutoff.

**Kill:** issuers reject the ownership model; no sanctioned historical-data sponsor; no recurring cash-readiness problem beyond the incumbent's service. Keep R1 a discovery priority, but do not make omnibus holdings its prerequisite.

### B5. Digital-asset authority and post-quantum migration assurance

**Buyer/job:** custody CISO/security head, with signing-infrastructure engineering and risk committee. Recurring journey: inventory authority and recovery paths, identify classical bypasses, approve migration policy, test signer compatibility, rehearse recovery, reconcile actual deployed controls and alert on later downgrades. This can become a cross-custodian assurance system; a one-off quantum report or verifier SDK is a service/feature.

**Mechanism:** authority graph plus policy-evidence engine, integration tests, staged migration gates and continuous drift monitoring. Preserve client custody initially. Model issuer/admin/guardian and consensus dependencies alongside spend signatures. KMS/HSM key recovery and payload binding are substantial engineering and organizational work.

**Dependencies:** **A:** authority inventory, existing policy monitoring and migration planning. **B:** native CAP-87 contract-enforced checks. **C:** production signer/custodian support, reviewed recovery design, institution procurement and any claimed protection beyond contract authority. PQ verification is not cryptographic privacy or a guarantee for classic account signatures.

**Competition/evidence:** Fireblocks is already exploring auditable migration across account models; [QuantumSafe](https://www.qsafe.dev/) markets adjacent signing/scanning products, with some enterprise/migration offerings upcoming. Institutional experiments establish interest, not current willingness to purchase from this founder. There is no defensible emergency quantum deadline in the evidence inspected.

**Commercial H:** paid implementation plus annual integration/authority coverage. Expand across chains and competing custody stacks, with neutral, reusable control models and accepted evidence as possible defenses. A recurring buyer need and institutional credibility are unproven; an incumbent can bundle many checks.

**First eight:** three custody security heads, two issuer security/risk leads, two signing-infrastructure engineers, one institutional security assurance/procurement lead. Start with public institutional wallet/signing integrations and targeted DevRel referrals, expecting low response rates. Ask for actual migration obligations, procurement owner, authority diagrams and current control gaps, not quantum opinions.

**Kill:** no current budget or procurement trigger; only one-time consulting demand; required classical recovery remains unrestricted while buyers demand a complete PQ security claim. This is the strongest technically distinctive Bell challenger and one of the hardest for this founder to sell now.

## 6. Relative decision: what actually changes across the four research areas

**I, qualitative judgments—not measured scores or validated company rankings.**

| Candidate | Concrete Bell effect | Demand/access constraint | Decision |
|---|---|---|---|
| C1 liquidity-aware DeFi risk and recovery | Later clock/decoder telemetry; possible account-control modules. Does not improve current exit depth, oracle quality or incident response demand. | Requires real operating sponsor and exposure data. | Keep first discovery hypothesis; no Bell-driven promotion or demotion. |
| R1 RWA execution/cash readiness | W can simplify compatible receipts; B4 is an adjacency. | Issuer/holder rights, cash access and paid operations need remain decisive. | Keep backup; no automatic liquidity improvement. |
| B1 collections/payment exceptions | Direct CAP-84 receipt-routing fit, concrete builder request, feasible read-only entry. | Incumbent coverage, actual exception cost and sender adoption unproven. | Add as the strongest new parallel discovery challenger, not a new winner. |
| C2 issuer liquidity/capital operations | Better attribution may help treasury operations. | No new market-maker inventory, fee income, funding or executable liquidity. | No liquidity/LP ranking increase. |
| A1 procurement/recourse; B2/B3 variants | Funding/admin plumbing improves. | Real purchases, delivery evidence and recourse remain the hard part. | Retain conditionally; reject generic agent-wallet pivot. |
| P1 confidential disbursements | No cryptographic privacy gain from any Bell CAP. | Production privacy, supported assets, issuer/partner acceptance unchanged. | Do not promote on Bell; avoid a W-based “private account” thesis. |
| B5 authority migration assurance | New contract verifier creates a credible enforceable-control test. | Buyer urgency, secure signers, trust and incumbent distribution. | Research challenger only; highest institutional-access hurdle. |

The rankings can differ. **H/I:** B1 has the most direct CAP-84 commercial fit and a relatively accessible read-only pilot; B5 has the clearest new cryptographic mechanism but worse institutional delivery/access risk. R1/B4 carry the strongest issuer dependency. C1 still has the broadest operational wedge in the prior evidence, but neither it nor B1 has proven this founder can win a paying customer. Bell creates no reason to rank privacy higher, and no yield source: LP fees, borrower interest, underlying asset income and incentives must still be examined separately.

The credible venture path for B1 is **multichain payment operations with deep Stellar support**, not W-address software for a small ecosystem. Stellar value would remain actual SAC/anchor integrations, correctly attributed customer funds, asset-specific controls and operational adoption. CAP-84 is public infrastructure that incumbents can copy. Defensibility must accumulate in integrations, customer processes, reliable case resolution and distribution. None is secured today.

## 7. Evidence that would change the decision

Do not wait for activation to test demand, and do not interpret elapsed time or DevRel enthusiasm as customer validation.

1. **Buyer evidence, B1:** eight role-specific interviews; at least three show recurring material exception work, two supply redacted cases, one identifies a budget owner and credible paid pilot. Proposed thresholds are H, chosen to prevent a large speculative build.
2. **Counterfactual:** trace the same customer receipt under G+memo/M, separate C, explicit shared-contract deposit and proposed W. Establish why programmable pooled receipt is necessary. If a current route solves it cheaply, the Bell-specific wedge fails.
3. **Compatibility:** after testnet activation, require end-to-end evidence from the actual intended sender, wallet, ramp and custody stack. A generic SDK unit test is insufficient evidence of distribution.
4. **Correctness/security:** offline or testnet-only later experimentation should cover duplicate events, missing/zero/max IDs, valid-but-wrong customer, indexer restart, asset mismatch, partial refund, revoked authority and pooled-asset restrictions. Compare balances and liabilities, not just successful transfer screenshots. No such deployments or transactions were performed in this research.
5. **Economics:** benchmark account lifecycle, storage/rent, ingestion, concurrent funding/spend and staff exception costs against the current operator workflow. Include review/support costs and potential losses; do not assume pooled accounts save enough to fund a company.
6. **B5 promotion gate:** three budget-owner interviews, two real authority/recovery models and a paid ongoing-assurance scope. Then test final native costs and signer interoperability after activation. Without that evidence, do not build a PQ wallet to infer demand.
7. **Speed gate:** only revisit a CAP-88-dependent payments/trading thesis after production performance and downstream usability are observed. Timestamp precision is not that evidence.

**Small implementation, only after a pilot sponsor exists:** a read-only receipts-to-liabilities exception workbench using historical operator records, with existing receipt routes and a separate W compatibility adapter for a subsequently activated testnet. Demonstrate deterministic replay, duplicate-credit prevention, unresolved-receipt quarantine and reviewed refund instructions. A roughly $5,000 slice could validate accounting/integration value for one operator; it would not finance production custody, an independent security audit, fiat partnerships or the whole company. Grant selection should follow buyer evidence, and Bell testnet activation must remain an explicit dependency. No application is proposed or submitted here.

**Recommendation:** retain the prior company discovery order; add B1 to the next buyer interviews and let measured operational pain decide whether it overtakes C1/R1. The missing asset is a paying operational sponsor with records, not another protocol capability.
