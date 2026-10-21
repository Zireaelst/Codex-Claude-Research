# Stellar privacy and agent financial workflows: independent venture research

Research date: 20 October 2026. Read-only research only. No outreach, applications, deployments, transactions, or wallet setup. Instaward rules were not consulted. Findings distinguish verified documentation, vendor claims, research findings, anecdotes, and investment hypotheses. A functioning endpoint or funded project is not proof of commercial traction.

## Decision

**Reject a new generic Stellar agent wallet, MCP wrapper, policy generator, x402 facilitator, API marketplace, or “Ramp for agents” as the recommended company. Reject a company whose launch requires production-ready SPP or Confidential Tokens today.** The former territory is already crowded by funded Stellar projects and well-distributed cross-chain incumbents. The latter capabilities are explicitly developer previews, not safe production dependencies.

The best company-shaped investigation in this research area is **cross-provider stablecoin settlement operations**, beginning with reconciliation and exceptions for a licensed payout business. Privacy could become an optional feature after adoption; agents can automate evidence gathering and draft resolutions. Neither should be the initial demand claim. This is a conditional discovery recommendation, not a verified willingness-to-pay finding or a claim of venture backability. A no-network founder must first earn access to operational artifacts and a buyer. Builder introductions are a possible recruiting route, not customer distribution.

## 1. Exact privacy maturity

### SPP: developer preview, not mainnet money infrastructure

