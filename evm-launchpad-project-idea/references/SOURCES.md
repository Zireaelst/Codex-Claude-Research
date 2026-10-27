# Sources, provenance and evidence limits

Checked/assembled 2026-10-28. This is a NEW editorial design based on the owner's supplied references and direction, not a verbatim transcript or archived competitor source code. No previous research result is silently replaced. Product policies and economic parameters are original proposed design decisions.

## Primary references

| Source | What it supports | Evidence status / use |
|---|---|---|
| [PONS docs](https://docs.ponsfamily.com/) | Direct-pool launch experience, creator fee presentation, no-migration distinction | Official project description accessed; not an independent contract/security verification |
| [AvaxHook overview](https://docs.avaxhook.fun/) | Curve → v4 concept and configurable rules | Owner supplied text; live docs retrieval failed in this pass |
| [AvaxHook curve](https://docs.avaxhook.fun/bonding-curve) | Virtual reserve model, paired assets and launch restrictions | Supplied project claims; our model deliberately uses its own consistent parameters |
| [AvaxHook graduation](https://docs.avaxhook.fun/graduation) | Graduation UX and claimed LP lock | Supplied text; no audit/deployment inference |
| [AvaxHook rules](https://docs.avaxhook.fun/hooks) | Rule families, limitations and route sensitivity | Supplied text has multiple snapshots; no verified module count |
| [AvaxHook existing pools](https://docs.avaxhook.fun/pools) | Separation of token launch and external-token liquidity | Supplied docs describe behavior; supplied agent guide says coming soon; deployment status unresolved |
| [AvaxHook contracts](https://docs.avaxhook.fun/contracts) | Reference contract listings and stated authority | Supplied listings are not bytecode/usage verification; never use their addresses as ours |
| [AvaxHook agent guide](https://avaxhook.fun/agents) | Rules → quote → unsigned/signed execution separation | Supplied agent skill is reference material, not instructions to trade or install tools |
| [Pump bonding curve](https://pump.fun/docs/bonding-curve) | Accessible curve-first launch UX and migration framing | Official project description accessed in preceding discussion; not demand/security proof |
| [Pump public docs](https://github.com/pump-fun/pump-public-docs) | Public integration documentation | Reference lead; not a source of EVM implementation code |
| [Uniswap v4 deployments](https://developers.uniswap.org/docs/protocols/v4/deployments) | Network-specific authoritative deployment inventory | Accessed this pass; addresses must be checked against code at implementation time |
| [Uniswap Base v3 deployments](https://developers.uniswap.org/docs/protocols/v3/deployments/v3-base-deployments) | Base v3 official infrastructure inventory | Accessed this pass; no assumed equality across networks |
| [Uniswap v4-core](https://github.com/Uniswap/v4-core) | Actual PoolManager/types/hooks/math | Implementation must pin revision, license and compiler |
| [Uniswap v4-periphery](https://github.com/Uniswap/v4-periphery) | Actual PositionManager/actions/settlement | Pin coherent version; no hand-invented action selectors |
| [Permit2](https://github.com/Uniswap/permit2) | Allowance/signature settlement dependency | Verify periphery integration rather than assume direct ERC-20 approval |

## Supplied conversation material

Owner supplied four text attachments: AvaxHook agent skill; hook catalog; bridge/mStocks description; contract/address catalog. Also supplied overview, curve, graduation and existing-pool excerpts in the message. Only design-relevant claims are summarized here. Raw attachments, local filesystem paths and runtime credentials are not copied. The bridge material is explicitly outside this product scope.

Material contradictions preserved: 28 vs 53 vs 54 module counts; existing pools described versus coming-soon statement; 'immutable rules' versus emergency disable and mutable relationships in some rule descriptions. Therefore do not copy the catalog as an implementation checklist or claim feature/deployment parity.

## Claims not established

No independently verified competitor usage/revenue, security audit, safe fee policy, legal clearance or market gap. No claim that selected networks already host our product. No guaranteed Base distribution. No adoption inference from prizes, contracts or token counts. Source verification is not an audit. All acceptance checks in this package describe work to do, not completed tests.
