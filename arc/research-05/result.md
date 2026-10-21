# Research 05: Product-first reassessment — paid-tool procurement

## Original result

Source: this conversation, message timestamp `2026-10-21T08:30:34.364Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

**My recommendation is a buyer-side workbench for paid agent tools: discover services, test them on your own tasks, compare actual cost and quality, then run the chosen services under a controlled USDC budget.** Start with onchain data services used by Arc developers—not a general agent marketplace.

The strongest alternative is **a forecasting league for humans and agents**, built around objectively measurable onchain outcomes, transparent scoring, and sponsor-funded USDC prizes. It should compete on useful forecasts and community participation, rather than trying to bootstrap another prediction exchange.

Neither opportunity is proven. They are the best product hypotheses from this scan because they create a recurring loop and make useful connections between existing Arc infrastructure. I would retire the earlier generic escrow, invoice, splitter, and privacy-wrapper recommendations.

Research checked **October 21, 2026**. Below, **verified** means supported by inspected documentation, repositories, or local tool output; **project claim** means the team describes it but I have not independently demonstrated it; **hypothesis** means my proposed opportunity.

## What changed my view

Three findings matter most.

**Arc has more product infrastructure than an “empty ecosystem” narrative suggests.** Its official product already includes wallet onboarding, asset discovery, swaps, borrowing, earning, and agent-wallet management. A general Arc dashboard, yield directory, or bounded agent wallet would compete directly with the platform. [Arc Portal documentation](https://help.arc.io/support_arc/en/arc-portal-faqs?id=arc_article_view&sysparm_article=KB0011405)

**Several apparently original agent ideas already have close Arc predecessors.** OpenBook handles paid data with freshness conditions; Verdikt proposes delivery verification and refunds; ACR studies agent-compute prices; NanoCrawl combines paid browsing with a privacy-pool-funded wallet. The opportunity is not “agents can pay each other.” It is helping a buyer reliably decide **what deserves payment and continued use**.

**A prediction-market interface is substantially easier than a credible prediction product.** Circle’s own starter includes an AMM and market lifecycle, but its documented setup uses freely mintable ARCT collateral, mock oracle infrastructure, and static prices for some displayed markets. It is a useful engineering sample, not evidence that production resolution and liquidity are solved. [Source repository](https://github.com/circlefin/arc-prediction-markets)

## Arc reality check and product map

| Area | What the evidence supports | Product implication |
|---|---|---|
| Network and USDC | Mainnet is live; USDC gas, EVM execution, deterministic finality. Published mainnet addresses include USDC, EURC, CCTP, Gateway and StableFX. [Network announcement](https://www.arc.io/blog/arc-economic-os-internet), [addresses](https://docs.arc.io/arc/references/contract-addresses) | Small USDC workflows are natural. Fast local finality does not make external data, bridges, or withdrawals instantaneous. |
| Wallets and agents | Circle Agent Wallets explicitly support Arc mainnet and testnet, with spending policies. Portal already exposes agent funding and management. [Supported networks](https://developers.circle.com/agent-stack/agent-wallets/supported-blockchains), [Agent Wallets](https://developers.circle.com/agent-stack/agent-wallets) | Reuse wallet controls. A spending-limit screen alone is not a differentiated product. |
| Crosschain payments | CCTP and Gateway have mainnet deployments. Gateway provides a chain-abstracted balance; supported routes and assets remain product-specific. [Gateway](https://developers.circle.com/gateway), [deployment registry](https://docs.arc.io/arc/references/contract-addresses) | Users can arrive from elsewhere. Avoid making “bridge to Arc” the first product benefit. |
| SDKs and APIs | App Kits covers financial actions; Earn Kit integrates Morpho vaults. Public examples still mix testnet configurations with available production products. [App Kits](https://www.arc.io/app-kits), [Earn Kit](https://www.arc.io/blog/how-earn-kit-keeps-usdc-in-arc-apps-productive-with-morpho-vaults) | Verify the particular adapter, asset, account permissions, and network—not just the SDK’s existence. |
| Trading, lending and assets | Official launch materials identify Uniswap, Aave, Morpho and other integrations. Tokenized assets may impose eligibility restrictions. | Neither “a DEX” nor “USDC yield” is an established gap. A listing is not evidence of deep liquidity in every market. |
| Consumer launches | TOLLY describes mainnet token launches, locked liquidity, creator fees and trading. Argus also presents launch/discovery functionality. [TOLLY](https://tollylabs.com/guide), [Argus](https://argus.world/docs) | A pons-style launch port is already crowded at the feature level. These product claims do not establish sustained trader demand. |
| Commerce and subscriptions | Strimz, SubscriptonArc and ArcPay present payments/subscription products. Production maturity varies; I did not establish recurring customer usage. [Strimz](https://www.strimz.finance/), [SubscriptonArc](https://www.subscriptonarc.com/), [ArcPay listing](https://partners.circle.com/partner/arcpay-systems) | “Stripe on Arc” is not a defensible gap claim. |
| Prediction and agent applications | Circle’s prediction starter, Justify, OpenBook, ACR, Verdikt and NanoCrawl cover considerable ground, largely through prototypes or testnet submissions. | There is room to improve full workflows, but not to claim these categories are absent. |
| Privacy | The current APS documentation explicitly says privacy features are **not yet available**. ERC-8183’s reference address is listed as testnet; ERC-8004 has mainnet entries. [Privacy status](https://docs.arc.io/arc/concepts/opt-in-privacy), [addresses](https://docs.arc.io/arc/references/contract-addresses) | No proposal below depends on native confidential execution or assumes a production commerce contract from a testnet listing. |

**Search scope and gap confidence:** official Arc/Circle pages and documentation, ETHGlobal showcases, linked repositories and demo endpoints, and named independent Arc products. This supports **moderate confidence in workflow opportunities**, but **low confidence in ecosystem-wide absence**. I did not obtain an exhaustive, independently verified inventory of active apps or paying users.

### What the Studio inspection actually established

I ran the requested read-only commands:

- `arc-studio whoami`: authentication failed in this execution environment.
- `arc-studio agent-guide`: available; describes hosted code generation, contract testing/auditing, testnet deployment, artifact export, and an embedded preview.
- `arc-studio skills --json`: returned `agent-standards`, `chainlink`, `circle-agent-wallet`, `ens`, `morpho`, `polymarket`, `pyth`, and `uniswap`.

The distinction matters: **the Polymarket skill promises displaying market data; it does not promise deploying a prediction exchange.** The Uniswap skill says Arc mainnet, but that does not override Studio’s terms.

I discovered no connected Arc Studio or Circle MCP tools in this session. Circle does publish an [open-source skills collection](https://github.com/circlefin/skills). Build-time skills/MCP tools are not automatically runtime services for the finished app. Current Arc documentation also directs developers to its Arc-specific Foundry tooling. [Arc Foundry](https://docs.arc.io/arc/tutorials/install-arc-foundry)

Studio’s September 14 terms explicitly place mainnet deployment and production operation outside Studio, using the builder’s own tooling and credentials. The CLI’s embedded preview is not public production hosting. **Generating and testing in Studio, then independently deploying and hosting, is consistent with those terms; organizer acceptance of that precise workflow remains unconfirmed.** The official competition page could not be retrieved in this pass. [Studio terms](https://studio.arc.io/terms-of-use), [competition page](https://dorahacks.io/hackathon/arc-microgrants-2/detail)

No apps were created or inspected behind authentication, and no transactions were sent.

## What to learn from existing projects

Awards below are taken from ETHGlobal’s displayed award entries. A repository establishes inspectable implementation material, not security or adoption.

| Reference | What was actually evidenced | Lesson for an Arc product |
|---|---|---|
| **[OpenBook](https://ethglobal.com/showcase/openbook-8ngw6)** — Arc agent-stack prize | Repository contains buyer agents, sellers, contracts, MCP and indexing. Architecture uses server-signed payload hashes and block metadata. Submission describes testnet components. [Architecture](https://github.com/Aliserag/OpenBook/blob/main/docs/architecture.md) | Freshness conditions are useful. A signed timestamp does not prove factual accuracy or complete data. |
| **[ACR](https://ethglobal.com/showcase/acr-sgdjr)** — Arc Best DeFi or Agentic Application | Substantial source repository; compute-price estimation, payment analysis and a trading experiment. Current README explicitly discusses batching and wash-trade contamination. [Source](https://github.com/kaustubh76/ACR---Arc-Compute-Rate) | Measure economic outcomes carefully; payment volume alone is a poor reputation signal. |
| **[NanoCrawl](https://ethglobal.com/showcase/nanocrawl-egxyi)** — Arc chain-abstraction first place | Describes MCP browsing, publisher middleware, nanopayments, Arc testnet and Base Sepolia privacy funding. Linked repository inspected; live endpoint was inaccessible here. | A complete buyer-and-seller loop is stronger than a payment primitive. Burner wallets do not justify “no trace” claims. |
| **[Verdikt](https://ethglobal.com/showcase/verdikt-mi2xq)** — no award verified | x402 service delivery/refund prototype. Submission discloses simulated CRE workflow execution rather than enabled production deployment. | Testable service conditions matter; “TEE verified” must match the actual deployed execution path. |
| **[Justify](https://ethglobal.com/showcase/justify-pob50)** — World first place, **not an Arc prize** | Arc-testnet creator markets, FPMM contracts, social distribution and agent participation. Price resolution references Sepolia feeds; subjective questions use an LLM. | Creator distribution is promising. An LLM’s explanation is not a robust financial oracle. |
| **[CrossMeter](https://ethglobal.com/showcase/crossmeter-w9zay)** — Circle multichain payments second place, New York 2025 | Billing/API hackathon implementation; no production adoption established. | Chain abstraction belongs inside a business workflow, not as the entire proposition. |
| **[Autonome](https://ethglobal.com/showcase/autonome-d8cxe)** — New Delhi 2025 finalist; Polygon x402 first place | Publisher/agent payment and identity prototype with source. | Paid web access predates the Arc implementations; distribution to publishers remains difficult. |
| **[Proofs of Inference](https://ethglobal.com/showcase/proofs-of-inference-6rug4)** — Protocol Labs and Hedera prizes | EZKL circuits, backend/frontend/contracts; repository lists Flow and Hedera **testnet** addresses. [Source](https://github.com/markhovs/proofs-of-inference) | Proving a specific small-model computation is credible; proving useful general agent judgment is a different problem. |
| **[Virtuals ACP](https://github.com/Virtual-Protocol/acp-cli)** | Current implementation documents discovery, paid jobs, subscriptions, wallet policies and mainnet/testnet separation. Usage was not independently quantified. | A generic agent marketplace with escrow and reputation would face an existing full workflow. |
| **[Metaculus FutureEval](https://www.metaculus.com/questions/38928/)** | Operating human/agent forecasting program, scoring rules, bot resources and published results. | Accuracy, repeat participation and evaluation are viable product loops without a trading order book. |
| **[CoW Protocol](https://docs.cow.fi/cow-protocol/concepts/introduction/fair-combinatorial-auction)** | Production protocol documentation for solver competition and batch auctions. | Improve execution quality, not merely swap UI. Solver participation and order flow are essential dependencies. |
| **[DeFi Saver](https://help.defisaver.com/general/compatibility/automation-compatibility)** | Existing protocol-specific automation and protection features across supported networks. | Exit automation is useful, but “automatic stop-loss on Arc” is a port unless the workflow improves materially. |
| **[Blend on Stellar](https://stellar.org/solutions/borrowing-and-lending)** | Operating lending product with wallet integrations; Stellar reports supplied capital, not revenue or unique customers. | Distribution through an everyday wallet can matter more than a new lending mechanism. |
| **[Kamino](https://kamino.com/markets)** — Solana | Integrated lending, borrowing and strategy interface. | Users benefit from managing a position across its lifecycle, not collecting disconnected DeFi buttons. |

For Avalanche, AvaxHook’s supplied documentation was inaccessible in this pass, so I cannot responsibly upgrade its claims into verified functionality. The accessible [pons documentation](https://docs.ponsfamily.com/) does demonstrate a coherent launch → discovery → trading → creator-revenue loop. That product coherence is worth borrowing; its token mechanics are not the opportunity.

## Ten product directions, filtered

These are hypotheses, not claims of unoccupied markets.

| Direction | First user and complete recurring loop | Arc advantage, smallest credible product, and verdict |
|---|---|---|
| **1. Paid-tool procurement workbench** | Agent developer selects a task, trials providers, compares delivered results and total spend, approves a route, monitors regressions, switches providers. | USDC purchasing and budgets across independent services. Start with onchain data APIs, buyer-defined tests and recurring routing. **Lead candidate; demand must survive comparison with Langfuse plus existing gateways.** |
| **2. Forecast leagues** | Community/operator publishes questions; humans and bots forecast, update, discuss evidence, receive scores and prizes, return next round. | Arc-native observations and transparent USDC funding. Start with one league and objective questions. **Strong alternative; Metaculus is a formidable competitor.** |
| **3. USDC exit-readiness console** | Depositor connects positions, sees realistic withdrawal capacity and changing exposures, sets alerts, rehearses an exit, approves action. | Integrates Arc lending, swaps and eventual crosschain withdrawal. Start with two vault integrations and one executable exit path. **Useful; must exceed Portal and DeFi Saver.** |
| **4. Confidential service procurement** | Team requests quotes privately, compares signed offers, selects a supplier, pays, retains an audit trail, repeats procurement. | USDC settlement with confidential commercial terms. Start with one service category and encrypted bids. **Distinct, but confidentiality demand and seller participation are unproven.** |
| **5. Community prediction exchange** | Creator brings an audience, launches markets, seeds liquidity, moderates resolution, earns fees and repeats. | Familiar USDC balances and rapid settlement. Requires market contracts, oracle, indexing and market makers. **Reject initially: Justify already targets this, while liquidity and adjudication dominate.** |
| **6. Forecast-resolution newsroom** | Market operators define rules, collect evidence, publish proposed outcomes, handle challenges and maintain a resolution record. | Arc could settle service fees and bonds. Small version is an evidence desk for one market vertical. **Interesting service, but Arc is a weak necessity and distribution depends on market operators.** |
| **7. Community group-buy exchange** | Fans discover a creator offer, commit demand, unlock quantity pricing, receive goods/access, resolve delivery issues and reorder. | USDC commitments and transparent thresholds. Needs order management, inventory/fulfilment and customer support. **Do not recommend without a creator channel; otherwise generic escrow in disguise.** |
| **8. Stablecoin FX execution desk for small teams** | User schedules conversions, compares quotes, approves limits, receives settlement and reconciles repeated payments. | EURC/USDC and StableFX integration. Requires accessible counterparties and a meaningful retail/SMB route. **Crowded; not a gap simply because institutional FX exists behind different access rules.** |
| **9. Crosschain liquidity inventory manager** | App operator forecasts payout needs, watches balances, moves inventory, tracks pending transfers and replenishes. | CCTP/Gateway are directly relevant. Start with one operator’s recurring routes. **Useful but too close to existing treasury tooling without a specific operational pain.** |
| **10. Verifiable computation purchasing desk** | Developer submits a supported computation, compares provers, obtains a proof, verifies and pays, then repeats. | USDC settlement for machine services. Requires a narrow supported workload and verifier contracts. **Reject as a broad marketplace; proof availability is not evidence of a buyer problem.** |

The strongest rejected idea is the community prediction exchange. It could be entertaining and shareable, but **USDC gas does not supply liquidity, a trustworthy resolution process, or an audience**.

## Deeper assessment of the best four

### 1. Paid-tool procurement workbench — recommended

**First user:** an independent developer operating an agent that repeatedly buys onchain data: token metadata, indexed events, historical queries, or risk signals.

Today that developer stitches together vendor documentation, API keys, payment interfaces, tracing, and hand-written checks. The proposed product answers a narrower question: **“Which paid tool performs my particular job reliably, and what does each successful result actually cost?”**

**User journey**

1. Connect a wallet and import a small set of representative tasks.
2. Select compatible providers and define measurable requirements.
3. Trial them under a capped budget.
4. Inspect outputs, failures, latency, payment receipts and cost per accepted result.
5. Approve a provider and fallback policy.
6. Monitor production results; periodically rerun comparisons.

**Architecture:** browser console and MCP interface → policy-controlled buyer runtime → provider adapters → evaluator and receipt store → payment/settlement adapter.

Use Circle wallet limits for basic financial control. A narrowly scoped contract can manage explicit service reservations, expiry and buyer-approved settlement where providers support those terms. Ordinary x402 prepayment must remain visibly distinct: it does **not** automatically become refundable because our evaluator dislikes the output.

The smallest complete version needs one category, several genuinely interchangeable providers, deterministic checks, a recurring workflow and an exportable purchase history. It does not need a token, public reputation score or universal marketplace.

**Closest competitors:** OpenBook, Virtuals ACP and Langfuse. OpenBook is already close on delivery conditions. ACP already provides service commerce. Langfuse already offers evaluations, datasets, tracing and production alerts—so “Langfuse with a wallet” is insufficient. [Langfuse capabilities](https://langfuse.com/resources/engineering/clarifications)

**Differentiation hypothesis:** buyer-owned acceptance tests that influence future purchasing, combined with actual payment accounting across independent vendors. Integrate existing observability tools rather than rebuild them.

**Why Arc:** low-friction dollar budgets, agent-wallet support and crosschain funding make small experimental purchases practical. This is an ecosystem advantage, not an exclusive technical moat; useful providers should not be forced to relocate to Arc.

**Main failure modes:** too few independent paid providers; evaluation gaming; malicious tool responses; providers changing output semantics; buyers preferring conventional subscriptions. A provider signature proves who asserted a result—not its truth. An LLM judge should not have unilateral authority over significant funds.

**Evidence needed:** developers already making repeated paid tool calls who will import their own tasks and use the comparison to change purchasing decisions.

### 2. Forecast leagues — strong alternative

**First user:** an Arc community operator or protocol research group that wants recurring participation and useful forecasts about measurable ecosystem outcomes.

Examples include future borrowing utilization, execution spreads for a fixed trade size, or whether a specified service meets an agreed availability threshold. Avoid poorly defined “will this project succeed?” questions.

**Loop:** join a league → submit a probability and rationale → revise before cutoff → inspect resolution evidence → receive a calibrated score → compare against peers and agents → return for the next round.

A league can be sponsor-funded without requiring participants to buy positions or seed an AMM. This removes the initial liquidity problem, although it does not automatically remove jurisdiction-specific contest obligations.

**Architecture:** question registry with immutable rules; timestamped forecasts or salted commitments; reproducible observation pipeline; transparent scoring service; challengeable result publication; USDC prize distribution. Start with a disclosed resolver and clear cancellation rules rather than claiming trustless resolution.

**Closest competitors:** Metaculus FutureEval, Manifold and Justify. The proposed wedge is **Arc-specific operational forecasting with inspectable onchain evidence and portable participant histories**. Human-versus-agent rankings alone are already well explored.

**Why Arc:** the subjects, data sources, participants and rewards can share one ecosystem. Arc settlement supports transparent prize funding, but most forecasting computation belongs offchain.

**Smallest complete product:** one recurring league, a limited question template set, submissions, discussion, scoring, results and funded rewards.

**Failure modes:** questions nobody needs answered; self-influenced outcomes; reward farming; agents copying each other; community activity disappearing when subsidies stop. Proper scoring also does not make every prize-allocation rule incentive-compatible.

This becomes the recommendation if a real community commits to recurring participation and identifies decisions the forecasts will inform.

### 3. USDC exit-readiness console

**First user:** a small team or individual holding meaningful USDC positions across Arc vaults who needs to know how much is withdrawable—not just the displayed balance or APY.

The recurring job is: **“What changed in my exposure, and can I get my money out through the route I expect?”**

**Loop:** connect positions → map underlying exposures and available liquidity → set notifications → inspect proposed parameter changes → simulate withdrawal → approve an exit or maintain the position.

**Architecture:** protocol adapters, event indexer, historical snapshots, withdrawal simulations and a transaction composer. Optional automation must be limited by approved destinations, maximum slippage and allowed actions.

**Closest competitors:** Arc Portal, DeFi Saver and Kamino’s integrated risk interface. Portal already warns that withdrawals depend on liquidity and that removed vaults may require direct protocol access. That is a concrete product-design issue, not proof of willingness to pay. [Portal withdrawal documentation](https://help.arc.io/support_arc/en/arc-portal-faqs?id=arc_article_view&sysparm_article=KB0011405)

**Arc advantage:** a focused map of Arc assets, vaults and exit routes, with USDC remaining the accounting unit. The valuable differentiation would be position-specific explanations and executable recovery paths—not another APY ranking.

**Smallest complete product:** support two actual vault types, explain their withdrawal constraints, detect material changes and prepare a user-approved exit.

**Failure modes:** users interpret monitoring as insurance; liquidity disappears between simulation and execution; alerts arrive too late; protocol upgrades break adapters. No automation can promise an exit when the underlying market has no liquidity.

### 4. Confidential service procurement

**First user:** a trading or research team seeking quotes for data or compute without publicly advertising its intended strategy or budget.

**Loop:** privately request offers → compare price and terms → select → receive service → settle → retain an auditor-readable procurement record.

**Architecture:** encrypted requests and bids, signed quote commitments, offchain selection, minimal onchain settlement. A later ZK circuit could prove that selection followed a specified rule over committed bids, but only if the bid set is complete and the rule is precisely defined.

**Exact privacy guarantee:** request contents and losing quotes can be hidden from the public and other bidders. The chosen provider sees the information necessary to fulfil the order. The coordinator sees plaintext unless client-side selection or a stronger architecture removes that access.

**Still public on Arc:** ordinary settlement amounts, payer and recipient addresses, transaction timing, gas payer and contract events. RPC and service providers can observe network metadata. This is **commercial-term confidentiality, not anonymous purchasing**.

ZK verifies a predicate; it does not hide an ordinary USDC transfer. A TEE introduces hardware and attestation trust. MPC distributes trust among operators. FHE enables computation over encrypted inputs but adds a different infrastructure burden. Stealth addresses alone do not defeat timing and funding correlation.

**Closest alternatives:** private RFQ systems, Virtuals’ service negotiation and confidential-computation networks. Its advantage over encrypted email plus payment is not yet established. **Keep it as a research option, not the primary build.**

## Decision and first experiment

**Build toward the paid-tool procurement workbench, subject to one demand test.** It has a clear potential role in Arc: helping developers consume real services responsibly, rather than producing more listings, agent registrations or synthetic transactions.

Its strongest objection is substantial: **there may not yet be enough genuine paid-tool purchasing to justify a separate product**, and Langfuse plus existing commerce tooling may already be adequate.

Before implementing anything, run a **buyer-workflow comparison study**:

- Recruit five developers already using paid data tools; ask for representative, non-sensitive tasks and their current purchasing workflow.
- Identify three substitutable providers in one category.
- Design a static comparison showing delivered result, acceptance test, latency, total USDC cost, failure handling and repeat-purchase controls.
- Ask each developer to make a concrete provider decision and identify what they would replace in their current setup.

The pass condition is not enthusiasm: **at least three should want to bring their own tasks back repeatedly, and the comparison should change an actual provider or spending decision.** If users mainly want better tracing, integrate with an incumbent. If independent providers and repeat buyers cannot be found, stop.

**Choose forecast leagues instead** if an existing Arc community commits to repeat rounds and can name useful, objectively resolvable questions. That would be stronger evidence than theoretical demand for agent commerce.

No experiment, implementation, deployment or payment has been performed.
