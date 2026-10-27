# Product requirements

## Thesis and audience

A creator should be able to launch an understandable programmable market, not assemble a token, a DEX position, a locker and a collection of opaque taxes. A buyer should see what they can trade, what it costs, which rules apply and what can change before signing.

First audience: meme-community founders, creator collectives and active EVM token traders. Secondary users: existing-token communities, LPs, referral partners, content contributors and agent developers. Distribution hypothesis: shareable token/rule pages and creator communities, with a public API enabling independent integrations. This is a hypothesis, not established demand or an adoption forecast.

## Mandatory capabilities

| ID | Requirement | Observable outcome |
|---|---|---|
| P01 | V4 curve launch is default | Creator completes configuration, simulates and launches; buyers trade before graduation |
| P02 | V3 instant launch is supported | Creator seeds an immediate pool; founding LP is locked in the same transaction |
| P03 | One canonical path per launch | Registry stores immutable path; no button converts an active v3 token into a curve launch |
| P04 | Rule composition is bounded | Invalid combinations rejected by frontend and contracts; identical configuration hash displayed |
| P05 | Trading is end-to-end | Quote, approvals, simulation, execution, confirmation and indexed activity all correspond to real state |
| P06 | Discovery is honest | New, active, graduation progress and graduated views; no fake volume or paid ranking disguised as organic |
| P07 | Creator earnings are usable | Accrual, collection, asset-specific claims and payout history |
| P08 | Existing-token pools are separate | Opener provides both assets, receives removable LP, cannot mint the external token |
| P09 | Rewards have real backing | Fund, accrue, claim and close a campaign without spending reserved claims |
| P10 | Community allocation is optional | Treasury spending and contributor payments work when selected; no mandatory treasury tax |
| P11 | API supports independent clients | Rules, address-specific quotes, unsigned transaction plans and events documented |
| P12 | Multiple EVM networks are architecturally supported | Per-chain manifests, separate accounting and network-qualified identifiers; no shared liquidity fiction |
| P13 | Rule presets can be reused | Immutable blueprint definitions; users review parameters and costs before launch |
| P14 | Both standard and bounded advanced token profiles exist | Standard defaults; temporary transfer restrictions only when explicitly selected and disclosed |
| P15 | Risk and administration are visible | Token page lists transfer constraints, maximum fees, lock scope and emergency powers |
| P16 | Operational product works | Reorg recovery, monitoring, abuse reports, backup/restore and admin audit log |

## End-to-end scope, not release labels

All P01–P16 belong to the target product. Engineers may build sequentially but cannot quietly remove v3, existing-token pools or the contribution loop to announce completion. Module catalog scope is explicit in 05-rules: the product does not promise every rule ever shown by AvaxHook.

## Not part of this product

No platform token, validator bridge, synthetic stock issuance, lending/leverage, guaranteed yield, anonymous payments, permissionless arbitrary-code module marketplace, predictable winner pots, cross-chain shared token supply, or claim that bots can be excluded universally. Trading bots may consume the API; we are not building an agent marketplace.

Limit orders, cross-asset zaps and native cross-chain routing are deliberate optional extensions, not hidden dependencies of any required journey. The complete baseline handles direct quote-asset trading correctly.

## Success measures

Track returning traders, creators with repeat community activity, quote-to-confirmed-trade success, meaningful liquidity, payout completion, indexer lag and recovery incidents. Label sybil/wash-adjusted estimates as estimates. Launch count, volume and rule count are not sufficient success measures. Do not fabricate targets from a theoretical market size.

## Definition of product completion

Every required journey passes against local real protocol deployments and a verified network fork; public release additionally needs address verification, authorization and independent security review. App, API and contracts agree on path, status, price units, exact fee breakdown, claimable assets and rule reach. Every disabled action has a true reason and recovery path. A public-chain launch is not required to truthfully complete a local implementation, but cannot be claimed without evidence.
