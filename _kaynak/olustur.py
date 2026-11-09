"""Çelikel Oto Servis sitesini üretir.
Kullanım:  python3 _kaynak/olustur.py   (depo kök klasöründen)
Metinleri değiştirmek için bu dosyadaki HIZMETLER, MARKALAR ve SSS listelerini düzenleyin."""
import pathlib, html, json
KOK = pathlib.Path(__file__).resolve().parent.parent
K = KOK / "_kaynak"

TEL, TEL_YAZI = "+905421401974", "0542 140 19 74"
TEL2, TEL2_YAZI = "+905354943400", "0535 494 34 00"
WA = "905421401974"
YOL, YOL_YAZI = "+905380648205", "0538 064 82 05"   # yol yardım / acil hat
ADRES1, ADRES2 = "Yarımburgaz, Selvi Sk. 65/1", "34303 Küçükçekmece / İstanbul"
HARITA = "https://www.google.com/maps/search/?api=1&amp;query=%C3%87elikel%20Oto%20Servis%20Yar%C4%B1mburgaz&amp;query_place_id=ChIJf1T-sSWlyhQR2FDqjvk1wW4"
def wa(m):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(m)}"

# ---------------- ikonlar ----------------
def I(inner, w=22, sw=2): return f'<svg width="{w}" height="{w}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
TEL_I = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
WA_I = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3 .78.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.25-.12-1.47-.72-1.7-.8s-.39-.12-.56.12-.64.8-.78.97-.29.18-.54.06a6.7 6.7 0 0 1-3.34-2.92c-.25-.43.25-.4.72-1.34a.45.45 0 0 0-.02-.43c-.06-.12-.56-1.34-.76-1.84s-.4-.41-.56-.42h-.48a.92.92 0 0 0-.67.31 2.8 2.8 0 0 0-.87 2.08 4.9 4.9 0 0 0 1.02 2.58 11.1 11.1 0 0 0 4.25 3.76c1.58.68 2.2.74 3 .62a2.55 2.55 0 0 0 1.68-1.18 2.1 2.1 0 0 0 .14-1.18c-.06-.1-.23-.16-.48-.28z"/></svg>'
KONUM_I = I('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', 18)
SAAT_I = I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', 18)
TIK_I = I('<path d="M4 12l5 5L20 6"/>', 18, 2.6)
OK_I = I('<path d="M6 9l6 6 6-6"/>', 16, 2.4)
YILDIZ = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.6 7.2.8-5.4 4.9 1.5 7.1L12 17.8 5.7 21.4l1.5-7.1L1.8 9.4 9 8.6z"/></svg>'
CEKICI_I = I('<path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>', 20)
KALKAN_I = I('<path d="M12 2l8 3v6c0 5-3.5 9.3-8 11-4.5-1.7-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>', 26, 1.8)
YILDIZ_I = I('<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>', 26, 1.8)
ARABA_I = I('<path d="M5 16l1.5-5a2 2 0 0 1 1.9-1.4h7.2a2 2 0 0 1 1.9 1.4L19 16"/><rect x="3" y="16" width="18" height="4" rx="1.5"/><path d="M7 20v1M17 20v1"/>', 26, 1.8)
CEKICI_I2 = I('<path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>', 26, 1.8)
KAMYON_I = I('<path d="M3 16V8h11v8M14 11h4l3 3v2h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>', 28, 1.8)
EKRAN_I = I('<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M7 21h10M12 17v4M7 9l2 2-2 2M12 13h4"/>', 28, 1.8)
KUTU_I = I('<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>', 28, 1.8)
FIYAT_I = I('<path d="M20 12l-8 8-9-9V3h8z"/><circle cx="7.5" cy="7.5" r="1.5"/>', 28, 1.8)
USTA_I = I('<circle cx="12" cy="7" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>', 28, 1.8)
KALP_I = I('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/>', 28, 1.8)
GOZ_I = I('<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>', 28, 1.8)

