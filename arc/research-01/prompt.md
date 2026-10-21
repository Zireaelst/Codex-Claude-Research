# Research 01: Arc Microgrants product scan — CohortLock

## Original prompt

Source: this conversation, message timestamp `2026-10-18T14:09:59.577Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

Act as a critical onchain product researcher, EVM engineer, and hackathon advisor. Research project opportunities for “Arc Microgrants: Built with Arc Studio” before we choose what to build. Do not write code, create a project, deploy, or send transactions. Write your findings in English.

CONTEXT
Today is October 18, 2026. The program description I provided says submissions close November 1, 2026. It requires a working public app built with Arc Studio, contracts created and tested through Studio, deployment on Arc mainnet, and at least one real USDC transfer through the app and contract. Verify the current rules on the official competition page. Do not confuse this round with an earlier Arc Microgrants round.

The judging weights are: verifiable mainnet USDC movement (30%), use of Arc Studio across the build (25%), working product (25%), and potential to grow (20%). We have roughly two weeks, so favor a sharp, demonstrable product over a broad platform.

STARTING REFERENCES
- Arc Studio: https://studio.arc.io/
- Arc docs: https://docs.arc.io/
- pons: https://docs.ponsfamily.com/
- AvaxHook: https://docs.avaxhook.fun/#what-makes-it-different

pons and AvaxHook are inspiration, not specifications. Study what makes their product experiences compelling: launch flows, programmable rules, locked commitments, creator economics, discovery, and visible onchain activity. Do not assume a token launchpad or Uniswap v4 integration is the right answer for Arc.

RESEARCH TASK 1 — ARC REALITY CHECK
Establish what Arc mainnet and Arc Studio currently support, particularly USDC transfers, gas, smart contracts, wallet support, deployment, app hosting, indexing, and relevant payment infrastructure.

Resolve a critical apparent conflict: the competition asks for an Arc Studio-built mainnet submission, while Arc Studio’s public terms say Studio does not deploy or transact on mainnet or host apps on the builder’s behalf. Find the organizer’s accepted build and deployment workflow. If it remains unclear, label it an eligibility blocker and give the fastest way to confirm it.

RESEARCH TASK 2 — CROSS-ECOSYSTEM OPPORTUNITY SCAN
Look beyond Arc. Examine working products and recent experiments on at least four relevant ecosystems, such as Avalanche, Base, Solana, Ethereum/L2s, and other stablecoin-focused networks. Search across these themes:

- programmable USDC payments and conditional payouts;
- escrow, milestones, bounties, and refunds;
- revenue splits, shared treasuries, and creator payments;
- AI-agent or software-to-software payments;
- launchpad-style user experiences and programmable “hooks”;
- one or two unexpected categories you discover during research.

Identify 6–10 specific products or projects, link their primary sources, and state what is actually live versus announced or planned. For each promising pattern, investigate whether an equivalent already exists on Arc. “I could not find one” is not proof that none exists; report your search scope and confidence.

Evaluate whether bringing the pattern to Arc solves a real problem better because of Arc’s properties or ecosystem. Reject ideas whose only distinction is “the same app on a different chain.” Include likely user acquisition, liquidity dependencies, custody/trust assumptions, and material legal or platform constraints where relevant.

RESEARCH TASK 3 — GENERATE AND FILTER IDEAS
Generate 6–8 distinct Arc project ideas, including:
1. at least one concept inspired by pons or AvaxHook without copying its token-launch mechanics;
2. at least one programmable USDC payment concept;
3. at least one software-to-software or agent payment concept;
4. at least one unconventional idea from the cross-ecosystem scan.

For each idea, give:
- first customer and painful job to be done;
- existing alternative and closest competitor;
- specific differentiation and why Arc matters;
- smallest contract + app that proves the claim;
- exact real-USDC mainnet demo transaction;
- hardest technical dependency;
- largest product or security risk.

If you use the word “hook,” distinguish a Uniswap v4 swap hook from a payment rule and an offchain webhook. Do not imply they are interchangeable.

Shortlist the best three ideas. Compare them against the competition’s judging criteria, originality, two-week feasibility, security complexity, and credible post-grant potential. Challenge each idea with: “Does this already exist?”, “Why must this be onchain?”, and “Who would use it after the demo?” Recommend one winner, even if it differs from my references.

RESEARCH TASK 4 — PLAN THE WINNING MVP
For the recommended idea, provide:
- a one-sentence pitch and a narrow first user;
- the minimum user journey and a three-minute demo script;
- contract responsibilities, essential security invariants, and failure/refund paths;
- exactly what must be created, tested, and reviewed in Arc Studio;
- what must happen outside Studio for mainnet deployment and public hosting;
- the smallest safe real-USDC transaction that proves the product works;
- essential SDKs/APIs and development tools, separating build-time MCP tools from runtime dependencies;
- a prioritized schedule through November 1;
- a submission evidence checklist: Studio project URL, live app, repo, contract addresses, explorer transaction, video, and builder profile.

SOURCE AND OUTPUT RULES
Prefer current official documentation, competition rules, project documentation, deployed contracts, public repositories, and live apps. Cite consequential claims with direct links. Distinguish verified facts, project claims, and your own inferences. Note source dates and unresolved questions. Do not invent Arc ecosystem gaps or technical support.

Keep the answer decision-focused: approximately 1,200–1,600 words, compact comparison tables, no exhaustive catalog. End with your recommendation, its strongest objection, the evidence that would change your mind, and at most three questions for me. Stop before implementation.

