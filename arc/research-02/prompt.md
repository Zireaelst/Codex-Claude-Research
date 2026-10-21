# Research 02: Protocol and privacy comparison — BlindClaim

## Original prompt

Source: this conversation, message timestamp `2026-10-18T16:56:24.144Z` (UTC).

**Archive editorial note:** Original text follows, without updated conclusions. Any safety redactions use explicit `[REDACTED ...]` markers.

---

Act as a senior protocol researcher, cryptography-aware EVM engineer, and skeptical hackathon judge. Find an ambitious but shippable project for “Arc Microgrants: Built with Arc Studio.”

This is a new research pass. Do not default to CohortLock, generic escrow, a payment splitter, or a token launchpad. Do not write code, create a project, deploy, or transact. Research first and recommend a direction. Respond in English.

CONTEXT
Today is October 18, 2026. The supplied competition rules require a public app built with Arc Studio, Studio-created and tested smart contracts deployed on Arc mainnet, and at least one real USDC transfer through the app and contract. Submissions close November 1. Verify the current official rules and distinguish this Studio round from older Arc Microgrants rounds.

Your central question is:
“What technically impressive product or primitive has demonstrated value elsewhere in crypto, remains meaningfully underserved on Arc, and can be proven with a real Arc-mainnet USDC transaction before the deadline?”

Investigate two competing paths:
A. A strong product pattern from another ecosystem that Arc is missing.
B. A deeper privacy, cryptography, or verifiable-computation primitive with a compelling Arc-specific use case.

Do not favor either path in advance.

1. MAP THE COMPETITIVE LANDSCAPE
Examine ETHGlobal Showcase projects and their source repositories, especially:
- Arc-sponsored winners and finalists from 2025–2026;
- ETHGlobal projects built on Arc but awarded by other sponsors;
- privacy, ZK, confidential computation, agent payments, programmable USDC, and cross-chain settlement projects.

Also examine strong live products and notable hackathon projects across Base, Ethereum/L2s, Avalanche, Solana, and relevant privacy-focused networks. Include pons and AvaxHook as optional references, not anchors.

For each serious reference, verify:
- exact project and award, if any;
- problem and technical mechanism;
- testnet, mainnet, or demo-only status;
- live app, repository, deployed contract, and evidence of actual usage where available;
- whether an equivalent or close competitor already exists on Arc.

A showcase description is a team claim, not proof of production deployment or security. Do not label a project an Arc winner merely because it uses Arc. Do not infer that an Arc product is absent from failed search alone; state search scope and confidence.

Study at least 15 relevant projects at a screening level and 6–8 technically at source/repository level. Spend depth on findings that could change our choice, rather than producing a long catalog.

2. INVESTIGATE PRIVACY HONESTLY
Verify which Arc privacy capabilities are usable on public mainnet today, which are in development, and which require third-party protocols. Do not build a proposal around an unreleased Privacy Sector or AgentVM as though it already works.

Search for a narrow privacy problem with an identifiable user and a testable security claim. Consider, but do not limit yourself to:
- selective disclosure of USDC payment or payroll information;
- private conditional payouts or sealed bids;
- unlinkable agent payments and payment metadata;
- confidential invoices or B2B settlement;
- verifiable private eligibility, balances, or compliance predicates;
- ZK proofs, commitments/nullifiers, viewing keys, TEEs, MPC, FHE, and encrypted offchain data with onchain settlement.

For each promising privacy architecture, specify precisely:
- what data is hidden, from whom, and at what stage;
- what remains visible on Arc, including USDC transfers, gas payer, timing, amounts, events, RPC metadata, and withdrawals;
- trust assumptions, setup requirements, key custody, leakage paths, and failure modes;
- whether the privacy claim survives a realistic observer linking deposits and withdrawals;
- proof system or trusted service required, estimated implementation complexity, and what can actually be demonstrated in two weeks.

Reject “private” designs that merely encrypt data offchain while publishing linkable payment details, unless the limited privacy guarantee itself solves a real customer problem. Never claim anonymity, confidentiality, or trustlessness beyond what the mechanism proves.

3. FIND THE ARC GAP
Create 8–10 candidate ideas across both paths. At least three must be technically deep privacy/verifiability ideas; at least three must be proven cross-ecosystem product patterns adapted to Arc.

For each candidate, provide:
- target user and concrete pain;
- closest existing products, including Arc competitors;
- why the gap remains and why Arc improves the solution;
- one-sentence technical novelty;
- minimum architecture and smart-contract role;
- the exact real-USDC transaction that would prove it;
- biggest dependency, privacy/security risk, and deadline risk.

Separate “technically novel,” “novel on Arc,” and “commercially useful.” A difficult cryptographic demo with no user is not automatically a strong project. A chain port with no Arc-specific benefit is not automatically a gap.

4. PRESSURE-TEST THE BEST OPTIONS
Shortlist 4 candidates: two product-gap ideas and two privacy/deep-tech ideas. Score them against the competition’s official 30/25/25/20 criteria, plus defensible differentiation, technical depth, two-week feasibility, and security risk. Scores are your estimates, not predicted judge scores.

For each finalist, answer:
- What existing project most threatens its originality?
- What is the hardest technical claim to prove?
- Which dependency could make it impossible to ship by November 1?
- What would the smallest honest mainnet demo show?
- Would a real user choose it over an existing offchain or onchain option?

Recommend one winner and one backup. It is acceptable to recommend a less technically ambitious idea if the deep-tech candidates cannot honestly demonstrate their claims by the deadline. Conversely, do not downgrade a feasible privacy primitive just because it is harder than an escrow template.

5. TURN THE WINNER INTO A BUILDABLE RESEARCH BRIEF
Provide:
- precise product thesis and first user;
- trust/threat model and security invariants;
- architecture diagram in text;
- onchain versus offchain responsibilities;
- minimum contracts, tests, frontend, and external services;
- what is built and tested inside Arc Studio;
- independent mainnet deployment and public hosting workflow;
- a small-value real-USDC proof transaction and explorer evidence;
- 3-minute demo script;
- critical-path schedule through October 30, leaving submission buffer;
- 3 technical experiments that must succeed before full implementation.

Resolve the apparent eligibility conflict between the contest’s Studio-built-mainnet requirement and Arc Studio’s terms saying Studio does not deploy or host on mainnet on the builder’s behalf. If organizer confirmation is unavailable, state the exact unanswered question and do not treat an assumed workflow as confirmed.

EVIDENCE AND OUTPUT
Start with official competition, Arc/Circle, ETHGlobal award pages, project repositories, deployed contracts, and current protocol documentation. Use direct links for consequential claims. Label verified facts, project claims, and your inferences. Check publication and event dates.

Write a decision-focused report of about 1,800–2,200 words. Use compact comparison tables. Put the recommendation near the top, then show the evidence and technical reasoning. End with the single most important unresolved question and the next research/build decision. Stop before coding.

