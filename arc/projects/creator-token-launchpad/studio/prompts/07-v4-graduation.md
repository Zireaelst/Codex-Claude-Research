Implement permissionless v4 graduation and the v4 founding-position locker.
Authenticate canonical pool initialization to the registered executor.
Atomically deposit backing and reserved tokens, lock the position, finalize
graduation and enable 1:1 token claims.

Permit retries after failed graduation and the specified timeout-to-refund
path. Restrict fee collection to the exact zero-liquidity action sequence;
prohibit principal withdrawal and arbitrary PositionManager commands.

Test pool initialization attacks, both currency orders, rounding, price
continuity, incomplete settlement, repeated graduation and failed token claims.
No deployment.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
