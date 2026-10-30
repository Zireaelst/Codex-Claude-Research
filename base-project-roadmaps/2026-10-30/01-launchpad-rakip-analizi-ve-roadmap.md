# Base Launchpad — Rakip Karşılaştırması ve Grant Odaklı Yol Haritası

30 Ekim 2026 · Sürüm 2.0 · Önceki sürüm: [`2026-10-29/01-launchpad-roadmap.md`](../2026-10-29/01-launchpad-roadmap.md)
Durum: planlama dokümanı. Rakip rakamları üçüncü taraf kaynaklardan derlenmiştir, kaynaklar arasında çelişki vardır; on-chain doğrulama yapılmamıştır.

**Bu sürümde ne değişti:** v1 roadmap güvenlik açısından sağlam ama ilk kamuya açık sürüm 10–14 hafta sonra. Base Builder Grant ise canlı ürün, kontrat adresi ve kullanım metrikleri istiyor. Bu sürüm pump.fun, PONS ve Base'deki rakiplerden çıkan derslerle sıralamayı değiştirir: **önce dar ama canlı ürün → dağıtım → grant → curve ve gelişmiş modüller.**

---

## 1. Rakip karşılaştırması

| | pump.fun | PONS | Clanker | Zora | Flaunch | **Biz (hedef)** |
|---|---|---|---|---|---|---|
| Ağ | Solana | Robinhood Chain | Base | Base | Base | Base |
| Launch modeli | Bonding curve → PumpSwap (kendi AMM'i) | v1: doğrudan v3 havuzu; v2: curve → v4 + hook | Anında v4 havuz, kilitli LP | Content/creator coin, anında havuz | Sabit fiyatlı açılış → price discovery, v4 hook | **MVP: anında v4 havuz; Faz 3: curve modu** |
| İşlem ücreti | Curve ~%1,25; PumpSwap'ta market cap'e göre kademeli | %1 | Statik/dinamik hook | Creator/pool fee + arayüz ücreti | Hook tabanlı | **%1 sabit, değişmez** |
| Creator payı | Kademeli: küçük cap'te yüksek (~%0,95), büyük cap'te düşük (~%0,05) | %70 creator / %30 protokol, ETH olarak ödenir | Pozisyon bazlı ödül | Creator + referral | Gelir hakkı, topluluk treasury'si | **%70 creator / %30 protokol, WETH olarak** |
| Holder ödülü | Yok | Var (fee'yi holder'lara pro-rata yönlendirme) | Kısmen | Yok | Buyback/treasury | **Faz 2: holder ödül modu** |
| Platform token / buyback | PUMP; gelirin büyük kısmı buyback | PONS; protokol payının %80'i buyback-burn | CLANKER | ZORA | FLAUNCH | **Yok (bilinçli karar)** |
| Dağıtım kanalı | Kendi sitesi, mobil app, livestream, Solana trader kültürü | Yeni zincirin "yerli" launchpad'i olmak | Farcaster bot (Farcaster/Neynar'a ait) | Base App içine gömülü | Web + topluluklar | **Base App mini app + X/Farcaster** |
| Güçlü yanı | Hız, alışkanlık, ölçek (aylık on milyonlarca $ gelir) | Cömert creator payı, ETH ile ödeme, özel pair'ler | Sosyal akıştan tek mesajla launch | Base App içinde varsayılan olmak | Creator gelir yönetimi | **Şeffaf kural kartı + creator gelir paneli** |
| Zayıf yanı | Churn'ü ödüllendiriyor, rug/sniper itibarı | Yeni, v2 audit'i süren bir dönemde canlıya çıktı | Gelir yalnızca belirli havuzlara ait | Content coin talebi sürdürülebilir değil | Karmaşık ekonomi | Dağıtım yok, marka yok |

