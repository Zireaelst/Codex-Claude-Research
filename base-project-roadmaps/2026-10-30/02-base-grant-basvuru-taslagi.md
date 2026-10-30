# Base Builder Grant — Launchpad: Feedback, Revize Plan ve Başvuru Taslağı

30 Ekim 2026 · Kaynak: [`2026-10-29/01-launchpad-roadmap.md`](../2026-10-29/01-launchpad-roadmap.md) · Yeni roadmap: [`01-launchpad-rakip-analizi-ve-roadmap.md`](01-launchpad-rakip-analizi-ve-roadmap.md)

---

## 1. En kritik bulgu: roadmap ile grant birbirini tutmuyor

Grant **canlı ve kullanılan ürün** istiyor: Base'de kontrat adresi, canlı link, Loom demo, DAU/WAU, all-time ve son 30 gün volume, bugünkü gelir, Builder Code.

Roadmap ise:

| Roadmap | Grant ne istiyor |
|---|---|
| İlk davetli beta (L1) 10–14 hafta sonra | Şu an canlı ürün |
| Tam kapsam 18–24+ hafta | "Past the idea stage" |
| L1 öncesi bağımsız güvenlik incelemesi şart | Kontrat adresi + kullanım sayıları |
| Pilot hedefi: 30 günde 3 lansman | Kullanıcı / volume metrikleri |

Bu haliyle başvurursan "idea stage" diye elenme ihtimali yüksek. Çözüm planı küçültmek değil, **sıralamayı değiştirmek**: önce küçük, denetlenmiş parçalarla mainnet'e çık, veri topla, sonra başvur. v4 curve + hook mimarisi grant sonrası büyüme hikâyesi olsun.

---

## 2. Roadmap feedback'i

### Güçlü yanlar (koru)
- Güvenlik disiplini çok iyi: invariant testleri, gerçek upstream harness, reorg-safe indexer, integer-string miktarlar, imzasız işlem planı API'si.
- "İşlem öncesi kural/maliyet görünümü" (Rules inspector) gerçekten ayrıştırıcı bir UX fikri.
- Creator gelirini platform gelirinden ayırma, wash volume'u ayrı raporlama → grant reviewer'ları buna değer verir.
- Builder Code iddiasında dürüst sınır koyulmuş.

### Değişmesi gerekenler

**1. Kapsam çok büyük, audit yüzeyi devasa.**
Registry, TokenFactory, CurveSale, GraduationExecutor, V4Locker, CompositeHook (6 modül), FeeVault, DustVault, Router, V3Launcher, ExistingPoolFactory, Reward/Maintenance/Community vault'ları… Bu, 2 kişilik ekip için ciddi bir audit bütçesi (muhtemelen 5 haneli $ üstü) ve aylar demek. $5K grant bunun yanında küçük kalır.
→ **İlk sürümde tek yol: tek bir launch tipi, tek fee modeli, kilitli LP.** Modüler hook, community, blueprints, harici havuzlar L3'e değil "grant sonrası" listesine.

**2. Sıralama tersine çevrilmeli: v3 instant / mevcut altyapı önce, özel v4 curve sonra.**
Roadmap v3 instant launch'ı L2'ye koymuş; oysa en hızlı ve en az riskli yol bu. Base'de v4 tabanlı açık kaynak/denetlenmiş launch altyapıları var (ör. Doppler protokolü, Clanker'ın açık kontratları — lisans ve audit durumlarını kendin doğrula). Bunların üstüne kurulup farklılaşmayı **UX + creator gelir yönetimi** katmanında yapmak, 4–6 haftada mainnet demek.

