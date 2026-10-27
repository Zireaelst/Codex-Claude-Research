# Lifecycles, failure paths and claims

## V4 launch

DRAFT is offchain only. One atomic launch transaction registers immutable configuration, deploys token and curve custody, mints S, optionally executes a disclosed creator buy, and ends in CURVE_ACTIVE. Revert unwinds every effect including launch fee.

CURVE_ACTIVE permits buys and sells until expiry (30 days from launch, immutable). Final capped buy sets GRADUATION_PENDING; further curve trading stops. The same transaction attempts an external self-contained atomic graduation call. On failure, catch only at the boundary so the purchase and pending state survive while ALL pool initialization/minting/approvals of the failed attempt roll back. Emit the failure selector and attempt number. Never catch a partial error and leave a pool half initialized.

GRADUATION_PENDING permits permissionless retry using only committed config. No caller-supplied hook, recipients, price or fee policy. On success, transition atomically to GRADUATED, store canonical pool and locker, enable actual token claims. On failure, funds remain in curve custody. Retry is allowed for 72 hours measured from first pending timestamp, not extended by failed calls. At/after that deadline retry is disallowed and anyone can activate REFUNDABLE. A persistent dependency failure cannot lock funds indefinitely.

Expired CURVE_ACTIVE becomes REFUNDABLE through a permissionless activation call. Every buy/sell checks expiry itself; absence of a keeper cannot prolong trading. GRADUATED never becomes REFUNDABLE. REFUNDABLE freezes denominator/backing and permits perpetual entitlement-burn claims. SETTLED is a display/accounting state once all entitlements are redeemed; it does not create a confiscation path.

## V3 launch

Offchain DRAFT → atomic pool create/init + full-range mint + founding locker custody + registry record → ACTIVE_LOCKED. Failed transaction returns to no launch. Reject any already initialized pool for the predicted token, even if claimed price matches. A malicious pre-initialization must not cause fee loss or seed transfer. V3 cannot use hooks to restrict initializers: new token salt/preflight and atomic rollback are the recovery mechanism. No graduation migration.

## Existing-token pools

DRAFT → atomic initialize and initial two-sided LP → ACTIVE. Multiple pools per token allowed, differentiated by complete pool key, rules and quote. A new contract instance/address is needed where a distinct ruleset would otherwise collide with a pool key. LP NFT belongs to depositor; full-range deposits only. Zero liquidity is ILLIQUID (derived, not a confiscation state). Users may add liquidity again. Swaps with partial-fill behavior unsupported by rules must revert atomically. The UI never confuses this removable LP with locked launch liquidity.

## Work funding and disputes

Optional community jobs use a separately authorized manager and reviewer; never access LP principal. Manager creates OPEN job with funded budget, submission deadline and review period (7 days). Manager assigns contributor → ASSIGNED; contributor accepts within 48 hours or anyone can release assignment back to OPEN. No submission by deadline → CANCELLED and treasury gets unspent reservation. Submission before deadline → SUBMITTED with immutable content hash/URI. Reviewer must accept or reject with public reason within review period.

ACCEPTED → contributor claimable; pull payment can be made to contributor-selected recipient, no expiry. REJECTED → contributor may revise once within 72 hours; reviewer then has 7 days. Second rejection or no revision → CANCELLED, funds return to treasury. If reviewer misses either review deadline → ACCEPTED automatically on permissionless finalize. Once submitted, manager cannot cancel. UI discloses that reviewer judges quality and timeout favors contributor. Manager/reviewer cannot be the contributor; this prevents trivial self-approval but not collusion. Treasury contributors must understand manager authority.

## Rewards

Fund campaign → ACTIVE until committed end time → ENDED. Stake principal remains withdrawable even if reward computation/transfer fails. Accrue reward through reward-per-share accounting, not loops over holders. Claimed + reserved + unallocated never exceeds funded. Only unallocated budget can return to sponsor after end; accrued claims never expire. Reward-token transfer failure must not block principal exit; preserve claim liability.

## Irreversible facts versus editable presentation

Frozen: chain, token supply, canonical path, economics hash, module addresses/parameters, maximum fees, founding locker policy, recipients and splits. Metadata description/image/socials may be updated by declared metadata authority; every update is logged and old revisions retained. Metadata authority cannot change token name/symbol, economic state or fee recipients. Content hiding is an offchain moderation action, not a contract pause.
