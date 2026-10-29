# Consumer Prediction — Teknik ve Tasarım Yol Haritası

29 Ekim 2026 · Planlama sürümü 1.0 · Kullanıcı kararı: mevcut piyasalara bağlanan sosyal/consumer uygulama.

## 1. Ürün tezi ve ilk kitle

**Ürün vaadi:** “Topluluğunla tahmin yap, gerekçeni kaydet, sonuçlardan öğren; istersen aynı piyasada kendi cüzdanınla pozisyon aç.”

Bu ürün yeni AMM, order book, oracle veya settlement protokolü kurmaz. İlk venue adayı Limitless; SDK bulunması teknik bir başlangıç sağlar, ticari entegrasyon hakkı veya uygun kullanıcı erişimi sağlandığını kanıtlamaz. İlk iki haftanın ana kapısı bu bağımlılığı doğrulamaktır.

İlk kitle: zaten kripto piyasalarını takip eden iki veya üç Telegram/Discord topluluğu. İlk katalog: venue’da gerçekten bulunan ve yeterli veri/likidite gözlemlenen kısa vadeli kripto piyasaları. Seçim bizim ürünümüzde market oluşturmak anlamına gelmez. Spor ve politika, ayrı kullanıcı araştırması ve erişim değerlendirmesi sonrasında kategori genişlemesidir.

Farklılaşma hipotezi: topluluk içinde haftalık seçki, sonuçtan önce kaydedilmiş gerekçe, dürüst başarı geçmişi ve sade işlem deneyimi. Kullanıcının “bir sonraki sonucu görmek için geri gelmesi” esas döngüdür. Para yatırma veya her gün işlem yapma serileri ödüllendirilmez.

## 2. Üç ürün katmanı

| Katman | Kullanıcı işi | İlk sürüm |
|---|---|---|
| Keşif | Bana uygun gerçek piyasayı ve bitiş koşulunu anlamak | Editoryal seçki, arama, takip listesi |
| Sosyal tahmin | Fikrimi zamanında kaydetmek ve toplulukla karşılaştırmak | Oda, tahmin, gerekçe, sonuç geçmişi |
| İşlem | Açıkça onaylayarak mevcut venue’da pozisyon açmak/kapamak | Tek venue, sınırlı emir türü, cüzdan imzası |

Tahmin kaydetmek emir vermez. Birinin görüşünü takip etmek otomatik copy-trade başlatmaz. Sosyal oda ortak fon veya ortak yatırım hesabı değildir. İlk sürümde entry fee, prize pot, leverage, platform tokenı, fon tutan özel vault ve kullanıcı adına arka planda işlem yok.

**Dar çekirdek:** Explore → market → tahmin kaydet → oda → sonuç → geçmiş. Gerçek işlem isteğe bağlı ikinci akıştır. Böylece sosyal değer ve işlem dönüşümü ayrı ölçülür; ücretsiz tahmin kullanıcıları sahte onchain traction sayılmaz.

## 3. Sürümler ve kapsam

| Sürüm | Teslim |
|---|---|
| P0: entegrasyon ispatı | Gerçek katalog, kimlik/erişim modeli, order/position okuma, quote/fill/claim yetenek matrisi |
| P1: sosyal alpha | Gerçek market verisi, ücretsiz tahminler, iki oda, sonuçlandırma geçmişi; canlı trade kapalı |
| P2: davetli işlem beta | Kullanıcı imzalı emir, fill takibi, pozisyon ve claim; sadece doğrulanan route ve hesap türleri |
| P3: consumer v1 | Moderasyon, bildirim tercihleri, haftalık recap, ölçümlenmiş onboarding ve sürdürülebilir oda araçları |
| P4: talebe bağlı genişleme | İkinci venue, ek kategoriler, gelişmiş filtreler/organizer aboneliği; ayrı karar |

P1 bir tahmin topluluğu ürünüdür. Para hareketi üretmediği için gerçek trading ürünü tamamlandı diye sunulmaz. P2 ancak entegrasyon/erişim ve güvenlik kapıları tamamlanınca açılır.

## 4. Venue doğrulama kapısı

İlk iki haftada aşağıdaki tablo gerçek SDK/API davranışıyla doldurulur. Durumlar `verified`, `unsupported`, `blocked` olarak tutulur; bilinmeyenler UI’da etkinleştirilmez.