# ---------------- içerik ----------------
import sys; sys.path.insert(0, str(K))
from hizmetler import HIZMETLER, GRUPLAR
from bolgeler import KUCUKCEKMECE_MAHALLELER, ILCELER
SITE_URL = "https://celikeloto.github.io/oto-servis-sitesi/"   # domain bağlanınca değiştirin
TARIH, TARIH_YAZI = "2026-11-09", "9 Kasım 2026"
ANA_HIZMETLER = [h for h in HIZMETLER if h.get("ana")]
MARKALAR = ["Fiat","Renault","Dacia","Volkswagen","Ford","Opel","Peugeot","Citroën","Toyota","Hyundai","BMW","Mercedes-Benz","Audi"]
LOGO_SLUG = {"Mercedes-Benz":"mercedes"}
LOGO_CDN = "https://cdn.jsdelivr.net/npm/simple-icons@16.16.0/icons/"   # Simple Icons, sürüm sabit
def logo(m, boy=28): return f'<img class="marka-logo" src="{LOGO_CDN}{LOGO_SLUG.get(m, mslug(m))}.svg" alt="" width="{boy}" height="{boy}" loading="lazy" onerror="this.remove()">'
def mslug(m): return m.lower().replace("ë","e").replace("ç","c").replace("ü","u").replace("ö","o").replace("ş","s").replace("ı","i").replace("ğ","g").replace(" ","-")
SSS = [
 ("Çalışma saatleriniz nedir?", "Pazartesiden cumartesiye 08:00–19:00 arası açığız. Pazar günü kapalıyız."),
 ("Gelmeden önce randevu almam gerekiyor mu?", f"Aramanızı öneririz; böylece aracınız için yer ayırır, beklemenizi önleriz. {TEL_YAZI} numarasından arayabilir ya da WhatsApp'tan yazabilirsiniz."),
 ("Aracımı adresimden alabilir misiniz?", "Evet. Aracınızı adresinizden alıyor, iş bitince yine adresinize getiriyoruz. Uygun günü birlikte belirlemek için bizi arayın."),
 ("Fiyatı önceden öğrenebilir miyim?", "Evet. Arıza tespitinden sonra ne yapılacağını ve tutarını işe başlamadan söyleriz; onayınız olmadan işe başlamayız."),
 ("Motor arıza ışığı yandı, ne yapmalıyım?", "Işık sabit yanıyorsa aracı en kısa sürede getirin; yanıp sönüyorsa ya da araç çekişten düştüyse yola devam etmeden bizi arayın. Cihazla hata kodlarını okuyup sorunun kaynağını buluruz."),
 ("Yedek parçayı siz mi temin ediyorsunuz?", "Evet. Orijinal ve muadil parça seçeneklerini fiyatlarıyla birlikte size söyleriz. Stokta olmayan parçayı kısa sürede getirtiriz."),
 ("Hangi markalara bakıyorsunuz?", "Binek araçların büyük çoğunluğuna bakıyoruz: " + ", ".join(MARKALAR) + " ve diğer markalar. Aracınızdan emin değilseniz arayıp sorabilirsiniz."),
 ("Aracım yolda kaldı, ne yapmalıyım?", f"Güvenli bir yere çekilip dörtlüleri yakın ve yol yardım hattımızı arayın: {YOL_YAZI}. Durumu dinleyip size en hızlı çözümü söyleyelim."),
 ("Aracın hangi parçalarına bakıyorsunuz?", "Aracın bütün parçalarına bakım ve onarım yapıyoruz: motor, triger, debriyaj, şanzıman, soğutma ve yakıt sistemi, turbo, egzoz, fren, süspansiyon ve direksiyon, lastik ve balans, elektrik, klima ve kaporta. Gereken yedek parçayı da biz temin ediyoruz."),
 ("Ustanız ne kadar tecrübeli?", "Servisimizi yöneten Sebahattin Usta 40 yıldır bu işi yapıyor. Aracınızla bizzat ilgilenir."),
 ("İşçiliğinize garanti veriyor musunuz?", "Evet. Yaptığımız işçiliğe garanti veriyoruz; ayrıntıları iş öncesinde size söyleriz."),
 ("Fatura veriyor musunuz?", "Evet, faturalı çalışıyoruz. Yapılan işler ve kullanılan parçalar faturada ayrıntılı yazar."),
 ("Yol yardım hattınız 7/24 açık mı?", f"Evet. Yol yardım hattımız {YOL_YAZI} günün her saati açıktır ve Küçükçekmece'nin tamamına hizmet veriyoruz."),
 ("Hibrit ve elektrikli araçlara bakıyor musunuz?", "Evet. Hibrit ve elektrikli araçların bakım, fren, süspansiyon, klima ve elektrik işlerini yapıyoruz."),
 ("Garantisi devam eden aracımın bakımını yaptırabilir miyim?", "Evet. Bakımı üretici talimatlarına uygun yağ ve parçayla yapar, faturalı olarak belgeleriz. Kesin şartlar için aracınızın garanti kitapçığına da bakmanızı öneririz."),
 ("Neredesiniz?", f"{ADRES1}, {ADRES2}. Yol tarifi için sayfanın altındaki haritayı kullanabilirsiniz."),
]

CSS_SURUM = "15"
# ---------------- parçalar ----------------
def ust(aktif=""):
    hl = "".join(f'<li class="grup-bas" role="presentation">{g}</li>' + "".join(f'<li><a href="hizmet-{h["slug"]}.html">{I(h["ikon"],18)}{h["ad"]}</a></li>' for h in HIZMETLER if h["grup"]==g) for g in GRUPLAR)
    def a(href, ad, k): return f'<a href="{href}"{" aria-current=\"page\"" if aktif==k else ""}>{ad}</a>'
    return f'''<a class="atla sr-only" href="#icerik">İçeriğe geç</a>
<div class="bilgi-cubuk"><div class="kap">
  <ul>
    <li>{TEL_I}<a href="tel:{TEL}">{TEL_YAZI}</a></li>
    <li class="gizle-mobil">{KONUM_I}<a href="{HARITA}" target="_blank" rel="noopener">Yarımburgaz, Küçükçekmece</a></li>
    <li>{SAAT_I}Pzt–Cmt 08:00–19:00</li>
  </ul>
  <ul><li class="acil">{CEKICI_I}<a href="tel:{YOL}">Yol yardım 7/24: <b>{YOL_YAZI}</b></a></li><li class="gizle-mobil">{WA_I}<a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li></ul>
</div></div>
<header class="ust">
  <div class="kap">
    <a class="logo" href="index.html" aria-label="Çelikel Oto Servis ana sayfa"><img src="assets/logo/logo-yatay.svg" alt="Çelikel Oto Servis" width="460" height="120"></a>
    <button class="menu-dugme" type="button" aria-controls="ana-menu" aria-expanded="false" aria-label="Menüyü aç">{I('<path d="M4 7h16M4 12h16M4 17h16"/>',24)}</button>
    <nav id="ana-menu" aria-label="Ana menü">
      <div class="acilir"><button type="button" aria-expanded="false">Hizmetlerimiz {OK_I}</button>
        <ul class="mega">{hl}<li class="tumu-li"><a class="tumu" href="hizmetler.html">Tüm hizmetler</a></li></ul></div>
      {a("markalar.html","Markalar","marka")}
      {a("rehber.html","Rehber","rehber")}
      {a("bolgeler.html","Bölgeler","bolge")}
      {a("hakkimizda.html","Hakkımızda","hak")}
      {a("iletisim.html","İletişim","ilet")}
      <a class="btn btn-sari" href="tel:{TEL}">{TEL_I}<span>Hemen ara</span></a>
    </nav>
  </div>
</header>'''