Kaynaklar: [Blockworks — pump.fun dinamik fee](https://blockworks.co/news/pumpdotfun-fee-model), [The Block — PumpSwap creator revenue](https://www.theblock.co/post/354038/pumpswap-revenue-tokens), [BlockEden — PumpSwap 2026](https://blockeden.xyz/blog/2026/04/12/pumpswap-16b-volume-pumpfun-amm-raydium-solana-dex/), [Crypto Briefing — pump.fun aylık gelir](https://cryptobriefing.com/pump-fun-50m-monthly-revenue-surpasses-solana/), [DefiLlama — PUMP](https://defillama.com/token/PUMP), [PONS docs](https://docs.ponsfamily.com/), [Datawallet — PONS](https://www.datawallet.com/crypto/pons-explained), [DefiLlama — PONS v2](https://defillama.com/protocol/pons-v2), [Crypto Briefing — PONS günlük fee](https://cryptobriefing.com/pons-record-daily-fees-robinhood-chain/), [The Block — Clanker gelir](https://www.theblock.co/post/349549/clanker-team-earns-13-million-in-revenue-from-over-200000-tokens-on-base-in-just-five-months), [The Block — Zora ve Base App](https://www.theblock.co/post/365384/base-solana-zora), [Flaunch FAQ](https://docs.flaunch.gg/protocol/frequently-asked-questions), [Clanker v4 contracts](https://github.com/clanker-devco/v4-contracts), [Base — launch tokens](https://docs.base.org/cookbook/launch-tokens).

---

## 2. Rakiplerden alınacak dersler

1. **Kazanan, en iyi kontrat değil, en iyi dağıtım kanalı** (pump.fun'da alışkanlık, Clanker'da Farcaster, Zora'da Base App). Bizim en büyük riskimiz teknik değil, dağıtım.
2. **Launch sonrası işlemin gerçekleştiği yeri kontrol etmek gelirin kaynağıdır.** pump.fun gelirini PumpSwap ile büyüttü. Bizim karşılığımız: havuz hook'u, yani launch sonrası her swap'tan ücret almak.
3. **Creator'a cömert ve anlaşılır pay vermek ekosistemi hızla büyütür** (PONS: %70, ETH olarak ödeme). Creator'ın kendi tokenıyla ödeme almak kötü bir UX; WETH ile ödeme standart olmalı.
4. **Kademeli creator fee (pump.fun) churn'ü azaltır ama karmaşıktır.** MVP'de sabit oran kullan, kademeliyi veri gelince değerlendir.
5. **Platform tokenı ve buyback** rakiplerde talebi şişiriyor ama düzenleyici ve itibar riski getiriyor; ayrıca grant reviewer'ları için iyi bir sinyal değil. İlk 6 ayda yok.
6. **Audit'i süren kontratla canlıya çıkmak (PONS v2)** risktir. Bizim yolumuz: küçük kontrat yüzeyi, düşük limitler, açık beta etiketi.
7. **Sniper'lar ilk dakikayı bozuyor.** Clanker'daki sniper auction ve dinamik fee'ler buna yanıt. MVP'de en basit önlem: ilk N blokta yüksekten düşen fee (fee decay).
8. **Bizim ayrışma noktamız (v1'den taşınıyor):** işlemden önce görünen **kural/maliyet kartı** ve **creator gelir paneli**. Bunlar her token sayfasında ve paylaşılan her linkte görünmeli; sosyal kartın kendisi pazarlama aracı olmalı.

---

## 3. Konumlandırma

> **"Base'de creator'ın en çok kazandığı, trader'ın ne aldığını gördüğü launchpad."**
> %70 creator payı ETH olarak · değişmez %1 ücret · kilitli likidite · her tokenda tek bakışta kural kartı · Base App ve sosyal akıştan tek tıkla launch.

Hedef kullanıcı: Base App / Farcaster creator'ları, X'teki meme toplulukları, aktif Base trader'ları.

---

## 4. Yeni yol haritası

| Faz | Hafta | Kapsam | Çıkış koşulu |
|---|---|---|---|
| **F0 — Karar** | H1 | Altyapı seçimi (aşağıda), %1 / 70-30 fee modeli, WETH pair, marka adı, Builder Code kaydı (base.dev), Dune şeması | Yazılı karar kaydı; 5 creator + 5 trader görüşmesi |
| **F1 — Canlı MVP** | H2–4 | Anında v4 launch + kilitli LP + fee hook (70/30, WETH), ilk bloklarda fee decay, 3 adımlı launch wizard, token sayfası + kural kartı, creator claim paneli, basit board (yeni / trend). Sepolia'da uçtan uca → mainnet, düşük limitlerle | **Base mainnet kontrat adresi, canlı site, Loom demo** |
| **F2 — Dağıtım** | H5–8 | Base App / Farcaster mini app, X bot ile launch, paylaşılabilir kural kartı (OG image), creator leaderboard (kazanılan fee), holder ödül modu, referral linki, Dexscreener / GeckoTerminal indekslenmesi | 2–4 haftalık gerçek DAU/WAU/volume → **grant başvurusu (H6–8)** |
| **F3 — Curve modu** | H9–16 | pump tarzı bonding curve → kendi v4 havuzumuza graduation (v1 roadmap'teki CurveSale/GraduationExecutor, sadeleştirilmiş), bağımsız audit (grant + credit desteğiyle), canlı işlem akışı / terminal iyileştirmeleri | Audit bulguları kapatılmış; curve modu açık |
| **F4 — Genişleme** | H16+ | v1 roadmap'teki L2/L3: modüler kurallar, mevcut token havuzları, LP ödülleri, community funding, imzasız API, kademeli creator fee (veriye göre) | Her yeni modül ayrı inceleme kapısından geçer |

### F0 altyapı kararı

| Seçenek | Hız | Risk | Not |
|---|---|---|---|
| **A. Açık kaynak, denetlenmiş v4 launch kontratları üzerine kurmak** (ör. Clanker v4 kontratları, Doppler) | En hızlı (2–3 hafta) | Lisansa ve bağımlılığa bağlı | Lisans ve audit kapsamı mutlaka doğrulanmalı; fork ederken yalnızca fee/payout katmanını değiştir |
| **B. Minimal kendi kontratımız** (factory + v4 static fee hook + LP locker + fee splitter) | 3–4 hafta | Audit yok; düşük limit şart | v1'deki test disiplini korunur (gerçek upstream harness, invariant testleri) |
| C. v1'deki tam mimari | 10–14 hafta | En büyük audit yüzeyi | Grant zamanlamasına uymuyor → F3/F4'e |

**Öneri:** Lisans izin veriyorsa A; vermiyorsa B. Her iki durumda da v1'deki LP-01, LP-02 ve LP-06 test kanıtları MVP için de zorunlu.

### F1 MVP kapsamı (net liste)

**Var:** tek launch tipi (anında havuz), WETH pair, sabit 1 milyar arz, %100 LP kilitli, %1 fee (%70 creator / %30 protokol, WETH), fee decay, isteğe bağlı creator ilk alımı, kural kartı, claim, board, Builder Code, Dune dashboard.
**Yok:** curve, USDC, refund, modüler hook, holder ödülleri, referral, community, harici havuzlar, platform tokenı.

---

## 5. Metrikler ve hedefler

Grant formundaki 5 metrik ilk günden itibaren Dune'da (ekip/test cüzdanları hariç): all-time kullanıcı, DAU, WAU, all-time volume, son 30 gün volume. Ek olarak: launch sayısı, ikinci token çıkaran creator oranı, creator'a ödenen toplam fee, 7 günlük trader dönüşü.

| Zaman | Hedef (planlama varsayımı, taahhüt değil) |
|---|---|
| H4 (mainnet) | 5 pilot launch, 100+ benzersiz trader |
| H8 (grant başvurusu) | 50+ launch, 500+ kullanıcı, haftalık volume trendi pozitif |
| H16 | Curve modu canlı, creator tekrar kullanım oranı %20+ |

Wash trading ve kendi cüzdan aktiviteleri ayrı raporlanır, başvuruda hariç tutulur.

---

## 6. Gelir modeli

- Her swap'ta %1 → %0,7 creator, %0,3 protokol (WETH).
- Örnek: aylık $1M volume → $3.000 protokol geliri, $7.000 creator'lara.
- Opsiyonel (F3): küçük launch ücreti veya curve fee'si; kademeli creator fee'si veriye göre.
- Platform tokenı, buyback ve airdrop vaadi yok.

---

## 7. Riskler

| Risk | Önlem |
|---|---|
| Dağıtım yok, kimse launch etmiyor | F2'yi F1 ile paralel başlat; ilk 20 creator'ı birebir onboard et |
| Rug / scam tokenlar itibarı bozar | Kilitli LP, kural kartında açık risk etiketleri, sabit arz, mint/owner fonksiyonu yok |
| Sniper botlar | Fee decay; F3'te daha güçlü koruma |
| Audit olmadan kontrat hatası | Küçük yüzey, düşük limitler, beta etiketi, F3'te bağımsız audit |
| Clanker/Zora ile doğrudan rekabet | Creator payı + şeffaflık + mini app; feature sayısıyla yarışma |
| Fork edilen kodun lisans sorunu | F0'da yazılı lisans kontrolü |

---

## 8. İlk 10 iş günü

- [ ] Altyapı kararı (A/B) ve lisans kontrolü
- [ ] Marka adı, domain, X hesabı
- [ ] base.dev'de Builder Code kaydı
- [ ] Fee hook + LP locker + splitter: Sepolia deploy, gerçek upstream testleri
- [ ] Launch wizard + token sayfası + kural kartı (mobil öncelikli)
- [ ] Dune dashboard iskeleti
- [ ] 5 pilot creator listesi ve launch tarihleri
- [ ] Loom demo senaryosu

İlgili doküman: [`02-base-grant-basvuru-taslagi.md`](02-base-grant-basvuru-taslagi.md) (v1 feedback'i ve grant form cevap taslakları).
