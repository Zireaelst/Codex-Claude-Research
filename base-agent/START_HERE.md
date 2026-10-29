# Yeni oturum başlangıcı

## Bu araştırma reposunu okuyabilen herhangi bir coding agent

```text
base-agent/skills/base-builder/SKILL.md dosyasını oku ve bu görev için uygula.
Önce gerçek tool/runtime envanteri çıkar; kurulu olmayan MCP veya erişimi varmış gibi davranma.
Base Docs MCP varsa güncel kaynakları onunla oku; yoksa resmî llms.txt ve ilgili .md sayfalarını kullan.
Çalışacağımız uygulama ayrı repoda olacak; araştırma arşivini uygulamaya dönüştürme.
Profil: launchpad veya prediction (aşağıda seçiyorum).
Hedef: Base; local ve fork doğrulamasıyla başla. Public deployment bu görevde yok.
Kaynak spec ve roadmap'leri okuyup ilk bağımsız iş paketini, kabul kriterlerini ve uygulanabilir adımları çıkar.
Yetkili yerel işi tamamla ve gerçek test kanıtını kaydet. Eksik erişim yalnız ilgili adımı bloke etsin.
Profil: launchpad
Görev: gerçek v4/Permit2 integration harness'ini ve sabitlenmiş ağ manifestini hazırlamak.
```

## Kurulu skill ile Launchpad

```text
$base-builder kullan. Profil launchpad.
Araştırma kaynağı: https://github.com/Zireaelst/Codex-Claude-Research/tree/main/evm-launchpad-project-idea
Roadmap: aynı repoda base-project-roadmaps/2026-10-29/01-launchpad-roadmap.md
Bu uygulama reposunda WP01'i uygula: gerçek upstream kontrat harness'i, revision/compiler pinleri,
network manifest şeması ve test kanıtı. Mock settlement'ı integration başarı sayma.
Mainnet/testnet broadcast yapma. İlerlemeyi docs/agent/STATUS.md'ye kaydet.
```

Claude Code’da başlangıç çağrısını `/base-builder` olarak kullan; geri kalan görev aynı kalabilir.

## Kurulu skill ile Consumer Prediction

```text
$base-builder kullan. Profil prediction.
Roadmap: https://github.com/Zireaelst/Codex-Claude-Research/blob/main/base-project-roadmaps/2026-10-29/02-prediction-consumer-roadmap.md
Mevcut venue'lara bağlanan sosyal uygulama kuruyoruz; kendi AMM/oracle veya ortak para havuzu kurma.
İlk iş: Limitless aday adapter'ı için read-only katalog/lifecycle spike'ı ve capability matrisi.
Uygunluğu doğrulanmayan wallet/order/claim yollarını açıkça unsupported veya blocked işaretle.
HTTP 200'ü fill sayma. Gerçek para emri gönderme. Sonuçları ve sonraki paketi kaydet.
```

## Agentlarla bölme

```text
Bu görevde alt agent kullanabilirsin. Ana agent kapsamı ve entegrasyonu yönetsin.
Bir worker gerçek kontrat testlerine, biri API/indexer'a, biri UX/state testlerine baksın.
Önce ortak tip/ABI sözleşmesini sabitle; dosya sahipliği çakışmasın.
Reviewer kendi implementasyonunu bağımsız audit diye sunmasın.
Yalnız bizim yetkilendirdiğimiz yerel kapsamda çalış; dışa yayın veya para hareketi devretme.
```

Agent aracı yoksa aynı iş sırasını tek oturumda uygula. Çoklu agent bir zorunluluk veya güvenlik denetiminin yerine geçen mekanizma değildir.