def form_bolum():
    return f'''<section class="sor" id="parca-sor" aria-labelledby="h-sor"><div class="kap">
  <div><span class="etiket">Hızlı iletişim</span><h2 id="h-sor">Parça sorun, <span class="vurgu">randevu alın</span></h2>
    <p class="aciklama">Formu doldurun, mesajınız WhatsApp'ta hazır açılsın. Size sadece gönder'e basmak kalır.</p>
    <ul class="ipuclari"><li>{TIK_I}<span>Doğru parça için aracın marka, model ve yılını yazın.</span></li>
    <li>{TIK_I}<span>Ruhsattaki şasi numarası varsa işimiz daha da kolaylaşır.</span></li>
    <li>{TIK_I}<span>Mesai saatlerinde genelde kısa sürede dönüyoruz.</span></li></ul></div>
  <form id="form" novalidate>
    <fieldset><legend>Ne istiyorsunuz?</legend><div class="secim">
      <label><input type="radio" name="tur" value="parca" checked> Parça fiyatı</label>
      <label><input type="radio" name="tur" value="randevu"> Servis randevusu</label></div></fieldset>
    <label class="alan"><span>Araç <small>(marka, model, yıl)</small></span><input type="text" name="arac" id="arac" placeholder="Örn. Fiat Egea 1.3 Multijet, 2019" autocomplete="off"></label>
    <label class="alan"><span id="aciklama-etiket">Hangi parça lazım?</span><textarea name="aciklama" id="aciklama" placeholder="Örn. Ön balata ve disk"></textarea></label>
    <p class="hata" id="hata" role="alert">Aracınızı ve ne istediğinizi yazın, öyle gönderelim.</p>
    <button class="btn btn-wa" type="submit">{WA_I} WhatsApp'ta gönder</button>
    <p class="form-not">WhatsApp yüklü değilse <a href="tel:{TEL}">{TEL_YAZI}</a> numarasını arayın.</p>
  </form></div></section>'''

def cagri(baslik="Gelemiyorsanız aracınızı biz alalım", metin="Aracınızı adresinizden alıyor, işi bitince yine adresinize getiriyoruz. Arayın, uygun günü birlikte belirleyelim."):
    return f'''<section class="cagri"><div class="kap"><div class="cagri-kart">
  <div><span class="etiket">Adresten alma</span><h2>{baslik}</h2><p>{metin}</p></div>
  <div class="eylemler"><a class="btn btn-sari" href="tel:{TEL}">{TEL_I} {TEL_YAZI}</a>
  <a class="btn btn-wa" href="{wa("Merhaba, aracım için gün ayarlamak istiyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp</a></div>
</div></div></section>'''

def alt():
    hl = "".join(f'<li><a href="hizmet-{h["slug"]}.html">{h["ad"]}</a></li>' for h in ANA_HIZMETLER[:6])
    ml = "".join(f'<li><a href="marka-{mslug(m)}.html">{m} servisi</a></li>' for m in MARKALAR[:6])
    return f'''<footer><div class="kap">
  <div><a class="logo alt-logo" href="index.html" aria-label="Çelikel Oto Servis ana sayfa"><img src="assets/logo/logo-yatay-acik.svg" alt="Çelikel Oto Servis" width="460" height="120"></a>
    <p style="margin:0;max-width:36ch">Oto bakım, tamir ve yedek parça. Aracınızı adresinizden alıyoruz.</p></div>
  <div><h3>Hizmetler</h3><ul>{hl}<li><a href="hizmetler.html">Tümü</a></li></ul></div>
  <div><h3>Rehber ve bölgeler</h3><ul><li><a href="rehber.html">Oto tamir rehberi</a></li><li><a href="kucukcekmece-yol-yardim-lastik-tamiri.html">Küçükçekmece yol yardım</a></li>{"".join(f'<li><a href="{i["slug"]}-oto-servis.html">{i["ad"]} oto servis</a></li>' for i in ILCELER[:4])}<li><a href="bolgeler.html">Tüm bölgeler</a></li></ul></div>
  <div><h3>İletişim</h3><ul><li><a href="tel:{TEL}">{TEL_YAZI}</a></li><li><a href="tel:{TEL2}">{TEL2_YAZI}</a></li>
    <li><a href="tel:{YOL}">Yol yardım 7/24: {YOL_YAZI}</a></li>
    <li>Pzt–Cmt 08:00–19:00</li><li><a href="{HARITA}" target="_blank" rel="noopener">{ADRES1}</a></li></ul></div>
  <p class="telif">© <span id="yil">2026</span> Çelikel Oto Servis · <a href="gizlilik.html">Gizlilik ve KVKK</a></p>
</div></footer>
<div class="alt-cubuk"><a class="btn btn-sari" href="tel:{TEL}">{TEL_I} Ara</a><a class="btn btn-wa" href="{wa("Merhaba, web sitenizden ulaşıyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp</a></div>
<button class="yukari" type="button" aria-label="Sayfanın başına dön">{I('<path d="M18 15l-6-6-6 6"/>',20,2.6)}</button>
<script src="assets/site.js?v={CSS_SURUM}"></script>'''

