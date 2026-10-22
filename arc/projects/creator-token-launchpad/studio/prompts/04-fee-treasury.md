Implement per-launch, per-asset fee accounting and the community treasury.
Apply the immutable 40/50/10 split to actual received fees. Support bounded
creator-team recipients and pull claims. Separate USDC cash, token balances,
uncollected estimates and committed budgets.

Recipient changes must preserve previously accrued entitlements. Permissionless
collection must not let callers redirect proceeds. A failing recipient must
not block other recipients. Treasury cannot access LP principal.

Test rounding, repeated collection, duplicate claims, asset isolation, launch
isolation, recipient transitions and malicious token/recipient callbacks.
Do not add token-fee conversion or general treasury execution.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
