# Bu siteyle çalışan Claude için kurallar

Site sahibi bu kuralların her zaman uygulanmasını istedi. Kullanıcıyla Türkçe konuş.

## 1. Onay almadan yayına gönderme
- `main` dalına gönderilen her değişiklik birkaç dakika içinde canlı siteye çıkar.
- Bu yüzden `git push` yapmadan önce kullanıcıya neyi değiştirdiğini kısaca anlat ve açıkça onay iste. Onay gelmeden gönderme.
- Kullanıcı "ekle" ya da "yap" dese bile, yayına göndermeden önce özeti gösterip onay al.

## 2. Her fotoğrafı ve videoyu kontrol et, sorun varsa kullanıcıyı uyar
Siteye eklenecek her görseli ve videoyu tek tek aç, bak. Şunlardan biri varsa eklemeden önce kullanıcıya söyle ve ne yapılacağını sor:
- **Plaka:** Okunabilir ya da kısmen okunabilir bir araç plakası (müşteri aracı olabilir). Videolarda plakanın göründüğü bölümü kesmeyi ya da bulanıklaştırmayı öner.
- **Kişiler:** Tanınabilir yüz, müşteri adı, telefon numarası, fatura, evrak, ekran görüntüsündeki kişisel bilgi.
- **Konu dışı:** Fotoğraf eklendiği sayfanın konusuyla ilgisizse (ör. fren sayfasına raf fotoğrafı).
- **Kalite:** Bulanık, çok karanlık, ters dönmüş ya da yarım kalmış görüntü.
- **Başkasına ait içerik:** İnternetten alınmış görsel, başka bir firmanın logosu öne çıkan reklam görseli.

Her durumda:
- Fotoğraflardaki ve videolardaki tüm meta verileri (GPS konumu, cihaz bilgisi) sil.
- Görselleri küçült (büyük boy en fazla ~1000–1200 px genişlik, ayrıca `-kucuk` sürümü). Videoların sesini kaldır, 720p'ye indir, `+faststart` kullan.
- Her görsele anlamlı Türkçe `alt` metni yaz.

## 3. Başkası bir şey değiştirdiyse söyle
- Çalışmaya başlamadan önce ve `git push`'tan önce `git pull` yap, `git log` ile son değişikliklere bak.
- Bu sohbette yapılmamış yeni değişiklikler varsa (özellikle yeni ya da silinmiş fotoğraf, video), bunları kullanıcıya kısaca listele.
- Başka bir değişikliği kullanıcı istemeden geri alma ya da üzerine yazma.

## Sitenin yapısı
README.md'ye bak. Sayfalar elle düzenlenmez; `_kaynak/` içindeki dosyalar değiştirilir ve `python3 _kaynak/olustur.py` çalıştırılır. Bu komut `_kaynak/__pycache__` dosyalarını da değiştirir; onları göndermeden önce `git checkout -- _kaynak/__pycache__` ile geri al.
