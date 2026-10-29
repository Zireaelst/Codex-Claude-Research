# Consumer prediction project profile

Source roadmap: [consumer prediction](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/base-project-roadmaps/2026-10-29/02-prediction-consumer-roadmap.md). The owner selected a social consumer app integrating existing venues. No new AMM, oracle, shared betting pot, leverage or custody vault is required. Limitless is an initial candidate, not an already-approved partner.

First prove read-only market catalog, lifecycle, auth/account/wallet capabilities and order/claim semantics against [official venue SDK](https://github.com/limitless-labs-group/limitless-exchange-ts-sdk). Pin version; verify current auth rather than trusting old header examples. Record each capability as verified, unsupported or blocked. Missing live/sandbox access stays blocked; mocks do not prove a real trade path. Venue data/commercial/eligibility terms need separate verification before public trading.

Separate `Forecast` from `OrderIntent`. A free forecast must not sign a trade or move funds. User-selected wallet/account signs bounded intent; app does not acquire spending keys. Normalize market identity by venue+ID and preserve outcome/terms version. Keep order submission, acceptance, partial fill, cancel requested, cancelled, filled, settlement and claim distinct. HTTP 200 is not a fill.

On timeout after signature/submission, persist `SUBMISSION_UNKNOWN` and reconcile the original venue ID/client ID/hash. Never retry with a fresh nonce blindly. Handle duplicate/out-of-order events, partial fills and cancellation races. New quote/cost needs user review; stale book data is not executable price. A venue handoff is a disclosed fallback, not native integration completion or a way to bypass access restrictions.

Social model: rooms, predetermined weekly market sets, time-locked forecasts, immutable revision history, outcome corrections and opt-in results notifications. Public wallet data does not imply consent to public profile aggregation. Authorization checks protect private rooms. Moderation does not erase financial records or user claims.

Forecast score can use Brier loss with visible sample count and fixed comparison windows; it is not percent accuracy. Exclude void/disputed unresolved outcomes; version corrected scores. Small samples remain provisional. Forecast score and realized/unrealized PnL are separate. Avoid sponsored ranking presented as organic, transaction streaks and loss-chasing messages.

Consumer UX: Explore/Rooms/Activity/Profile, clear question and resolution terms, a separate forecast sheet and trade sheet, total cost and payout-versus-profit disclosure. Design rejected signature, stale quote, restricted access, partial fill and delayed resolution states. Test quote→signature→fill recovery separately from forecast→result→return retention.

Acceptance: source roadmap PP01–PP12. Verify idempotency, replay prevention, room authorization, score correction, claim target/chain, unsubscribe, restore and venue outage recovery. Builder attribution applies only where the actual venue/transaction path supports it; don't add a suffix to foreign signed orders. Unconfirmed referral revenue is zero in planning.
