# Research 01: Arc Microgrants product scan — CohortLock

## Original result

Source: this conversation, message timestamp `2026-10-18T14:14:58.901Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

**Recommend CohortLock: minimum-enrollment workshop payments with fixed creator splits and deadline refunds.** It offers a clear demonstration without liquidity pools or a delivery oracle. The recommendation is conditional: validate one paying organizer and resolve the Studio deployment eligibility question first.

Research checked **October 18, 2026**. “Documented” below means supported by primary sources; project-reported deployment or usage is not an independent security audit.

**The competition and Arc reality**

The [official Studio-round page](https://dorahacks.io/hackathon/arc-microgrants-2/detail) confirms eight **$500 USDC** grants, a November 1 deadline, and your **30/25/25/20** weights. Contracts must be written and tested in Studio; the Studio-built public app must move real mainnet USDC through its contract. Previously funded Circle/Arc work is ineligible. Earlier-round entries may qualify, but each project receives only one microgrant.

The page’s timeline displays November 2, 04:59 without an explicit timezone in the retrieved view, while its description says November 1. **Submit October 30; confirm the cutoff timezone.**

[Studio’s terms, §§1.2 and 4.1](https://studio.arc.io/terms-of-use), explicitly require independent mainnet deployment and operation outside Studio. The coherent workflow is:

**Studio authors/tests → export to GitHub → independently review → deploy with your wallet/tooling → externally host.**

However, the competition does **not explicitly confirm** that workflow, and its [Q&A](https://dorahacks.io/hackathon/arc-microgrants-2/qa) showed no clarification. **Eligibility blocker:** obtain written organizer confirmation that externally deploying and hosting Studio-generated code qualifies. Fastest route: the competition’s organizer Message/Q&A, quoting those terms and asking about external deployment, hosting, and permitted external fixes. I have not contacted anyone.

| Capability | Verified support and engineering consequence |
|---|---|
| Mainnet | Official docs announce September 16 launch. Chain **5042**, RPC `https://rpc.mainnet.arc.io`, [explorer](https://explorer.arc.io/). [Network configuration](https://docs.arc.io/arc/references/connect-to-arc) |
| USDC/gas | Native USDC uses **18 decimals**; its ERC-20 interface uses **6**, sharing one balance. USDC pays gas; retain a separate spending reserve. Solidity/EVM support has Arc-specific differences, including blocklist-enforced transfer failures. [EVM reference](https://docs.arc.io/arc/references/evm-differences) |
| Wallets/deployment | MetaMask, Rabby, Coinbase Wallet and Rainbow setup is documented, alongside viem/wagmi. [Arc Foundry](https://docs.arc.io/arc/tutorials/install-arc-foundry) supports Arc-specific testing/deployment. |
| Studio/hosting | Contract generation, initial reviews, testnet deployment, frontend preview and tracing are advertised. Production hosting is external; AgentVM remains “coming soon.” [Studio](https://studio.arc.io/) |
| Indexing/payments | JSON-RPC logs suffice for this MVP. Current [system-event documentation](https://docs.arc.io/arc/references/usdc-system-events) describes two transfer emitters—avoid double counting. Some older indexing guidance conflicts. Circle reports mainnet CCTP, Gateway and payment infrastructure; none needs to become an MVP dependency. [Launch announcement](https://www.arc.io/blog/arc-economic-os-internet) |

**What the cross-ecosystem scan suggests**

These seven references span Avalanche, Base, Solana, Ethereum/Optimism and Robinhood Chain.

| Product | Live versus planned evidence; transferable lesson |
|---|---|
| [pons](https://docs.ponsfamily.com/) | Documents deployed factories and active launches on Robinhood Chain. Single-transaction creation, locked liquidity, progress displays and snapshotted creator economics make commitments legible. Fully immutable automated buybacks remain future work. |
| [AvaxHook](https://docs.avaxhook.fun/contracts) | Publishes live Avalanche contracts. Selectable trading rules and launch/discovery flows are compelling. External audit is planned; emergency registry powers qualify “immutable” marketing. |
| [Juicebox](https://juicebox.money/learn) | Working Ethereum/L2 fundraising app; [Base project activity](https://juicebox.money/base%3A3) documents V6. Inspectable funding rules matter more than token issuance. |
| [Splits Recoup](https://splits.org/protocol/docs/templates/recoup/) | Deployed mainnet template, including Base/Avalanche: repay costs before distributing profits. A generic waterfall is already commoditized. |
| [Streamflow](https://streamflow.finance/faqs) | Operating Solana app for vesting, payments and escrow. Public schedules and claims replace spreadsheet coordination. |
| [x402 V2](https://x402.org/x402-v2-launch/) | Released protocol/SDK supporting Base and Solana payment flows. Paying an endpoint does not itself prove useful delivery. |
| [Drips](https://docs.drips.network/support-your-dependencies/overview/) | Operating Ethereum/other-network dependency funding. Unexpected opportunity: route revenue to software dependencies rather than only direct collaborators. |

**Arc is not empty.** [ArcBounty](https://www.arcbounty.app/developers) documents mainnet escrow and arbitration; [CrowdMint’s repository](https://github.com/mliell/crowdmint) documents testnet crowdfunding/refunds, with yield planned. [SELAT’s October 12 spotlight](https://www.arc.io/blog/how-selat-uses-circle-gateway-to-make-arc-the-home-treasury-for-every-agent) describes per-call escrow/refunds. [PayNote’s June showcase](https://community.arc.io/public/forum/boards/ecosystem-showcase-and-launches-pdq/posts/paynote-payment-coordination-infrastructure-on-arc-drdofmo6dz) claims working payment links; mainnet status was not established there.

Search scope: Arc’s ecosystem directory, community showcases, official blogs, public repositories, and targeted searches for crowdfunding, workshops, bounties, recoup, dependency funding and API refunds. Confidence is **high that generic payments/escrow overlap exists**, but **low that any narrower category is absent**.

A **Uniswap v4 swap hook** executes pool callbacks; a **payment rule** controls settlement; an **offchain webhook** notifies a server. They are different mechanisms. Borrow the references’ readable commitments and visible activity, not their swap machinery.

**Six candidate products**

All demonstrations below are proposed **real Arc-mainnet USDC transfers through the app’s contract**, excluding gas.

| Idea; first customer and painful job | Alternative, differentiation and Arc rationale | Smallest proof; hardest dependency and biggest risk |
|---|---|---|
| **CohortLock**: workshop organizer cannot commit instructor costs before minimum enrollment | Luma/manual refunds; CrowdMint. Fixed-price seats, immutable instructor/producer split, enrollment deadline. Arc-native communities already holding USDC avoid another gas asset. | Launch/join/claim page plus escrow. Two **0.01** deposits release **0.016/0.004**. Dependency: deadline/accounting correctness. Risk: organizer fails after payout. |
| **MilestoneReceipt**: small agency needs deposit-backed approval and payment evidence | Manual invoices; ArcBounty. Narrow client acceptance receipts instead of an open marketplace. Arc benefits existing USDC-paying teams. | One milestone, approve/refund interface; **0.10** escrow → contractor. Dependency: acceptance/timeout design. Risk: buyer withholding approval or disputed quality. |
| **CostFirst**: creator duo needs expenses repaid before revenue sharing | Spreadsheet; Splits Recoup. Invoice-specific recoup ledger for Arc revenue. | Two-tier waterfall/dashboard; **0.10 → 0.06** expense recovery, **0.02/0.02** collaborators. Dependency: payout integration. Risk: fake expenses/off-contract revenue. **Reject generic port.** |
| **CallBond**: API buyer fears paying for failed requests | x402 plus manual credits; SELAT. One narrowly defined response-validity guarantee. Arc fits agent USDC treasuries. | Escrow and request receipt UI; **0.01** releases on attestation or refunds on timeout. Dependency: trustworthy attester. Risk: valid-looking but worthless output. |
| **DependencyTip**: paid tool maker wants dependencies compensated automatically | GitHub Sponsors; Drips. Checkout-linked, fixed dependency receipts rather than a donation directory. Arc matters only for existing Arc sales. | Three-recipient splitter/receipt; **0.10 → 0.08/0.01/0.01**. Dependency: authenticated maintainer addresses. Risk: little willingness to divert revenue. |
| **RefundClock**: API subscriber wants unused prepaid time recoverable | SaaS billing; Streamflow-style schedules. Visible time accrual and cancellation, denominated entirely in USDC. | Prepaid entitlement/refund screen; **0.10** deposit, halfway cancellation pays **0.05/0.05**. Dependency: runtime access enforcement. Risk: time purchased does not guarantee uptime. |

Acquisition should start with **one organizer**, one agency, or one API maintainer—not a marketplace launch. None requires trading liquidity; all require funded wallets. Escrows hold customer funds in contracts, and issuer blocking remains relevant. Consumer refund obligations, service terms and recipient tax treatment need jurisdiction-specific consideration; avoid investment promises and transferable revenue rights.

**The shortlist**

Design estimates, **1–5**; weighted score uses the official criteria, not predicted judging outcomes.

| Candidate | USDC 30% | Studio 25% | Product 25% | Growth 20% | Weighted | Originality / two-week feasibility / security complexity |
|---|---:|---:|---:|---:|---:|---|
| CohortLock | 5 | 5 | 5 | 3 | **92/100** | Medium / high / moderate |
| DependencyTip | 5 | 5 | 4 | 3 | **87/100** | Low–medium / high / low |
| CallBond | 5 | 5 | 3 | 3 | **82/100** | Medium / medium / high |

- **CohortLock:** Already exists? Crowdfunding primitives do. Why onchain? Organizer cannot rewrite funding/refund terms. After demo? Repeat workshop organizers—if they actually accept USDC.
- **DependencyTip:** Already exists? Drips/Splits cover most mechanics. Why onchain? Enforce allocation at checkout. After demo? Arc tool vendors; distribution is unproven.
- **CallBond:** Already exists? SELAT materially overlaps. Why onchain? Shared escrow across operators. After demo? API merchants, but attestation disputes weaken the proposition.

Arc is a useful settlement environment, **not a defensible moat**. Without an Arc-native customer, these become chain ports.

**Winning MVP proposal**

Pitch: **“Launch a paid workshop only when enough seats are funded; otherwise participants recover their USDC.”**

First user: one independent Arc educator paying an instructor and producer.

Minimum journey: publish price, minimum seats, cap, deadline and split → participants fund seats → anyone finalizes after deadline → recipients claim if successful; participants claim refunds otherwise.

Three-minute demo:

1. **0:00–0:40:** Show Studio project, tests and immutable workshop terms.
2. **0:40–1:30:** Two wallets buy **0.01-USDC** demo seats; show enrollment and receipts.
3. **1:30–2:15:** Finalize an expired successful cohort; claim **0.016/0.004 USDC**.
4. **2:15–3:00:** Refund a **0.01-USDC** failed cohort; show explorer evidence.

Use shortened, clearly labelled demo deadlines. **0.03 USDC total principal** proves both paths; it is a practical tiny demonstration, not a protocol minimum. Fund estimated gas separately.

Contract responsibilities: immutable cohort terms, contribution accounting, finalization and pull-based claims. Invariants: liabilities never exceed assets; no double claims; success and failure are mutually exclusive; no mutable recipients, arbitrary calls or administrator withdrawals. Use six-decimal ERC-20 accounting consistently. Reentrancy protection and isolated claims prevent one failing recipient blocking everyone. Refunds cover failed enrollment or pre-settlement organizer cancellation; post-payout service failure remains a disclosed trust assumption.

Inside Studio: create the contract, frontend, ABI wiring and tests; review authorization, deadline boundaries, rounding, cancellation, duplicate claims, malicious callers and failed transfers. Preserve review outputs and test traces.

Outside Studio, **after eligibility confirmation**: independently review exported code, reproduce tests with Arc-aware tooling, deploy/sign with the builder’s wallet, verify source and host the app externally. Runtime needs only viem/wagmi, wallet connection, RPC and hosting; event reads can avoid a separate indexer. Studio and the [Arc documentation MCP](https://docs.arc.io/ai/mcp) are build-time tools, not runtime services.

| Dates | Priority |
|---|---|
| Oct 18–19 | Resolve eligibility; interview organizer; confirm willingness to charge USDC |
| Oct 20–23 | Studio contract, app and adversarial tests |
| Oct 24–26 | Independent review; testnet success/refund rehearsal |
| Oct 27–29 | Authorized mainnet deployment, tiny transfers, public-host verification |
| Oct 30 | Submit complete evidence |
| Oct 31–Nov 1 | Buffer for corrections |

Submission checklist: **Studio project URL, live app, public repo/commit, contract addresses, explorer transaction links, walkthrough video, builder profile**, plus a concise explanation of Studio’s role.

**Recommendation:** choose CohortLock only with an organizer pilot. Its strongest objection is that conventional ticketing may solve the real problem better. An existing Arc product offering the same workflow—or interviews showing unwillingness to pay in USDC—would change my recommendation.

1. Can you recruit one workshop organizer this week?
2. Are their intended attendees already using Arc USDC?
3. Has this project previously received Circle or Arc funding?
