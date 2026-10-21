# Research 02: Protocol and privacy comparison — BlindClaim

## Original result

Source: this conversation, message timestamp `2026-10-18T17:06:47.668Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

**Recommendation: BlindClaim—USDC rewards for verified customer feedback, without revealing which approved customer claimed.** Its core claim is narrow and testable: membership in a fixed cohort, one claim per campaign, and payment to a proof-bound recipient. Payments remain public.

**Backup: QuietInvoice**, stealth-address invoicing adapted to Arc’s shared USDC payment-and-gas balance. Neither invents new cryptography. BlindClaim offers the stronger demonstration; QuietInvoice has the simpler customer proposition.

These are conditional recommendations, not established market gaps. Research checked October 18, 2026; no implementation or transactions performed.

**Competition and platform reality**

The official [“Built with Arc Studio” round](https://dorahacks.io/hackathon/arc-microgrants-2/detail) confirms November 1 submissions, eight $500 grants, and the supplied **30% mainnet USDC / 25% Studio / 25% working product / 20% growth** weights. It requires Studio-created/tested contracts, a public Studio-built app calling them, and real Arc-mainnet USDC movement. This is distinct from the older twenty-grant round closing October 14. Previously Circle/Arc-funded projects are excluded.

The deployment conflict remains **an eligibility blocker**. [Studio’s terms](https://studio.arc.io/terms-of-use), §§1.2 and 4.1, contemplate exporting work and independently deploying/operating it; Studio does not deploy, transact, or host mainnet applications on builders’ behalf. That makes an external deployment workflow technically coherent, but I found no organizer statement explicitly accepting it for this round.

Arc mainnet launched September 16. Solidity/EVM contracts, RPC, wallets and USDC settlement are available. USDC uses **18 native decimals and six ERC-20 decimals against the same balance**—a consequential porting hazard. [Arc launch](https://www.arc.io/pressroom/circle-launches-arc-mainnet-an-economic-operating-system-for-the-internet), [EVM differences](https://docs.arc.io/arc/references/evm-differences).

**Native confidential balances, Privacy Sector and AgentVM are not usable assumptions.** Official materials describe privacy and AgentVM as developing capabilities. A working MVP must use independently verified third-party cryptography or explicitly limited metadata privacy.

**What the competitive scan actually establishes**

Below are 18 screened references. Awards are verified page labels; deployment and usage descriptions remain project claims unless supported independently. “Demo” does not establish production security.

| Reference | Mechanism, award and evidence status |
|---|---|
| [Manila](https://ethglobal.com/showcase/manila-fv16y), New York 2026 | Arc **Best Private Nanopayments**, plus Unlink/Dynamic awards. Private payroll and public vesting; testnet. Repository explicitly identifies mock USDC in its privacy pool. |
| [ACR](https://ethglobal.com/showcase/acr-sgdjr), ETHOnline 2026 | Arc **Best DeFi or Agentic Application**. Compute-price benchmarks and agent execution analysis. Showcase says testnet; current repository lists September 27 mainnet deployment. |
| [ArcBeam](https://ethglobal.com/showcase/arcbeam-e0bey), Buenos Aires 2025 | Circle **Best Crosschain USDC Experience with Circle’s Bridge Kit and Arc**; Privy sponsorship award. Testnet bridging/payment requests. |
| [Arcane–Tachyon](https://ethglobal.com/showcase/arcane-tachyon-2jkhj), Buenos Aires 2025 | Espresso cross-chain award, **not an Arc award**. Strategy vault demo; simulated TEE and mock exchange. |
| [Verdikt](https://ethglobal.com/showcase/verdikt-mi2xq), ETHOnline 2026 | API delivery verification/refunds; no award displayed. CRE simulator broadcasts, not production confidential execution. Linked repository returned 404. |
| [Vouch DeFi](https://ethglobal.com/showcase/vouch-defi-hfvw3), New York 2026 | Arc liquidity-hub first place; World ProveKit second; Chainlink CRE award. Private-income credit demo; input provenance remains crucial. |
| [PaintGlobal](https://ethglobal.com/showcase/paintglobal-v4pwo), Cannes 2026 | ETHGlobal finalist using Arc testnet; NFC identities, art auctions. Finalist status is not an Arc sponsor prize. |
| [HongBao](https://ethglobal.com/showcase/hongbao-oaust), New York 2026 | World-gated USDC gifts; Gateway testnet and explicit mock mode. Close eligibility-payout competitor. |
| [Remate](https://ethglobal.com/showcase/remate-jy0mg), ETHOnline 2026 | Hedera bond/Arc cash auction. Confidential CRE simulated; operator confirms delivery. Not atomic cross-chain settlement. |
| [Cloak](https://ethglobal.com/showcase/cloak-7zm7s), Cannes 2026 | Base Sepolia private invoicing through Unlink; server-controlled temporary swap wallet. Strong privacy claims exceed demonstrated evidence. |
| [Gabhru](https://ethglobal.com/showcase/gabhru-yf6hd), ETHOnline 2026 | ENS stealth payments; Ethereum resolver address and Base-mainnet architecture reported. No independent adoption established. |
| [CoW Protocol](https://docs.cow.fi/cow-protocol/reference/contracts/core) | Live signed-intent batch settlement across Ethereum, Base, Avalanche and other networks; deployed addresses documented. |
| [Squads](https://docs.squads.so/main/development) | Live Solana treasury permissions and spending limits; deployment addresses and verifiable-build instructions available. Usage figures are provider-reported. |
| [Umbra](https://github.com/ScopeLift/umbra-protocol) | Live stealth-payment implementation/app; recipient association protection, not hidden amounts or sender anonymity. |
| [Semaphore](https://docs.semaphore.pse.dev/) | Deployed membership/nullifier primitive; audited versions and setup artifacts. Not itself a payment product. |
| [Unlink](https://docs.avax.network/integrations/unlink) | Avalanche integration documents private UTXO transfers and relaying. This does not establish native-USDC Arc-mainnet support. |
| [Arcveil](https://arcveil.dev/docs/bridge) | Privacy-pool bridge documentation explicitly marks bridge components **not deployed**; adapter/relayer assumptions remain. |
| [Oasis Sapphire](https://docs.oasis.io/build/sapphire/) | Available confidential EVM infrastructure; bringing its decisions to Arc introduces attestation/transport trust. |

Eight repository-level inspections informed the decision: [Manila](https://github.com/max-andrew/manila), [ArcBeam](https://github.com/kavehtehrani/arcbeam), [ArcaneFi](https://github.com/muskbuster/AcaneFi), [ACR](https://github.com/kaustubh76/ACR---Arc-Compute-Rate), [Umbra](https://github.com/ScopeLift/umbra-protocol), [Semaphore](https://github.com/semaphore-protocol/semaphore), [CoW](https://github.com/cowprotocol/contracts), and [Squads](https://github.com/Squads-Protocol/v4). Scope included repository architecture, deployment records and selected implementation files—not executed tests or audits.

Three findings matter particularly:

- Manila separates private mock-token salaries from public native-USDC vesting; its award does not establish production private payroll.
- Umbra’s original contract sweeps native balance as toll revenue while holding ERC-20 payments. **My inference:** directly porting that accounting onto Arc’s shared balance could expose custodial USDC.
- Semaphore exposes separate proof verification and nullifier consumption. A payout wrapper must prevent outsiders consuming a proof without paying its recipient. Recent [releases](https://github.com/semaphore-protocol/semaphore/releases) also fix root-expiration handling.

Arc is already crowded: [Cycles](https://community.arc.io/public/blogs/arc-cycles-multilateral-clearing-and-settlement-on-arc-2026-07-17), [Setoff](https://setoff.anshverma.tech/docs) and Contraflow undermine a netting pitch; [Arc Portal](https://www.arc.io/blog/arc-portal-the-easiest-place-to-get-started-on-arc) undermines generic agent-budget differentiation.

Search scope covered official ecosystem material, ETHGlobal 2025–2026 showcases, GitHub, and targeted privacy/netting/eligibility/invoicing searches. Confidence is **high that generic payment categories are occupied; moderate-to-low that BlindClaim’s exact workflow is underserved**. No complete Arc application registry was available.

**Eight candidates, filtered**

All customer and commercial-value statements below are hypotheses. “Novel on Arc” remains provisional; none warrants claiming new cryptographic research.

| Candidate and first customer | Differentiation, minimum mechanism and exact USDC proof | Main dependency, security and deadline risk |
|---|---|---|
| **BlindClaim — privacy**. Arc wallet team rewarding candid beta-user feedback without linking respondents to known wallets. Closest: Semaphore, HongBao. | Frozen membership root, browser proof, campaign nullifier and payout contract. Claim **0.10 USDC** alongside encrypted-feedback commitment. Arc gives sponsor and relayer one operating currency. | Correct artifacts and enrollment; colluding members/metadata shrink privacy. Medium implementation risk; customer need unvalidated. |
| **QuietInvoice — product**. Freelancers avoiding public aggregation of client payments. Closest: Umbra, Gabhru, Cloak. | Stealth derivation, announcement and noncustodial payment adapter; forward **0.10 USDC** to a fresh address. Received USDC can fund later gas, removing separate-token funding linkage. | Key recovery/scanning; consolidation deanonymizes. No custom proofs, medium deadline risk; Arc equivalent search inconclusive. |
| **SealedRFQ — deep tech**. Small buyers seeking confidential supplier quotes. Closest: Remate, Sapphire. | Encrypted bids, attested confidential comparison, Arc award contract; winner receives **0.10 USDC**. Novelty is constrained attestation-to-payment binding. | Production TEE access, attestation verification and operator censorship. High risk; no anonymity after public settlement. |
| **InvoiceOnce — product**. Two independently operated reimbursement agents sharing a budget. Closest: Request Network and verified e-invoice research. | Issuer-signed canonical invoice ID plus atomic consumed-ID/payment registry; first **0.10-USDC** reimbursement succeeds, replay fails. | Issuers can mint alternate IDs; only participating payers share protection. Low technical risk, substantial integration/acquisition risk. |
| **NetSettle — product**. Reciprocally invoicing agencies. Closest: Cycles/Setoff already on Arc. | All-party signed obligations and atomic residual settlement; settle **0.02 USDC** instead of three gross transfers. | No demonstrated gap; signatures cannot establish external legal discharge. Reject as redundant. |
| **AgentBudget — product**. API operators delegating spending. Closest: Squads, Arc Portal/Arcanum. | Merchant/epoch-limited session authority; allow **0.01 USDC**, reject excess. | Revocation and concurrent accounting; easy build, weak originality. Reject generic version. |
| **PrivatePayroll — deep tech**. Small remote teams. Closest: Manila/Unlink. | Pool commitments, encrypted notes, nullifiers, viewing access; private **0.10-USDC** transfer. | Native Arc-mainnet token support, anonymity set, custody and payroll records. High deadline risk; reject until infrastructure proven. |
| **OutcomeBond — product**. Buyers of deterministic machine services. Closest: Verdikt/Notch. | Bond plus precisely defined failure receipt; slash **0.10 USDC** for a provable failed obligation. | Proving non-delivery without trusting observer; disputes and false slashing. Reject broad “AI judges quality” framing. |

InvoiceOnce has precedent in a [September 29 Ethereum research implementation](https://arxiv.org/abs/2609.37819), evaluated on a private network—not proof of public adoption. Its commercial advantage requires several payers sharing one registry.

**Privacy claims that survive scrutiny**

BlindClaim hides the connection between an enrolled commitment and a claim. It does **not** hide sponsor, reward amount, recipient, transaction time, relayer, public proof/nullifier, events or subsequent spending. Relayers/RPC providers can observe network metadata. Enrollment timing, identifiable feedback, collusion and wallet consolidation can identify claimants. Sponsor-funded rewards avoid individual deposit–withdrawal correlation, but do not provide general transaction anonymity.

QuietInvoice hides public association with the recipient’s long-term identity; payer and amount remain visible. Sender, invoice server and viewing-key holder may know the association. Withdrawal to a known wallet destroys that protection.

SealedRFQ hides bids before award from public observers, conditional on TEE hardware, attestation and key-management integrity. Winner/payment become public; losing bids may remain encrypted. MPC or FHE would replace assumptions and add integration work, not automatically remove leakage.

Encryption alone is worthwhile only for genuinely private invoice text or feedback. It cannot make visible payment graphs confidential.

**Four finalists**

Scores are my estimates, out of five. Weighted total applies only the official 30/25/25/20 criteria.

| Finalist | USDC / Studio / product / growth → total | Differentiation / depth / feasibility | Security risk |
|---|---|---|---|
| **BlindClaim** | 5 / 5 / 4 / 3 → **87/100** | 4 / 4 / 4 | Medium |
| **QuietInvoice** | 5 / 4 / 4 / 3 → **82** | 3 / 3 / 4 | Medium |
| **InvoiceOnce** | 5 / 4 / 3 / 3 → **77** | 2 / 3 / 5 | Low–medium |
| **SealedRFQ** | 4 / 3 / 3 / 3 → **66** | 3 / 5 / 2 | High |

- **BlindClaim:** HongBao threatens originality. Hardest claim is end-to-end identity unlinkability, not membership verification. Artifact/Studio incompatibility could block delivery. The honest demo proves eligibility, replay rejection and payment—not population anonymity. A customer chooses it only if independent payout enforcement and privacy matter more than survey-platform convenience.
- **QuietInvoice:** Gabhru/Umbra threaten originality. Secure derivation, recovery and spending are hardest. Wallet/scanner compatibility is the blocker. Demo shows a fresh recipient receiving spendable USDC, with visible leakage. Freelancers could use it after the grant; recruitment should target existing stablecoin earners.
- **InvoiceOnce:** Request/e-invoice systems threaten originality. Canonical identity across issuers is hardest. Partner adoption, rather than Solidity, blocks usefulness. Demo prevents a duplicate within one registry. A single company’s database usually suffices.
- **SealedRFQ:** Remate threatens originality. Authentic confidential execution and complete bid inclusion are hardest. Production attestation access could make shipping impossible. A demo must distinguish TEE execution from simulation. Buyers need recurring competitive procurement to justify it.

**Buildable brief: BlindClaim**

**Thesis:** Let an Arc product team pre-fund feedback rewards that approved customers can redeem once without publishing their roster identity.

Acquire one wallet or developer-tool team with 15–30 willing beta users. No trading liquidity, bridge or yield dependency; sponsor funds the complete reward budget. Growth would come from repeat research campaigns and an embeddable claim component, not token incentives.

```text
Team approves identity commitments → freezes cohort root + funds campaign
Customer browser → encrypts feedback → generates membership proof
Proof + recipient + ciphertext digest → replaceable relayer
Arc claim contract → verifies → consumes nullifier → transfers USDC
Researcher decrypts feedback; public explorer verifies payment
```

The enrollment operator is trusted for eligibility and duplicate enrollment. Users retain randomly generated identity secrets and recipient keys. Relayer compromise may censor or observe requests, but must not redirect payment. No claim proves feedback quality.

Minimum contracts: a campaign/payout contract and pinned upstream verifier dependencies. Freeze root, reward, expiry and researcher key before opening. Bind proof message to chain, contract, campaign, recipient and ciphertext digest. Consume application-owned nullifiers atomically; use verification without a separately callable consumption dependency. Require conservation of funded rewards, exact recipient binding, replay resistance and no administrator withdrawal before expiry.

Failed transfers must revert nullifier consumption. Unclaimed rewards return to the sponsor after expiry. Lost identity secrets cannot receive an administrator override without weakening uniqueness. Public ciphertext retention and participant consent need an explicit policy.

Inside Studio: create the application contract, integration harness, frontend and adversarial tests; review upstream verifier integration and generated code. Test wrong roots, recipients, domains, duplicate/concurrent claims, expiry, failed USDC transfers, precision and sponsor refunds. Preserve Studio history and test evidence.

Outside Studio—**proposed, not organizer-confirmed**—export the same source, independently review/reproduce builds, deploy using the builder’s wallet and Arc-compatible Foundry, verify contracts, and host the exported app publicly.

Runtime dependencies: pinned Semaphore identity/group/proof libraries and matching artifacts, viem/wagmi, Arc RPC, static hosting and a minimal relayer. Studio, Foundry and Arc documentation MCP are build-time tools; MCP is unnecessary at runtime.

Three experiments must pass first:

1. Matched corrected verifier/circuit/artifacts accept valid browser proofs and reject malformed inputs on Arc testnet.
2. Proof-bound payout survives replay, front-running, domain mutation and transfer-failure tests.
3. A metadata walkthrough finds no automatic enrollment-wallet linkage; mobile proving remains usable. Multiple independently held identities are required—synthetic members demonstrate correctness only.

Schedule: **October 18–20:** eligibility confirmation, customer validation, experiments. **21–23:** Studio contracts/tests. **24–25:** frontend, relayer, enrollment. **26–27:** adversarial review and independent deployment rehearsal. **28–29:** authorized mainnet proof and customer walkthrough. **30:** freeze evidence; October 31–November 1 submission buffer.

Three-minute demo: **0:00–0:30** show funded campaign and privacy boundary; **0:30–1:30** encrypt feedback, generate proof and claim **0.10 USDC**; **1:30–2:15** show recipient balance, explorer transfer and failed replay; **2:15–3:00** show Studio tests, independent build provenance and remaining leakage. Fund approximately **1 USDC**, keeping relayer gas separate.

Submit Studio URL, public app/repository, pinned dependency versions, verified addresses, successful explorer transaction, video and builder profile.

**Strongest objection:** this could remain a polished Semaphore wrapper without a customer who values its guarantees. A credible Arc-native equivalent, failed artifact experiment, or unwilling pilot would change my recommendation.

**Single unresolved question:** Will organizers explicitly accept Studio-created/tested code exported for independent mainnet deployment and public hosting, including a pinned upstream ZK verifier?

The next decision is to obtain that answer through the competition’s organizer contact/Q&A and validate one pilot before authorizing implementation.
