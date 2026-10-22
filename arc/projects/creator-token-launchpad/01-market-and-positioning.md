# Market evidence and product positioning

> Current planning document, organized from [the complete original report](../../research-06/result.md). The [final user decision](00-final-decision.md) takes precedence: both v3 and v4 are required for the complete initial product. Sequential engineering does not remove either path from scope. Research claims retain the original evidence limitations; this is not a fresh deployment verification.

**The competitive evidence changes the positioning.**

| Arc product | What the inspected material supports | Implication for us |
|---|---|---|
| [ArcPad](https://arcpad.meme/docs) | Documents immediate v3 launches, fixed supply, a permanent fee locker, creator/holder rewards, charts and public APIs. Its launcher example identifies `0x24196CD6e534cfCE8F480B53E70809b68Ea86F29`. **Project claims**, not an independently verified deployment in this pass. | Instant v3 launch and locked LP are already offered. Documentation also contains inconsistent descriptions of transfer restrictions and fee treatment; implementation must determine actual behavior. |
| [Arcfun](https://arcfun.app/docs) | Documents a USDC curve graduating into a locked v4 pool, a hook, router and indexer. Factory: `0xBBf81Fd835B471C86d094eAaD35BB10068a987f8`. | Direct competitor to our programmable path. Graduation alone is not differentiation. |
| [moon](https://moon.family/docs) | Describes itself as a PONS v2 port: curve launches, v4 graduation, creator-fee or holder-reward modes, and burns. Documents a 1 USDC launch fee and 10,000 USDC graduation threshold for USDC launches. | Much of the requested feature set is already documented on Arc. Adoption and security remain separate questions. |
| [Arcade](https://www.arcade.trading/docs) | Publishes an [integration repository](https://github.com/obseasd/arcade-integrations) and [deployment manifest](https://www.arcade.trading/deployments.json), including curve and instant-launch modes. Current hook: `0x7706d261f0C370e8f0E273164A603E885C89beC2`. | A broad trading terminal is a crowded position. Its documented inactivity-based liquidity recovery also shows why “permanently locked” needs precise qualification. |
| [TOLLY](https://tollylabs.com/guide) | Publishes extensive launch, trading, fee-routing and rewards documentation, with a contract-source verification package. Listed launcher: `0xcad7ee36ac193bf2eddb7b3e2736c5bdb8269c8b`. Distinguishes calculated rewards from claimable rewards. | Strongest warning against competing on dashboards, fee splits or feature count alone. Borrow its evidence discipline. |
| [Parabola](https://parabola.meme/) | Public material describes USDC curves and graduation; inspected evidence did not establish a functioning launch/trade lifecycle or verified deployment. | Treat as announced competition, not proven adoption and not nonexistent. |

I attempted independent bytecode checks against Arc’s public RPC. Those requests returned access errors; explorer pages did not expose sufficient machine-readable evidence. **The addresses above are published identifiers, not deployment or security attestations.** I have not established organic trading volume, retained creators or revenue for these competitors.

The most useful cross-chain comparisons are:

| Reference | Mechanics and growth loop worth learning | Revenue, liquidity and protection | Weakness or constraint |
|---|---|---|---|
| [Pump.fun](https://pump.fun/docs/fees) | Extremely short creation flow, discovery, live activity and repeated creator launches. | Curve → PumpSwap; documented curve fee currently 1.25%, with separate post-graduation schedules and interface fees. | Distribution is the advantage; copying the curve does not reproduce the audience. Incentives can reward churn rather than enduring communities. |
| [PONS v1](https://docs.ponsfamily.com/) / [v2](https://docs.ponsfamily.com/v2) | Simple launch choices and persistent creator economics. | v1 documents direct v3 launches; v2 documents curve graduation and hook-based fees, with optional creator tax/buybacks. | Versions differ materially. Quote-asset fee claims require inspecting conversion paths, permissions and execution assumptions. |
| [Hookr](https://hookr.fun/docs/pools/core-blocks) | Understandable rule blocks, fixed launch configuration, reusable launcher infrastructure. | Anti-snipe, dynamic fees, burn and LP-reward mechanisms; some additional blocks explicitly remain “deploying soon.” | Permitted fee bounds can be extreme. More configurability expands the attack surface and makes comparison harder. The older AvaxHook reference should not be assumed identical to every current Hookr release. |
| [Flaunch](https://docs.flaunch.gg/protocol/frequently-asked-questions) | Creator economics plus community-managed revenue, rather than launch-only engagement. | Fixed-price opening period, subsequent price discovery, revenue rights and community buyback/treasury options. | Closest conceptual competitor. “Fees fund the community” is not our invention; our differentiation must be funded work, contributor coordination and transparent spending. |
| [Clanker](https://github.com/clanker-devco/v4-contracts) | Distribution through social creation workflows; modular deployment, rewards and launch protection. | Public v4 contracts include static/dynamic hooks, lockers and sniper-auction components. | Creator revenue belongs to particular positions and pools, not every market for the token. Existing social distribution is difficult to recreate. |
| [Zora](https://support.zora.co/en/articles/2509953) | Content itself becomes discovery inventory; creator, referral and trading loops reinforce each other. | Documents creator/content pool fees and additional interface transaction fees. | Tokenizing content does not automatically grant IP rights or create sustainable demand. Fee stacking needs clear presentation. |
| [Four.meme](https://four-meme.gitbook.io/four.meme/guide/how-it-works) | Familiar curve progression, ecosystem distribution, straightforward graduation. | Documents curve trading, reserved LP supply and migration to PancakeSwap. | Graduation targets and product versions change. The transferable lesson is predictable lifecycle presentation, not copying an old numeric threshold. |

These sources establish documented mechanics and inspectable implementations where linked. They do not establish comparative security or prove that a particular mechanism caused adoption.



**Three plausible positions emerge; only one is attractive enough to pursue first.**

| Position | First audience | Why they might choose it | Assessment |
|---|---|---|---|
| “The fastest Arc meme launcher” | Speculative launchers | Speed, low friction, discovery | Weak: ArcPad, moon, Arcfun and others already address this. |
| “The programmable launch laboratory” | Sophisticated creators and traders | Bounded rule presets, visible simulations, unusual market behavior | Credible second-stage identity, but expensive to secure and easy to turn into a confusing settings panel. |
| **“Launch a community with an operating budget”** | Small meme-art collectives, recurring content teams and community managers already commissioning work | Launch, trade, earn, commission, review and publish outcomes in one place | **Recommended.** Specific recurring workflow; still a hypothesis requiring creator validation. |

The first users should be **existing teams that already publish weekly and pay artists, editors or moderators**, not anonymous creators hoping token trading will manufacture a community.

Arc improves this experience because budgets, payouts, trading quotes and gas can all be expressed in USDC. It removes a volatile gas-token requirement and reduces conversion work for contributors. It does **not** supply audience, liquidity or sustainable fee income.

A useful product promise is:

> Launch a community token, see exactly what its founding liquidity earns, and turn available USDC into completed community work.

Avoid promises of passive income, guaranteed price support or token-holder entitlement to business profits.
