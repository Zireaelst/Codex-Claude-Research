# Base Programlanabilir Launchpad — Teknik ve Tasarım Yol Haritası

29 Ekim 2026 · Planlama sürümü 1.0 · Durum: önerilen yol haritası, uygulanmış ürün veya güvenlik onayı değildir.

## 1. Ürün kararı

Creator, tokenın lansmanını ve sınırlandırılmış ekonomik kurallarını seçer. Trader işlem yapmadan önce maliyeti, kısıtları ve değiştirilemeyen şartları görür. Ana deneyim bonding curve → Uniswap v4 havuzu → kalıcı kilitli kurucu likiditesidir. Instant v3 ve mevcut token havuzları tam ürünün ayrı yollarıdır.

Hedef kullanıcı: meme toplulukları, creator kolektifleri ve aktif Base trader’ları. Community funding isteğe bağlı bir özelliktir; ürünün merkezine milestone fonlama koymuyoruz. Pons ve AvaxHook deneyim referansıdır; kodlarının veya ekonomik parametrelerinin güvenli olduğu varsayılmaz.

**Ürün vaadi:** “Tokenını, baştan anlaşılabilen ekonomik kurallarla başlat.” Farklılaşma hipotezi; kullanışlı presetler, işlem öncesinde anlaşılır kural/maliyet görünümü ve lansman sonrası creator gelir yönetimidir. Bunun kullanıcı tercihi yarattığı pilotta ölçülecek.

## 2. Kaynak ve kapsam sınırı