| Konu | Aranan kanıt | Olmazsa davranış |
|---|---|---|
| Katalog ve sonuçlar | Stabil market ID, status, deadline, resolution kaynakları | Sosyal tahmin için dahi belirsiz market gizlenir |
| Fiyat/derinlik | Executable ask/bid, order book yaşı, min order, fee | Son fiyat işlem quote’u diye gösterilmez |
| Wallet desteği | EOA ve seçilen smart-wallet imza/hesap akışı | Desteklenmeyen wallet’ta read-only veya açık alternatif |
| Emirler | Desteklenen exact order tipleri, miktar/rounding, client ID/dedupe | İspatlanmamış tip için adapter capability false |
| Durum/iptal | Accepted/partial/filled/cancelled/rejected ve recovery | Yanıt kaybında kör tekrar emir yok |
| Claim | Position owner için doğru target/calldata ve tekrar claim davranışı | Belgelenmiş venue handoff; otomatik claim iddiası yok |
| Erişim/şartlar | Kullanıcı ülkesi, yaş/uygunluk, partner erişimi ve veri kullanımı | İlgili işlem açılmaz; onaylı sosyal kapsamla devam |
| Ücret/attribution | Partner fee ve Builder Code desteğinin kanıtı | Gelir veya bize atfedilen volume varsayılmaz |
| Operasyon | Rate limit, streaming/reconnect, pagination ve tarihçe | Backoff, cache ve açık “veri gecikiyor” durumu |

