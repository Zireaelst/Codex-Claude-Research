# Research updates and continuation

**Archive editorial note:** These are original user-visible interim messages, not a substitute for the completed report. Tool logs, internal reasoning, system context and internal agent communications are excluded.

### Assistant — 2026-10-18T16:56:51.006Z

I’ll compare product gaps and privacy primitives on equal terms, with particular attention to existing Arc hackathon work and what a mainnet transaction can actually prove. I’ll use the brainstorming framework for the shortlist, without moving into implementation.


### Assistant — 2026-10-18T16:58:21.205Z

Two findings materially change the shortlist: Manila already won Arc’s private-nanopayments prize, so “private payroll on Arc” is not an unexplored idea. Verdikt also already demonstrates API refunds on Arc testnet—but its submission explicitly relied on CRE simulation because production deployment access was unavailable. I’m checking those implementation boundaries rather than taking the showcase headlines at face value.


### Assistant — 2026-10-18T17:01:45.011Z

Repository evidence changes one important conclusion: ACR’s hackathon page describes testnet, but its current repository lists an Arc-mainnet deployment dated September 27. I’m separating submission-time claims from current status. Anonymous eligibility claims and multilateral invoice netting look more promising than another private-payroll or agent-payment wrapper, though both still need a credible first user.

### Assistant — 2026-10-18T17:02:55.021Z

The netting gap does not hold up: Arc already has Cycles, plus public Setoff and Contraflow implementations. Agent spending controls are also crowded. I’m dropping both as “missing on Arc” pitches. The stronger privacy direction is narrower: proving eligibility for a USDC reward without publishing which approved participant claimed it—while keeping the payment itself explicitly public.

### Assistant — 2026-10-18T17:04:51.165Z

The leading option is a paid-feedback app with a precise ZK claim: one approved participant, one reward, without revealing their roster entry. The backup is stealth invoicing, where Arc’s USDC gas removes the need to fund a fresh recipient address with a separate gas token. I also found recent Semaphore fixes, so matching the corrected contracts, circuit, and proving artifacts is a hard build gate.