LD = {"@context":"https://schema.org","@type":"AutoRepair","name":"Çelikel Oto Servis",
 "telephone":TEL,"contactPoint":[{"@type":"ContactPoint","telephone":TEL2,"contactType":"customer service"},{"@type":"ContactPoint","telephone":YOL,"contactType":"emergency","hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}}],
 "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"19:00"}],
 "address":{"@type":"PostalAddress","streetAddress":ADRES1,"postalCode":"34303","addressLocality":"Küçükçekmece","addressRegion":"İstanbul","addressCountry":"TR"},
 "geo":{"@type":"GeoCoordinates","latitude":41.0456607,"longitude":28.7519682},
 "areaServed":["Küçükçekmece","Başakşehir","Avcılar","Beylikdüzü","Esenyurt","Bakırköy"],"priceRange":"₺₺"}

URLLER = []
def sayfa(dosya, baslik, aciklama, govde, aktif="", ek_ld=None, og_tur="website"):
    ld = json.dumps(LD, ensure_ascii=False)
    ek = f'\n<script type="application/ld+json">{json.dumps(ek_ld, ensure_ascii=False)}</script>' if ek_ld else ""
    h = f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(baslik)}</title>
<meta name="description" content="{html.escape(aciklama)}">
<meta name="theme-color" content="#23272b">
<meta property="og:title" content="{html.escape(baslik)}">
<meta property="og:description" content="{html.escape(aciklama)}">
<meta property="og:type" content="{og_tur}">
<meta property="og:url" content="{SITE_URL}{"" if dosya=="index.html" else dosya}">
<meta property="og:locale" content="tr_TR">
<link rel="canonical" href="{SITE_URL}{"" if dosya=="index.html" else dosya}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={CSS_SURUM}">
<script type="application/ld+json">{ld}</script>{ek}
</head>
<body>
{ust(aktif)}
<main id="icerik">
{govde}
</main>
{alt()}
</body>
</html>
'''
    (KOK / dosya).write_text(h, encoding="utf-8")
    URLLER.append(dosya)

def bas_orta(etiket, baslik, metin="", hid=""):
    m = f"<p>{metin}</p>" if metin else ""
    return f'<div class="bas-orta"><span class="etiket">{etiket}</span><h2 id="{hid}">{baslik}</h2>{m}</div>'

def hizmet_kartlari(liste, one_son=True):
    o = []
    for i, h in enumerate(liste):
        one = one_son and i == len(liste) - 1
        o.append(f'<li class="hizmet{" one" if one else ""}"><span class="ikon">{I(h["ikon"],30)}</span><h3>{h["ad"]}</h3><p>{h["kisa"]}</p><a class="detay" href="hizmet-{h["slug"]}.html">Detaylı bilgi<span class="sr-only">: {h["ad"]}</span></a></li>')
    return "\n".join(o)

def marka_kartlari():
    return "".join(f'<li><a href="marka-{mslug(m)}.html"><span class="harf" aria-hidden="true">{logo(m, 30)}</span><b>{m}</b><span>Bakım ve onarım</span></a></li>' for m in MARKALAR)

def sss_bolum():
    q = "".join(f'<details><summary>{s}</summary><p>{c}</p></details>' for s, c in SSS)
    return f'''<section class="sss" aria-labelledby="h-sss"><div class="kap">
  <div class="yan"><span class="etiket">SSS</span><h2 id="h-sss">Sık sorulan <span class="vurgu">sorular</span></h2><p>Aradığınız cevabı bulamadıysanız arayın ya da WhatsApp'tan yazın, hemen yardımcı olalım.</p>
  <a class="btn btn-koyu" href="{wa("Merhaba, bir sorum var.")}" target="_blank" rel="noopener">Soru sorun</a></div>
  <div>{q}</div></div></section>''', {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":s,"acceptedAnswer":{"@type":"Answer","text":c}} for s,c in SSS]}

def harita_bolum(sinif=""):
    return f'''<section class="iletisim {sinif}" id="iletisim" aria-labelledby="h-ilet"><div class="kap">
  <div><span class="etiket">İletişim</span><h2 id="h-ilet">Bize <span class="vurgu">ulaşın</span></h2>
  <ul class="bilgi">
    <li><span class="ikon">{TEL_I}</span><div><b>Telefon ve WhatsApp</b><a href="tel:{TEL}">{TEL_YAZI}</a><br>İkinci hat: <a href="tel:{TEL2}">{TEL2_YAZI}</a></div></li>
    <li><span class="ikon acil-ikon">{CEKICI_I}</span><div><b>Yol yardım / acil</b><a href="tel:{YOL}">{YOL_YAZI}</a></div></li>
    <li><span class="ikon">{SAAT_I}</span><div><b>Çalışma saatleri</b>Pazartesi–Cumartesi 08:00–19:00<br>Pazar kapalı</div></li>
    <li><span class="ikon">{KONUM_I}</span><div><b>Adres</b>{ADRES1}<br>{ADRES2}<br><a href="{HARITA}" target="_blank" rel="noopener">Yol tarifi al</a></div></li>
  </ul></div>
  <div class="harita"><iframe title="Çelikel Oto Servis haritada" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
    src="https://maps.google.com/maps?q=%C3%87elikel%20Oto%20Servis%20Yar%C4%B1mburgaz%2C%20Selvi%20Sk.%2065%2F1%2C%20K%C3%BC%C3%A7%C3%BCk%C3%A7ekmece&amp;z=16&amp;output=embed"></iframe></div>
</div></section>'''

def sayfa_bas(yol, baslik, metin, eylem=True):
    y = "".join(f'<li>{f"<a href=\"{h}\">{a}</a>" if h else a}</li>' for a, h in yol)
    e = f'''<div class="eylemler"><a class="btn btn-sari" href="tel:{TEL}">{TEL_I} Hemen ara</a>
      <a class="btn btn-wa" href="{wa("Merhaba, web sitenizden ulaşıyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a></div>''' if eylem else ""
    return f'''<section class="sayfa-bas"><div class="kap"><nav aria-label="Konum"><ol class="yol-izi">{y}</ol></nav>
  <h1>{baslik}</h1><p>{metin}</p>{e}</div></section>'''

def kirinti_ld(yol):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,**({"item":h} if h else {})} for i,(a,h) in enumerate(yol)]}

# ---------------- ana sayfa ----------------
def ana():
    yildiz5 = YILDIZ * 5
    YILDIZ5 = yildiz5
    seritler = "".join(f'<li><a href="marka-{mslug(m)}.html">{logo(m)}<span>{m}</span></a></li>' for m in MARKALAR)
    sss, sss_ld = sss_bolum()
    govde = f'''<section class="giris giris-videolu tek-sutun" aria-labelledby="baslik" style="padding-bottom:72px">
  <video class="giris-video" autoplay muted loop playsinline preload="metadata" poster="assets/video/giris-kapak.jpg" aria-hidden="true">
    <source src="assets/video/giris-mobil.mp4" type="video/mp4" media="(max-width: 720px)">
    <source src="assets/video/giris.mp4" type="video/mp4">
  </video>
  <div class="kap">
    <div>
      <a class="puan-rozet" href="{HARITA}" target="_blank" rel="noopener"><span class="yildiz">{yildiz5}</span> Google'da 5,0 <small>müşteri yorumları</small></a>
      <h1 id="baslik">Aracınız için <span class="alt-satir">güvenilir oto servis.</span></h1>
      <p class="ozet">Periyodik bakımdan motor tamirine, şanzımandan kaportaya kadar aracınızın her işi tek serviste. Gereken parçayı da biz buluruz.</p>
      <div class="eylemler">
        <a class="btn btn-sari" href="tel:{TEL}">{TEL_I} Hemen ara</a>
        <a class="btn btn-wa" href="{wa("Merhaba, web sitenizden ulaşıyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a>
      </div>
      <a class="acil-serit" href="tel:{YOL}">{CEKICI_I}<span>Yolda mı kaldınız? <b>7/24 yol yardım: {YOL_YAZI}</b></span></a>
      <ul class="guven"><li>{TIK_I}Ücretsiz ön kontrol</li><li>{TIK_I}Garantili işçilik</li><li>{TIK_I}Faturalı çalışma</li><li>{TIK_I}Adresten araç alma</li></ul>
      <div class="durum-satir" style="margin-top:18px"><p class="durum" id="durum" role="status"><i aria-hidden="true"></i><span>Pazartesi–Cumartesi 08:00–19:00</span></p>
        <span>İkinci hat: <a href="tel:{TEL2}">{TEL2_YAZI}</a></span></div>
    </div>
  </div>
</section>
<section class="one-kartlar" style="padding:0"><div class="kap"><div class="izgara">
  <div class="one-kart gorselli">
    <div class="mini mini-liste"><span class="mini-ikon">{KALKAN_I}</span>
      <ul><li>Fiyat önceden</li><li>Garantili işçilik</li><li>Faturalı çalışma</li></ul></div>
    <h3>Şeffaf servis</h3><p>Ne yapılacağını ve tutarını işe başlamadan söyleriz.</p>
  </div>
  <a class="one-kart gorselli acil-kart" href="tel:{YOL}">
    <div class="mini mini-canli"><span class="nabiz" aria-hidden="true"></span><div><b>7/24</b><small>YOL YARDIM AKTİF</small></div></div>
    <h3>7/24 yol yardım</h3><p>Gece gündüz arayın: <span class="no">{YOL_YAZI}</span></p>
  </a>
  <div class="one-kart gorselli">
    <div class="mini mini-grafik" aria-hidden="true"><i style="height:30%"></i><i style="height:48%"></i><i style="height:40%"></i><i style="height:66%"></i><i class="tam" style="height:92%"></i></div>
    <h3>Cihazla arıza tespit</h3><p>Hata kodlarını okur, sorunun kaynağını buluruz.</p>
  </div>
</div></div></section>

<section class="marka-serit" style="padding-top:56px;padding-bottom:0" aria-label="Bakımını yaptığımız markalar">
  <p>Bakımını ve onarımını yaptığımız markalardan bazıları</p>
  <div class="kayan"><ul>{seritler}</ul><ul aria-hidden="true">{seritler.replace('<a ','<a tabindex="-1" ')}</ul></div>
</section>

<section id="hizmetler" aria-labelledby="h-hizmet" style="padding-top:40px"><div class="kap">
  {bas_orta("Hizmetlerimiz", 'Aracınızın her işi <span class="vurgu">tek serviste</span>', "Aracınızı getirin, sorunu birlikte bakalım. Ne yapılacağını ve fiyatı işe başlamadan söyleriz.", "h-hizmet")}
  <ul class="hizmet-izgara">{hizmet_kartlari(ANA_HIZMETLER)}</ul>
  <p class="tum-hizmet"><a class="btn btn-koyu" href="hizmetler.html">Tüm hizmetleri görün ({len(HIZMETLER)} hizmet)</a></p>
</div></section>

<section class="neden" aria-labelledby="h-neden"><div class="kap">
  {bas_orta("Farkımız", 'Neden <span class="vurgu">Çelikel Oto</span>?', "", "h-neden")}
  <ul class="rakam-kartlar">
    <li><span class="yuvarlak">{YILDIZ_I}</span><b>5,0</b><em>Google puanı</em><p>Müşterilerimizin değerlendirmeleriyle</p></li>
    <li><span class="yuvarlak">{USTA_I}</span><b>40</b><em>Yıllık tecrübe</em><p>Sebahattin Usta 40 yıldır bu işi yapıyor</p></li>
    <li><span class="yuvarlak">{ARABA_I}</span><b>10+</b><em>Araç markası</em><p>Fiat'tan Toyota'ya, binek araçların çoğuna bakıyoruz</p></li>
    <li><span class="yuvarlak">{CEKICI_I2}</span><b class="kucuk-b">7/24</b><em>Yol yardım</em><p><a href="tel:{YOL}">{YOL_YAZI}</a></p></li>
  </ul>
</div></section>

<section class="alti-neden" aria-labelledby="h-alti"><div class="kap">
  <div class="alti-bas">
    <div>
      <h2 id="h-alti">Aracınızı bize bırakmanız için <span class="vurgu">6 neden</span></h2>
      <p>Bakırköy'deki dükkânımızdan beri bize gelen müşterilerimiz, yeni yerimize de gelmeye devam ediyor. Sadece tamir etmiyoruz, aracınızla gerçekten ilgileniyoruz.</p>
    </div>
    <figure class="alti-foto"><img src="assets/img/motor.jpg" srcset="assets/img/motor-kucuk.jpg 800w, assets/img/motor.jpg 1600w" sizes="(max-width: 900px) 100vw, 520px" alt="Motor bölümünde çalışan usta" loading="lazy" width="1600" height="900">
      <figcaption><span class="yildiz">{YILDIZ5}</span><b>5,0</b> Google puanı</figcaption></figure>
  </div>
  <ul class="neden-kartlar">
    <li><span class="kare">{USTA_I}</span><div><h3>Usta kadro</h3><em>40 yıllık tecrübe</em><p>İşinizle 40 yıldır bu işi yapan Sebahattin Usta birebir ilgilenir, sorunun kaynağını doğru bulur.</p></div></li>
    <li><span class="kare">{FIYAT_I}</span><div><h3>Sürpriz fatura yok</h3><em>Fiyat önceden</em><p>Ne yapılacağını ve tutarını işe başlamadan söyleriz; onayınız olmadan başlamayız.</p></div></li>
    <li><span class="kare">{YILDIZ_I}</span><div><h3>Garantili ve faturalı</h3><em>Google'da 5,0</em><p>İşçiliğimize garanti veriyor, faturalı çalışıyoruz. Müşteri yorumlarımızı Google'da okuyabilirsiniz.</p></div></li>
    <li><span class="kare">{CEKICI_I2}</span><div><h3>Yol yardım hattı</h3><em>7/24</em><p>Aracınız yolda kaldıysa <a href="tel:{YOL}">{YOL_YAZI}</a> numarasını arayın.</p></div></li>
    <li><span class="kare">{EKRAN_I}</span><div><h3>Cihazla teşhis</h3><em>Önce teşhis</em><p>Arıza tespit cihazıyla hata kodlarını okur, gereksiz parça değiştirmeyiz.</p></div></li>
    <li><span class="kare">{KAMYON_I}</span><div><h3>Kapınızdan alırız</h3><em>Adresten alma</em><p>Vaktiniz yoksa aracınızı adresinizden alır, iş bitince geri getiririz.</p></div></li>
  </ul>
</div></section>

<section aria-labelledby="h-yorum" style="padding-bottom:0"><div class="kap"><div class="yorum-kart">
  <div><div class="puan">5,0</div><div class="yildiz">{yildiz5}</div></div>
  <div><h2 id="h-yorum">Müşterilerimiz ne diyor?</h2><p>Google'daki yorumlarımızı okuyun; servisimizi bize gelenlerden dinleyin.</p></div>
  <a class="btn btn-koyu" href="{HARITA}" target="_blank" rel="noopener">Yorumları Google'da okuyun</a>
</div></div></section>

<section class="usta" aria-labelledby="h-surec"><div class="kap">
  <div><span class="etiket">Süreç</span><h2 id="h-surec">Nasıl <span class="vurgu">çalışıyoruz</span></h2><p class="giris-yazi">Aradığınız andan aracınızı teslim alana kadar her adımda ne olduğunu bilirsiniz.</p>
  <figure class="ilke"><p>Gereksiz parça değiştirmeyiz. Önce sorunu buluruz, sonra ne yapılacağını size söyleriz.</p></figure></div>
  <ol class="adimlar">
    <li><div><h3>Arayın ya da yazın</h3><p>Sorunu kısaca anlatın, size uygun bir gün ayarlayalım.</p></div></li>
    <li><div><h3>Aracı getirin ya da biz alalım</h3><p>Vaktiniz yoksa aracınızı adresinizden alırız.</p></div></li>
    <li><div><h3>Sorunu bulup fiyatı söyleriz</h3><p>Arıza tespitinden sonra ne yapılacağını ve tutarını işe başlamadan bildiririz.</p></div></li>
    <li><div><h3>Onayınızla tamir ederiz</h3><p>İş bitince aracınızı teslim eder, neyin değiştiğini gösteririz.</p></div></li>
  </ol>
</div></section>

<section aria-labelledby="h-marka" style="padding-top:0"><div class="kap">
  {bas_orta("Markalar", 'Servis verdiğimiz <span class="vurgu">markalar</span>', "Binek araçların büyük çoğunluğuna bakıyoruz. Markanızı seçin, o markada en sık yaptığımız işleri görün.", "h-marka")}
  <ul class="marka-izgara">{marka_kartlari()}</ul>
  <p class="diger">Listede olmayan bir marka mı? <a href="tel:{TEL}">Arayıp sorun</a>, büyük ihtimalle bakıyoruz.</p>
</div></section>

{cagri()}
{sss}
{form_bolum()}
{harita_bolum()}'''
    sayfa("index.html", "Çelikel Oto Servis | Oto Tamir, Bakım ve Yedek Parça",
          f"Çelikel Oto Servis: periyodik bakım, arıza tespit, motor, şanzıman, fren, klima, kaporta ve yedek parça. Aracınızı adresinizden alıyoruz. {TEL_YAZI}",
          govde, "ana", sss_ld)

# ---------------- hizmet sayfaları ----------------
def hizmet_sayfasi(h):
    yol = [("Ana sayfa","index.html"),("Hizmetlerimiz","hizmetler.html"),(h["ad"],None)]
    neler = "".join(f"<li>{TIK_I}<span>{n}</span></li>" for n in h["neler"])
    bel = "".join(f"<li>{b}</li>" for b in h["belirti"])
    diger = "".join(f'<li><a href="hizmet-{x["slug"]}.html"{" aria-current=\"page\"" if x is h else ""}>{x["ad"]} <span aria-hidden="true">›</span></a></li>' for x in HIZMETLER if x["grup"]==h["grup"]) + '<li><a href="hizmetler.html">Tüm hizmetler <span aria-hidden="true">›</span></a></li>'
    govde = f'''{sayfa_bas(yol, h["ad"], h["giris"])}
<section class="icerik"><div class="kap">
  <div class="metin">
    <h2>Bu belirtiler varsa bize gelin</h2><ul class="belirti">{bel}</ul>
    <h2>Neler yapıyoruz?</h2><ul class="tik">{neler}</ul>
    <h2>Nasıl ilerliyoruz?</h2>
    <p>Aracınızı getirdiğinizde ya da adresinizden aldığımızda önce kontrol eder, sorunun kaynağını buluruz. Ne yapılması gerektiğini ve tutarını işe başlamadan söyleriz; onayınızla işe başlar, iş bitince değişen parçaları gösteririz.</p>
    <p>Gereken parçayı biz temin ederiz. Orijinal ve muadil seçenekleri fiyatlarıyla birlikte size söyler, tercihi size bırakırız.</p>
  </div>
  <aside class="yan-kutu">
    <div class="kutu"><h2>Fiyat ve randevu</h2><p>Aracınızı ve sorunu yazın, size dönelim. Gelemiyorsanız aracınızı adresinizden alırız.</p>
      <a class="btn btn-sari" href="tel:{TEL}">{TEL_I} {TEL_YAZI}</a>
      <a class="btn btn-wa" href="{wa("Merhaba, " + h["ad"].lower() + " hakkında bilgi almak istiyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a>
      <p class="yan-acil">Yolda mı kaldınız? <a href="tel:{YOL}">{YOL_YAZI}</a></p></div>
    <div class="liste-kutu"><h3>{h["grup"]}</h3><ul>{diger}</ul></div>
  </aside>
</div></section>
{cagri()}
{harita_bolum()}'''
    ld = {"@context":"https://schema.org","@type":"Service","name":h["ad"],"serviceType":h["ad"],"provider":{"@type":"AutoRepair","name":"Çelikel Oto Servis","telephone":TEL},"areaServed":"Küçükçekmece, İstanbul","description":h["giris"]}
    sayfa(f'hizmet-{h["slug"]}.html', f'{h["ad"]} | Çelikel Oto Servis',
          f'{h["ad"]}: {h["kisa"]} Fiyatı işe başlamadan söyleriz. {TEL_YAZI}', govde, "", [ld, kirinti_ld(yol)])

def hizmetler_sayfasi():
    yol = [("Ana sayfa","index.html"),("Hizmetlerimiz",None)]
    govde = f'''{sayfa_bas(yol, "Hizmetlerimiz", "Aracınızın motorundan frenine, elektriğinden kaportasına kadar bütün parçalarının bakımını ve onarımını tek serviste yapıyoruz. Gereken parçayı da biz buluyoruz.")}
{"".join(f'<section class="grup-bolum" aria-label="{g}"><div class="kap"><h2 class="grup-baslik">{g}</h2><ul class="hizmet-izgara">{hizmet_kartlari([h for h in HIZMETLER if h["grup"]==g], one_son=False)}</ul></div></section>' for g in GRUPLAR)}
{cagri()}{form_bolum()}'''
    sayfa("hizmetler.html", "Hizmetlerimiz | Çelikel Oto Servis", "Çelikel Oto Servis hizmetleri: periyodik bakım, arıza tespit, motor, şanzıman, fren, oto elektrik, klima, kaporta boya ve yedek parça.", govde, "", kirinti_ld(yol))

# ---------------- marka sayfaları ----------------
def marka_sayfasi(m):
    yol = [("Ana sayfa","index.html"),("Markalar","markalar.html"),(f"{m} servisi",None)]
    hk = hizmet_kartlari(ANA_HIZMETLER[:6], one_son=False)
    diger = "".join(f'<li><a href="marka-{mslug(x)}.html"{" aria-current=\"page\"" if x==m else ""}>{x} <span aria-hidden="true">›</span></a></li>' for x in MARKALAR)
    govde = f'''{sayfa_bas(yol, f"{m} <span style=\"color:var(--ikaz)\">servisi</span>", f"{m} aracınızın bakımını, arıza tespitini ve onarımını yapıyoruz. Gereken {m} parçasını orijinal ya da muadil seçenekleriyle biz temin ediyoruz.")}
<section class="icerik"><div class="kap">
  <div class="metin">
    <h2>{m} aracınız için neler yapıyoruz?</h2>
    <ul class="tik">
      <li>{TIK_I}<span>Üretici aralıklarına uygun periyodik bakım</span></li>
      <li>{TIK_I}<span>Arıza tespit cihazıyla hata kodlarının okunması</span></li>
      <li>{TIK_I}<span>Motor, şanzıman, fren ve yürüyen aksam onarımları</span></li>
      <li>{TIK_I}<span>Elektrik, klima ve kaporta işleri</span></li>
      <li>{TIK_I}<span>Şasi numarasıyla doğru {m} parçasının temini</span></li>
    </ul>
    <h2>Parçayı biz buluyoruz</h2>
    <p>{m} aracınız için gereken parçayı şasi numarasıyla eşleştirir, orijinal ve muadil seçenekleri fiyatlarıyla birlikte size söyleriz. Stokta olmayan parçayı kısa sürede getirtir, serviste takarız.</p>
    <h2>Fiyatı önceden söylüyoruz</h2>
    <p>Aracınızı kontrol ettikten sonra ne yapılacağını ve tutarını işe başlamadan bildiririz. Onayınız olmadan işe başlamayız; iş bitince değişen parçaları gösteririz.</p>
  </div>
  <aside class="yan-kutu">
    <div class="kutu"><h2>{m} için fiyat sorun</h2><p>Modelinizi ve yılını yazın, size dönelim.</p>
      <a class="btn btn-sari" href="tel:{TEL}">{TEL_I} {TEL_YAZI}</a>
      <a class="btn btn-wa" href="{wa(f"Merhaba, {m} aracım için bilgi almak istiyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a></div>
    <div class="liste-kutu"><h3>Diğer markalar</h3><ul>{diger}</ul></div>
  </aside>
</div></section>
<section aria-labelledby="h-mh" style="padding-top:0"><div class="kap">{bas_orta("Hizmetler", f'{m} için <span class="vurgu">hizmetlerimiz</span>', "Hizmete tıklayın, ayrıntıları görün.", "h-mh")}<ul class="hizmet-izgara">{hk}</ul></div></section>
{cagri()}'''
    sayfa(f"marka-{mslug(m)}.html", f"{m} Servisi | Çelikel Oto Servis",
          f"{m} bakım, arıza tespit ve onarım. {m} yedek parça temini, fiyat işe başlamadan. {TEL_YAZI}", govde, "", kirinti_ld(yol))

def markalar_sayfasi():
    yol = [("Ana sayfa","index.html"),("Markalar",None)]
    govde = f'''{sayfa_bas(yol, "Markaya göre servis", "Binek araçların büyük çoğunluğuna bakıyoruz. Markanızı seçin; listede yoksa arayıp sorun.")}
<section aria-label="Marka listesi"><div class="kap"><ul class="marka-izgara">{marka_kartlari()}</ul>
<p class="diger">Listede olmayan bir marka mı? <a href="tel:{TEL}">Arayıp sorun</a>, büyük ihtimalle bakıyoruz.</p></div></section>
{cagri()}'''
    sayfa("markalar.html", "Markalar | Çelikel Oto Servis", "Fiat, Renault, Dacia, Volkswagen, Ford, Opel, Peugeot, Citroën, Toyota, Hyundai ve diğer markalar için bakım ve onarım.", govde, "marka", kirinti_ld(yol))

def hakkimizda():
    yol = [("Ana sayfa","index.html"),("Hakkımızda",None)]
    govde = f'''{sayfa_bas(yol, "Aracınız Sebahattin Usta'ya emanet", "Çelikel Oto Servis'i 40 yıldır bu işi yapan Sebahattin Aksaç yönetiyor. Bakırköy'deki dükkânımızdan beri bize gelen birçok müşterimiz, yeni yerimize de gelmeye devam ediyor.")}
<section class="usta"><div class="kap">
  <div><h2>Nasıl çalıştığımız</h2><p class="giris-yazi">Bir servise aracınızı bırakırken içinizin rahat olması gerekir. Bu yüzden her adımda ne yaptığımızı size anlatırız.</p>
    <figure class="ilke"><p>Gereksiz parça değiştirmeyiz. Önce sorunu buluruz, sonra ne yapılacağını size söyleriz.</p></figure>
    <a class="google" href="{HARITA}" target="_blank" rel="noopener">Müşteri yorumlarını Google'da okuyun</a></div>
  <ol class="adimlar">
    <li><div><h3>Arayın ya da yazın</h3><p>Sorunu kısaca anlatın, size uygun bir gün ayarlayalım.</p></div></li>
    <li><div><h3>Aracı getirin ya da biz alalım</h3><p>Vaktiniz yoksa aracınızı adresinizden alırız.</p></div></li>
    <li><div><h3>Sorunu bulup fiyatı söyleriz</h3><p>Ne yapılacağını ve tutarını işe başlamadan bildiririz.</p></div></li>
    <li><div><h3>Onayınızla tamir ederiz</h3><p>İş bitince aracınızı teslim eder, neyin değiştiğini gösteririz.</p></div></li>
  </ol></div></section>
{cagri()}
{harita_bolum()}'''
    sayfa("hakkimizda.html", "Hakkımızda | Çelikel Oto Servis", "Çelikel Oto Servis'i Sebahattin Aksaç yönetiyor. Bakırköy'den bu yana müşterilerimizin güvendiği oto servis.", govde, "hak", kirinti_ld(yol))

def iletisim():
    yol = [("Ana sayfa","index.html"),("İletişim",None)]
    govde = f'''{sayfa_bas(yol, "İletişim", "Arayın, WhatsApp'tan yazın ya da servisimize gelin. Gelemiyorsanız aracınızı adresinizden alırız.")}
{harita_bolum("iletisim-sayfa")}
{form_bolum()}'''
    sayfa("iletisim.html", "İletişim | Çelikel Oto Servis", f"Çelikel Oto Servis iletişim: {TEL_YAZI}, {ADRES1}, {ADRES2}. Pazartesi–Cumartesi 08:00–19:00.", govde, "ilet", kirinti_ld(yol))

def css():
    (KOK / "assets" / "site.css").write_text((K / "temel.css").read_text(encoding="utf-8") + (K / "ek.css").read_text(encoding="utf-8") + (K / "tema.css").read_text(encoding="utf-8"), encoding="utf-8")

def llms():
    satir = [
"# Çelikel Oto Servis",
"",
"> Çelikel Oto Servis; aracın bütün parçalarının bakımını ve onarımını yapan, gereken yedek parçayı da temin eden bir oto servistir. Ne yapılacağını ve tutarını işe başlamadan söyler, aracı müşterinin adresinden alıp geri getirir. Servisi 40 yıllık tecrübeye sahip Sebahattin Aksaç yönetir.",
"",
"## İletişim",
f"- Adres: {ADRES1}, {ADRES2}",
f"- Telefon ve WhatsApp: {TEL_YAZI}",
f"- İkinci hat: {TEL2_YAZI}",
f"- Yol yardım / acil hat (7/24): {YOL_YAZI}",
"- Garantili işçilik, faturalı çalışma, ücretsiz ön kontrol",
"- Kasko/sigorta hasar onarımı, akü, boyasız göçük ve pasta cila, hibrit/elektrikli araç bakımı",
"- Çalışma saatleri: Pazartesi–Cumartesi 08:00–19:00, pazar kapalı",
"- Hizmet bölgesi: Küçükçekmece, Başakşehir, Avcılar, Beylikdüzü, Esenyurt, Bakırköy",
"",
"## Öne çıkanlar",
"- Usta: Sebahattin Aksaç, 40 yıllık tecrübe",
"- Google puanı: 5,0",
"- Fiyat işe başlamadan söylenir; onay alınmadan işe başlanmaz",
"- Araç müşterinin adresinden alınıp geri getirilir",
"- Arıza tespit cihazıyla teşhis",
"- Orijinal ve muadil yedek parça temini",
"",
"## Hizmetler"]
    for g in GRUPLAR:
        satir.append(f"### {g}")
        for h in HIZMETLER:
            if h["grup"]==g: satir.append(f'- [{h["ad"]}](hizmet-{h["slug"]}.html): {h["kisa"]}')
        satir.append("")
    satir += ["## Bakılan markalar", ", ".join(MARKALAR) + " ve diğer binek araç markaları.", "", "## Sık sorulan sorular"]
    for q,c in SSS: satir += [f"- **{q}** {c}"]
    satir += ["", "## Sayfalar", "- [Ana sayfa](index.html)", "- [Hizmetlerimiz](hizmetler.html)", "- [Markalar](markalar.html)", "- [Hakkımızda](hakkimizda.html)", "- [İletişim](iletisim.html)"]
    (KOK / "llms.txt").write_text("\n".join(satir) + "\n", encoding="utf-8")
    (KOK / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")

if __name__ == "__main__":
    import ek_sayfalar
    ek_sayfalar.calistir()
