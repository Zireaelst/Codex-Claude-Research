# Design decisions and rejected alternatives

Owner decisions: independent EVM product; both v3 and v4; v4 primary; AvaxHook/PONS/Pump-inspired complete launch/trading experience; documentation usable by a coding agent; ignore the old Arc implementation. No request to implement or deploy in this documentation task.

Proposed defaults below resolve ambiguity so an agent can proceed once separately authorized. They are design policy, not past owner quotations.

| Decision | Chosen behavior | Reason / alternative rejected |
|---|---|---|
| D01 | New repository, no Arc code dependency | Old mocks and network semantics cannot establish new product correctness |
| D02 | V4 main, V3 required alternative | Preserves explicit user choice without pretending hooks work on v3 |
| D03 | Complete scope split into work packages | Sequential dependencies are unavoidable; no arbitrary 'MVP finished' shortcut |
| D04 | Six bounded modules, presets plus advanced configuration | Raw feature count does not justify combinatorial risk |
| D05 | Standard and optional bounded Advanced token profiles | Transfer-wide limits require token logic; pool hook alone cannot provide them |
| D06 | Pre-graduation internal entitlements | No early external pool; explicit claim/receipt UX instead of hidden global token tax |
| D07 | 80/20 token allocation and 16x price ratio | Mathematically consistent reference; do not mix with AvaxHook's 20x + residual burn policy |
| D08 | Automatic graduation attempt plus pending/retry/refund | A failed dependency must not permanently block final buyers' exit |
| D09 | Permanent founding LP; external LP removable | Lock guarantee is position-specific, not a false platform-wide slogan |
| D10 | Optional treasury; no mandatory community levy | Product is programmable launch/trading, not a bounty platform |
| D11 | Asset-specific fee claims | Token earnings are not automatically USDC revenue |
| D12 | No per-buy subsidy or predictable jackpot | Wash trades/ordering can farm rewards; funded time-weighted programs are explicit |
| D13 | No platform token, stock bridge or arbitrary-code marketplace | Unnecessary risk and scope; templates reuse approved code only |
| D14 | Independent deployments per EVM network | No fake cross-chain common supply/liquidity |
| D15 | Governance affects future launches only | Existing immutable behavior cannot be silently changed under a registry label |
| D16 | Fees and bounds in economics are proposed defaults | Need model and actual integration proof before real funds; no competitor-copy constants |

## Additional discovery that must occur during implementation

Network addresses and exact upstream code/compiler/license correspondence must be verified with evidence. This does not reopen the product's design or justify fabricating addresses. If selected versions cannot meet a security invariant, submit a focused design change identifying affected requirement, attack, alternative and tests. Do not replace a failing real integration with a mock or quietly drop the feature.

Public deployment authority, branding/domain, legal operating entity and reviewer/governance wallet identities are not supplied by this package. Use local fixtures and clearly labeled configuration requirements; do not invent people or keys. Those omissions do not prevent local product implementation but block real deployment.

## History boundary

Earlier Arc research remains historically preserved elsewhere in this repository. It is not an implementation instruction for this project. The new specification supersedes it only for this EVM product. Do not rewrite historical research to make it appear the original conclusion was always this design.
