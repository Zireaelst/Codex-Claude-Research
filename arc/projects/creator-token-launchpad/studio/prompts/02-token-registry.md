Implement only the fixed-supply token factory and launch registry for the
approved model, with Foundry tests. Bind each token to one canonical launch
path and version. Mint once; prohibit owner minting, transfer taxes and
blacklists. Separate immutable economics from versioned social metadata.

Test unauthorized registration, duplicate launch identifiers, salt collisions,
supply conservation and metadata authorization. Use pinned dependencies.
Do not implement the launcher, frontend or deployment. Report actual tests.

Follow product-brief.md and specification.md. No public-network deployment, broadcasts, wallet creation, secret exposure or spending is authorized by this prompt.
