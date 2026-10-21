# Original research prompt

Editorial note: copied from the user message; transport escaping is normalized for readability in research-01 only. `prompt-source.txt` retains the accessible source text, subject to privacy redaction.

Important new development — Stellar Bell / Protocol 30:

Investigate the newly announced Bell upgrade as a potential change to the opportunity landscape, not as proof that its features are already live. Start with the official announcement and upgrade guide:
- https://stellar.org/blog/developers/introducing-bell-protocol-30-on-stellar
- https://stellar.org/blog/developers/bell-protocol-30-upgrade-guide

Examine the product implications of each proposal:

- CAP-84, muxed contract addresses: A W address adds a customer identifier to a contract address. Explore whether this makes multi-customer smart-account products economically and operationally viable: agent spending accounts, payment acceptance, ramps, marketplaces, treasury accounts, or privacy-aware financial applications. Compare it with the previous one-contract-per-customer approach. Examine internal balance accounting, authorization isolation, refunds, event indexing, address compatibility, and what happens if a customer ID is misassigned. A shared contract address and a visible customer ID must not be presented as cryptographic privacy.

- CAP-87, ML-DSA verification in smart contracts: Explore whether post-quantum authorization creates a real customer problem and product opportunity for wallets, custodians, high-value RWA holders, or long-lived agent mandates. Distinguish smart-contract authorization from network transaction signatures, which remain Ed25519. Do not treat post-quantum signatures as payment confidentiality or invent urgent demand without buyer evidence.

- CAP-88, millisecond-resolution ledger timing: Examine whether it creates any plausible future opportunity for payments, trading, or agent workflows. Do not assume Bell itself produces sub-second ledgers or faster user-facing settlement. Identify what further protocol changes and observed performance would be required.

For every Bell-enabled thesis, classify the dependency as: buildable on today's mainnet, buildable only after a successful Protocol 30 activation, or dependent on further upgrades or third-party adoption. Check the announced vote status at research time.

Search for 3–5 product opportunities that become materially stronger because of Bell, then compare them against the other agentic, RWA, DeFi, and privacy ideas. Do not promote a Bell idea just because the upgrade is new. Re-rank the finalists only if Bell changes customer value, distribution, economics, or defensibility in a concrete way.