**3. USDC-öncelikli tercih tartışmalı.**
Base'deki meme/creator trader'ı ağırlıkla ETH ile işlem yapıyor; launchpad'lerin çoğu WETH eşli. USDC'yi ilk ve tek varlık yapmak dönüşümü düşürebilir. → **WETH ilk**, USDC opsiyonel (stabil fiyat isteyen "creator collective" preset'i için).

**4. Curve sırasında transfer edilemeyen "internal entitlement" sürtünme yaratır.**
Dexscreener/GeckoTerminal'de görünmez, cüzdanda görünmez, paylaşılamaz. Bu, launchpad'in en önemli büyüme kanalı olan sosyal viralliği keser. Güvenlik açısından mantıklı, ama ilk sürümde instant (havuz anında açık) model daha iyi dağıtım sağlar.

**5. 30 gün curve + 72 saat retry + refund mantığı** hem audit yükü hem de kullanıcıya anlatması zor. MVP'de çıkar.

**6. Farklılaşma çok soyut.** Clanker, Zora, Flaunch, Bankr, Doppler tabanlı launchpad'ler zaten Base'de. "Anlaşılır kurallar" bir hipotez; grant reviewer'ı "neden sen?" diye soracak. Daha keskin bir wedge seç, örneğin:
- **Creator gelir paneli + otomatik dağıtım** (fee'leri topluluğa/katkıcılara split etme), ya da
- **Dağıtım kanalı**: Base App mini app / Farcaster cast'ten ya da X bot'tan tek mesajla launch. Launchpad'lerde kazanan çoğu zaman en iyi kontrat değil, en iyi dağıtım kanalı.

**7. GTM bölümü yok denecek kadar ince.** "3 creator" bir pilot hedefi, GTM değil. Grant formu doğrudan 3 aylık GTM soruyor (aşağıda taslak var).

**8. Gelir modeli somut değil.** "Kaynak spec'teki ücretler" yazıyor. Forma net bir sayı lazım: ör. "her swap'ta %1 LP fee: %X creator, %Y protokol".

**9. Metrikler grant'ın sorduğu formatta değil.** Roadmap iyi metrikler ölçüyor ama formdakiler: all-time users, DAU, WAU, all-time volume, 30d volume. → İlk günden bu 5 sayıyı veren bir Dune dashboard'u kur; başvuruda link ver.

**10. Builder Code'u ilk deploy'dan itibaren ekle.** base.dev'den kodu al, uygulamanın gönderdiği her işleme attribution suffix'ini ekle. Hem formda soruluyor hem de Base'in senin trafiğini görmesinin yolu bu.

**11. Ekip/kapasite:** Prediction market roadmap'i de aynı ekipteyse, grant "exclusively building on Base" diyor — sorun değil, ama tek ürüne odaklandığını göster. İki ürünü paralel yürütmek ikisini de geciktirir.

---

## 3. Revize plan

Revize plan, rakip karşılaştırmasıyla birlikte [`01-launchpad-rakip-analizi-ve-roadmap.md`](01-launchpad-rakip-analizi-ve-roadmap.md) dosyasına taşındı. Özet: F1 (H2–4) canlı MVP → F2 (H5–8) dağıtım ve **grant başvurusu** → F3 curve modu + audit → F4 v1'deki L2/L3 kapsamı.

---

## 4. Başvuru formu taslağı (İngilizce, köşeli parantezleri doldur)

> ⚠️ Sayıları asla tahmin/şişirme ile doldurma; Base ekibi on-chain doğrulayabilir. Gerçek veri yoksa başvuruyu birkaç hafta ertele.

**Project name + one-line description**
> [Name] — the Base token launchpad where creators earn the most: launch in one click from the Base App or socials, earn 70% of every trade's fee in ETH, with locked liquidity and a clear rules card traders see before they buy.

**Tell us about the founding team**
> [Name 1] — [role], [background: e.g., Solidity/EVM experience, prior protocols, hackathon wins]. [Name 2] — [role], [full-stack/product background]. [Funding raised: e.g., "Bootstrapped, no outside funding"]. Domain expertise: [Uniswap v4 hooks, launch mechanics research, previous Arc/Stellar launchpad implementations].

**Link to live product / Loom / Contract address**
> [https://...] / [Loom: 2–3 dk — launch → buy → creator claim akışı] / [0x... (Base mainnet factory)]

**Track**
> Trading (ya da "Diğer: Token Launchpads" — açıklamada launchpad kategorisi zaten geçiyor, "Diğer"e "Token Launchpad" yazmak daha net)

**Key usage numbers**
> All-time users: [X] unique wallets · DAU: [X] · WAU: [X] · All-time volume: $[X] · Last 30 days: $[X] · [N] tokens launched, [N] creators claimed fees. Dashboard: [Dune link]. (Team/test wallets excluded.)

**How does your product make money today?**
> Every trade on a launched token's pool pays a fixed 1% fee, paid in WETH: 70% to the creator, 30% to the protocol. No platform token. To date: $[X] protocol revenue, $[X] paid out to creators.

**GTM plan for the next 3 months**
> 1) Creator pipeline: onboard [20] creators/communities from Farcaster and X with 1:1 launch support; each launch comes with a shareable rules card.
> 2) Distribution: ship a Base App / Farcaster mini app so tokens can be launched and traded inside the feed; [X bot] for launch-by-mention.
> 3) Creator earnings as the hook: public leaderboard of fees earned by creators, weekly "creator payout" posts.
> 4) Integrations: get indexed on Dexscreener/GeckoTerminal and aggregators; listing on Base ecosystem pages.
> Targets by end of month 3: [X] launches, [X] WAU, $[X] monthly volume, [X]% of creators launching a second token.

**Base Builder Code**
> [base.dev'den alınan kod]

**Primary challenge**
> **User acquisition** (launchpad için gerçek darboğaz dağıtımdır). Kontratlar denetlenmediyse ikinci olarak "Smart contract security/auditing" de mantıklı, ama tek seçim gerekiyorsa User acquisition.

**Credits**
> Privy (embedded wallets / social login ile kripto-yeni kullanıcı onboarding), Coinbase Developer Platform (Paymaster ile gasless ilk işlem, OnchainKit), RPC credits (Alchemy/QuickNode), audit desteği/indirimi, AWS.

**Applying for the second time?**
> İlk başvuruysa: "First application." Tekrarsa: geçen seferden beri değişen somut metrikler (ör. "Since last application: mainnet launch, X users, $Y volume, mini app shipped").

---

## 5. Başvurudan önce kontrol listesi

- [ ] Base mainnet'te doğrulanmış (Basescan verified) kontrat
- [ ] Canlı, mobilde çalışan site
- [ ] 2–3 dakikalık Loom: launch → trade → creator claim (gerçek mainnet işlemi)
- [ ] Builder Code tüm işlemlerde ekli
- [ ] Dune dashboard (5 grant metriği, test cüzdanları hariç)
- [ ] Net fee modeli ve UI'da görünür olması
- [ ] X hesabı aktif, en az birkaç launch duyurusu
- [ ] En az 2–4 haftalık gerçek kullanım verisi