Kaynak: [EVM ürün spesifikasyonu](https://github.com/Zireaelst/Codex-Claude-Research/tree/main/evm-launchpad-project-idea). Araştırma deposu uygulama deposu değildir. Eski Arc ve Stellar uygulamaları taşınmaz; yeni uygulama ayrı repoda geliştirilir. Bu doküman araştırma deposunu değiştirmez.

Kaynakta P01–P16 ürün gereksinimleri, S01–S16 güvenlik koşulları, A01–A32 kabul senaryoları ve WP01–WP12 iş paketleri bulunuyor. Bu yol haritası onları kullanıcıya teslim edilen aşamalara dönüştürür. Aşağıdaki kısmi beta, tüm ürün tamamlandı anlamına gelmez.

**Bu çalışmadaki önerilen uyarlama:** ilk kamuya açık ağ yalnızca Base. Çoklu ağ için veri kimlikleri ve manifest mimarisi korunur; ikinci ağın açılması ayrı karardır. Repo’daki nihai çoklu ağ hedefi silinmez. USDC ilk ödeme varlığı; doğrulanmış WETH desteği izleyen aşamada. Gerçek ekonomik sabitler bağımsız model ve güvenlik incelemesinden sonra dondurulur.

## 3. Sürüm haritası

| Sürüm | Kullanıcıya açılan kapsam | Açılmayan kapsam |
|---|---|---|
| L0: yerel protokol ispatı | Gerçek upstream kontratlarla curve, graduation, swap ve claim | Herhangi bir kamuya açık para akışı |
| L1: davetli v4 beta | USDC, Standard token, standart/açılış/gelir paylaşımı presetleri; keşif, terminal, gelirler | Advanced transfer profili, bakım işlemleri, v3 ve harici token havuzları |
| L2: creator ürünü | V3 instant, WETH, fonlanmış Lock & Earn, referral, blueprints | Henüz doğrulanmamış bakım modülleri ve harici token türleri |
| L3: tam Base kapsamı | Mevcut token havuzları, LP ödülleri, auto-LP veya buyback, advanced profiller, community işleri ve unsigned API | Yeni ağlara otomatik açılma, platform tokenı, keyfi kod marketplace’i |

L1’de küçük kullanıcı sayısı veya küçük bakiye, güvenlik incelemesinin yerine geçmez. L2/L3 yeni kontratları ve modül kombinasyonları yeni inceleme kapısından geçer.

## 4. Teknik mimari

Önerilen yeni uygulama düzeni:

```text
apps/web                 React/TypeScript, responsive arayüz
apps/api                 typed HTTP API, unsigned işlem planları
apps/indexer             event ingestion, reorg ve read model
packages/contracts       Solidity, Foundry, gerçek upstream testleri
packages/sdk             üretilmiş ABI, miktar tipleri, şemalar
packages/config          ağ manifestleri ve özellik doğrulaması
packages/db              PostgreSQL şema ve migration’ları
packages/ui              cüzdan/işlem/erişilebilir bileşenler
docs/evidence            kabul senaryoları ve çalıştırma kanıtları
docs/runbooks            olay, restore ve deploy prosedürleri
```

Node, package manager, Solidity compiler ve Uniswap/Permit2 revision’ları ilk teknik pakette uyumlu bir set olarak sabitlenir. Uydurulmuş “en son sürüm” kullanılmaz. PostgreSQL kalıcı read model; Redis isteğe bağlı cache/rate limit katmanıdır. Muhasebenin otoritesi kontratlardır. Metadata object storage’da; hash/URI ve sürüm ilişkisi kaydedilir.

### Kontrat sınırları

| Birim | Sorumluluk | Kritik sınır |
|---|---|---|
| LaunchRegistry + TokenFactory | Tekil kimlik, sabit arz, değişmez config | Bir launch başka launch’ı değiştiremez |
| CurveSale + CurveMath | Hak alım/satımı, backing, expiry ve iade | Fee borcu ile backing ayrı |
| GraduationExecutor + V4Locker | Gerçek v4 settlement ve kurucu NFT kilidi | Ana likidite çıkışı veya keyfi çağrı yok |
| CompositeHook + HookRegistry | Onaylı modüllerin sabit config ile çalışması | Bir havuz tek hook adresi; en fazla altı seçili modül |
| FeeVault + DustVault | Varlık bazlı claim ve kilitli artıkların ayrılması | Dust gelir sayılmaz; fon gelmeden fee yazılmaz |
| Router + QuoteLens | Kimliği doğrulanmış, sınırlı exact-input işlemler | İmzasız hookData kullanıcı kimliği değildir |
| V3Launcher + V3Locker | Atomik instant launch ve kilitli pozisyon | V4 kuralları burada sunulmaz |
| ExistingPoolFactory | Harici token için iki taraflı likidite | LP depositor’a aittir ve çekilebilir |
| Reward/Maintenance/Community vault’ları | Ayrı fonlanmış ödül, bakım, katkı ödemeleri | Ana rezervlere veya kazanılmış claim’lere erişim yok |

Pool hook’u başka havuzları yönetmez. Ekonomik kullanıcı ile router adresi aynı kabul edilmez. Aggregator rotası kimlik doğrulayamıyorsa referral gibi kimliğe dayalı ödüller verilmez; destek sınırı açıklanır. Hook uyumluluğu aggregator’dan otomatik trafik garantisi değildir.

### Durum makinesi ve muhasebe

```text
DRAFT → CURVE_ACTIVE → GRADUATION_PENDING → GRADUATED
               └─ expiry → REFUNDABLE
                            ↑
           pending + 72 saat başarısızlık
```

Kaynak varsayılanı: curve 30 gün açık. Son alımda graduation atomik olarak denenir; başarısızlıkta final alım ve pending durumu kalır, başarısız havuz işlemlerinin tamamı geri alınır. İlk pending zamanından itibaren 72 saat boyunca permissionless retry; sonra permissionless refund aktivasyonu. Tekrarlanan deneme süreyi uzatmaz.

Curve’de alınan şey transfer edilebilir ERC-20 değil, curve’e geri satılabilen internal entitlement’tır. Graduation sonrasında actual token claim edilir. İade, eski satın alma tutarının garantisi değildir: dondurulan backing, outstanding entitlement oranında paylaştırılır; geçmiş fee’ler geri gelmez. UI bu ayrımı gizleyemez.

Kaynak ekonomik model: 1 milyar arz, %80 curve / %20 kurucu LP. Referans rezerv fonksiyonu `R(q)=15*A*q/(16*S-15*q)`; USDC örneğinde A=2.000, terminal net backing 6.000 USDC. Bunlar ürün politikasına ait önerilerdir. Kümülatif rezerv yuvarlaması, son alımın artan tutarı, fee tavanları ve LP başlangıç fiyatı bağımsız rasyonel modelle doğrulanır. USDC 6, token 18 decimal varsayımı her varlık için manifestten kontrol edilir.

### API ve veri

Kaynak endpoint’leri korunur: `/v1/networks`, `/launches`, `/tokens/{chainId}/{address}`, `/pools/{chainId}/{poolId}`, `/modules`, `/quotes`, `/transactions/launch`, `/transactions/trade`, `/transactions/claim`, `/accounts/{chainId}/{address}`. İşlem planı endpoint’leri imzasız payload üretir; sunucu kullanıcının fonunu imzalayamaz.

Quote cevabı: raw input/output, varlık bazlı fee kırılımı, price impact, minOut, chain, phase, configHash, block/hash, expiry ve desteklenmeyen rota nedeni. Miktarlar integer string; fiyat için JS floating-point muhasebesi yok. Varsayılan 20 saniyelik TTL tek başına koruma değildir; kontratta deadline ve minOut gerekir.

Indexer anahtarı `(chainId, txHash, logIndex)`; block hash ve parent hash saklanır. Reorg’da ortak ataya geri dönülüp projection yeniden üretilir. Submission, confirmation, finality ve indexer’ın görmesi ayrı durumlar. OHLC gerçek execution miktarlarından; gösterilen quote’lardan volume üretilmez.

## 5. Tasarım sistemi ve ekranlar

**Yön:** yoğun veri içeren fakat creator’a kolay başlayan bir trading ürünü. Koyu nötr arka plan, mavi vurgu önerisi; durumlar ikon ve metinle de anlatılır. Ortak spacing 4/8/12/16/24/32; metin tabanı 16 px; miktarlar tabular numerals. Kontrast hedefi WCAG AA, dokunma hedefleri yaklaşık 44 px. Ürün markası henüz seçilmiş değildir.

| Ekran | Bilgi sırası | Önemli etkileşim |
|---|---|---|
| Board | Yeni/aktif/graduation’a yakın; token kimliği; işlem aktivitesi | Adres arama, açık sponsor etiketi, veri yaşı |
| Launch wizard | Kimlik → ekonomi → kurallar → gelirler → son kontrol | Varsayılan preset; advanced ayrıntılar isteğe bağlı |
| Token terminal | İsim+adres+ağ+phase; grafik; ticket; kurallar; aktivite | Masaüstünde sağ ticket, mobilde sabit al/sat düğmesi ve sheet |
| Rules inspector | Şimdi uygulanan kurallar; süre; toplam maliyet; yetkiler | İnsan dili özeti, altında kontrat/modül/hash ayrıntıları |
| Earnings | Tahsil edilecek LP fee / claimable / ödenen | Her varlık ayrı; “collect” ve “claim” farklı |
| Portfolio | Curve hakları / liquid token / stake / LP / claims | Her bakiye için uygun eylem |
| Pool terminal | Tam pool kimliği; likidite; opener; pozisyonlar | Harici LP için ekle/azalt/çık |
| Campaign + Community | Fon, ayrılan haklar, süreler, reviewer yetkisi | Finansal durum ile içerik incelemesini ayrı göster |

**Wizard ayrıntısı:** ilk üç adımda aynı config ile buy/sell örnek maliyeti gösterilir; son ekranda değişmez ayarlar ve isteğe bağlı creator ilk alımı açıkça listelenir. Fonlama miktarı ile FDV aynı etiket altında gösterilmez. Preset değişince ücret örneği ve configHash yeniden hesaplanır.

**İşlem durumları:** quote loading → onay gerekli → simülasyon → imza bekleniyor → gönderildi → confirmed → indexed. Rejected, reverted, replaced, expired, wrong network ve insufficient gas ayrı açıklanır. Kullanıcı imzayı reddettiğinde draft korunur. Graduation yarışında eski quote güvenli şekilde reddedilir, kullanıcı yeni phase quote’unu görüp yeniden onaylar.

**Zorunlu tasarım teslimatları:** sitemap; creator/trader/claim/LP akışları; mobile ve desktop wireframe; etkileşimli prototip; component ve state matrisi; içerik sözlüğü; klavye/kontrast kontrolü; gerçek local kontrat E2E videosu. Görsel prototip ile settlement ispatı ayrı kanıttır.

## 6. Aşamalı takvim ve teslim kapıları

Tahmin: deneyimli Solidity mühendisi + full-stack mühendis; tasarım ve bağımsız inceleme desteğiyle 18–24 hafta tam Base kapsamı için planlama zarfı. İlk v4 davetli beta 10–14 hafta bandında düşünülebilir; audit rezervasyonu, kritik bulgular veya entegrasyon engelleri süreyi uzatır. Bunlar taahhüt değildir. Aynı ekip prediction’ı da yürütürse toplam takvim ayrıca uzar.

| Aşama | Yaklaşık zaman | Teknik teslim | Tasarım teslim | Çıkış koşulu |
|---|---|---|---|---|
| L-A | H1–2 | Manifest şeması, upstream pinleri, gerçek local v4 harness; WP01 | 5 creator + 5 trader görüşmesi; akış ve wireframe | Gerçek swap/settlement/fee harvest ispatı; 3 pilot creator niyeti |
| L-B | H3–5 | Registry/token/curve/FeeVault; WP02–03 | Wizard, entitlement ve refund prototipi | Bağımsız modelle reserve/fee/refund eşleşmesi |
| L-C | H6–8 | Executor/locker/hook, sınırlı kurallar/router; WP04 + WP06 çekirdeği | Terminal ve phase transition’ları | Pre-init saldırısı, final buy ve rollback testleri geçer |
| L-D | H7–10 | Indexer/API/frontend dikey akışı; WP10–11’in L1 kısmı | Gerçek verili mobile kullanım testi | Kullanıcı local launch→trade→graduate→claim yapabilir |
| L-E | H10–14 | Bağımsız inceleme, düzeltme, fork ve operasyon; WP12 ilk dilim | Hata/claim/recovery ekranlarının son kontrolü | L1 kapsamındaki tüm kabul kanıtları ve yayın kapıları |
| L-F | H13–18 | V3, WETH, referral, token rewards, blueprint; WP05/06/08/09 dilimleri | Instant wizard, earnings ve campaign UX | Gerçek v3 LP kilidi/harvest; fonlanmış ödül solvency |
| L-G | H18–24+ | Harici havuz/LP rewards, maintenance, advanced, community; WP07–09 kalanları | Pool, LP exit, treasury ve work lifecycle | Tüm P01–P16 için Base kapsam kanıtı; yeni inceleme |

Örtüşen haftalar bağımsız full-stack ve kontrat işlerini gösterir. Audit personeli aynı anda yeni modüller yetiştirmek için sayılmaz. Takvimle birlikte kapasite planı `00` dokümanında yer alır.

## 7. Öncelikli iş listesi ve test kanıtı

Her madde ayrı review edilebilir teslimdir. Uygulama sırasında önce davranışı yakalayan test, sonra implementation, ardından etkilenen regression ve kayıt yapılır. Buradaki dosya yolları önerilen yeni repo yollarıdır; bugün mevcut oldukları iddia edilmez.

| İş | Önerilen dosya/test alanı | Kabul kanıtı |
|---|---|---|
| LP-01 Gerçek protokol harness | `packages/contracts/test/integration/UpstreamHarness.t.sol` | CREATE2 hook izinleri ve gerçek settlement; mock kabul edilmez |
| LP-02 Curve muhasebesi | `src/curve/`, `test/invariant/CurveAccounting.t.sol` | Rastgele al/sat serilerinde backing+fee+dust korunur; rounding kârı yok |
| LP-03 Graduation ve iade | `src/v4/`, `test/integration/V4Lifecycle.t.sol` | Her hata noktasında atomik rollback; 72 saat sınırında doğru çıkış |
| LP-04 Kural validator | `src/rules/`, `test/integration/RulesAndRoutes.t.sol` | Conflict, altı modül sınırı, fee ceiling ve sahte actor reddi |
| LP-05 Trading API/UI | `apps/api/src/routes/quotes.ts`, `apps/web/e2e/trade.spec.ts` | Quote→approval→sign→confirmed; phase değişiminde yeni onay |
| LP-06 Read model | `apps/indexer/src/reorg.ts` | Duplicate/reorg/replay sonrası aynı canonical balances/volume |
| LP-07 V3 ve harici LP | `test/integration/V3Lifecycle.t.sol`, `ExistingPools.t.sol` | Kurucu LP çekilemez; harici LP tamamen çıkabilir |
| LP-08 Ödül ve bakım | `test/invariant/RewardSolvency.t.sol`, `Maintenance.t.sol` | Fon üstü ödeme yok; başarısız reward token principal’ı kilitlemez |
| LP-09 Community ve template | `test/unit/WorkLifecycle.t.sol`, `Blueprints.t.sol` | Reviewer timeout, tek revision, claim ve immutable template |
| LP-10 Yayın kanıtı | `docs/evidence/acceptance.md` | A01–A32 eşleme, komut/commit/seed/block ve gerçek sonuç |

Kurulacak standart doğrulama komutları: `pnpm typecheck`, `pnpm lint`, `pnpm test:contracts`, `pnpm test:integration`, `pnpm test:api`, `pnpm test:e2e`, `pnpm build`, `pnpm verify:manifests`. Bunlar planlanan script adlarıdır, bugün çalıştırılmış testler değildir. Foundry paketinde targeted test örneği: `forge test --match-path 'test/integration/V4Lifecycle.t.sol'`. Hedef: sıfır açıklanmamış hata, doğru balances ve sabit principal; yalnızca “compile geçti” yeterli değil.

## 8. Tam kapsam izlenebilirliği

| Gereksinim | Teslim aşaması |
|---|---|
| P01 v4 / P03 canonical path | L-B/C |
| P02 v3 | L-F |
| P04 composition / P05 trading | L-C/D; ek modüller L-F/G |
| P06 discovery / P07 earnings | L-D; tüm varlıklar L-F/G |
| P08 existing pools | L-G |
| P09 rewards | L-F token / L-G LP |
| P10 community | L-G |
| P11 unsigned API | L-D çekirdek / L-G tam dokümantasyon |
| P12 ağ mimarisi | L-A; iki bağımsız local chain testi L-G; ikinci public ağ ayrı karar |
| P13 blueprints | L-F |
| P14 advanced profiles | L-G |
| P15 görünür yetki/risk / P16 operasyon | Her sürümde zorunlu; L-E/G yayın kapısı |

M01/02/05 L1; M06/07 L2; M03/04/08/09/10/11/12 L3. M09 ve M10 birlikte seçilemez; M11 ve M12 de birlikte seçilemez. Test edilmemiş modül UI’da aktif gösterilmez. Geçmiş versiyonun davranışı yeni registry kararıyla değiştirilmez.

## 9. Pilot, gelir ve operasyon

Pilot önerisi: önce üç creator ve kendi toplulukları. İlk hedef launch sayısını büyütmek değil; insanların kuralları anlayıp işlem yapabilmesi ve creator’ın gerçek gelirini çekebilmesidir. İlk 30 gün için 3 gerçek lansman ve 20 bağımsız trader görüşmesi planlama hedefidir, beklenen sonuç değildir.

Ölç: ilk quote→confirmed trade dönüşümü; rejection ile teknik hata ayrımı; 7/28 günlük trader dönüşü; creator tekrar kullanımı; graduation başarısızlığı; claim tamamlama; inceleme sonrası hata; creator/protocol net gelir. Kendi cüzdanları, test akışı ve şüpheli wash aktivitesi ayrı raporlanır. Sadece volume’a göre ödül dağıtılmaz.

Gelir kaynakları kaynak spec’teki launch ve işlem ücretleridir. Creator geliri platform geliri sayılmaz. LP fee, service fee, gas, swap fiyat etkisi ayrı gösterilir. Builder Code entegrasyonu yalnızca kontrol ettiğimiz işlem rotalarında doğrulanır; bütün downstream işlemleri bize ait gösterme iddiası yok.

Operasyon: iki RPC sağlayıcısı; indexer lag alarmı; reserve/liability uyuşmazlığında kritik alarm; başarısız graduation kümeleri; claim hataları; database restore tatbikatı. Yeni launch/modül açmayı durdurmak ile eski kullanıcının earned claim hakkını durdurmak farklı yetkilerdir. Immutable swap-critical bug için gizli upgrade varsayımı yapılamaz; açıklanan kurtarma sınırları incident planında bulunur.

## 10. İlk on iş günü

- [ ] Kaynak P/S/A matrisi yeni repo iş listesine bağlansın; brand ve ekran dili seçilsin.
- [ ] USDC ilk preset ve internal entitlement UX kararı yazılı tasarım kaydına alınsın.
- [ ] Gerçek upstream harness kurulsun; ABI/compiler/lisans provenance kaydedilsin.
- [ ] Üç creator adayından ilk lansman ve topluluk dağıtım planı alınsın.
- [ ] Wizard, token terminali, graduation pending ve refund prototipi test edilsin.
- [ ] Matematik için bağımsız referans model ve saldırı senaryoları hazırlansın.
- [ ] Bağımsız güvenlik incelemesinin kapsamı, zamanı ve teklifi alınsın.

## Kaynaklar

- [Ürün ve yolculuklar](https://github.com/Zireaelst/Codex-Claude-Research/tree/main/evm-launchpad-project-idea/specs)
- [Ekonomi](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/evm-launchpad-project-idea/specs/03-economics.md)
- [Lifecycle](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/evm-launchpad-project-idea/specs/04-lifecycles.md)
- [Kurallar](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/evm-launchpad-project-idea/specs/05-rules.md)
- [İş paketleri](https://github.com/Zireaelst/Codex-Claude-Research/blob/main/evm-launchpad-project-idea/agent/IMPLEMENTATION_PLAN.md)
- [Uniswap hook modeli](https://developers.uniswap.org/docs/protocols/v4/concepts/hooks)
- [Base ağ bilgileri](https://docs.base.org/get-started/connect-to-base)

Kaynak repo indirilen snapshot üzerinden okunmuştur; güncel deployment adresleri, ticari talep, audit sonucu veya grant seçilme ihtimali bu çalışma tarafından doğrulanmış değildir.
