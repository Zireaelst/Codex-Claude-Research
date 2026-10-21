# Agentic commerce: fresh company search and prior-art audit

Checked 20 October 2026. Research only: no outreach, purchases, signing, deployment, or grant investigation. This reopens the company choice; the earlier payout-operations recommendation is not a premise.

Labels: **Fact** means an observable source or published product behavior, not independent verification of every implementation claim. **Vendor** means the author's implementation, adoption or economic claim. **Inference** means our interpretation. **Hypothesis** means proposed company, price or customer behavior requiring interviews and experiments. Public code and a transaction are not evidence of unrelated paying demand.

## Decision-changing findings

1. The three requested projects are substantial prior art, but the verified organizer designation is **finalist**, not a ranked overall win. Omamori and Yohaku appear in the [Tokyo closing ceremony](https://streameth.org/ethglobal/y/ethglobal-tokyo-2026); OnchainRouter appears in the [ETHOnline finale](https://streameth.org/ethglobal/y/ethonline-2026). Their current showcase pages do not display award badges. The recordings have imperfect automatic transcripts; the matching project demos establish identification. Do not infer a sponsor prize from finalist status.
2. All three demonstrate financial execution on **testnets**. None establishes an operating company with unrelated recurring paying buyers. Yohaku explicitly discloses generated requests and zero fee collection. OnchainRouter's author says all six tools are his. Reading real mainnet financial data does not make testnet payments mainnet commerce.
3. Generic budget/approval/audit wallets and merchant payment/refund dashboards are occupied. [Ramp](https://agents.ramp.com/) explicitly sells agent identity, owner, budget, merchant restrictions, human approvals, cards/MPP/x402 and accounting context. [Stripe](https://docs.stripe.com/payments/machine) already offers machine-payment refunds, reconciliation, reporting, fiat settlement and Connect. A company must own a recurring procurement or fulfillment outcome, rather than add a wallet permission screen.
4. There is real paid demand for human data and evaluation, but [Prolific](https://www.prolific.com/pricing), its [task API](https://researcher-help.prolific.com/en/articles/445138-key-features-of-ai-task-builder), and [managed expert evaluation](https://www.prolific.com/resources/building-enterprise-ai-a-guide-to-working-with-human-experts) already address much of Yohaku's commercial direction. World personhood does not verify expertise, truth, buyer need, or legal recourse.
5. Stellar is a plausible optional treasury/reward rail, but no verified evidence here shows buyers require it for agent procurement. Support existing card/API purchases and Base/Solana/Tempo where counterparties already transact; do not force a chain migration to manufacture differentiation.

## Requested projects: architecture, source, awards and maturity

### Omamoris / Omamori

**Sources:** [showcase](https://ethglobal.com/showcase/omamoris-rn3nc), [public yakusoku repository](https://github.com/juanmaagd/yakusoku), [organizer finale](https://streameth.org/ethglobal/y/ethglobal-tokyo-2026), [founder's finalist statement](https://www.linkedin.com/posts/juan-manuel-gomez-omil_we-were-finalists-at-ethglobal-tokyo-2026-activity-7512864188730441728-JRV8).

**Fact/vendor:** Tokyo 2026 finalist. Per-user smart accounts spend USDC on **Base Sepolia**. A human approves task intent outside the agent context; a presign firewall re-fetches merchant requirements, checks budget/expiry/network and merchant binding, screens with Intercepta, checks semantics with Jev, and can request World step-up. EIP-3009/EIP-1271 signing supports a public facilitator. The agent lacks the signer key. Demo merchants and purchases demonstrate technical execution, not organic external commerce.

**Source inspection:** Public TypeScript/Bun monorepo with firewall, merchant, screening, semantic-check, World approval, provenance and SQLite state modules; MCP tools, Astro UI, Foundry account/factory, shared schemas and read-only verifier. The README reports tests and onchain purchases. We read repository README/layout and showcase, did not clone successfully, run tests, inspect all source lines, audit cryptography, or independently reconcile transaction hashes. Commit counts are activity, not adoption. Intercepta's Sepolia-to-mainnet token mapping and World sandbox flow are dependencies, not production assurances.

**Implication:** A proposed “semantic spend authorization” startup must explain what Omamori plus a production policy wallet cannot deliver. The missing business may be accepted deliverables, seller contracts and remediation—not another inference-based allow/deny gate.

### Yohaku

**Sources:** [showcase](https://ethglobal.com/showcase/yohaku-m2d72), [public repository](https://github.com/kou-uni/ethglobal-tokyo2026-uni), [organizer finale](https://streameth.org/ethglobal/y/ethglobal-tokyo-2026).

**Fact/vendor:** Tokyo finalist. Agents request first-hand human insight; a deterministic policy routes auto/human/deny and constrains attention. The model can ask/drop rather than grant permission. Financial settlement uses **Base Sepolia** USDC, while ENS delegation is on **Ethereum Sepolia**. The README describes generated requests, emulated buyers and two test-token rewards, not incoming customer demand. Routing fees were not collected. Curvegrid NEO/MultiBaas is proposed, not implemented. Later World credential work does not change the settlement network.

**Source limitations:** README/layout and linked evidence were inspected, not a line-by-line audit; author test counts changed between showcase and repository and are not our verification. The author itself records sandbox freshness caveats and distinction between personhood, truthful experience and ownership. Do not call it production-ready or treat a World credential as a truth oracle.

**Implication:** Human-task routing, user attention policy, reward settlement and an agent inbox are already demonstrated. A company must recruit a defensible supply of qualified people and deliver measurable buyer quality/latency/rights, not simply pay verified humans.

### OnchainRouter

**Sources:** [showcase](https://ethglobal.com/showcase/onchainrouter-8r4jm), [public web3xDev repository](https://github.com/web3xDev/onchainrouter), [organizer finale](https://streameth.org/ethglobal/y/ethonline-2026).

**Fact/vendor:** ETHOnline 2026 finalist. Six analytical tools normalize Graph data; advertised mainnet protocol coverage refers to inputs. Payments are **Hedera testnet HBAR** through Blocky402 and **Arc testnet USDC** through Circle Gateway. Author says all six tools are his; direct author payouts and zero router commission do not establish a marketplace's unit economics. HTTP/MCP errors prevent settlement; a successful response is not a guarantee that its content is correct. Mainnet was described as coming soon, not demonstrated by this evidence.

**Architecture/source:** Registry defines schema, execution and payout; relay handles already-paid endpoints; HTTP and MCP share tool execution; a client wallet signs payments. Arc uses developer-controlled Circle wallet/Gateway funding. README and architecture descriptions inspected; no tests or independent runtime verification. Distinguish this `onchainrouter.io` / `web3xDev` project from the separate `OnchainRouter` GitHub organization and `onchainrouter.dev` inference router.

**Implication:** Listing paid tools, wrapping APIs, multi-rail payment routing and refusing obvious errors are baseline prior art. Recovery must address acceptance criteria, partial/late/incorrect work, repeated billing and seller solvency to support a full business.

## Broader hackathon prior art

These are exact displayed sponsor labels, distinct from overall finalist selection. Architecture is author-reported; none below was independently established as a company with recurring third-party revenue.

| Project | Verified displayed recognition | What already exists / maturity boundary |
|---|---|---|
| [Lifeline](https://ethglobal.com/showcase/lifeline-mygz6) | “Sui - DeFi, Payments, Agents 3rd place”; “World - Best Use of World ID for Agents” | Human-associated agent credit, screening, step-up, repayment; Sui Move explicitly lends **testnet USDC**. Personhood is neither underwriting nor legally collectible debt. |
| [BitRouter](https://ethglobal.com/showcase/bitrouter-mu1z5) | “Sui - Best product integrating Walrus for storage”; “Arc - Arc Continuity Track: Extend the Arc Ecosystem 2nd place” | Rust inference routing, x402/MPP, encrypted Walrus memory; **Arc testnet** payments. Author reports payments landing while backend failed to return responses: real technical failure mode, not customer-demand evidence. |
| [Turnstile](https://ethglobal.com/showcase/turnstile-ovks1) | “Hedera - AI & Agentic Payments on Hedera”; “The Graph - Best AI Tooling or AI Use Case with The Graph (From Scratch) 2nd place” | Paid analytical market, ENSv2 Sepolia offers, wallet quorum controls, HCS receipts and Arc batching. CRE enclave is **simulated** because access gated. Author says 197 registrations but only one readable price: identity count is not seller supply. |
| [Pay402](https://ethglobal.com/showcase/pay402-zjrbf) | “Sui - Notable Projects” | Sponsored Sui testnet payments and merchant invoice/settlement modes. Not a first-place award or proof that other chains cannot do equivalent flows. |
| [Reckn](https://ethglobal.com/showcase/reckn-47t6m) | “Uniswap Foundation - Best Uniswap Stack Contribution 3rd place” | Escrow with deterministic re-execution before release. Bounded reproducibility is meaningful; it does not prove arbitrary deliverable truth or real-world fulfillment. No mainnet commerce established here. |
| [Unwind](https://ethglobal.com/showcase/unwind-pqp3a) | “WalletConnect - Best use of WalletConnect Pay 2nd place” | Merchant POS escrow/refunds; author reports Base mainnet plus Arc testnet deployments. A deployed vault does not prove merchant adoption or refund economics. |
| [YourTurn 2.0](https://ethglobal.com/showcase/yourturn-2-0-od7iw) | ETHOnline continuity project; earlier Hedera prize stated by author, not reclassified here | Booking-specific recovery mandates, expiry/nonce, user approval and backend executor. Hardware signature is not the Hedera settlement transaction. Vertical booking recovery has prior art. |
| [Interact](https://ethglobal.com/showcase/interact-9qtx7) | “Flare Network - BONUS TRACK: external data source or cross chain application” | Agent browser purchasing plus escrow, verification, delayed release and timeout refunds. Prototype; named retail sites in a demo are not real merchant integrations. |
| [Threeer](https://ethglobal.com/showcase/threeer-2xgz4) | “Phala Network - Best use of Agent Contract 1st place”; “Worldcoin - Pool Prize” | Agent/human service tasks and bounty settlement. AI quality judgment remains an oracle/commercial dispute problem. |
| [Assay](https://ethglobal.com/showcase/assay-qiz12) | “Bazantic - Best Recipe that uses EthGlobal Hackathon Sponsor APIs 3rd place” displayed; no exhaustive award assertion | Policy-controlled paid assessments and receipts on **Hedera testnet, Arc testnet, Base Sepolia**. |

For Solana, [Amiko x402](https://github.com/HCF-STUDIOS/amiko-x402) claims “Best Trustless Agent” at a Solana x402 hackathon; independent organizer corroboration was not established in this pass, so do not present that as an ETHGlobal award. [Solana MPP SDK](https://github.com/sendaifun/solana-mpp) implements session funding/closing and server refunds; inspect server key/custody assumptions rather than claiming all MPP sessions are fully self-custodial.

## Production alternatives and demand evidence

| Product/category | Public fact or vendor claim | Consequence |
|---|---|---|
| [Ramp agent finance](https://agents.ramp.com/), [tools reference](https://agents.ramp.com/docs/reference/agent-tools) | Identity/owner, budget, merchant restrictions, human approver; cards/MPP/x402; receipts and accounting. Bill tools respect configured approval/release behavior. | Generic approval-and-receipt procurement is already inside a large finance suite. Its overall spend volume is not agentic spend volume. |
| [Stripe machine payments](https://docs.stripe.com/payments/machine) | MPP cards and stablecoins; x402 stablecoins. Refunds, reconciliation, fiat settlement and Connect. Current table: Tempo/Solana MPP, Base x402. Access restrictions and approval apply. Minimums: cards $0.50, stablecoin settlement $0.01; sessions meter below a cent. | Neither a refund button nor an x402 gateway is whitespace. A startup needs service-specific commercial responsibility and buyer workflow. |
| [Privy policy docs](https://docs.privy.io/security/wallet-infrastructure/policy-and-controls), [agent wallets](https://www.privy.io/agent-wallets) | Keys/quorums, policies, recipient/contract limits and approvals; both user and service-controlled arrangements. Some limits require off-enclave simulation. Supports EVM and Solana. | Calling a wallet “noncustodial” does not settle who controls this specific deployment. Programmatic policy is infrastructure, not a company moat. |
| [Coinbase agent wallets](https://docs.cdp.coinbase.com/agentic-wallet/welcome), [product](https://www.coinbase.com/en-ca/developer-platform/products/agentic-wallets) | CLI and MCP discover/pay x402; enclave keys and screening vendor claims. | An MCP wallet plus spend caps is occupied. No assumption that advertised infrastructure volume equals useful agent purchases. |
| [Crossmint September 17 announcement](https://www.crossmint.com/announcement/universal-vault-for-agent-cards) | Card vault live; scoped credentials/expiration/spend limits; cards, x402 and MPP. Agent Checkout was **pre-release** in that announcement. | Cross-rail checkout infrastructure has funded incumbents. Card recovery/chargeback rights differ from stablecoin authorizations. |
| [Parallel MPP](https://parallel.ai/blog/tempo-stripe-mpp), [dual-rail implementation](https://parallel.ai/blog/parallel-mpp-dev?trk=article-ssr-frontend-pulse_little-text-block) | Live paid search/extract/task APIs on Tempo MPP and Base x402. Published search/extract prices $0.01, extract per URL. No verified recurring MPP buyer count disclosed. | Real available supply, useful interview prospect; availability is not measured agent-channel demand. |
| [Virtuals Butler](https://whitepaper.virtuals.io/info-hub/virgens-hub/butler-quick-start-guide), [EconomyOS](https://os.virtuals.io/) | Base-mainnet USDC wallet, discovery/negotiation/escrow/job execution; beta and ecosystem metrics vendor-reported. Subsidies/credits and token trading must be separated from service purchases. | Agent service marketplace/escrow is established competitive prior art. Public aggregate jobs/revenue need ownership and incentive analysis. |
| [Prolific pricing](https://www.prolific.com/pricing), [AI task API](https://researcher-help.prolific.com/en/articles/445138-key-features-of-ai-task-builder), [Shovels case](https://www.prolific.com/resources/building-enterprise-ai-a-guide-to-working-with-human-experts) | Corporate platform fee 42.8% of participant reward; published minimum/recommended compensation. API plus recruitment/quality/managed services. Named Shovels example: domain professionals needed for construction permit classification. | Stronger paid-job evidence than testnet transfers, but much tougher competition for a human-task startup. The unmet wedge must be specific domain/locale/SLA/data rights. |
| [User Interviews pricing](https://www.userinterviews.com/pricing?source=navbarPricingResearcher) | Research recruitment, workspaces, incentives, panel; current incentive processing 3%. Session price not reliably exposed in accessible page. | Do not reuse stale $30/$70 recruitment numbers as current pricing. Recruiting a verified panel is an established business. |

**Independent measurement:** [How Agentic Is Agentic Commerce?](https://arxiv.org/abs/2607.12575), July 2026 preprint, studies Base settlements and finds substantial linked/self-manufactured activity; its organic service floor and broad upper bound differ greatly. Ownership heuristics and labels have limitations. This supports requiring unrelated paid-job evidence; it does not prove every x402 service is fake or extrapolate to Stellar. [When HTTP 402 Meets the Blockchain](https://arxiv.org/abs/2607.19545) and [Five Attacks on x402](https://arxiv.org/abs/2605.11781) document payment/fulfillment security failure modes, not willingness to buy a startup.

**Anecdotes, low weight:** [developer production discussion](https://www.reddit.com/r/AI_Agents/comments/1r86g99/is_anyone_actually_using_agentic_payment/), [paid-tool friction discussion](https://www.reddit.com/r/AI_Agents/comments/1sywivv/if_youre_building_an_agent_that_pays_for_tools/), [seller experiment](https://www.reddit.com/r/mcp/comments/1u0plxc/would_agents_actually_pay_per_call_for_their_own/). Anonymous participants report custody/spend control, failure/retry, receipts and initial human wallet funding friction. Some posters sell the proposed tools. These are interview leads and failure hypotheses, not market sizing or independently verified customer demand.

## Four distinct full-company hypotheses

All pricing and distribution below are hypotheses. All require buyer interviews beyond hackathon builders, and all may fail.

### A1. Delegated procurement and recourse for bounded technical services

**Buyer / weekly job:** Head of AI operations or engineering operations at a 10–100 person AI-enabled research or software agency, with the controller as budget approver. Repeatedly buy third-party data enrichment, document extraction and bounded technical analyses for customer projects; verify results, allocate cost to client, recover failed/duplicate/late work. Require existing outside vendor spend and multiple providers before eligibility.

**Workaround:** API subscriptions/prepaid credits, shared credentials, ad-hoc agent wallets, Slack approvals, engineering error handling, finance spreadsheets and vendor support tickets. This workflow is a hypothesis until buyers show recent orders and failures.

**Full company / differentiation:** Contracted supplier network and service acceptance templates; purchase orders, caps, independently stored intent, result acceptance/rework, evidence-backed claims, seller response SLAs, customer-project cost allocation, refunds and provider replacement. Own contractual remediation for a defined task class. Omamori covers presigning; Ramp covers authorization/accounting; Stripe covers charging/refunds. A1 earns its place only if cross-provider technical fulfillment and recoverable recourse remain unsolved.

**Money/control/recovery:** Buyer funds stay with buyer or licensed provider; scoped authorizations bound merchant, task, cap, deadline, nonce and immutable acceptance criteria. Agent cannot amend its own mandate. Unknown seller/changed terms/ambiguous results require human approval. Avoid post-payment irreversible calls where acceptance cannot be meaningfully checked. Seller-funded reserve or payment delayed under agreed terms may support refunds, but this is not insurance and must not promise guaranteed recovery without capital/contract. Timeout, partial work, replay, dispute, provider outage and revocation must be explicit. Maintain card and fiat support; preserve existing rails, with optional Stellar USDC only for willing suppliers.

**Price hypothesis:** $500–1,500/month plus a transparent supplier-management fee on qualifying recovered/managed work; buyer must show material savings in staff time or recoverable loss. No percentage of all spend for a dashboard. Start manual commercial operations before automation to learn acceptance disputes.

**Distribution:** Build a 40-account cold list from agencies publicly shipping research/data workflows and vendors' public customer case studies; contact founders/AI-ops heads/controllers through public professional profiles. Ask DevRel contacts for possible introductions to operating customers, with no assumption any will occur. Aim at 5–10 qualified buyer interviews, not five fellow wallet builders. Learn recent external spend, failed-job frequency, responsibility, proof of remediation, current terms, rail constraints, who can sign a pilot and which control is missing from Ramp/Stripe.

**Stellar fit:** Technically optional; must win commercially first. Do not tell a Stellar-only story for buyers paying card subscriptions. Confidence in new-company demand: **low**, despite coherent product scope.

### A2. Managed human evidence fulfillment for research agents

**Buyer / repeated job:** AI evaluation lead or research-ops lead at an applied AI product company, buying qualified human observations/evaluations in a narrow domain or under-served language every week. Begin one repeatable job, such as expert evaluation of construction-document extraction, only after qualification supply and incumbents' limitations are evidenced.

**Workaround:** Prolific/User Interviews, specialist recruiting agencies, contractors and manual QA. Existing paid category is real; agent-specific incremental demand is unverified.

**Company:** Recruit/qualify supply, participant consent and rights, task templates, matching, turnaround, independent QA/rework, appeals, incentives, buyer dataset delivery and repeat panel. An agent may purchase within preapproved study scope, but human research lead owns study eligibility/ethics. World ID can reduce one form of duplication, not certify professional expertise or correct answers. Differentiate by demonstrated qualification/latency/rights, not by paid human inbox. Prolific already has API and managed service, so reject if its service meets the intended need.

**Price hypothesis:** 20–35% markup on participant rewards with a $500–2,000/month minimum for specialist fulfillment; pricing must cover recruitment, QA, consent and dispute labor. Benchmark Prolific's published corporate fee, but do not assume matching it is sufficient.

**Distribution:** 5 evaluation leads, 2 research-ops leads and 2 specialist research agencies from public named case studies/open technical evaluation reports; cold requests for recent procurement examples. Participant creators/DevRel are supply leads, not buyer evidence. Learn order cadence, rejected labels, QA cost, incumbent SLA, country/qualification access and acceptable research consent.

**Money/partners/multichain:** Buyer payment via licensed PSP, rewards via partner/provider or ordinary contractor payments; fiat option mandatory. Participant data access, cross-border research consent, labor classification and payout obligations need jurisdiction-specific mapping. Stellar rewards might help one measured country, but no need shown yet. Confidence: **medium in underlying paid job; low in differentiated agent-native company**.

### A3. Commercial operations for asynchronous agent-service sellers

**Buyer / repeated job:** Founder, product lead or revenue operations lead at a data/research API business with existing customers, adding autonomous buyers while delivering asynchronous or partial jobs. Repeatedly quote, accept, meter, deliver, invoice and resolve unsuccessful/late jobs.

**Workaround:** Existing Stripe/API key billing, custom queues/webhooks, customer support and provider logs. Live Parallel infrastructure supports the channel's feasibility, not demand for A3.

**Company:** Service order book, versioned acceptance/SLA contracts, job progress, cancellation windows, partial delivery pricing, customer credentials/consent, dispute evidence, customer communication and recoverable refunds across channels. For one supplier category, own commercial operations and onboarding. x402/MPP gateway, catalog, receipts and reconciliation alone are insufficient because Stripe, Parallel and OnchainRouter already implement much of that.

**Price hypothesis:** $199–999/month plus per completed managed job; existing PSP/network fees remain visible. Charge only if commercial failure handling and support costs improve.

**Distribution:** Cold list 30 existing paid API/data vendors with public asynchronous jobs and customer support; interview 5 product/revops heads and 3 support/engineering operators. Ask which failures make money move incorrectly, chargeback/refund rate, current channels, agent-specific request volume and willingness to delegate commercial operations. Hackathon listing counts do not qualify.

**Money/partners/multichain:** Seller stays merchant of record; PSP handles custody/fiat conversion; platform must establish its agency and liability. If instead acting merchant of record, tax, consumer/contract obligations and payment risk materially expand. Support card and stablecoin methods customers have, not exclusively Stellar. Confidence: **low; severe platform-feature risk**.

### A4. Reproducible technical work exchange

**Buyer / repeated job:** Engineering/security lead buying bounded regression reproduction, synthetic test cases or independently repeatable analysis for shipped software. Repeated job must have an objective verifier and sufficient ticket value to pay support/QA costs.

**Workaround:** Contractors, specialist consultancies, internal CI and bug-bounty programs. Never treat a DevRel introduction as access to paid security budgets.

**Company:** Qualified supplier network, scoped confidential inputs, versioned executable specification/environment, bids, job management, independent deterministic replay, delivery rights, staged acceptance, seller accountability, dispute and repayment operations. Reckn provides escrow/re-execution prior art; an “AI judge approves arbitrary work” marketplace has no credible guarantee.

**Price hypothesis:** 10–15% of accepted $500–5,000 jobs plus buyer team plan; all values hypotheses. $0.01 tasks cannot carry human dispute handling. Cold reach to 5 software/security leads who recently bought external reproduction/testing work and 3 service firms selling it; learn frequency, confidentiality, objective acceptance and repeat procurement budgets.

**Money/partners/multichain:** Escrow control can create custody/payment-service questions even with smart contracts. Prefer licensed partner or buyer-controlled staged payment pending counsel. Public chain stores commitments/minimal receipts, confidential inputs remain private. Stellar settlement is optional; EVM/Solana compatibility where sellers already operate. Confidence: **low; two-sided acquisition and narrow verifier scope are major obstacles**.

## Strongest A finalist, weekly journey and kill gates

**Provisional choice for the cross-category shortlist: A1, narrowly technical procurement and commercial recourse.** This is an investable hypothesis to compare, not a validated recommendation or a presumption that agentic commerce wins. A2 has stronger evidence of existing spending, but an incumbent API/managed-service offering occupies its core; A1 has a cleaner potential company boundary if buyers show real recent fulfillment loss outside existing tools. Without that evidence, do not promote it on crypto transaction counts.

**Weekly journey:** Monday controller assigns client-project budget, approved vendors and result criteria; AI-ops owner approves scope. Agent requests quote, human approves new counterparty/changed terms. Provider supplies scoped payment credential; system atomically reserves budget and creates unique order. Seller accepts clear delivery deadline and remedy. Agent receives job progress and result; independent acceptance checks machine-verifiable criteria; ambiguous quality goes to the buyer. Accepted work settles under agreed terms, with cost allocated to project. Rejection produces evidence and rework/cancel/refund case with a responsible seller and deadline. Friday owner reviews exceptions, actual savings and expired mandates; refunds are reconciled to beneficial buyer/project. Every participant knows who can cancel or release funds during an outage.

**First learning product:** A real bounded procurement workflow using historical and consented sample orders, one seller task class, actual purchase terms, rejection/rework evidence and an auditable policy state machine. Do not call a read-only transaction dashboard the full product. Live execution later requires verified partner access, buyer authorization, reliable idempotency, recovery agreement and legal review; this research grants none of those permissions.

**Three kill observations:**

1. In 5–10 qualified buyer interviews, fewer than three show weekly external service purchases with costly acceptance/refund/remediation failures, or budgets are merely internal/model subscriptions already handled adequately by Ramp/Stripe.
2. Existing provider dashboards/wallet policies plus ordinary support resolve the observed cases; buyers will not pay for a separate operator, and sellers will not accept objective criteria, response SLAs, staged release or enforceable refunds.
3. Trust/QA/dispute/support cost exceeds the plausible fee, or the only feasible live model requires startup-funded credit, open-ended guarantees, unavailable regulated partners, or a forced Stellar migration without buyer benefit.

No interviews were conducted; no counterparties agreed to supply, accept terms, pilot or pay. No blanket assertion of “no licenses needed” is supported. Software-only read access narrows initial financial control but still creates data security and contracting obligations; custody, initiating transactions, escrow, acquiring, FX, fiat payout, credit and insurance boundaries require the actual jurisdiction and role to be assessed.
