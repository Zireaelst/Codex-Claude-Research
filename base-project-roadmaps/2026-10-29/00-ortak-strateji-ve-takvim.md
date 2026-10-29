# İki Base Ürünü — Ortak Strateji ve Uygulama Sırası

29 Ekim 2026 · Yol haritası paketi v1.0

## Okuma sırası

1. Bu doküman: ekip, ortak altyapı, takvim, karar kapıları.
2. [Launchpad teknik ve tasarım yol haritası](01-launchpad-roadmap.md).
3. [Consumer prediction teknik ve tasarım yol haritası](02-prediction-consumer-roadmap.md).

Bu paket ürün geliştirme yol haritasıdır. Kod satırı seviyesinde görev talimatı, uygulanmış yazılım, yayın veya test sonucu değildir. Sprint başlamadan ilgili iş paketi dosya/arayüz/test düzeyinde dar bir implementation planına çevrilir. Bu paket yalnızca belgelendirmedir; uygulama veya kontrat deployment’ı yapılmamıştır.

## 1. Netleşen iki ürün

| | Launchpad | Consumer prediction |
|---|---|---|
| Temel iş | Tokenı programlanabilir kurallarla başlatıp trade etmek | Mevcut market’lerde toplulukla tahmin yapmak ve isteğe bağlı işlem açmak |
| Başlangıç kullanıcıları | Meme/creator toplulukları ve Base trader’ları | Kripto odaklı Telegram/Discord toplulukları |
| Teknik ağırlık | Curve muhasebesi, v4 hook, graduation ve custody sınırları | Venue adapter, order recovery, sosyal veri ve consumer UX |
| Kalıcı değer hipotezi | Anlaşılır kurallar + çalışan creator gelir ekonomisi | Sonuçlardan öğrenme + oda alışkanlığı + görünür tahmin geçmişi |
| İlk büyük kapı | Gerçek protocol entegrasyonu ve bağımsız security review | Venue erişimi, hesap/imza yolu ve tekrar kullanım |
| Tam ürün sınırı | V4 ana, v3 alternatif, mevcut token havuzları ve fonlanmış programlar | Tek venue consumer v1; kendi prediction protokolü kapsam dışı |

Prediction yönü kullanıcı tarafından bu konuşmada seçildi. İki ürünün domain mantığı ayrı tutulur. İlk sürümlerde launchpad tokenlarının geleceğine bahis açan ortak ürün yapılmaz; tarafların sonucu etkileyebilmesi ve birleşen ekonomik riskler yeni bir tasarım sorunudur.

## 2. Kaynak kullanımı ve değişiklikler

