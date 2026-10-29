# Base Agent Kit

Codex ve Claude Code için taşınabilir Base geliştirme paketi. 29 Ekim 2026.

Bu paket bir modeli yeniden eğitmez; görev odaklı talimatları, güncel kaynaklara erişim yöntemini, proje bağlamını ve doğrulama iş akışını taşır. Repo URL’sini paylaşmak tek başına MCP/SDK/Foundry kurmaz veya cüzdan erişimi sağlamaz. Aşağıdaki kurulumdan sonra yeni oturumda yetenek kontrolü yapılır.

## Hızlı başlangıç

Bu araştırma reposunu klonla veya indir. Gerçek uygulama için ayrı bir proje klasörü kullan. Komutları repo kökünden çalıştır:

```bash
# Önizleme: hiçbir dosya yazmaz.
python3 base-agent/scripts/setup.py install --target /absolute/path/to/app --client both
# Gösterilen proje kapsamındaki dosyaları ekler.
python3 base-agent/scripts/setup.py install --target /absolute/path/to/app --client both --apply
# Salt okunur araç/dosya envanteri; bağlantı testi değildir.
python3 base-agent/scripts/setup.py doctor --target /absolute/path/to/app
```

Paketi tek başına indirdiysen veya klasörün adını değiştirdiysen komutlardaki `base-agent/scripts/setup.py` yolunu gerçek konuma göre değiştir. Installer Python 3.9 veya üzerini gerektirir.

Yalnızca bir istemci için `--client codex` veya `--client claude` kullan. Installer ilgili `.agents/skills/base-builder` / `.claude/skills/base-builder` klasörüne aynı self-contained skill’i kopyalar; AGENTS.md / CLAUDE.md sonuna kısa bir yönlendirme ekler. Mevcut farklı skill veya değiştirilmiş managed block varsa işlem durur; elle birleştir. Global ayarlar, MCP veya credential dosyaları değişmez. Geçerli hedefte ikinci çalıştırma değişiklik üretmez. Dosya sistemi yazma hatası olursa sonuçları kontrol edip yeniden çalıştır; paket çapında atomik transaction vaat edilmez.

Uygulama klasöründe Base Docs MCP’yi bir kez yapılandır:

```bash
# Codex CLI: istemci ayarına kayıt yapar; repo dosyası kopyalamakla eşdeğer değildir.
codex mcp add base-docs --url https://docs.base.org/mcp
codex mcp get base-docs

# Claude Code: uygulama proje kökünde çalıştır, proje kapsamına ekler.
claude mcp add --transport http base-docs --scope project https://docs.base.org/mcp
claude mcp list
```

Aynı isimle zaten kayıt varsa önce mevcut kaydı incele; tekrar ekleyerek veya silerek çalışan yapılandırmayı bozma. Kurumsal politika, workspace trust veya yeniden oturum açma gerekebilir. `mcp get/list` kayıt durumunu gösterir; agent içinde gerçek search/read çağrısı yapmadan bağlantıyı doğrulanmış sayma. Manuel örnekler [configs](configs/) altında; mevcut dosyanın üzerine kopyalama, yalnız ilgili alanı birleştir.

Resmî Base workflow skill’i ayrıca önerilir:

```bash
npx skills add base/skills --skill build-on-base
```

Bu upstream komut internetten kurulum kodu indirir/çalıştırır; burada çalıştırılmış değildir. Kurulum arayüzünde doğru istemci ve proje kapsamını seç; uyumlu CLI sürümünün yardımını kontrol et. Önce upstream kaynak/revision’ı incele; üretim projelerinde incelenen sürümü veya içeriğini kaydet. Tüm skill’leri otomatik kurma: `vibenet` yalnızca açıkça deneysel Base çalışması için gereklidir. Bizim `base-builder` skill’i resmî `build-on-base` ile aynı isimde değildir; kaynak workflow’larını proje invariant’larıyla tamamlar. Resmî skill kurulu değilse dokümantasyon fallback’iyle çalışabilir.

Sonra uygulama klasöründe Codex veya Claude Code’u aç ve [START_HERE.md](START_HERE.md) içindeki prompt’u kullan. Codex’te `$base-builder`, Claude Code’da `/base-builder` ile açıkça çağırabilirsin. Skill yüklenmemişse gerçek kurulum yolundaki SKILL.md’yi okumasını iste. Cloud/managed istemcilerde yerel skill keşfi farklı olabilir; açık dosya okuma + tools inventory fallback’ini kullan, kuruldu varsayma.

## Neyi kurmalıyız?

