Adversarially review the implemented dual-path contract system. Attempt to violate
supply, principal custody, fee conservation, treasury solvency and work-payment
invariants using multi-user fuzz sequences and malicious callbacks.

Include wrong-network configuration, manipulated pool initialization,
unexpected transfers, dust accumulation and Arc native/ERC-20 balance aliasing.
Mocks do not establish Arc compatibility: mark missing real-fork tests as gates.

Produce reproducible findings with severity and failing tests. Fix findings
within the approved design and rerun relevant tests. Do not describe automated
review as an independent security audit. No deployment.
Include curve insolvency, graduation griefing, price continuity, expiry/refunds, v4 callback permissions and both locker implementations.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
