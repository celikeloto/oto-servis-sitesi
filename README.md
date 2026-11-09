# Çelikel Oto Servis web sitesi

Yarımburgaz / Küçükçekmece'deki Çelikel Oto Servis'in sitesi. GitHub Pages ile yayınlanır; `main` dalına gönderilen her değişiklik birkaç dakika içinde yayına girer.

## Yapı
- `index.html`: ana sayfa
- `hizmetler.html`, `hizmet-*.html`: hizmet sayfaları
- `markalar.html`, `marka-*.html`: marka sayfaları
- `hakkimizda.html`, `iletisim.html`
- `assets/site.css`, `assets/site.js`: ortak stil ve betikler

## Düzenleme
Sayfalar elle değil, `_kaynak/olustur.py` ile üretilir. Metinleri, hizmetleri, markaları veya sık sorulan soruları değiştirmek için bu dosyayı düzenleyip depo kökünden çalıştırın:

    python3 _kaynak/olustur.py

Stiller `_kaynak/temel.css` ve `_kaynak/ek.css` dosyalarındadır. Çalışma saatleri `assets/site.js` içindeki `AYAR` satırındadır.
