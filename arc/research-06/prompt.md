We have chosen a project direction: build a **full-featured meme and creator token launchpad on Arc**, using Arc Studio throughout the build where possible. I need a research-backed product specification, technical architecture, implementation roadmap, and ready-to-use Arc Studio prompts. Do not start coding or deploy contracts yet.

## Product direction

Creators should choose one of two launch paths:

1. **Classic / instant launch on Uniswap v3:** create a fixed-supply token and USDC pool immediately, lock the founding liquidity, and enable trading from launch.
2. **Programmable launch on Uniswap v4:** start on a fair USDC bonding curve, then graduate into a locked Uniswap v4 pool. The creator can select compatible, bounded pool rules such as anti-snipe protection, dynamic fees, burns, LP rewards, and community rewards.

Present these as understandable product choices rather than assuming users know v3 and v4. A token should have one canonical launch path. Do not pretend that v4 hooks work on a v3 pool or that rules on one pool control trading in every possible external pool.

The ambition is a **feature-rich, complete launchpad**, inspired by the strongest ideas from Pump.fun, PONS, AvaxHook/Hookr, Flaunch, Zora, Clanker, Four.meme, and other leading launchpads. It must have a distinctive reason to exist on Arc. Explore a community layer in which transparent USDC trading revenue can fund creator teams, meme/content bounties, and ongoing community activity. Do not treat “we combined many features” as differentiation by itself.

## Research tasks

- Reassess current Arc competitors, including ArcPad, Arcfun, moon, Arcade, Parabola, and other live or announced launchpads. Verify contract addresses, actual deployments and demonstrated product behavior where possible. Separate live facts from website claims.
- Compare leading launchpads across chains. For each, identify its best product mechanics, growth loops, revenue model, launch protection, liquidity model, and weaknesses.
- Verify official Uniswap v3/v4 deployments on Arc, USDC behavior and decimals, Arc Studio’s contract/testing/app capabilities, Arc Studio CLI workflow, and whether Studio itself supports mainnet deployment.
- Evaluate at least three plausible product positions, then recommend one with a specific first user group and a credible reason they would choose us over existing Arc launchpads.

## Design tasks

Produce a detailed specification covering:

- Complete user journeys for creator, buyer, trader, contributor, and community manager.
- Separate v3 and v4 launch lifecycles, including exact states, failure recovery, refunds, graduation, LP custody/locking, fee claims, and what is immutable.
- A feature matrix: shared features, v3-only features, v4-only features, and later extensions.
- Contract boundaries and data flow: token factory, v3 launcher and locker, curve, v4 graduation executor, hook/module registry, fee escrow/splitter, community USDC treasury, bounty payouts, and any needed indexing service.
- Economic parameters with sensible bounds: supply, curve and graduation parameters, pool fees, creator/protocol/community splits, launch fees, reward funding, and abuse-resistant defaults.
- Security analysis of curve math, price continuity, slippage, first buys, MEV, external pools bypassing hook rules, locked-LP fee collection, hook permissions, fee accounting, USDC’s Arc-specific representations, reentrancy, griefing, sybil attacks, and malicious creator settings.
- Analyze whether an “every Nth buy wins the pot” mechanic can be made fair. If it is predictably exploitable, redesign it or exclude it with a clear explanation.
- Frontend screens, indexer/API needs, public token pages, discovery, charts, creator dashboards, shareable social content, and the post-launch community loop.
- Which functionality is truly feasible on Arc testnet and mainnet. Mark any missing dependency or unverified assumption as a gate.

## Delivery roadmap

Give me a staged roadmap that leads to a **working MVP**, then expands toward the full platform. Each stage needs concrete deliverables and acceptance criteria. The MVP must be a usable product, not a landing page or token factory alone. Favor a narrow, secure first launch path if implementing both paths at once would prevent shipping; keep the second path in the architecture and roadmap.

Explain how to build and test the contracts and app in Arc Studio, export/review the result, deploy to Arc mainnet if Studio cannot do that directly, and verify a small real-USDC transaction. Do not perform any deployment or spend funds during this planning task.

## Arc Studio handoff

If the Arc Studio CLI is available, start with read-only checks such as `arc-studio whoami`, `arc-studio agent-guide`, and `arc-studio skills --json`. Use available MCP tools or official documentation to verify capabilities. Never print or expose credentials. If CLI access fails, continue the research and produce prompts I can paste into Arc Studio manually.

Provide:

1. A concise **master product brief** for Arc Studio.
2. A sequence of **ready-to-run Studio prompts**, one coherent build task per turn: first contracts and tests, then app, then integration and adversarial review.
3. The corresponding CLI commands using named sessions, `--output json`, and `--prompt-file` where appropriate. Respect Studio’s prompt-size limit. Include a manual copy/paste alternative for each turn.
4. A verification checklist with explicit pass/fail criteria before any mainnet launch