Limitless’ın resmî SDK’sı market/order/portfolio erişimini belgeliyor. Güncel SDK commit’i, auth yöntemi ve partner şartları uygulama başlangıcında ayrıca sabitlenmeli; eski örneklerde görülen header’ların hâlâ geçerli olduğu varsayılmamalı. [Resmî SDK](https://github.com/limitless-labs-group/limitless-exchange-ts-sdk)

Hedef ülkeler henüz seçilmedi. Bu belge hukuki uygunluk sonucu vermez. Hedef ülke listesi ve venue koşulları incelenmeden gerçek işlem açılmaz; başka arayüze yönlendirme, erişim şartlarını aşma yöntemi değildir.

## 5. Teknik mimari

Önerilen yeni repo:

```text
apps/web                        Mobil öncelikli React/TypeScript PWA
apps/api                        Kimlik, oda, tahmin, emir orkestrasyonu
apps/worker                     Katalog sync, reconciliation, sonuç ve bildirim
packages/venue-core             Normalleştirilmiş tipler ve capabilities
packages/venue-limitless        Venue’a özgü adapter ve contract testleri
packages/domain                Forecast, room, scoring ve order state kuralları
packages/db                    PostgreSQL migration ve outbox
packages/wallet                İmza ve işlem durumu bileşenleri
packages/ui                    Paylaşılan erişilebilir primitive’ler
docs/evidence                  Entegrasyon ve senaryo kanıtları
docs/runbooks                  Venue kesintisi, data correction, restore
```

İlk sürüm modüler monolith + worker yeterli; mikroservis, Kafka ve ayrı arama cluster’ı başlangıç şartı değil. PostgreSQL ana veri kaynağı; Redis cache/rate limit için opsiyonel. Queue işleri idempotent; transactional outbox ile aynı sonucun iki kez bildirilmesi engellenir.

### Veri sahipliği

- Venue: market koşulları, order/fill/position ve sonuçlandırma gerçekliği.
- Bizim backend: oda üyeliği, tahmin/gerekçe sürümleri, takipler, bildirim tercihleri ve sosyal puan.
- Kullanıcı cüzdanı: emir/transaction imzası; sunucu kullanıcı fonlarını imzalamaz.
- Public profil: yalnızca kullanıcının açıkça paylaşmayı seçtiği alanlar. Wallet bağlamak bütün portföyü otomatik olarak herkese açmaz.

### Venue adapter sözleşmesi

Uygulamaya ait önerilen arabirim; venue’nun gerçek API imzaları değildir:

```text
capabilities()                         desteklenen market/order/wallet/claim özellikleri
listMarkets(cursor, filters)           katalog + cursor + observedAt
getMarket(venueMarketId)               kurallar + resolution status + termsVersion
getOrderBook(marketId, outcomeId)       bid/ask + depth + observedAt
prepareOrder(intent, wallet)           kullanıcıya gösterilecek typedData/tx + maliyet
submitSignedOrder(planId, signature)   venueOrderId veya belirsiz submission durumu
getOrderStatus(orderRef)               normalized status + filled/remaining + evidence
cancelOrder(orderRef, authorization)   venue tarafından doğrulanan iptal sonucu
getPositions(accountRef)               miktar + maliyet + mark kaynağı + claimability
prepareClaim(positionRef, wallet)      doğrulanmış unsigned tx veya handoff nedeni
```

Capabilities olmayan işlem genel arayüz üzerinden zorlanmaz. İlk beta tek outcome’a tek emir verir. Uygunsa IOC/FAK tarzı “hemen doldur, kalanı iptal et” davranışı tercih edilir; gerçek destek ve semantik doğrulanmadan bu isim altında emir gönderilmez. Multi-market basket ve otomatik emir zinciri ilk sürümde yok.

### Temel veri modeli

`User`, `WalletLink`, `VenueAccount`, `Market`, `Outcome`, `MarketTermsVersion`, `MarketSnapshot`, `Room`, `RoomMembership`, `RoomMarket`, `Forecast`, `ForecastRevision`, `OrderIntent`, `Order`, `Fill`, `PositionSnapshot`, `ResolutionEvent`, `ScoreRevision`, `NotificationPreference`, `OutboxEvent`, `ModerationCase`.

Market kimliği `(venueId, venueMarketId)`; outcome kimliği venue tanımına bağlı. Aynı soru metni farklı venue’larda aynı market sayılmaz. İşlem miktarları integer string, fiyatlar kontrollü decimal/rational tipleri. `filled` durumu yalnızca HTTP 200 veya wallet imzasından türetilmez.

Oda yöneticisi seçki ve üyelik yönetebilir; venue market koşullarını veya kullanıcı geçmiş tahminini değiştiremez. Private oda için her okuma/yazmada üyelik yetkisi kontrol edilir. Davet tokenı kısa ömürlü ve iptal edilebilir; URL ile sızan private içerik herkese açılmaz.

## 6. Emir yaşam döngüsü ve hata davranışları

```text
DRAFT → REVIEW → AWAITING_SIGNATURE → SUBMITTING
                                   → ACCEPTED → PARTIALLY_FILLED → FILLED
                                              → CANCEL_REQUESTED → CANCELLED
             REJECTED / EXPIRED / FAILED / SUBMISSION_UNKNOWN
```

`SUBMISSION_UNKNOWN`: kullanıcı imzaladı, yanıt kayboldu. UI “işlem başarısız” demek yerine venue order/client ID veya imzalı order hash’iyle reconcile eder. Aynı order’ın tekrar gönderimi yalnızca venue’nun dedupe garantisi kanıtlanmışsa yapılır; yeni nonce ile kör retry yok.

Partial fill sonrasında kalan bakiye ve ortalama gerçekleşen fiyat gösterilir. Cancel requested, cancelled değildir; iptal yarışı sırasında ek fill gelebilir. Yeniden fiyatlanan quote kullanıcıya tekrar gösterilir. Order book staleness eşiği adapter bazında belirlenir; ilk öneri 5 saniyeyi aşan snapshot’ta yeni işlem öncesi refresh ve yeniden kontrol. Bu bir venue SLA iddiası değildir.

Ekranda üç farklı kavram vardır: order kabulü, fill, onchain settlement. Provider bunları ayrı sunmuyorsa “confirmed” terimi uydurulmaz; eldeki kanıtın adı gösterilir. Transaction receipt varsa gerçek zincir durumu ayrıca takip edilir.

Backend secrets manager venue uygulama kimlik bilgilerini tutar; frontend bundle’a konmaz. Kullanıcı wallet signature, nonce/domain/deadline ve plan hash’iyle bağlanır. SIWE benzeri giriş challenge’ı trade yetkisi vermez. API rate limit ve hesap-başına order idempotency zorunludur.

## 7. Sosyal tahmin ve itibar modeli

**Tahmin ile trade ayrı kayıtlar:** bir forecast market/outcome, olasılık, gerekçe ve zaman damgası içerir; finansal pozisyon açmak zorunda değildir. Trade için ekstra wallet ve açık maliyet onayı gerekir. Tahmin düzenlemeleri geçmişi silmez; eski sürüm görünür kalır.

İlk yarışma/oda modeli para ödülsüz haftalık tahmin sezonudur. Admin sezon başlamadan uygun market listesini ve her marketin tahmin kilit zamanını belirler. Yeni açılan bir market, sonraki sezona veya ayrı önceden ilan edilmiş tura eklenir. Böylece bazı kullanıcıların sonuca saniyeler kala girip diğerlerini haksız karşılaştırması azaltılır.

Binary market puanı için öneri: Brier loss `mean((p-y)^2)`; p, kullanıcının YES olasılığı, y nihai sonuç 0/1. Görsel puan `100*(1-Brier)` olabilir; bunun “yüzde doğruluk” olmadığı açıkça yazılır. Basit accuracy tek başına gösterilmez. En az 20 sonuçlanmış uygun tahmini olmayan kullanıcı “geçici geçmiş” etiketi taşır. Bu eşik ürün önerisidir, istatistiksel güven garantisi değildir.

Sıralama yalnızca aynı sabit market sepetinde, kilit öncesi tahmin yapan ve marketlerin en az %80’ine katılan kullanıcılar arasında yapılır; completion sayısı görünür. Küçük ilk pilotta leaderboard yerine kişisel sonuç geçmişi yeterlidir. Uzun vadede calibration ve örnek sayısı birlikte gösterilir; küçük örneklemden “en iyi trader” iddiası çıkarılmaz.

Void/cancelled/disputed sonuçlar kesin outcome gibi puanlanmaz. Nihai sonuç düzeltilirse eski score silinmeden yeni score revision üretilir. Trading PnL ile forecast puanı ayrı sekmededir. PnL gösterilecekse fee, gerçekleşmiş/gerçekleşmemiş kâr, dış transferler, değerleme zamanı ve desteklenmeyen pozisyonlar açıkça belirtilir; ilk sürümde güvenilmez toplam yerine venue bazlı pozisyon görünümü tercih edilir.

Anti-abuse: aynı hesap/market/sezon için tek puanlanan forecast; geçmişi silerek kötü sonuçları saklama yok; rate limit, moderasyon ve açık sponsorluk etiketi. Wallet sayısı insan sayısı değildir. Bakiye büyüklüğü itibar puanını satın alamaz.

## 8. Tasarım yönü ve ekran sistemi

**Görsel yaklaşım:** mobil öncelikli, sade editoryal kartlar. Launchpad’in yoğun terminal dilinden daha hafif. Açık nötr yüzey, koyu metin ve tek marka vurgusu önerisi; YES/NO yalnızca yeşil/kırmızıyla ayrılmaz. Kullanıcı önce soruyu ve bitiş koşulunu anlamalı. Sonsuz ticker, yanıp sönen kazanç animasyonu ve işlem yapmaya zorlayan sayaç yok.

Mobil ana navigasyon: **Keşfet · Odalar · Aktivite · Profil**. Pozisyonlar Aktivite içinde açık bir sekme. Desktop’ta sol navigasyon + ana feed + seçili market/oda paneli. Ana CTA “Tahminini kaydet”; “Pozisyon aç” ayrı, maliyet gösteren işlem akışıdır.

| Ekran | İçerik | Başarı ölçütü |
|---|---|---|
| Onboarding | Konu seç, örnek marketi oku, isteğe bağlı oda | Wallet bağlamadan ürünü anlayabilme |
| Explore | Açık soru, bitiş, gösterilen fiyatın türü, venue, veri yaşı | İlk anlamlı markete ulaşma |
| Market detay | Soru ve resolution koşulları, outcome, tahminler, kaynak, trade | Kullanıcı bitiş ile sonuçlandırmayı ayırabilir |
| Forecast sheet | Olasılık, gerekçe, kilit zamanı, görünürlük | Para harcamadan forecast kaydı |
| Trade sheet | Amount, alınacak pay, fee, maksimum harcama, fiyat etkisi | “Ne kadar kaybedebilirim?” sorusuna net yanıt |
| Room | Haftalık seçki, kurallar, üyeler, tahminler, geçmiş | İkinci hafta geri dönüş |
| Activity | Emir/fill/iptal/claim; sosyal bildirimler ayrı | Yanıt kaybında kullanıcı tekrar emir açmaz |
| Profile | Örnek sayısı, forecast geçmişi, score tanımı, privacy | Seçerek yalnızca kazanç paylaşma engellenir |
| Organizer | Seçki, davetler, moderasyon, katılım özeti | Kodsuz ikinci sezon oluşturma |

Market kartındaki “%62” otomatik olarak hakiki olasılık diye etiketlenmez. Kaynak son işlem, mid veya executable ask ise hangisi olduğu belirtilir; spread ve gerçek alınabilir fiyat detayda gösterilir. Süre dolması ödemenin hazır olduğu anlamına gelmez: `closed`, `resolving`, `disputed`, `resolved`, `claimable` ayrı UI durumlarıdır.

**Örnek trade sheet:** “10 USDC harca” → güncel quote’a göre pay sayısı → toplam ücret → tahmini gerçekleşen fiyat → “YES sonucu gerçekleşirse tahmini brüt ödeme” → bunun net kârdan farkı → onay. Gerçek fiyat alınmadan örnek rakam canlı işlem gibi gösterilmez. Olası kayıp, fee ve slippage aynı görünümde erişilebilirdir.

### Tasarım üretim sırası

1. 8–10 hedef kullanıcıyla günlük alışkanlık ve mevcut topluluk akışını araştır.
2. Explore→forecast→result ve market→trade→position akışlarını ayrı wireframe yap.
3. 390 px mobil ve 1440 px desktop prototip; 320 px reflow ve 200% zoom kontrolü.
4. Beş kullanıcıyla görev testi: market koşulunu anlat, forecast kaydet, fee’yi bul, partial fill’i yorumla.
5. Component/state matrisi: loading/empty/stale/offline/restricted/rejected/partial/disputed.
6. Metin rehberi: probability/price, forecast/order, potential payout/profit ve close/resolve terimleri.
7. Gerçek entegrasyonda wallet ve order state’lerini gözle; tasarım testini yalnızca mock prototiple bitirme.

Bildirimler opt-in: takip edilen market sonuçlandı, emir durumu değişti, haftalık özet hazır. Varsayılan günlük digest; sessiz saat tercihi; oda mention’ları ayrı kontrol. Kayıp sonrası “hemen geri kazan” mesajı, sürekli para yatırma çağrısı veya işlem streak’i kullanılmaz.

## 9. Haftalara göre geliştirme planı

Tahmin: bir deneyimli full-stack mühendis + yarı zamanlı tasarım/QA ve entegrasyon desteğiyle 8–12 hafta consumer v1 planlama zarfı. Partner erişimi ve inceleme bekleme süreleri bunun dışında uzama yaratabilir. Launchpad’i de aynı kişi geliştiriyorsa bu süreler toplanır, paralel kabul edilmez.

| Aşama | Zaman | Teknik teslim | Tasarım/ürün teslim | Çıkış kapısı |
|---|---|---|---|---|
| P-A | H1–2 | Adapter spike, katalog ve capabilities, auth/order recovery tasarımı | Görüşmeler, iki pilot oda, clickable prototip | Venue ve wallet yolu kanıtlı veya açık blocked |
| P-B | H3–4 | Market sync, rooms, auth, forecast revision, sonuç worker’ı | Explore, market, oda, forecast akışı | Gerçek katalogla sosyal alpha; tahmin geçmişi silinemiyor |
| P-C | H5–6 | Signed order, idempotency, fill reconciliation, positions | Trade sheet ve tüm hata durumları | Partial fill, timeout ve cancel race testleri |
| P-D | H7–8 | Claim/handoff, moderation, outbox, score revision | Aktivite, profil, privacy, haftalık recap | İki toplulukta iki tamamlanmış kullanım döngüsü |
| P-E | H9–12 | Hardening, restore, load, erişim/partner kapıları | Onboarding iyileştirmesi, organizer araçları | Production checklist ve bağımsız inceleme tamam |

P-A sonucu olumsuzsa P-C’ye geçilmez. Gerçek verili sosyal ürün, onaylı veri kullanım koşullarında devam edebilir; farklı venue spike’ı ayrı kararla yapılır. “API erişilemiyor” diye sahte trade endpoint’iyle ürün tamamlanmış gösterilmez.

## 10. Teknik iş paketleri ve kabul senaryoları

Önerilen dosya yolları yeni uygulama içindir. Birim testleri business kurallarını; adapter contract testleri gerçek veri semantiğini; E2E testleri kullanıcı akışını kanıtlar. Gerçek para işlemleri, test adında otomatik yapılmaz.

| Paket | Dosya alanı | Zorunlu senaryo |
|---|---|---|
| PR-01 Venue adapter | `packages/venue-limitless/src/adapter.ts` | Pagination, missing field, rate limit, timestamp ve unsupported capability |
| PR-02 Market lifecycle | `packages/domain/src/market.ts` | Closed ama unresolved market, void ve revised outcome |
| PR-03 Kimlik/odalar | `apps/api/src/rooms/`, `auth/` | Private odaya üye olmayan erişemez; nonce tekrar kullanılamaz |
| PR-04 Forecast/reputation | `packages/domain/src/forecast.ts`, `scoring.ts` | Kilit sonrası revizyon puanı etkilemez; cherry-pick geçmiş silinemez |
| PR-05 Order coordinator | `apps/api/src/orders/`, `apps/worker/src/reconcile.ts` | Venue kabul ederken HTTP timeout: ikinci order oluşmaz |
| PR-06 Fill ve cancel | `packages/domain/src/order-state.ts` | Partial fill ardından cancel, geç fill, duplicate websocket, out-of-order event |
| PR-07 Position/claim | `apps/api/src/positions/`, `claims/` | Yanlış wallet/chain/target reddi; ikinci claim güvenli hata |
| PR-08 Bildirim/moderasyon | `apps/worker/src/outbox.ts`, `apps/api/src/moderation/` | Tek sonuç tek bildirim; silinen içerik finansal kaydı silmez |
| PR-09 Arayüz | `apps/web/e2e/forecast.spec.ts`, `trade.spec.ts` | Forecast parasız; emir için ayrı açık imza; unsupported wallet açıklaması |
| PR-10 Operasyon | `docs/runbooks/venue-outage.md`, `restore.md` | Stream kesintisi sonrası tam reconciliation; backup restore |

Önerilen kök script’ler: `pnpm typecheck`, `pnpm test:domain`, `pnpm test:adapter`, `pnpm test:api`, `pnpm test:e2e`, `pnpm build`. Deterministik fixture testleri CI’da çalışır; fixture kaynağı ve tarihi bellidir. Read-only canlı adapter smoke testi izinli ağ ortamında ayrı çalışır. Sandbox/testnet mevcut değilse gerçek para trade testinin yerine mock konup entegrasyon onayı verilmez; o kapı blocked kalır ve ayrı yetkili kontrollü test gerekir.

### Release kabul matrisi

- [ ] PP01: Market soru, deadline, outcome ve kaynak koşulu venue ile eşleşiyor.
- [ ] PP02: Login olmadan public veri okunabiliyor; private oda korunuyor.
- [ ] PP03: Forecast oluşturmak wallet onayı veya fon hareketi üretmiyor.
- [ ] PP04: Her emir exact user intent, domain, nonce ve expiry ile bağlı.
- [ ] PP05: HTTP timeout veya tekrar tıklama çift emir oluşturmuyor.
- [ ] PP06: Fill ve cancel durumları venue reconciliation ile doğru.
- [ ] PP07: Resolved/void/disputed geçmişi ve skor revizyonu korunuyor.
- [ ] PP08: Pozisyon ve claim kullanıcının doğrulanan hesabına ait.
- [ ] PP09: Stale fiyat, kesinti ve unsupported rota yanıltıcı sıfır/başarı göstermiyor.
- [ ] PP10: Bildirim tercihi, unsubscribe, rate limit ve moderation çalışıyor.
- [ ] PP11: Gerçek erişim/partner şartları ve hedef ülke değerlendirmesi tamam.
- [ ] PP12: Restore, monitoring, wallet-signature ve dependency incelemesi tamam.

## 11. Ölçüm ve gelir doğrulaması

Ana ürün metriği: bir haftada en az bir geçerli tahmin kaydedip sonucunu görmeye dönen kullanıcı. Trading metriği ayrı: gerçek fill alan ve sonraki hafta tekrar kullanan trader. Para yatırmak, imza vermek veya accepted order tek başına aktif trader değildir.

Funnel: market_view → forecast_saved → result_viewed → next_week_return. Finansal funnel: trade_reviewed → signature_requested → order_submitted → order_filled → position_viewed/claimed. Kullanıcı imza reddi, yeterli bakiye olmaması ve teknik hata ayrılır. Analytics’e özel anahtar, signature veya oturum tokenı gönderilmez.

Pilot hedefleri, tahmin değil: iki oda, toplam 40–80 davetli, iki haftalık tamamlanmış sezon, en az 15 nitel görüşme. İlk karar ölçütü: katılanların %30’unun ikinci haftada yeni tahmin kaydetmesi ve her odanın yöneticisinin ikinci sezonu yeniden açması. Küçük örneklemde bu oranlar kesin başarı ölçütü sayılmaz; kullanıcıların neden dönüp dönmediği görüşmelerle değerlendirilir.

Monetizasyon sırası:

1. Önce ücretsiz pilot; gerçek tekrar kullanımını doğrula.
2. Organizer için ücretli analitik, oda yönetimi veya özel görünüm talebini test et.
3. Venue partner/referral geliri ancak gerçek sözleşme ve teknik attribution varsa ekle.
4. Premium filtre/bildirim paketi, ücretsiz çekirdek kullanımı bozmadan test edilebilir.

Kullanıcıdan alınan uygulama ücreti, venue ücreti ve network maliyeti ayrı açıklanır. İlk finansal modelde doğrulanmamış referral geliri sıfır kabul edilir. Sponsorlu market seçkisi açıkça etiketlenir; itibar sıralaması satın alınamaz.

## 12. Öncelikli riskler ve sonraki karar

| Risk | Erken işaret | Yanıt |
|---|---|---|
| Venue bağımlılığı | Auth/partner yolu doğrulanamıyor | Sosyal scope’u dürüstçe sınırla; trade açma |
| Sosyal değer zayıf | Kullanıcı direkt venue’ya gidiyor | Oda ve sonucu görme döngüsünü test et; daha fazla özellik ekleme |
| Trader sayısı düşük | Forecast var, fill az | Consumer değerini trading’den ayrı ölç; zorla parasallaştırma |
| İnce piyasa | Spread/price impact kullanıcıyı şaşırtıyor | Market seçki filtresi, taze quote ve açık maliyet |
| İtibar manipülasyonu | Son dakika tahmin ve geçmiş temizleme | Sabit sepet, kilit zamanı, revizyon geçmişi |
| İçerik/mahremiyet | Sahte hesaplar, private oda sızıntısı | Yetki testleri, report/block ve görünürlük tercihleri |

İkinci venue ancak ilk venue’da tekrarlı kullanım ve adapter stabilitesi sağlanınca eklenir. Farklı marketlerin koşulları eşleşmeden odds karşılaştırması veya tek ortak outcome yaratılmaz. Kendi prediction protokolü bu yol haritasının devam zorunluluğu değildir; ayrı ürün ve sermaye kararıdır.

## İlk on iş günü

- [ ] İki topluluk yöneticisiyle pilot planı ve içerik takvimi oluştur.
- [ ] Tek venue market türü, erişim ve wallet capability matrisini tamamla.
- [ ] Explore, forecast sheet, trade sheet ve result prototipini kullanıcılarla dene.
- [ ] Typed adapter ile gerçek katalog ve lifecycle alanlarını oku.
- [ ] Timeout/partial fill/cancel davranışını test planına ve state machine’e bağla.
- [ ] Forecast kilidi, revision ve skor kurallarını ürün kararı olarak kaydet.
- [ ] Hedef ülkeler, şartlar ve veri kullanım değerlendirmesini başlat.

## Kaynak ve kanıt sınırı

- [Limitless resmî TypeScript SDK](https://github.com/limitless-labs-group/limitless-exchange-ts-sdk): entegrasyon olanağına kaynak; bizim partner iznimiz veya test başarımız değildir.
- [Araştırma arşivi](https://github.com/Zireaelst/Codex-Claude-Research): launchpad bağlamı ve önceki ürün araştırmaları. Bu consumer ürünün detaylı spec’i repo’da varmış gibi sunulmaz; buradaki ürün/UX/scoring kararları bu çalışmanın önerileridir.
- [Base ağ bilgileri](https://docs.base.org/get-started/connect-to-base): ağ bağlamı; venue işlem desteğinin bağımsız kanıtı değildir.

Bu plan hazır bir güvenlik denetimi, hukuki görüş, venue anlaşması veya deployment yetkisi değildir. Yerel geliştirme ve gerçek para ile yayın kapıları ayrı tutulmuştur.