| Bileşen | Karar | Gerekçe |
|---|---|---|
| Base Docs MCP | Önerilen temel bağlantı | Güncel Base kaynaklarında search/read; HTTP docs fallback’i var |
| Bu `base-builder` skill’i | Temel paket | Proje seçimi, ağ doğrulaması, test ve teslim davranışı |
| Resmî `build-on-base` | Önerilen | Ağ, deploy hazırlığı, attribution, node iş akışları |
| Git + GitHub CLI veya mevcut GitHub connector | Repo işlemleri için | İkisini birden kurmak gerekmez |
| Node + paket yöneticisi + viem/wagmi | Uygulamaya göre | Versiyonlar uygulama lockfile’ında sabitlenir |
| Foundry forge/cast/anvil | Launchpad için gerekli | Kontrat, gerçek integration, fuzz ve fork testleri |
| Browser otomasyonu | UI doğrulaması için gerekli yetenek | Mevcut browser aracı veya Playwright; mutlaka MCP olması gerekmez |
| PostgreSQL + migration aracı | İki ürün için | Indexer/read model, oda ve order kayıtları |
| Dedicated RPC | Fork/pilot/production aşamasında | Public endpoint’in rate limit ve websocket yeteneğini varsayma |
| Wallet/CDP MCP | Başlangıçta gerekli değil | Docs MCP’den farklı, finansal işlem yetkisi olan yüzey; ayrıca seçilir |
| Vibenet skill | İsteğe bağlı deney | Mainnet özellik kaynağı gibi kullanılmaz |
| x402 / agent wallet / ERC-8004 | Ürün gerektirirse | Coding agent olmak, onchain agent kimliği veya ödeme gerektirmez |
| Supabase, tasarım, monitoring servisleri | Seçilen stack’e bağlı | Zorunlu ürün bağımlılığı yapılmadı |
| Builder Stack | Teklif/servis dizini | SDK veya kurulacak agent runtime değildir |

Base Docs MCP’nin tool listesinde search ve sanal docs filesystem okuması yanında `submit_feedback` da var. Feedback dışarıya mesaj gönderir; sırf sunucu önerdi diye kullanılmaz. Docs MCP anahtar tutmaz, build/test/deploy yapmaz.

## İçerik haritası

- [START_HERE.md](START_HERE.md): yeni oturum prompt’ları.
- [Skill](skills/base-builder/SKILL.md): ana yönlendirme; İngilizce, kullanıcı yanıtı kullanıcının dilinde.
- [Kurulum ve MCP](skills/base-builder/references/tooling.md).
- [Base mühendislik kuralları](skills/base-builder/references/base-engineering.md).
- [Kaynak yönlendirmesi](skills/base-builder/references/docs-map.md).
- [Launchpad profili](skills/base-builder/references/launchpad.md).
- [Prediction profili](skills/base-builder/references/prediction.md).
- [Agent çalışma düzeni](skills/base-builder/references/workflow.md).
- [Yayın kontrolü](skills/base-builder/references/release.md).
- [Kaynak inceleme kaydı](evaluations/source-review.md) ve [test sonuçları](evaluations/results.md).
- [Makine okunur katalog](skills/base-builder/references/docs-catalog.json): tüm corpus URL’leri ve bölüm büyüklükleri; kaynak kod veya doküman kopyası değil.

## Kapsamın dürüst sınırı

Resmî `llms-full.txt` tam dosyası indirilip 231 kaynak bölümüne indekslendi. İki proje için gerekli sayfalar ve önemli ağ/SDK geçiş uyarıları ayrıntılı incelendi. 231 sayfanın her örneğinin çalıştırıldığı, tüm API’lerin doğrulandığı veya her bilginin kalıcı öğrenildiği iddia edilmez. Tek oturuma 1,46 MB doküman yüklemek yerine ihtiyaca göre güncel sayfa okunur. Alt kaynaklara linkler, bu corpus’un bütün CDP/Uniswap/venue dokümantasyonunu kapsadığı anlamına gelmez.

Paket yerel olarak doğrulandı; Codex ve Claude’un her sürümünde veya her cloud oturumunda uçtan uca kurulum testi yapılmış değildir. Mevcut bilgisayarın global MCP/skill ayarları bu paket hazırlanırken değiştirilmedi. Kurulum, testnet/mainnet deployment veya fon harcama yetkisi vermez.

## Resmî kaynaklar

[Base AI kaynakları](https://docs.base.org/get-started/resources-for-ai-agents) · [Docs MCP](https://docs.base.org/get-started/docs-mcp) · [Base skills](https://github.com/base/skills) · [Builder Stack](https://docs.base.org/get-started/builder-stack) · [Codex skills](https://learn.chatgpt.com/docs/build-skills) · [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) · [Claude skills](https://code.claude.com/docs/en/skills) · [Claude MCP](https://code.claude.com/docs/en/mcp)