İncelenen kaynak: [Codex-Claude-Research](https://github.com/Zireaelst/Codex-Claude-Research), özellikle `evm-launchpad-project-idea/README.md`, `AGENTS.md`, 01–11 numaralı spec’ler, `agent/IMPLEMENTATION_PLAN.md` ve `references/SOURCES.md`.

29 Ekim 2026 tarihinde indirilen dosya listesinin Git tree SHA’sı: `0c98ec58f0d08d107717956f0db74d6b00ca6595`. Bu tree kimliğidir, commit SHA diye kullanılmamalıdır. Belgeler main dalının indirilen snapshot’ından okunmuştur; ilerleyen repo değişiklikleri otomatik olarak bu plana uygulanmaz.

| Karar | Kaynak/otorite | Bu plandaki durum |
|---|---|---|
| V4-first, v3 ve external pool tam kapsamı | Kullanıcının paylaştığı spec | Korundu; teslim aşamalarına bölündü |
| Internal entitlement, iade ve fee muhasebesi | Kaynak spec | Korundu; UX etkileri açıklandı |
| İlk public ağ Base | Bu konuşmanın yönü | Base-first rollout; çoklu ağ mimarisi korunuyor |
| Tek USDC asset ile ilk beta | Bu planın önerisi | Sonraki aşamada WETH; nihai kapsam daraltılmadı |
| Sosyal uygulama + mevcut prediction venue | Kullanıcının açık tercihi | Consumer planın temeli |
| Limitless ilk venue adayı | Resmî SDK incelemesi | Kullanım/partner/ülke şartları henüz doğrulanmadı |
| Marka, renkler, cohort hedefleri ve süreler | Bu planın önerileri | Uygulama öncesi karar kaydı; pazar verisi değildir |

Repo ekonomik parametreleri rakiplerden doğrulanmış değerler değil tasarım varsayımlarıdır. Yeni plan da grant veya gelir garantisi vermez. Grant başvuru kriterleri ayrıca güncel resmî kaynaklardan kontrol edilmelidir; ürünün yol haritası bir grant tarihine bağlanmamıştır.

## 3. Ortak altyapı, ayrı sorumluluklar

```text
                         Ortak UI primitive’leri
                         wallet bağlantısı / miktar biçimi
                         tx durumları / erişilebilirlik
                                  │
                     ┌────────────┴────────────┐
                     ▼                         ▼
              LAUNCHPAD APP              PREDICTION APP
              launch/curve/rules          market/room/forecast
              contracts + indexer         venue adapter + workers
              ayrı DB ve secrets          ayrı DB ve secrets
```

Paylaşılabilirler: button/input/modal, miktar parser/formatter, wallet bağlantı bileşenleri, receipt görünümü, toast/error sözlüğü, logging redaction yardımcıları, analytics event yapısı ve CI şablonları.

Paylaşılmayanlar: custody ve kontratlar, hook fee matematiği, venue order state’i, sosyal score, kullanıcı izinleri, production secrets ve veri tabanı muhasebesi. Prediction order accepted ile launchpad tx confirmed aynı enum’a zorlanmaz.

Öneri: iki ayrı application repo. Ortak paketler önce küçük ve sürümlenebilir tutulur; private registry zorunluluğu yok. İkinci üründe gerçekten tekrar edilen bileşen ortaya çıkmadan büyük bir “platform framework” kurulmaz. Aynı UI dilini paylaşmak iki markanın aynı ekran yoğunluğuna sahip olmasını gerektirmez.

## 4. Ekip ve takvim senaryoları

Aşağıdaki süreler kapasite planlama tahminidir; geçmiş velocity verisi yok. Audit/partner/hukuki inceleme için bekleme süreleri ve kritik bulgular ayrıca takvimi etkiler. H1, uygulama başlangıcının ilk haftasıdır; 29 Ekim’de kodlama başlamış sayılmaz.

| Ekip | Çalışma biçimi | Planlama zarfı |
|---|---|---|
| 3 geliştirici + tasarım/QA desteği | Launchpad’de Solidity + full-stack; prediction’da ayrı full-stack | Prediction v1 ~8–12 hafta; launchpad v4 beta ~10–14, tam Base ~18–24+ hafta |
| 2 geliştirici + yarı zamanlı tasarım | Solidity lead launchpad çekirdeği; full-stack önce prediction, sonra launchpad UI | Prediction ~10–14; launchpad beta ~16–22; tam ürün ~26–36+ hafta |
| Tek geliştirici | Kısa iki spike sonrası bir ürünün ilk sürümüne odaklan; ikincisine sonra geç | İki ürünün bu kapsamı için yaklaşık 9–15+ ay bütçe zarfı; ilk 2 sprintte yeniden hesapla |

Tek geliştirici senaryosunda önerim: iki haftalık launchpad protocol/consumer venue doğrulaması → consumer v1 → launchpad tam uygulama. Launchpad hedefi bırakılmaz; en yüksek belirsizliği erkenden test edilmiş olur. Daha önce güçlü Solidity altyapısı veya hazır ekip varsa sıra yeniden değerlendirilebilir.

### Önerilen 3 geliştiricili paralel takvim

| Dönem | Launchpad | Prediction | Ortak tasarım/operasyon |
|---|---|---|---|
| H1–2 | Gerçek upstream harness ve matematik planı | Venue capability ve pilot oda doğrulaması | Görüşmeler, flow’lar, kimlik ve içerik sözlüğü |
| H3–4 | Curve/registry/accounting | Sosyal alpha | Component/state matrisi ve prototip testleri |
| H5–8 | Graduation/hook/router, UI dikey akış | Emir/fill/position/claim | E2E, erişilebilirlik, hata metinleri |
| H9–12 | V4 inceleme ve düzeltmeler | Consumer v1 ve retention ölçümü | Incident/restore, erişim ve bağımsız inceleme |
| H13–18 | V3, creator rewards ve blueprints | Retention sorunlarına odaklı iyileştirme | Yeni feature yerine kanıta göre öncelik |
| H19–24+ | External pools, maintenance ve kalan tam kapsam | İkinci venue yalnızca talep varsa | Tam kapsam kanıtı ve sürüm sonrası değerlendirme |

Launchpad kontrat incelemesi başladığında scope dondurulur; o sırada eklenen modül eski review’un kapsamına otomatik girmez. Consumer ekip üyeleri audit uzmanı yerine sayılmaz.

## 5. Tasarım programı

Her iki ürün için ayrı sitemap, kullanıcı akışı ve etkileşim prototipi; ortak komponentlerin tek specification’ı hazırlanır. Tasarım bir “sonradan güzelleştirme” aşaması değil, her sprintin acceptance girdisidir.

1. **Anlama:** 5 creator/5 trader ve 8–10 prediction kullanıcısı. Mevcut araçları, son yaptığı işlem ve takıldığı somut adım konuşulur.
2. **Akış:** happy path ile birlikte yanlış ağ, başarısız imza, stale veri, partial fill, graduation pending ve claim sorunları çizilir.
3. **Wireframe:** 390 px mobile, 1440 px desktop; gerçek sayı yoğunluğu kullanılır. Demo verisi etiketlidir.
4. **Prototip:** görev odaklı beş kullanıcı testi; katılımcı sözleri ve hata noktaları kaydedilir.
5. **Handoff:** komponent durumları, metinler, veri kaynağı, input validation ve responsive davranış aynı iş paketinde yer alır.
6. **Doğrulama:** gerçek backend/kontrat akışında ekran yeniden test edilir; yalnızca Figma benzeri prototip kabul edilmez.

İlk tasarım geçişi için hedef: katılımcıların en az 4/5’i yönlendirmesiz ana görevi tamamlayıp maliyeti doğru anlatabilsin. Beş kişi istatistiksel ispat değildir; kritik usability hatalarını yakalama aracıdır.

## 6. Ortak yayın kapıları

| Kapı | Gerekli çıktı | Engellenen şey |
|---|---|---|
| G0 kapsam | Kabul edilen release scope, requirement matrisi | Dağınık özellik geliştirmesi |
| G1 dependency | Gerçek upstream/venue kanıtı, version/address provenance | Mock üzerinden “çalışıyor” iddiası |
| G2 UX | Ana görevler + hata yolları + veri anlamı | Yanlış fee, bakiye veya başarı gösterimi |
| G3 güvenlik | Threat model, testler, bağımsız kapsam incelemesi, bulgu disposition | Gerçek fonlu erişim |
| G4 operasyon | Monitoring, restore, outage ve incident tatbikatı | Kontrolsüz production yayını |
| G5 ticari/erişim | Venue/ülke koşulları, kullanıcı metinleri, sahiplik ve yayın yetkisi | Uygunluğu doğrulanmamış live trade |
| G6 pilot | Gerçek cohort, tekrar kullanım, teknik başarı | Kontrolsüz büyüme ve erken genişleme |

Launchpad custom math/hook/accounting için bağımsız kontrat incelemesi gerekir. Consumer uygulamada yeni custody kontratı eklememek, wallet signature/adapter/kimlik incelemesi ihtiyacını ortadan kaldırmaz. İnceleme bütçesi olmayan sürüm gerçek para yayınına hazır sayılmaz.

## 7. Bütçe ve gelir planlama çerçevesi

Bu çalışma güncel fiyat teklifi toplamamıştır; kesin dolar bütçesi vermek yanıltıcı olur. Bütçe şu ayrı satırlarda hazırlanmalı:

- İnsan emeği: kişi × ayrılan hafta × haftalık maliyet; yukarıdaki paralel senaryoda aynı insan iki kez sayılmaz.
- Launchpad bağımsız inceleme: curve math, hook, locker/vault ve genişleme modülleri için kapsamlı ayrı teklif.
- Consumer güvenlik/entegrasyon incelemesi: auth, order replay, signature, privacy ve dependency kapsamı.
- RPC, DB, worker hosting, object storage, monitoring ve e-posta; aylık maliyet ayrı izlenir.
- Venue/API/partner, tasarım ve hedef ülke değerlendirmesi; henüz bedel veya izin varsayımı yok.
- Düzeltme ve belirsizlik rezervi: iç planlama için emek/operasyon tahminine %25 pay önerilir; audit teklifinin yerine geçmez.

Launchpad protokol geliri ile creator payı ayrılır. Prediction finansal modelinde partner geliri doğrulanana kadar sıfır yazılır. İki ürünü finanse edecek grant alındığı varsayılmaz; ücretli altyapı veya fonlu test bu dokümanla satın alınmaz.

## 8. İlk 30 günde hangi kararları vereceğiz?

| Zaman | Karar | Devam kanıtı |
|---|---|---|
| Gün 1–5 | İki ürünün ilk kitlesi ve pilot ortakları | Launchpad creator’ları; prediction oda yöneticileri |
| Gün 6–10 | Teknik bağımlılıklar gerçek mi? | Real v4 harness; venue capability matrisi |
| Gün 11–15 | Kullanıcı akışı anlaşılır mı? | Entitlement/fee ve forecast/order ayrımı görev testinde anlaşılır |
| Gün 16–20 | İlk sürüm kapsamı ve maliyeti | İş paketleri, audit/partner takvimi ve kapasite |
| Gün 21–30 | İkinci ay önceliği | İlk sprint velocity, blokajlar, pilot geri bildirimi |

Başlamadan gerekli kararlar: geliştirici kapasitesi; review bütçesi; hedef kullanıcı ülkeleri; ürün adı ve arayüz dili. Bunların eksikliği bu stratejik yol haritasını engellemez; yerel implementation ve public release için farklı aşamalarda tamamlanırlar. Başlangıç önerisi global kullanıcı için İngilizce UI, Türkçe iç ürün belgeleri; henüz kullanıcı kararı değildir.

## 9. Ortak başarı ve durdurma sinyalleri

Launchpad: 7/28 günlük geri dönüş, creator tekrar kullanımı, quote→confirmed başarı, gelir claim’i ve teknik hata. Prediction: forecast→result view→gelecek hafta dönüş; ayrıca order→fill ve trader retention. İki ürünün volume ve user sayıları tek büyüme rakamında birleştirilmez.

İlk iki cohort sonrası tekrar kullanım yoksa yeni modül/kategori eklemek yerine ana döngü araştırılır. Launchpad creator’ları sadece ücretsiz tanıtım için geliyor veya prediction odaları sponsor yokken kapanıyorsa dağıtım hipotezi gözden geçirilir. Teknik dependency kapısı geçmediyse yalnızca o iş akışı durur; sahte veriyle tamamlandı ilan edilmez.

## 10. Uygulamaya devir biçimi

Her sprint için tek bir paket seçilir. Şu alanlarla dar implementation planı yazılır: amaç; kaynak requirement ID’leri; tüketilen/üretilen arayüzler; değişecek dosyalar; hata senaryoları; test komutları ve beklenen sonuç; migration/rollback; tasarım frame/state referansı; kanıt dosyası. Testin gerçekten çalıştığı commit ve çıktı kaydedilir.

Bu yol haritaları uygulanırken kaynak spec ile çelişki bulunursa sessiz değişiklik yapılmaz: etkilenen requirement, gerekçe, alternatif ve yeni kabul testi bir karar kaydına girer. Araştırma arşivi geçmişi korunur. Tam ürün, yalnızca landing page veya bir factory yazılmasıyla tamamlanmış sayılmaz.
