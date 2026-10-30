# Base Launchpad — Rakip Karşılaştırması ve Grant Odaklı Yol Haritası

30 Ekim 2026 · Sürüm 3.0 · Önceki sürüm: [`2026-10-29/01-launchpad-roadmap.md`](../2026-10-29/01-launchpad-roadmap.md)
Durum: planlama dokümanı. Rakip rakamları üçüncü taraf kaynaklardan derlenmiştir ve kaynaklar arasında çelişki vardır; on-chain doğrulama yapılmamıştır. Kontrat bilgileri 30 Ekim 2026'da ilgili GitHub repolarından okunmuştur.

**v3'te değişenler:**
1. Base App, Farcaster akışını ve mini app desteğini kaldırdı. Dağıtım planı buna göre yeniden yazıldı (§2).
2. MVP artık kendi kontratımızla değil, **denetlenmiş ve MIT lisanslı hazır kontratların kendi instance'ımızla** çıkıyor (§4).
3. Özel launch kısmı, AvaxHook'un kural kataloğundan seçilmiş, sınırlı bir v4 hook modül seti olarak tasarlandı (§5).

Ana sıra: **audit'li hazır kontratlarla canlı MVP → dağıtım + ekstra özellikler → grant → kendi v4 hook'umuzla özel launch.**

---

## 1. Rakip karşılaştırması

| | pump.fun | PONS | Clanker | Zora | Flaunch | AvaxHook / Hookr | **Biz (hedef)** |
|---|---|---|---|---|---|---|---|
| Ağ | Solana | Robinhood Chain | Base | Base | Base (+ ETH, Arb, Robinhood) | Avalanche | Base |
| Launch modeli | Bonding curve → PumpSwap | v1 doğrudan v3; v2 curve → v4 + hook | Anında v4 havuz, kilitli LP | Content/creator coin | 30 dk sabit fiyat → price discovery, bid wall | Curve → v4 + seçilebilir kurallar | **F1: anında v4 (Uniswap Liquidity Launcher); F3: curve + kendi hook'umuz** |
| İşlem ücreti | Curve ~%1,25; PumpSwap'ta kademeli | %1 | Statik/dinamik hook | Creator/pool + arayüz ücreti | %1 | Kural bazlı | **F1: %0,25 (Base'in en düşüğü); F3: creator seçimli** |
| Creator payı | Market cap'e göre kademeli | %70, ETH | Ödül alıcılarına bölünür (7'ye kadar) | Creator + referral | Dev payı + topluluk (bid wall/treasury) | Kural bazlı | **Fee'nin %60'ı, ETH** |
| Ekstra mekanikler | Livestream, mobil app | Holder ödülü, creator tax | Sniper auction, airdrop, vault | Content keşfi | Bid wall, treasury | 50+ kural (koruma, ödül, oyun) | **Seçilmiş 12 modül (§5)** |
| Audit | — | v2 canlıya çıkarken audit sürüyordu | Cantina + Macro (×2) | — | EnigmaDark + Omniscia | Doğrulanmadı | **F1: Uniswap'ın 6 audit'i; F3: kendi audit'imiz** |
| Platform tokenı | PUMP | PONS | CLANKER | ZORA | FLAY | — | **Yok** |
| Dağıtım | Alışkanlık, ölçek | Yeni zincirin ilk launchpad'i | Farcaster bot (Farcaster/Neynar'a ait) | Base App (eskiden gömülüydü) | Web + topluluk | Web | **Base.dev listesi, X/Telegram bot, partner arayüzler** |