**Verified from current first-party docs:** [Privacy on Stellar](https://developers.stellar.org/docs/build/apps/privacy) explicitly says SPP contracts, SDKs and demo are unaudited, testnet only, and not intended for production or real assets. It lists alpha JS/TS, native Rust and CLI surfaces. Therefore “Stellar supports privacy” cannot be translated into “use SPP to pay confidential salaries with real USDC now.”

The [developer preview](https://stellar.org/blog/developers/developer-preview-stellar-private-payments) describes a shared shielded pool. Public observers can see the addresses and amounts entering/exiting; they should not see the internal payer/payee link or internal amount. Anonymity is not guaranteed by merely depositing: timing, unique amounts, pool size and app metadata can leak information (our inference). Association-set policies, public-key registration and global viewing mechanisms are application choices, not automatic legal clearance. [Source repository](https://github.com/NethermindEth/stellar-private-payments).

### Confidential Tokens: different privacy property and same preview constraint

**Verified:** [June 29 developer preview](https://stellar.org/blog/developers/developer-preview-confidential-tokens-on-stellar) states not approved for mainnet, live on testnet, contract and verifier audits underway. It wraps SEP-41 assets; internal balances/transfer amounts are hidden but counterparties remain public. Deposits and withdrawals expose amounts. Noir circuits and Nethermind UltraHonk verify the confidential flow. Auditor viewing, selective disclosure, freeze passthrough and policy hooks are preview features.

Do not say “OpenZeppelin contracts are audited, therefore Confidential Tokens are audited.” The normal library and the preview are different scopes. [Current confidential branch](https://github.com/OpenZeppelin/stellar-contracts/tree/feat/confidential-verifier-ultrahonk/packages/tokens/src/confidential).

The [August 6 technical Q&A](https://developers.stellar.org/meetings/2026/08/06) clarifies that auditor IDs attach per registered account with a shared registry; the earlier verbal description of one global auditor per contract was corrected. It also warns that confidential tokens do not naively plug into agent payment protocols: encrypted balances change payment verification and policy evaluation. “Private agent payments” is an engineering project, not a flag.

### ZK primitives and verifiers

**Verified:** [ZK docs](https://developers.stellar.org/docs/build/apps/zk) distinguish native BN254/Poseidon primitives from higher-level private payments. A developer must still implement circuits, proof generation and verifier/application logic. Native support alone proves no confidential commercial workflow. [Protocol 25 announcement](https://stellar.org/blog/developers/announcing-stellar-x-ray-protocol-25) identifies BN254 and Poseidon additions; [software versions](https://developers.stellar.org/docs/networks/software-versions) records releases.

[Nethermind RISC Zero verifier](https://github.com/NethermindEth/stellar-risc0-verifier) provides verification/deployment/operator documentation, including parameter upgrades, roles and emergency stops. A deployable verifier is not a complete private payment product, audit of the consuming circuit, custody design, or evidence that an institution has put real assets through that application. No independently corroborated production SPP/Confidential Token real-asset usage was found in this research.

### Moonlight: important separate competitor, trust model and maturity uncertainty

**Verified award:** [Mainnet Launch of Private Payments](https://communityfund.stellar.org/submissions/recNF9qwGZwrMlDfu), SCF #37, $135k awarded. The submission describes channels, provider framework, SDKs and institution relationships; its “mainnet launch” title is a funded objective, not proof of launch. Its traction and planned integrations are vendor claims.

**Verified audit exists:** [Runtime Verification report landing page](https://runtimeverification.com/public-report/moonlight-audit), July 24 2026, scope Moonlight core contracts, design/code review, reports 0 critical/high, 3 medium and 12 low/informative findings. This is an audit scope fact, not an audit of every wallet/provider/backend component or proof that every finding is resolved.

**Verified technical distinction:** [August 27 developer meeting](https://developers.stellar.org/meetings/2026/08/27) says Moonlight uses UTXO bundling and trusted privacy providers/councils and **does not use ZK today**. Providers see their users' records and handle KYC/AML. The demonstrated dashboard was explicitly testnet and the browser wallet loaded from source in development mode. [Protocol site](https://moonlightprotocol.io/), [GitHub](https://github.com/Moonlight-Protocol).

**Unresolved:** ecosystem summaries ([example](https://lumenloop.com/media/stellar-developers-meeting-08-27-2026)) call the same event a mainnet launch and one incorrectly tags it ZK. These conflict with the primary technical notes' testnet demo. Do not present Moonlight mainnet commercial uptake as verified without a production deployment, asset, current provider and real transaction references. Even if mainnet code exists, that does not establish regulated providers or real-volume use.

### Other privacy competition is real, demand less established

* [Zarf distribution engine](https://communityfund.stellar.org/submissions/rec81hKwglu2sUT1N): SCF #42 $40k awarded, email/JWT ownership proofs and vesting/distribution. This is not confidential payroll with full hidden balances. Funded implementation plan, not revenue proof.
* [LumenShade](https://communityfund.stellar.org/awards/recXNYH3tfP4FZnSi): SCF #37 $135k awarded for Stellar privacy. Award establishes competition, not production security.
* [Hypertron protocol](https://www.hypertron.space/docs/protocol): vendor docs explicitly disclose testnet, single-coordinator Groth16 setup, no ceremony/no audit, replaceable verification keys without timelock; no assets of value. [Product docs](https://www.hypertron.space/docs) include payment links, checkout, API/webhooks, treasury and disclosures; reusable tooling is direction rather than a published SDK. This already resembles a complete privacy payment company, not just a chatbot.
* [Hypertron July 23 developer meeting](https://developers.stellar.org/meetings/2026/07/23) presents B2B payments/operations and opt-in privacy. Its SCF #44 “B2B Payments & Agentic Operations” $116k submission is **Panel Review Failed**, not funded; do not conflate an ecosystem appearance with an award.
* [ZetaPay](https://github.com/Adeel91/zetapay) calls itself an experimental testnet enterprise payroll implementation. [Another confidential payroll implementation](https://github.com/berkay1532/confidential-payroll-stellar) has a deployed testnet demo and explicit proof/toolchain constraints. Neither establishes paying payroll employers.

## 2. Agent infrastructure actually exists

### Stellar tooling

**Verified:** [Stellar CLI for Agents](https://developers.stellar.org/docs/tools/cli/agent-cli), updated October 12, documents typed token JSON outputs, balances, transfers, capped/time-bound allowances, unsigned build-only drafts and diagnostic errors. JSON coverage is incomplete. A token allowance is a hard token-spend limit, not an invoice policy, correct merchant selection or a guarantee of business intent. Giving the agent a full signing key would bypass a carefully designed delegated flow (inference).

**Verified:** [OpenZeppelin tooling docs](https://developers.stellar.org/docs/tools/openzeppelin-contracts) describe context rules, signers, policies and initial multisig/spending-limit policies. These are existing implementation components. An application still needs recovery, accounting, permission UX, monitoring and audit of its composition.

**Verified separate project:** [Stellar AI Agent Kit SCF #37](https://communityfund.stellar.org/submissions/recmbfFnpx6eVThqw), $108k awarded, one-person team, MCP generator + scoped policy signer tools + SDK. The project's claimed 2,047 downloads in seven weeks and ecosystem endorsements are developer-interest signals, not paid financial workflows. Its proposed product is infrastructure generation, not an agent creating contracts. Do not treat this as a MetaMask product.

**Verified policy competition:** [SCF #44 award record](https://communityfund.stellar.org/awards/rec4FnYypcsKpBRB4) lists Gateway.fm policy builder $98k, CredioLabs.AI policy builder $125k, Policywright $55k, ROZO MPP $98k and Paycashless operations $78k. [Policywright](https://policywright.lemmalabs.space/) says shipped on testnet and demonstrates record/simulate → minimal authorization → dry run → human-signed install. Thus “turn agent actions into least privilege” is not unoccupied territory.

### x402 and MPP

**Verified docs:** [Stellar x402](https://developers.stellar.org/docs/build/agentic-payments/x402) supports Soroban auth-entry signing, SEP-41 and default USDC. Coinbase facilitator support there is testnet; [Built on Stellar/OpenZeppelin facilitator](https://developers.stellar.org/docs/build/agentic-payments/x402/built-on-stellar) has documented testnet and mainnet URLs, `exact` v2 verification/settlement and API-key setup. Freighter browser supports signing; Freighter mobile is explicitly unsupported currently. Existence of a mainnet facilitator does not make all compatible services production-ready.

**Verified docs:** [Stellar MPP](https://developers.stellar.org/docs/build/agentic-payments/mpp) has one-time SAC transfer charges and sessions via funded unidirectional channels with cumulative signed commitments. Charge supports server-broadcast authorization and client-broadcast proof modes. MPP is a different payment flow, not privacy infrastructure.

**Existing seller/buyer products:** [Rail402](https://rail402.dev/) has SDK/CLI/MCP/Bazaar/facilitator, `exact` and `upto` metering, smart-account budget policy, playground and explorer. Its site labels testnet and also publishes mainnet example settlements. Vendor snapshot at research time claims 2,620 mainnet payments, 44 buyers, 28 sellers versus 54,434 testnet payments. Those are unverified indexer counts and not necessarily unique economic actors, organic API demand or revenues. [SCF funded project directory](https://communityfund.stellar.org/projects?2428add0_page=1&4ae4a42b_page=2) lists Rail402 and AgentSmith x402 in #45. Verify award amount against the submission; aggregators differ between amount awarded and total requested.

[ROZO MPP router](https://www.mpprouter.dev/) and [April 23 developer meeting](https://developers.stellar.org/meetings/2026/04/23) show an already-mainnet route from Stellar payments to Tempo services. The meeting's 400 endpoints is supply count, not 400 paying agents. [ROZO AI services page](https://rozo.ai/aiservices) still labels many branded provider integrations “coming soon” and says Stellar coming soon in part of the page, so product surfaces are inconsistent. Do not inflate the award into evidence every integration is live.

[xlm402](https://www.xlm402.com/) advertises paid weather/news/market/inference/image/extraction endpoints with mainnet/testnet pricing. Direct page fetch timed out during this research; search indexing found the catalog. That is a discoverable advertised service catalog, not a successfully tested paid call or evidence of paying demand. No payment was attempted.

### Three MetaMask/Stellar identities must not be merged

1. [Normal MetaMask Stellar support](https://support.metamask.io/de/configure/networks/stellar/) documents Stellar as a default network, XLM reserves and trustlines; [MetaMask Stellar adapter](https://github.com/MetaMask/connect-stellar) implements SEP-43. This is wallet distribution.
2. [MetaMask Agent Wallet supported chains](https://docs.metamask.io/agent-wallet/reference/supported-chains/) currently lists preconfigured **EVM** networks; Stellar is absent. `mm chains list` is authoritative for a CLI version, but no wallet setup was performed. [June 8 launch](https://metamask.io/en-GB/news/metamask-launches-agent-wallet-giving-ai-agents-full-defi-access-with-default-security-on-every-transaction) describes controlled autonomous EVM DeFi. Native Stellar wallet support does not imply Agent Wallet supports Stellar.
3. The separately funded Stellar AI Agent Kit above is Jose Toscano's tooling project, not the MetaMask agent product.

## 3. Demand evidence and incumbent baseline

**Important independent research finding, not uncontested market fact:** [Ling et al., July 14 2026 preprint](https://arxiv.org/abs/2607.12575) measures 136.7m Base settlements worth $44.1m over 280 days; it classifies 21.20% as fictitious and 63.78% as internal linked-cluster settlement, with severe concentration. The authors bound independent spend rather than calling every transfer adoption. This cannot be automatically generalized to Stellar, but it invalidates using raw x402 transfer counts as a venture TAM.

**Research finding:** [Wang et al.](https://arxiv.org/abs/2607.19545), listed as USENIX Security 2026, evaluated 15 major facilitators and found authorization/execution rule violations in all, reporting disclosure and mitigations. Potential jobs include correct retry/idempotency, receipt validation, sponsor-gas control and settlement monitoring. That does not prove a standalone startup budget; an existing facilitator may absorb fixes.

**Traditional incumbent is already agent-enabled:** [Ramp agent platform](https://agents.ramp.com/) gives agents identity/owner, budgets, approvers, cards/MPP/x402, receipts and accounting context. [Actual tool docs](https://agents.ramp.com/docs/reference/agent-tools) expose one-time card credentials, x402 wallet funding/payment, funds/limits and procurement programs. [API docs](https://docs.ramp.com/) describe ERP two-way sync. “An AI can spend within a budget and generate an audit trail” is already a feature set with distribution.

**Base/Ethereum incumbent:** [Coinbase Agentic Wallets](https://www.coinbase.com/en-ca/developer-platform/products/agentic-wallets) offers skills, gasless Base, session/transaction caps, enclave keys and transaction screening; counts are vendor claims. [Privy policy docs](https://docs.privy.io/security/wallet-infrastructure/policy-and-controls) cover cryptographic authorization, quorums, MFA, recipient/contract limits and calldata controls; some limit evaluation runs outside the enclave. [Privy agent authorization](https://www.privy.io/blog/empower-agents-to-transact-from-wallets-built-on-privy) already supports browser-approved scoped CLI/MCP access.

**Solana/commerce incumbent:** [Crossmint](https://www.crossmint.com/solutions/agentic-payments) combines wallets, cards, guardrails, credentials and checkout; [agent cards](https://www.crossmint.com/products/agentic-cards) names Lobster.cash as a working product and Solana stablecoin wallet infrastructure. Some features require access requests; advertised merchant reach is not verified agent sales. [Squads v4](https://github.com/Squads-Protocol/v4) has spending limits, roles, timelocks and multiple-party payments. Delegation is not uniquely Stellar.

**Privacy alternatives:** [Solana integration guide](https://solana.com/docs/tokens/extensions/confidential-transfer/integration-guide) documents client proof generation, encrypted balances, public addresses, keys and auditor integration. Do not repeat an old “confidential transfers disabled” claim as current without current network verification. [Inco](https://www.inco.org/) announces Base mainnet cToken September 2, but the same homepage FAQ still says Base Sepolia/Solana devnet; prefer versioned deployment docs before relying on it. [Fairblock Stabletrust Pro](https://docs.fairblock.network/ct/guides/apps/stabletrust-pro) already describes confidential multisig team payouts using Turnkey. Its 'available chains' table does not specify mainnet; [legacy SDK docs](https://stabletrust-docs.fairblock.network/introduction) explicitly say testnet-only. These are competitors with ambiguous maturity, not verified institutional scale. [RAILGUN POI](https://docs.railgun.org/wiki/assurance/private-proofs-of-innocence) provides a different privacy/compliance construction; allow/deny list proofs do not themselves equal regulatory approval.

## 4. ETHGlobal prior art: not novelty, not automatically companies

* [Trinity Guardian, Tokyo 2026](https://ethglobal.com/showcase/trinity-guardian-2hixe): ENS permissions, per-payment/daily limits, allowlists and proof-of-human escalation; Ethereum Sepolia. Risk responses simulated because API access absent. Clear prior art for agent mandate controls; not proof of paying buyers.
* [Railbridge x Unlink, New York 2026](https://ethglobal.com/showcase/railbridge-x-unlink-rdc11): merchant x402 control plane, pooled intake, private merchant allocations, sweeps/payouts. Prototype stores encrypted merchant mnemonics in SQLite; custody/privacy design needs production work. A full merchant ops company direction already exists.
* [Meridian, Cannes 2026](https://ethglobal.com/showcase/meridian-1x2ef): autonomous USDC/EURC treasury, TWAP, manual thresholds, confidential computation/Unlink. Public Base mainnet path versus private Base Sepolia path; CRE workflow simulated. Do not interpret claimed 1–3% bank FX saving as tested customer economics.
* [Ledgit source](https://github.com/cbonoz/ledgit): human hardware approval, agent identity and encrypted ordered action records; ETHGlobal 2026. Auditable agent control exists as hackathon prior art; no verified commercial adoption.

## 5. Four company theses and falsification

All prices/economics below are **hypotheses for discovery**, not observed willingness to pay, projections or market facts. No warm customer network is assumed. Recruiting is public company/anchor directories plus a specific DevRel/ambassador introduction request, if offered; builder communities are useful for introductions and technical learning, not sufficient buyer validation.

### A. Cross-provider settlement exception and reconciliation operations — investigate first

**Buyer/repeated job:** head of payment operations or reconciliation lead at a licensed payout fintech/anchor, controller as budget approver. Each day reconcile customer instruction → onchain transfer → anchor/custodian acceptance → beneficiary fiat payout → fees/refund/ERP entry. Focus on cases where chain settlement succeeds but beneficiary credit, reference match or provider reconciliation fails.

**Full company:** shared operational ledger, provider adapters, immutable evidence links, exception queue/ownership, safe resolution drafts and finance close. Agents classify evidence and prepare actions; users authorize money movement. Privacy can protect sensitive offchain records; real assets do not depend on preview privacy contracts.

**Demand basis:** operational hypothesis grounded in real cross-provider payment flows, not confirmed buyer interviews. [Wirex live stablecoin settlement release](https://stellar.org/press/wirex-and-stellar-go-live-with-dual-stablecoin-visa-settlement-in-usdc-and-eurc-for-7-million-users) verifies a deployed payment use case, not a signed prospect. [Nuvante prototype](https://stellar.org/press/nuvante-technologies-announces-stablecoin-clearing-prototype-built-on-stellar-network-integrated-to-bank-of-england-rtgs) is a prototype, not commercial clearing demand.

**Economics:** ask whether $500–$2,000/month can be justified by measured hours, avoidable loss and faster close; paid design partner before custom integrations. Example only: 20 hours/month saved at an assumed $30 loaded hourly cost gives $600 monthly labor value, so a $2k price cannot rest on that alone. Add measured loss/float value or target a larger operation. Read-only v1 lowers operational exposure. Support and bespoke connector cost can erase margin.

**Distribution/partners:** licensed anchors, payout platforms, accounting implementers and custodians. Begin with two operational providers and one accounting export; actual API access and data rights required. No “partner” label without agreement.

**Expansion/moat hypothesis:** eventually become the reconciliation system of record across providers/rails, with reusable mappings, exception history and operational performance data. Thin dashboards and generic agents have little defense. Platform vendors may own enough data to reproduce the workflow.

**Why it fails:** infrequent exceptions; fintech owns one provider already; data cannot leave provider; spreadsheets are adequate; integrations too bespoke; procurement slow; incident liability; Bitwave/PSP/provider already solves it. Kill if 5 interviews yield no repeated costly case, no redacted artifact access, or no budget holder willing to pilot.

**Interview recruiting and learning:** request intros specifically to the person who worked the last delayed payout, not a developer advocate. Interview 5 ops/reconciliation leads + 2 controllers + 2 engineers who own integrations. Ask for the last ten failed/delayed cases, a redacted reconciliation sheet, exact timestamps and manual touches, total monthly case count, who owns refund/settlement decisions, reconciliation cutoffs, current vendor, and purchase authority. Ask “walk me through the last one” before pitching privacy or AI. If no intros, use public anchor support/business channels only after user authorizes outreach; this research did not contact anyone.

### B. Confidential supplier/contractor payment operations — wait, do not choose now

**Buyer/job:** controller/payroll operations lead of a 20–200-person export-services company already paying stablecoins monthly. Approve roster/invoices, pay correct people, reconcile and selectively disclose to accountant without public salaries/supplier relationships.

**Full company:** compliant recipient onboarding, invoice/contract record, approvals, confidential settlement, recovery, bank/cash payouts and accounting. SEP-41 wrapper is one component. Zarf, Hypertron, ZetaPay, Stabletrust and regular payroll/AP providers constrain novelty.

**Economics/distribution hypothesis:** $3–$8/recipient/month or $300–$1k organization minimum, tested against savings and support per payout. Recruit via export agency finance managers/accountants or a payroll provider, not crypto builders. Required partners: employer payroll/legal adviser, regulated ramps, asset issuer compatibility, audited privacy implementation and key recovery.

**Why it fails now:** preview privacy stack; recipient UX; visibility at pool edges; sanctions/asset restrictions; payroll law/tax; employers already have private fiat rails. Clawback/freezing and audit view keys do not make legal analysis disappear. Choose only after 3 employers show privacy is blocking an existing stablecoin workflow, agree to a paid pilot, and a production-safe protocol is independently confirmed. Kill if pain is mainly FX/offramp rather than privacy: build ordinary payout ops or use an existing provider.

**Interviews:** 5 controllers/payroll operators with current stablecoin payouts; two recipient users; two payroll/ramp partners. Ask what leaked, who saw it, consequences, whether public addresses themselves are unacceptable, which disclosures are compulsory, tolerated recipient setup, payroll cutoff and who accepts security risk. Recruit through local export/software agency accountant networks and possible ambassador intros; access currently unproven.

### C. Agent procurement and financial control platform — reject generic version

**Buyer/job:** engineering/AI platform lead and finance controller jointly managing recurring paid data/compute/API use. Provision delegated budget, choose vendors, monitor consumption, reconcile receipts and revoke access.

**Demand basis:** protocols, paid-service supply and wallet capabilities exist; organic recurring independent paid usage remains uncertain. Ramp already handles agent identities/card/x402/MPP controls and accounting. Coinbase, Privy, Crossmint, Rail402, Policywright and AI Agent Kit remove basic infrastructure novelty.

**Company-sized wedge would need:** cross-provider cost attribution, vendor procurement obligations, refunds for failed jobs, evidence linking a payment to fulfilled useful work, and finance close. A protocol wrapper or prompt-driven wallet is not enough. Still may be a feature in incumbent spend platforms.

**Economics:** a 1% fee on $10k monthly agent spend is $100, unlikely to fund support/compliance. At $1m/month it becomes $10k, but such a buyer must actually exist and be reachable. A subscription tied to finance/reliability value is a test, not a pricing fact.

**Partners/legal/technical:** spend provider/card issuer, wallet infrastructure, regulated rails, service vendors and ERP access. Budget enforcement must live outside the agent, cover cumulative concurrent spending, use idempotency and distinguish payment from fulfillment. Refund/dispute authority matters. Cross-border stablecoin routing introduces compliance responsibilities.

**Interviews/recruiting:** 5 AI platform leads with live paid agents, 3 finance controllers, 3 API sellers. Public MPP/x402 directories can identify sellers; builders can introduce buyers but directory inclusion is not purchasing authority. Ask last 30-day bills and counts of independent paid jobs, refunds/failed delivery, vendor allowlisting, authorization boundaries, current Ramp/credit-card handling and incremental willingness to pay. Kill if all usage is demos, subsidized transfers, or developer testing, or existing Ramp controls solve it.

### D. Merchant settlement, fulfillment and private treasury for agent services — monitor, not first choice

**Buyer/job:** founder/revenue operations lead of a real paid data/API provider selling to unrelated agent customers repeatedly. Attribute receipts to delivered jobs, prevent replay/double charge, meter usage, handle refunds, treasury and payout.

**Company:** seller backoffice with revenue ledger, entitlement/fulfillment evidence, retry/refund operations, tax/invoicing and optional private treasury. Railbridge, Rail402/Bazaar, ROZO and Stripe/MPP are direct or adjacent competitors. New permissionless directory alone has a cold-start problem.

**Economics:** 0.5–2% of real processing volume plus subscription minimum; $20k/month merchant volume yields only $100–$400 gross processing revenue before fees/support. A serious company needs large merchants, a valuable subscription or a differentiated vertical. Neither x402 transaction count nor hundreds of listings prove that revenue base.

**Distribution/partners:** direct integrations with 2–3 API sellers; billing/usage gateways; facilitator and custody partners. Avoid holding merchant funds in v1. Real privacy adds selective disclosure, issuer and pool counterparties, plus custody/sanctions questions.

**Failure modes:** negligible organic sales, sellers prefer Stripe prepaid credits, upstream ToS prohibit resale, delayed or non-verifiable service delivery, payment rail cannot adjudicate usefulness, incumbent owns receipts/discovery. Kill unless 3 sellers show unrelated recurring revenue and quantified unreconciled jobs/refund work.

**Interviews:** 5 seller owners/RevOps leads and 3 buyers of those exact APIs; directory-based recruiting. Ask unique independent customers, actual monthly paid value excluding own wallets/tests, refund rate, fulfillment proofs, current billing tools, support labor and willingness to pay before proposing a privacy feature.

## 6. Compact maturity and audit matrix

| Capability/product | Status established by source | Privacy/authority boundary | Audit/mainnet/real-asset conclusion |
|---|---|---|---|
| [Native ZK host functions](https://developers.stellar.org/docs/build/apps/zk) | Protocol primitives shipped | Verification arithmetic, not private payments | Does not establish any consuming app's audit or commercial use |
| [SPP](https://developers.stellar.org/docs/build/apps/privacy) | Developer preview, testnet-only, alpha SDK | Pool internal counterparties/amounts hidden; edges public | Explicitly unaudited; no production/real assets |
| [Confidential Tokens](https://stellar.org/blog/developers/developer-preview-confidential-tokens-on-stellar) | Testnet preview; audits underway in preview notice | Hidden internal balances/amounts, public counterparties, public entry/exit | Not approved for mainnet in notice; current privacy docs still caution unaudited |
| [RISC Zero verifier](https://github.com/NethermindEth/stellar-risc0-verifier) | Deployable code/operator docs | Verifies selected computation | No end-to-end private financial product or real-asset use established here |
| [Moonlight](https://developers.stellar.org/meetings/2026/08/27) | Demonstrated testnet; secondary mainnet descriptions conflict | Provider-mediated UTXO bundles; provider visibility; no ZK today | Core design/code audit exists; full-stack audit and commercial mainnet adoption unverified |
| [Hypertron](https://www.hypertron.space/docs/protocol) | Testnet deployment with contract references | Shielded pool; coordinator/setup/admin trust | Explicit no audit, no ceremony, no valuable assets |
| [Stellar agent CLI](https://developers.stellar.org/docs/tools/cli/agent-cli) | Current CLI docs and token surface | Allowance caps/human signer, not semantic intent | Existing tooling; app/key use determines safety |
| [OZ smart accounts](https://developers.stellar.org/docs/tools/openzeppelin-contracts) | Contracts and policy framework | Context scope, signers, multisig/spend policies | Library audit statement is not a composition/front-end/SDK audit |
| [x402/OZ facilitator](https://developers.stellar.org/docs/build/agentic-payments/x402/built-on-stellar) | Documented mainnet and testnet service | Verifies transfer auth and settles | Production service availability; does not prove merchant demand/privacy |
| [Stellar MPP](https://developers.stellar.org/docs/build/agentic-payments/mpp) | Charge/session SDK and examples | Direct charges or prefunded channels | No privacy claim; real buyer volume not established |
| [Policywright](https://policywright.lemmalabs.space/) | Shipped testnet, live artifact claims | Human-signed least-privilege policy install | Not verified mainnet customer deployment |
| [Rail402](https://rail402.dev/) | Live testnet plus vendor mainnet examples | Noncustodial facilitator, metering, discovery | Self-reported activity is not verified independent paid demand |

**Moonlight audit exact scope:** [PDF, pages 6–8](https://strapi.runtimeverification.com/uploads/Moonlight_report_64808bfd8e.pdf) fixes initial scope at `d65780bbf0a6f8b2b601e4a536b38000775c8a15` and final reviewed remediation PRs at `867c23da1769a2f56e42449ce5d5315ffb5f4cdc`. Contracts: `channel-auth` (provider registry/authorization, owner/admin, upgrade lifecycle) and `privacy-channel` (P256 UTXO owner/Ed25519 depositor authority, conservation, deposit/transfer/withdrawal, TTL). It is a two-week design/manual-code review followed by remediation support, not a full formal proof of the system. A deployment must match the reviewed revision. One constraint is particularly relevant for recurring payments: byte-identical signed effects must not share a bundle; the reported mitigation documents the batching constraint. A documented constraint is not an eliminated implementation risk.

## 7. Consumer MetaMask earn/spend/subscription opportunity: reject broad clone

**Assessment:** normal MetaMask supporting Stellar makes connection and asset management easier. It does not provide an app listing, featured placement, customer acquisition, country eligibility, supported lending integration, card issuer approval or Agent Wallet support. No distribution agreement or access to MetaMask users has been verified. A consumer wallet integration is a capability, not a channel.

Actual alternatives already own the recurring job:

* [MetaMask Stablecoin Earn](https://metamask.io/en-GB/news/introducing-stablecoin-earn-passive-income-metamask-wallet) has in-wallet Aave USDC/USDT/DAI lending. [Current lending help](https://support.metamask.io/trade/earn/lending/how-to-lend/) confirms the flow. This does not show those features are available on Stellar.
* [MetaMask Card](https://metamask.io/en-GB/card) supports everyday spend and explicitly describes subscriptions such as Netflix/Spotify; it advertises card controls, transaction export, cashback and yield. Do not assume Stellar assets fund that card because the wallet supports Stellar. Check card-eligible chain/token and country separately.
* [Tuyo on Base](https://www.base.org/customers/tuyo), published October 15 2026, describes spending USDC directly from an earning strategy, with optional spending from ordinary balances. The page clearly labels 100k+ users as company-reported Tuyo-wide, not verified Base-active users; 175m acceptance locations are potential reach, not active merchants. This is strong feature competition, limited audited demand evidence.
* [Fuse on Solana](https://fusewallet.com/) advertises Visa card, yield, fiat movement, swaps and smart-account controls, with card country eligibility. [Fuse Earn](https://fusewallet.com/blog/fuse-earn) describes live Drift integration for USDC/PYUSD, and [security docs](https://fusewallet.com/support/what-is-fuse) describe spending limits/key recovery. Fuse wallet is distinct from the unrelated Fuse blockchain.

**Economics hypothesis:** a 0.5% annual platform fee on a consumer's $2,000 balance yields $10/year gross. Acquisition, support, ramp/KYC costs and security can exceed that. Subscription management is already available on familiar cards; a new wallet must show a larger repeated advantage than lower chain fees. Yield requires available liquidity, appropriate risk/eligibility and dependable withdrawal into spending balances. Privacy previews do not remove those issues.

**If tested:** choose a tightly specified cohort already receiving stablecoin income with a repeated local spend/offramp problem; interview 8 current recipients and 3 local accountants/ramp operators. Recruit through actual employer/agency payout relationships, not “MetaMask users” in general. Ask how last month's money arrived and was spent, full conversion fees, failed subscriptions, average retained balance, support incidents and willingness to switch. Kill if current card/offramp works, if user acquisition requires paid retail marketing, or if the only differentiation is “Stellar + earn.” No such cohort access is established.

## 8. Lower-confidence alternative: project/SOW/milestone financial operations

This is a potential third business investigation after payout delivery recovery and RWA lifecycle, more credible than forcing an agent company into the shortlist, but **not yet a validated business**.

**Buyer/job:** owner/finance lead of a 5–50-person export software/design agency repeatedly billing cross-border clients by project milestones. Convert accepted SOW and change orders into invoice/funding/acceptance/release evidence, reconcile partial payments and resolve late acceptance without losing the relationship. Product owns the whole project-to-cash workflow, not a generic escrow UI.

**Competition/primitives:** [Trustless Work pricing](https://www.trustlesswork.com/pricing) is already mainnet escrow infrastructure at 0.3% per successful release; [mainnet backoffice](https://backoffice.trustlesswork.com/) and [API role docs](https://docs.trustlesswork.com/trustless-work/api-rest/deploy) expose approver, service provider, release and dispute roles. [V2](https://www.trustlesswork.com/escrow-times/dev-update-trustless-work-v2) adds batch actions and role changes; do not assume an earlier audit covers V2 without revision comparison. [SCF #31](https://communityfund.stellar.org/awards/recmMAZ9NCDscGBnc) awarded $70k and [#41](https://communityfund.stellar.org/awards/recTLIVf9LOTBtkld) $80k for infrastructure/indexing. [Boundless](https://communityfund.stellar.org/submissions/recfC78Xt0enJyMa3), SCF #40 $110k, already applies milestone escrow to funding. Milestone escrow itself is not novelty.

**Value/economics hypothesis:** $100–$300/agency/month plus a modest platform fee, to be compared with actual collection hours and bad-debt reduction. If underlying escrow costs 0.3%, a 0.5% total processing fee leaves only 0.2% before other costs; $50k/month then yields $100 gross fee spread. Subscription value needs real workflow savings. The buyer's customer must also accept prefunding; smart contracts cannot force a large enterprise client to do so or objectively adjudicate design quality.

**Distribution/partners:** agency accountants, project-management implementers, export associations, existing contractor/payroll providers; a possible ambassador intro is not distribution. Potential technical partner Trustless Work, actual legal dispute-resolution partner and regulated offramp. No partner relationship is assumed.

**Moat/expansion hypothesis:** repeated contract terms, acceptance/change-order evidence, reconciliation history and integrations create switching cost; expand into receivables/working-capital operations only with legal/partner capacity. A simple escrow wrapper is easily copied.

**Why it fails:** clients refuse prefunding, payment terms are negotiation rather than tooling, agencies already use Wise/bank/Upwork, disputes require human legal work, low ticket/support economics, two-sided onboarding and jurisdiction uncertainty. In-app role design does not settle enforceability/custody/licensing questions.

**Discovery/recruiting:** interview 6 agency owners/finance leads, 3 of their actual client approvers and 2 accountants. Ask for the last SOW/change order, invoice, acceptance delay and collection follow-up; determine disputes per quarter, monthly billing, collection labor, whether escrow was ever requested/refused, and who pays. Ask for a paid concierge test using existing rails before custom contracts. Kill if agencies cannot introduce a client approver or will not change the workflow. User has no such network today, so customer access confidence is low.

## Remaining diligence limits

No customer conversations were conducted. No advertised service was paid for. No mainnet privacy transaction or real-asset volume was independently established. Source pages sometimes contradict their own or ecosystem maturity descriptions. That is a material reason to demand contract addresses, deployed revision/audit mapping, production provider list and real buyer references before launch commitments. No recommendation above should be presented as validated PMF or guaranteed institutional access.
