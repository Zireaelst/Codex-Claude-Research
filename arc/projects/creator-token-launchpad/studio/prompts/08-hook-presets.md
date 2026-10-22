Implement the reviewed hook registry and two fixed composite presets:
standard 1% and protected opening with at most 3% declining to 1% within
120 seconds. Existing launches cannot change preset or parameters.
No arbitrary modules, delegatecall, extra swap taxes, lottery or volume rewards.

Validate hook address permission bits, PoolManager-only callbacks, pool
registration, supported exact-input/exact-output behavior and fee bounds.
Test direct routers, malicious hook data, callback reentrancy and incompatible
configuration. Describe protection as a surcharge, not bot exclusion.
Leave more complex dynamic fees and LP incentives disabled.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