Kaynaklar: [Blockworks — pump.fun dinamik fee](https://blockworks.co/news/pumpdotfun-fee-model), [The Block — PumpSwap creator revenue](https://www.theblock.co/post/354038/pumpswap-revenue-tokens), [BlockEden — PumpSwap 2026](https://blockeden.xyz/blog/2026/04/12/pumpswap-16b-volume-pumpfun-amm-raydium-solana-dex/), [Crypto Briefing — pump.fun gelir](https://cryptobriefing.com/pump-fun-50m-monthly-revenue-surpasses-solana/), [PONS docs](https://docs.ponsfamily.com/), [Datawallet — PONS](https://www.datawallet.com/crypto/pons-explained), [DefiLlama — PONS v2](https://defillama.com/protocol/pons-v2), [The Block — Clanker](https://www.theblock.co/post/349549/clanker-team-earns-13-million-in-revenue-from-over-200000-tokens-on-base-in-just-five-months), [Clanker v4 contracts](https://github.com/clanker-devco/v4-contracts), [Flaunch FAQ](https://docs.flaunch.gg/protocol/frequently-asked-questions), [Flaunch contracts](https://github.com/flayerlabs/flaunchgg-contracts), [AvaxHook hooks](https://docs.avaxhook.fun/hooks), [Uniswap Liquidity Launcher](https://github.com/Uniswap/liquidity-launcher).

---

## 2. Base App değişikliği: gerçekten boşluk var mı?

**Ne oldu:**
- **Şubat 2026:** Base App, Farcaster tabanlı "Talk" akışını kaldırdı ve odağını onchain trading'e çevirdi ([The Block](https://www.theblock.co/news/ecosystems/2026-02-10-base-app-removes-farcaster-powered-talk-feed-to-sharpen-focus-on-onchain-trading-389191), [CryptoRank](https://cryptorank.io/news/feed/7469c-base-app-removes-farcaster-social-feed)).
- **9 Nisan 2026:** Base App, Farcaster mini app spec'ini ve Neynar altyapısını bıraktı. Artık her uygulama, Base App'in kendi tarayıcısında cüzdanı enjekte edilmiş **standart web app** olarak açılıyor; listeleme Base.dev metadata'sından geliyor; Farcaster ile giriş ve FID kimliği yok ([Base docs — migrate to standard web app](https://docs.base.org/apps/guides/migrate-to-standard-web-app), [Base Build duyurusu](https://x.com/buildonbase/status/2032126286542311778), [Paragraph — mini app stack ayrılığı](https://paragraph.com/@arcabot/base-and-farcaster-split-the-mini-app-stack), [Nicky Sap](https://nickysap.substack.com/p/are-we-still-doing-mini-apps)).
- Farcaster mini app'leri Farcaster istemcilerinde çalışmaya devam ediyor; değişiklik yalnızca Base App'i kapsıyor.

**Yorum: evet, boşluk var, ama "dağıtım problemi çözüldü" anlamına gelmiyor.**

| Lehimize | Aleyhimize |
|---|---|
| Base App içindeki sosyal akıştan token basma (Zora/Clanker'ın 2025'teki avantajı) ortadan kalktı; giriş engeli herkes için eşitlendi | Clanker hâlâ Farcaster'da, Zora hâlâ kendi app'inde; marka ve alışkanlık onlarda |
| Base App artık trading odaklı: Base'deki tokenlar orada işlem görüyor, yani bizim tokenlarımızın talep tarafı büyüyor | Sosyal akış yokken viral döngüyü X ve Telegram üzerinden kurmamız gerekiyor |
| Standart web app modeli: tek kod tabanı, Base.dev'e listelenmek mini app'ten basit | Base.dev listesinde öne çıkmak garanti değil |
| Base'de gas çok düşük: launch ve küçük işlemler neredeyse bedava | Düşük gas spam ve scam tokenı da kolaylaştırıyor; kalite filtresi şart |

**Sonuç:** Base App'in boşalttığı alan, **"web'den çalışan, Base App tarayıcısında da sorunsuz açılan, X/Telegram ile yayılan launchpad"** için gerçek bir fırsat. Bunu "Base'de kimse token bastırmıyor" diye değil, **"sosyal akış avantajı sıfırlandı; en iyi web deneyimi ve en iyi teşvikler kazanır"** diye anlatmalıyız (grant başvurusunda da bu dil).

---

## 3. Rakiplerden alınacak dersler

1. **Kazanan dağıtım kanalıdır.** Base App'in sosyal akışı gidince kanal: Base.dev listesi + X bot + Telegram bot + partner arayüzler.
2. **Launch sonrası işlem yeri gelirin kaynağıdır** (pump.fun → PumpSwap). Bizde: havuzun LP fee'si ve F3'te kendi hook'umuz.
3. **Creator'a cömert pay, ETH olarak** (PONS %70 ETH, Flaunch flETH). Creator kendi tokenıyla ödeme almamalı.
4. **Düşük ücret Base'in avantajıyla örtüşüyor.** Gas zaten düşük; işlem ücreti de en düşük olursa "Base'de token basmanın en ucuz yeri" mesajı tutar.
5. **Kural kataloğu çok büyük olursa güven kaybolur.** AvaxHook 50+ kural sunuyor; dokümanı bile birçoğunun bypass edilebildiğini, aggregator alımlarının çoğunun atfedilemediğini ve rastgeleliğin block hash'e dayandığını söylüyor. Biz az, test edilmiş, anlaşılır modül sunacağız (§5).
6. **Audit'i süren kontratla canlıya çıkmak risk** (PONS v2). F1'de yalnızca audit'li kodu config değiştirerek kullanıyoruz.
7. **Platform tokenı ve buyback** talebi şişiriyor ama düzenleyici ve itibar riski taşıyor. İlk 6 ayda yok.

---

## 4. Hazır, audit'li kontratlar: inceleme ve karar

| Seçenek | Lisans | Audit | Base'de | Özelleştirme | Bize uygunluk |
|---|---|---|---|---|---|
| **Uniswap Liquidity Launcher** | MIT | OpenZeppelin (×3), Spearbit (×2), ABDK; Cantina bug bounty | Evet (v3.3.0) | `FeeSplitter` dağılımları constructor parametresi → kendi instance'ımızda **kod değiştirmeden** creator/platform payı ayarlanabilir. LP fee %0,25, ETH pair ve 1 milyar arz sabit | **F1 için en iyisi**: en çok audit, Uniswap güveni, admin'siz kilitli LP, kendi kontrat adresimiz (grant için) |
| **Clanker v4** | Kaynak dosyalarda MIT (repoda ayrı LICENSE dosyası yok) | Cantina + Macro (×2) | Evet, deploy edilmiş | Deploy edilmiş kontratları SDK ile kullanmak mümkün: 7'ye kadar ödül alıcısı, arayüz kendini alıcı olarak ekleyebilir. Hook, locker, extension ve MEV modülleri Clanker ekibinin allowlist'ine bağlı | **Yedek F1** (sıfır deploy, en hızlı) ve F3 için hook referansı. Clanker'a bağımlılık ve marka gölgesi dezavantaj |
| **Flaunch** | MIT | EnigmaDark + Omniscia | Evet (v1.3.1) | SDK (`@flaunch/sdk`), bid wall, treasury, revenue manager | F3'te fair-launch/bid wall fikri için referans; kodu karmaşık |
| **Doppler** (Whetstone) | Public repo bulunamadı | 2024'te Cantina yarışması | SDK'ya göre Base'de canlı | Dutch auction tabanlı v4 hook | Lisans/kod erişimi netleşmeden kullanılmaz |
| Kendi kontratımız (v1 roadmap) | — | Yok | — | Tam | F3/F4'e |

**Karar:**
- **F1:** Uniswap Liquidity Launcher'ın `InstantLaunchStrategy` + `FeeSplitter` + `BeneficiaryVault` kontratlarının **kendi instance'ımızı**, kodu değiştirmeden yalnızca constructor parametreleriyle deploy et. Fee dağılımı: **%60 creator (BeneficiaryVault üzerinden, ETH) / %40 platform**. Audit'in geçerli kalması için kodu birebir aynı commit'ten deploy et ve config'i bağımsız birine kontrol ettir.
- **Plan B:** Instance deploy'unda engel çıkarsa Clanker v4'ün deploy edilmiş kontratlarını SDK ile kullan, platformu ödül alıcısı olarak ekle.
- **Uyarı:** Uniswap'ın `InstantLaunchStrategy`'si hook'suz. Anti-snipe, kural kartındaki özel kurallar ve dinamik fee **F1'de yok**; bunlar F3'teki kendi hook'umuzla gelir. F1'deki ekstralar kontrat dışı (UI, keşif, bot, ödül programları) olacak.
- **Kontrol listesi (F0):** commit hash eşleşmesi, Base'deki Uniswap v4 PoolManager/PositionManager adresleri, `FeeSplitter` dağılımlarının değişmezliği, `BeneficiaryVault` NFT'sinin creator'a geçişi, Uniswap v4 core'un BUSL lisansıyla ilgili sınırlar (biz core'u deploy etmiyor, kullanıyoruz).

---

## 5. Özel launch: kendi v4 hook'umuz (F3)

AvaxHook kataloğundan, saldırı yüzeyi ve anlaşılırlığa göre seçilmiş modüller. **Bir havuzda en fazla 6 modül.** Her modül kural kartında insan diliyle gösterilir.

| Grup | Modül | Neden | AvaxHook'taki karşılığı ve not |
|---|---|---|---|
| Koruma | **Anti-snipe** (ilk N blok yüksek vergi, vergi likiditeye) | Base'de sniper en büyük şikâyet | Anti-snipe (curve/pool open) |
| Koruma | **Whale guard** (tek işlem alım tavanı) | Basit, aggregator'la uyumlu | Whale guard |
| Koruma | **Yükselen cüzdan tavanı** (lansmanda %1, zamanla kalkar) | Adil dağıtım | Rising max per wallet; en fazla 7 gün |
| Koruma | **Satış vergisi azalması** (ilk saatlerde ekstra satış fee'si, sıfıra iner) | Dump'ı caydırır, satışı engellemez | Sell tax decay |
| Ücret | **Dinamik fee** (büyük işlemde fee artar, tavan sabit) | Sniper/MEV gelirini LP'ye çevirir | Dynamic fee; tavan ≤ %3 |
| Ücret | **Creator fee seçimi** (%0,25–%1) | pump/PONS seviyesinde gelir isteyen creator'a seçenek | Toplam fee tavanı sabit |
| Ücret | **Referral** | Dağıtımı X/Telegram'a taşır | Referral; yalnızca doğrudan router işlemlerinde atfedilir |
| Ödül | **Holder dividend** (fee'nin bir kısmı holder'lara ETH olarak) | PONS'un çalışan özelliği | Holder dividends |
| Ödül | **Lock & earn** (kilitleyen fee kazanır) | Uzun vadeli holder | Lock & earn; en fazla 365 gün |
| Ödül | **Auto-LP** | Likidite derinleşir | Auto-LP |
| Ödül | **Buyback & burn** | Topluluk talebi | Buyback & burn; fiyat etkisi ≤ %5 |
| Oyun (F4, hukuki kontrol sonrası) | **Last-buyer pot / King of the Hill** | Etkileşim çok yüksek | Şans/kumar algısı ve atfetme sorunları nedeniyle ayrı karar |

**Bilinçli olarak alınmayanlar:** allowlist/blocklist (yeni cüzdanla bypass), DEX-only (kontratla bypass), Plague, Polarity (kaldıraçlı ikiz coin, düzenleyici risk), Quantum jackpot (grind edilebilir rastgelelik), Market hours, Red light/green light, Ping pong, Arcade.

**Mimari:** Tek bir composite hook + onaylı modül registry'si (v1 roadmap'teki CompositeHook/HookRegistry ilkeleri). Referans olarak audit'li Clanker v4 hook'ları ve Flaunch PositionManager'ı (ikisi de MIT) incelenir; kopyalanan kısımlar lisans notuyla işaretlenir. Curve modu (pump tarzı) bu hook'la birlikte gelir ve graduation kendi v4 havuzumuza olur. **Bağımsız audit olmadan F3 mainnet'e çıkmaz.**

---

## 6. Ekstra özellikler (kontrat gerektirmeyen, F1–F2)

İnsanları Base'de token basmaya teşvik edecek, F1 kontratlarıyla uyumlu özellikler:

- **Tek tıkla launch:** isim, sembol, görsel → 30 saniyede canlı. Opsiyonel creator ilk alımı aynı işlemde (`UniversalRouterStrategy` ile).
- **Gasless ilk launch:** Coinbase Paymaster ile ilk launch'ın gas'ını biz öderiz (Base'de maliyet çok düşük).
- **Kural kartı:** her tokenda ücret, creator payı, kilitli LP ve sabit arz tek bakışta; X/Telegram'da paylaşılınca OG görseli olarak açılır.
- **Creator gelir paneli:** tüm tokenlardan birikmiş ETH, tek tıkla claim; kazanç leaderboard'u.
- **Launch bot'ları:** X'te "@bot launch $TICKER" ve Telegram'da `/launch` (Clanker'ın Farcaster'daki modelinin X/Telegram karşılığı).
- **Keşif:** yeni / trend / en çok kazandıran creator / graduation'a yakın (F3). Wash ve kendi cüzdan aktiviteleri filtrelenir.
- **Kalite filtresi:** metadata doğrulama, kopya ticker uyarısı, raporlama. Düşük gas spam'i çeker; board kalitesi güveni belirler.
- **Creator teşvik programı (grant fonuyla):** ilk 100 creator'a gas desteği + ilk ay için platform payından ek bonus.
- **Base App uyumu:** standart web app olarak Base App tarayıcısında test, Base.dev metadata'sı, enjekte cüzdan desteği.
- **Builder Code:** tüm işlemlerde.

---

## 7. Yol haritası

| Faz | Hafta | Kapsam | Çıkış koşulu |
|---|---|---|---|
| **F0 — Doğrulama** | H1 | Liquidity Launcher instance planı ve §4 kontrol listesi, fee dağılımı (%60/40), marka, Builder Code (base.dev), Dune şeması, 5 creator + 5 trader görüşmesi | Yazılı karar kaydı; Base Sepolia'da test launch |
| **F1 — Canlı MVP** | H2–4 | Kendi `FeeSplitter`/`BeneficiaryVault`/`InstantLaunchStrategy` instance'ımız mainnet'te; launch wizard, token sayfası + kural kartı, creator paneli, board, gasless ilk launch, Base App tarayıcı testi | **Base mainnet kontrat adresi, canlı site, Loom demo** |
| **F2 — Dağıtım + ekstralar** | H5–8 | X/Telegram launch bot'ları, leaderboard, paylaşılabilir kartlar, Base.dev listesi, referral programı (off-chain), creator teşvik programı, Dexscreener/GeckoTerminal | 2–4 haftalık gerçek DAU/WAU/volume → **grant başvurusu (H6–8)** |
| **F3 — Özel launch (kendi hook)** | H9–18 | Composite v4 hook + §5'teki modüller + curve modu → kendi havuzumuza graduation; invariant testleri, bağımsız audit (grant + credits desteğiyle) | Audit bulguları kapatılmış; "Özel launch" seçeneği açık, instant launch varsayılan kalır |
| **F4 — Genişleme** | H18+ | Oyun modülleri (hukuki kontrol sonrası), mevcut token havuzları, LP ödülleri, community funding, imzasız API, kademeli creator fee | Her yeni modül ayrı inceleme kapısından geçer |

---

## 8. Gelir modeli

- **F1:** Havuz LP fee'si %0,25 → %60 creator, %40 platform (ETH). $1M aylık volume → $1.500 creator, $1.000 platform.
- **F3:** Özel launch'ta creator %1'e kadar fee seçebilir. Platform payı modül bazlı ve kural kartında görünür.
- Platform tokenı, buyback ve airdrop vaadi yok.
- Gerçekçi not: F1'de gelir düşük. Hedef gelir değil, **kullanıcı ve launch hacmi** (grant'in ölçtüğü şey). Gelir F3'teki premium modüllerle büyür.

---

## 9. Metrikler

Grant'in istediği 5 metrik ilk günden Dune'da (ekip/test cüzdanları hariç): all-time kullanıcı, DAU, WAU, all-time volume, son 30 gün volume. Ek olarak: launch sayısı, ikinci token çıkaran creator oranı, creator'lara ödenen ETH, 7 günlük trader dönüşü, bot üzerinden yapılan launch oranı.

| Zaman | Hedef (planlama varsayımı, taahhüt değil) |
|---|---|
| H4 | 10 pilot launch, 200+ benzersiz trader |
| H8 (grant) | 100+ launch, 1.000+ kullanıcı, haftalık volume trendi pozitif |
| H18 | Özel launch canlı, creator tekrar kullanım oranı %20+ |

---

## 10. Riskler

| Risk | Önlem |
|---|---|
| Dağıtım yok | F2'yi F1 ile paralel başlat; bot'lar ve ilk 20 creator'ı birebir onboard etmek |
| Spam/scam token (düşük gas) | Kalite filtresi, kopya ticker uyarısı, raporlama; kural kartında risk etiketleri |
| Sniper'lar (F1'de hook yok) | UI'da creator ilk alımı + aynı blokta launch; asıl çözüm F3'teki anti-snipe. Bunu açıkça yaz |
| Audit'li kodun yanlış config'le deploy edilmesi | Aynı commit, deploy script'i incelemesi, Sepolia'da uçtan uca test |
| Clanker/Zora/Flaunch ile rekabet | En düşük ücret + creator payı + bot dağıtımı + kural kartı; özellik sayısıyla yarışmamak |
| F3 hook'unda güvenlik hatası | Modül sınırı, invariant testleri, bağımsız audit, düşük limitli beta |
| Oyun modüllerinde düzenleyici risk | F4'e ertelendi, hukuki görüş şart |

---

## 11. İlk 10 iş günü

- [ ] Liquidity Launcher repo'sunu klonla, v3.3.0 commit'ini sabitle, testleri çalıştır
- [ ] Kendi `FeeSplitter` (%60/40) + `BeneficiaryVault` + `InstantLaunchStrategy` instance'ını Base Sepolia'ya deploy et
- [ ] Marka adı, domain, X ve Telegram hesapları
- [ ] base.dev: Builder Code + uygulama metadata'sı
- [ ] Launch wizard + token sayfası + kural kartı (mobil öncelikli, Base App tarayıcısında test)
- [ ] Dune dashboard iskeleti
- [ ] 10 pilot creator listesi ve launch tarihleri
- [ ] F3 için hook modül spesifikasyonu (§5) ve audit firmalarından teklif

İlgili doküman: [`02-base-grant-basvuru-taslagi.md`](02-base-grant-basvuru-taslagi.md) (v1 feedback'i ve grant form cevap taslakları).
