"""Rehber ve bölge sayfaları, site haritası. Tüm siteyi üretmek için: python3 _kaynak/olustur.py"""
import re
import olustur as O
from olustur import (HIZMETLER, ANA_HIZMETLER, MARKALAR, TEL, TEL_YAZI, YOL, YOL_YAZI, ADRES1, ADRES2, HARITA,
                     SITE_URL, TARIH, TARIH_YAZI, TEL_I, WA_I, TIK_I, CEKICI_I2, KOK,
                     wa, sayfa, sayfa_bas, cagri, harita_bolum, hizmet_kartlari, bas_orta, kirinti_ld)
from rehber1 import MAKALELER_1
from rehber2 import MAKALELER_2
from rehber3 import MAKALELER_3
from bolgeler import KUCUKCEKMECE_MAHALLELER, ILCELER

from rehber4 import MAKALELER_4
MAKALE_GORSEL = {"yolda-kalinca-ne-yapmali":"yol-yardim-lastik","lastik-rehberi":"lastik-balans","kasko-hasar-onarim-sureci":"hasar-onarimi","aku-sarj-sistemi":"aku-takviye","arac-muayenesi-hazirlik":"muayene-oncesi","guvenilir-oto-servis-secimi":"on-kontrol"}
MAKALELER = MAKALELER_1 + MAKALELER_2 + MAKALELER_3 + MAKALELER_4
REHBER_GRUPLAR = ["Motor", "Aktarma organları", "Fren, süspansiyon ve direksiyon", "Elektrik ve konfor", "Bakım ve muayene"]
NAV_OK = '<span aria-hidden="true">›</span>'
def mah_ad(m): return m if m.endswith("Mahalle") else m + " Mahallesi"

def sss_html(liste): return "".join(f"<details><summary>{q}</summary><p>{c}</p></details>" for q, c in liste)
def sss_ld(liste): return {"@context": "https://schema.org", "@type": "FAQPage",
                           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": c}} for q, c in liste]}

# ---------------- REHBER ----------------
def blok_html(b):
    if isinstance(b, str): return f"<p>{b}</p>"
    if "liste" in b: return "<ul>" + "".join(f"<li>{x}</li>" for x in b["liste"]) + "</ul>"
    if "tablo" in b:
        bas, satirlar = b["tablo"]
        th = "".join(f'<th scope="col">{x}</th>' for x in bas)
        tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in satirlar)
        return f'<div class="tablo-sar"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
    return ""

def kelime_say(m):
    parca = [m["ozet"]]
    for _, bl in m["bolumler"]:
        for x in bl:
            if isinstance(x, str): parca.append(x)
            elif "liste" in x: parca += x["liste"]
            elif "tablo" in x: parca += [" ".join(r) for r in x["tablo"][1]]
    return len(re.sub("<[^>]+>", " ", " ".join(parca)).split())

def hizmet_bul(slug): return next(h for h in HIZMETLER if h["slug"] == slug)

def rehber_sayfasi(m):
    kisa_ad = m["baslik"].split(":")[0].split("?")[0]
    yol = [("Ana sayfa", "index.html"), ("Rehber", "rehber.html"), (kisa_ad, None)]
    dk = max(2, round(kelime_say(m) / 180))
    ids = [f"b{i}" for i in range(len(m["bolumler"]))]
    toc = "".join(f'<li><a href="#{i}">{h}</a></li>' for i, (h, _) in zip(ids, m["bolumler"]))
    bolumler = "".join(f'<section id="{i}"><h2>{h}</h2>{"".join(blok_html(x) for x in bl)}</section>' for i, (h, bl) in zip(ids, m["bolumler"]))
    hz = hizmet_bul(m["hizmet"])
    ilgili = [x for x in MAKALELER if x["grup"] == m["grup"] and x is not m][:4]
    il = "".join(f'<li><a href="rehber-{x["slug"]}.html">{x["baslik"].split(":")[0]} {NAV_OK}</a></li>' for x in ilgili)
    govde = f"""{sayfa_bas(yol, m["baslik"], m["meta"], eylem=False)}
<section class="makale"><div class="kap">
  <article class="metin makale-govde">
    <p class="makale-bilgi">{m["grup"]} · {dk} dakikalık okuma · Güncelleme: <time datetime="{TARIH}">{TARIH_YAZI}</time></p>
    {O.gorsel(MAKALE_GORSEL[m["slug"]], True) if m["slug"] in MAKALE_GORSEL else ""}
    <div class="kisaca"><b>Kısaca</b><p>{m["ozet"]}</p></div>
    <nav class="icindekiler" aria-label="İçindekiler"><b>İçindekiler</b><ol>{toc}<li><a href="#sss">Sık sorulan sorular</a></li></ol></nav>
    {bolumler}
    <section id="sss" class="sss makale-sss"><h2>Sık sorulan sorular</h2>{sss_html(m["sss"])}</section>
    <p class="uyari-not">Bu yazı genel bilgi amaçlıdır. Bakım aralıkları ve teknik değerler araca göre değişir; kesin bilgi için aracınızın kullanım kılavuzuna bakın ya da bize danışın.</p>
  </article>
  <aside class="yan-kutu">
    <div class="kutu"><h2>{hz["ad"]}</h2><p>{hz["kisa"]}</p>
      <a class="btn btn-sari" href="tel:{TEL}">{TEL_I} {TEL_YAZI}</a>
      <a class="btn btn-wa" href="{wa("Merhaba, " + hz["ad"].lower() + " hakkında bilgi almak istiyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a>
      <p class="yan-acil">Yolda mı kaldınız? <a href="tel:{YOL}">{YOL_YAZI}</a></p></div>
    <div class="liste-kutu"><h3>İlgili rehberler</h3><ul>{il}<li><a href="rehber.html">Tüm rehber {NAV_OK}</a></li></ul></div>
    <div class="liste-kutu"><h3>İlgili hizmet</h3><ul><li><a href="hizmet-{hz["slug"]}.html">{hz["ad"]} {NAV_OK}</a></li></ul></div>
  </aside>
</div></section>
{cagri()}"""
    url = SITE_URL + f'rehber-{m["slug"]}.html'
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": m["baslik"], "description": m["meta"],
           "datePublished": TARIH, "dateModified": TARIH, "inLanguage": "tr-TR", "mainEntityOfPage": url,
           "author": {"@type": "Organization", "name": "Çelikel Oto Servis", "url": SITE_URL},
           "publisher": {"@type": "Organization", "name": "Çelikel Oto Servis",
                         "logo": {"@type": "ImageObject", "url": SITE_URL + "assets/logo/logo-yatay.svg"}}},
          sss_ld(m["sss"]), kirinti_ld(yol)]
    ek = " | Çelikel Oto Servis"
    if len(m["baslik"]) + len(ek) <= 62: title = m["baslik"] + ek
    elif len(m["baslik"]) <= 62: title = m["baslik"]
    else: title = kisa_ad + " rehberi" + ek
    sayfa(f'rehber-{m["slug"]}.html', title, m["meta"], govde, "rehber", ld, "article")

def rehber_ana():
    yol = [("Ana sayfa", "index.html"), ("Rehber", None)]
    gruplar = ""
    for g in REHBER_GRUPLAR:
        kartlar = "".join(f'<li><a href="rehber-{m["slug"]}.html"><h3>{m["baslik"]}</h3><p>{m["meta"]}</p><span class="oku">Okuyun</span></a></li>'
                          for m in MAKALELER if m["grup"] == g)
        gruplar += f'<section class="grup-bolum"><div class="kap"><h2 class="grup-baslik">{g}</h2><ul class="rehber-izgara">{kartlar}</ul></div></section>'
    govde = f"""{sayfa_bas(yol, 'Oto tamir ve bakım <span style="color:var(--ikaz)">rehberi</span>',
        f"Aracınızın motorundan frenine, lastiğinden klimasına kadar bütün sistemleri ustamızın 40 yıllık tecrübesiyle sade bir dille anlatıyoruz: {len(MAKALELER)} konu, belirtiler, bakım aralıkları ve sık sorulan sorular.", eylem=False)}
{gruplar}
{cagri()}"""
    ld = [kirinti_ld(yol), {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Oto tamir ve bakım rehberi",
          "hasPart": [{"@type": "Article", "headline": m["baslik"], "url": SITE_URL + f'rehber-{m["slug"]}.html'} for m in MAKALELER]}]
    sayfa("rehber.html", "Oto Tamir ve Bakım Rehberi | Çelikel Oto Servis",
          f"Motor, triger, debriyaj, şanzıman, fren, süspansiyon, lastik, akü, klima ve daha fazlası: {len(MAKALELER)} konuda ders niteliğinde oto tamir ve bakım rehberi.",
          govde, "rehber", ld)

# ---------------- BÖLGELER ----------------
def kucukcekmece_sayfasi():
    dosya = "kucukcekmece-yol-yardim-lastik-tamiri.html"
    yol = [("Ana sayfa", "index.html"), ("Bölgeler", "bolgeler.html"), ("Küçükçekmece yol yardım", None)]
    n = len(KUCUKCEKMECE_MAHALLELER)
    mah = "".join(f"<li><h3>{mah_ad(m)}</h3><p>Lastik tamiri, lastik değişimi ve yol yardım</p></li>" for m in KUCUKCEKMECE_MAHALLELER)
    sss_l = [("Küçükçekmece'nin hangi mahallelerine yol yardım veriyorsunuz?", f"Küçükçekmece'nin {n} mahallesinin tamamına: " + ", ".join(KUCUKCEKMECE_MAHALLELER) + "."),
             ("Lastiğim patladı, ne yapmalıyım?", f"Aracı güvenli bir yere çekin, dörtlüleri yakın ve {YOL_YAZI} numaralı yol yardım hattımızı arayın. Konumunuzu ve aracınızı söyleyin, size ulaşalım."),
             ("Patlak lastik tamir edilir mi?", "Diş bölgesindeki küçük delikler genellikle kalıcı olarak tamir edilir. Yanakta kesik ya da şişlik varsa ya da lastik basınçsız uzun süre sürüldüyse lastiğin değişmesi gerekir."),
             ("Lastik değişiminden sonra balans gerekir mi?", "Evet. Lastik değişiminde ve tamirinden sonra balans ayarı yapılması direksiyonda titremeyi önler.")]
    govde = f"""{sayfa_bas(yol, 'Küçükçekmece yol yardım ve <span style="color:var(--ikaz)">lastik tamiri</span>',
        f"Küçükçekmece'nin {n} mahallesinin tamamına 7/24 yol yardım veriyoruz. Lastiğiniz patladıysa ya da aracınız yolda kaldıysa arayın; lastik tamiri, lastik değişimi ve balans için de servisimizdeyiz.", eylem=False)}
<section class="icerik"><div class="kap">
  <div class="metin">
    {O.gorsel("yol-yardim-lastik", True)}
    <a class="acil-buyuk" href="tel:{YOL}">{CEKICI_I2}<span><small>Yol yardım hattı</small><b>{YOL_YAZI}</b></span></a>
    <h2>Küçükçekmece'de yolda mı kaldınız?</h2>
    <p>Lastik patlaması, aracın çalışmaması ya da yolda kalma durumunda yol yardım hattımızı arayın. Konumunuzu, aracınızın markasını ve modelini, sorunun ne olduğunu söyleyin; Küçükçekmece içinde bulunduğunuz yere ulaşalım. Halkalı, Atakent, Sefaköy, Kanarya ve Cennet gibi semtler de dahil, ilçenin her noktasındayız.</p>
    <h2>Lastik tamiri, değişimi ve balans</h2>
    <ul class="tik">
      <li>{TIK_I}<span>Çivi, vida gibi nedenlerle patlayan ya da hava kaçıran lastiğin tamiri</span></li>
      <li>{TIK_I}<span>Tamir edilemeyecek lastikler için yeni lastik temini ve değişimi</span></li>
      <li>{TIK_I}<span>Lastik söküm, takım ve balans ayarı</span></li>
      <li>{TIK_I}<span>Lastik hava basıncı ve diş derinliği kontrolü</span></li>
    </ul>
    <p>Lastiğin tamir edilip edilemeyeceği hasarın yerine ve büyüklüğüne bağlıdır. Ayrıntılar için <a href="rehber-lastik-rehberi.html">lastik rehberimize</a> ve <a href="rehber-yolda-kalinca-ne-yapmali.html">yolda kalınca ne yapmalı</a> yazımıza bakabilirsiniz.</p>
    <h2>Yol yardım verdiğimiz Küçükçekmece mahalleleri</h2>
    <ul class="mahalle-izgara">{mah}</ul>
    <section class="sss makale-sss" id="sss"><h2>Sık sorulan sorular</h2>{sss_html(sss_l)}</section>
  </div>
  <aside class="yan-kutu">
    <div class="kutu"><h2>7/24 yol yardım</h2><p>Küçükçekmece'nin tamamında, gece gündüz. Konumunuzu söyleyin, size ulaşalım.</p>
      <a class="btn btn-sari" href="tel:{YOL}">{TEL_I} {YOL_YAZI}</a>
      <a class="btn btn-wa" href="{wa("Merhaba, yolda kaldım. Konumum: ")}" target="_blank" rel="noopener">{WA_I} Konum gönder</a></div>
    <div class="liste-kutu"><h3>Servisimiz</h3><ul><li><a href="{HARITA}" target="_blank" rel="noopener">{ADRES1} {NAV_OK}</a></li><li><a href="hizmet-lastik-balans.html">Lastik ve balans {NAV_OK}</a></li><li><a href="hizmetler.html">Tüm hizmetler {NAV_OK}</a></li></ul></div>
  </aside>
</div></section>
{harita_bolum()}"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": "Küçükçekmece yol yardım ve lastik tamiri",
           "serviceType": "Yol yardım, lastik tamiri, lastik değişimi, balans",
           "provider": {"@type": "AutoRepair", "name": "Çelikel Oto Servis", "telephone": YOL},
           "areaServed": [{"@type": "Place", "name": f"{mah_ad(m)}, Küçükçekmece, İstanbul"} for m in KUCUKCEKMECE_MAHALLELER]},
          sss_ld(sss_l), kirinti_ld(yol)]
    sayfa(dosya, "Küçükçekmece Yol Yardım ve Lastik Tamiri | Çelikel Oto Servis",
          f"Küçükçekmece'nin {n} mahallesine yol yardım, lastik tamiri, değişimi ve balans. Halkalı, Atakent, Cennet, Kanarya, Sefaköy dahil. Hat: {YOL_YAZI}",
          govde, "bolge", ld)

def ilce_sayfasi(i):
    dosya = f'{i["slug"]}-oto-servis.html'
    yol = [("Ana sayfa", "index.html"), ("Bölgeler", "bolgeler.html"), (i["ad"], None)]
    h, paras = i["ozel"]
    diger = '<li><a href="kucukcekmece-yol-yardim-lastik-tamiri.html">Küçükçekmece yol yardım ' + NAV_OK + "</a></li>" + "".join(
        f'<li><a href="{x["slug"]}-oto-servis.html"' + (' aria-current="page"' if x is i else "") + f'>{x["ad"]} {NAV_OK}</a></li>' for x in ILCELER)
    govde = f"""{sayfa_bas(yol, i["baslik"], i["giris"])}
<section class="icerik"><div class="kap">
  <div class="metin">
    <h2>{h}</h2>{"".join(f"<p>{x}</p>" for x in paras)}
    <h2>{i["ad"]} {"içinden" if i["km"] is None else "ilçesinden"} bize ulaşmak</h2>
    <p>Servisimiz {ADRES1}, {ADRES2} adresinde{"; " + i["ad"] + " ilçe merkezine kuş uçuşu yaklaşık " + str(i["km"]) + " km uzaklıkta" if i["km"] else ""}. Pazartesiden cumartesiye 08:00–19:00 arası açığız. Gelmeden önce arayın, aracınız için yer ayıralım; gelemiyorsanız aracınızı adresinizden alalım.</p>
    <h2>Neden Çelikel Oto Servis?</h2>
    <ul class="tik">
      <li>{TIK_I}<span>40 yıllık tecrübeli Sebahattin Usta aracınızla birebir ilgilenir</span></li>
      <li>{TIK_I}<span>Ne yapılacağını ve tutarını işe başlamadan söyleriz</span></li>
      <li>{TIK_I}<span>Arıza tespit cihazıyla teşhis; gereksiz parça değiştirmeyiz</span></li>
      <li>{TIK_I}<span>Orijinal ve muadil yedek parçayı biz temin ederiz</span></li>
    </ul>
    <section class="sss makale-sss"><h2>Sık sorulan sorular</h2>{sss_html(i["sss"])}</section>
  </div>
  <aside class="yan-kutu">
    <div class="kutu"><h2>Randevu ve fiyat</h2><p>Aracınızın marka, model ve yılını yazın, size dönelim.</p>
      <a class="btn btn-sari" href="tel:{TEL}">{TEL_I} {TEL_YAZI}</a>
      <a class="btn btn-wa" href="{wa("Merhaba, " + i["ad"] + " bölgesinden yazıyorum. Aracım için bilgi almak istiyorum.")}" target="_blank" rel="noopener">{WA_I} WhatsApp'tan yaz</a></div>
    <div class="liste-kutu"><h3>Diğer bölgeler</h3><ul>{diger}</ul></div>
  </aside>
</div></section>
<section aria-labelledby="h-ih" style="padding-top:0"><div class="kap">{bas_orta("Hizmetler", i["ad"] + ' için <span class="vurgu">hizmetlerimiz</span>', "Hizmete tıklayın, ayrıntıları görün.", "h-ih")}<ul class="hizmet-izgara">{hizmet_kartlari(ANA_HIZMETLER[:6], one_son=False)}</ul></div></section>
{cagri()}"""
    ld = [{"@context": "https://schema.org", "@type": "Service", "name": i["baslik"],
           "provider": {"@type": "AutoRepair", "name": "Çelikel Oto Servis", "telephone": TEL},
           "areaServed": {"@type": "City", "name": f'{i["ad"]}, İstanbul'}},
          sss_ld(i["sss"]), kirinti_ld(yol)]
    title = i["baslik"][0].upper() + i["baslik"][1:]
    title = " ".join(w if w in ("ve",) else w[:1].upper() + w[1:] for w in title.split())
    t = next((x for x in (f"{title} | Çelikel Oto Servis", f"{title} | Çelikel Oto", title) if len(x) <= 62), title)
    sayfa(dosya, t, i["meta"], govde, "bolge", ld)

def bolgeler_ana():
    yol = [("Ana sayfa", "index.html"), ("Bölgeler", None)]
    kart = f'<li><a href="kucukcekmece-yol-yardim-lastik-tamiri.html"><h3>Küçükçekmece</h3><p>{len(KUCUKCEKMECE_MAHALLELER)} mahallenin tamamına yol yardım, lastik tamiri ve oto servis</p><span class="oku">Ayrıntılar</span></a></li>'
    kart += "".join(f'<li><a href="{i["slug"]}-oto-servis.html"><h3>{i["ad"]}</h3><p>{("Kuş uçuşu yaklaşık " + str(i["km"]) + " km, adresten araç alma") if i["km"] else "Oto servis, bakım, tamir ve 7/24 yol yardım"}</p><span class="oku">Ayrıntılar</span></a></li>' for i in ILCELER)
    govde = f"""{sayfa_bas(yol, 'Hizmet verdiğimiz <span style="color:var(--ikaz)">bölgeler</span>', "Servisimiz Küçükçekmece'nin Yarımburgaz Mahallesi'nde. Küçükçekmece'nin tamamına yol yardım veriyor, çevre ilçelerden gelen müşterilerimizin aracını adresinden alıyoruz.")}
<section><div class="kap"><ul class="rehber-izgara">{kart}</ul></div></section>
{harita_bolum()}"""
    sayfa("bolgeler.html", "Hizmet Bölgelerimiz | Çelikel Oto Servis",
          "Küçükçekmece ve Halkalı oto servis, 21 mahalleye 7/24 yol yardım; Başakşehir, Avcılar, Esenyurt, Beylikdüzü ve Bakırköy'den araç alma.",
          govde, "bolge", kirinti_ld(yol))

def site_haritasi():
    x = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for d in sorted(set(O.URLLER)):
        oncelik = "1.0" if d == "index.html" else ("0.9" if d.startswith(("hizmet", "kucukcekmece")) else "0.7")
        x.append(f'  <url><loc>{SITE_URL}{"" if d == "index.html" else d}</loc><lastmod>{TARIH}</lastmod><priority>{oncelik}</priority></url>')
    x.append("</urlset>")
    (KOK / "sitemap.xml").write_text("\n".join(x) + "\n", encoding="utf-8")
    (KOK / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")

def llms_ek():
    yol = KOK / "llms.txt"
    s = yol.read_text(encoding="utf-8")
    ek = ["", "## Oto tamir ve bakım rehberi"]
    for g in REHBER_GRUPLAR:
        ek.append(f"### {g}")
        ek += [f'- [{m["baslik"]}](rehber-{m["slug"]}.html): {m["ozet"]}' for m in MAKALELER if m["grup"] == g]
    ek += ["", "## Hizmet bölgeleri",
           f"- [Küçükçekmece yol yardım ve lastik tamiri](kucukcekmece-yol-yardim-lastik-tamiri.html): Yol yardım Küçükçekmece'nin tüm mahallelerinde ({', '.join(KUCUKCEKMECE_MAHALLELER)})."]
    ek += [f'- [{i["baslik"]}]({i["slug"]}-oto-servis.html): {i["giris"]}' for i in ILCELER]
    yol.write_text(s + "\n".join(ek) + "\n", encoding="utf-8")

def gizlilik_sayfasi():
    yol = [("Ana sayfa", "index.html"), ("Gizlilik ve KVKK", None)]
    b = [("Genel", ["Bu metin, Çelikel Oto Servis web sitesini ziyaret ettiğinizde kişisel verilerinizin nasıl işlendiğini açıklar. 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamında veri sorumlusu Çelikel Oto Servis'tir."]),
         ("Sitemiz hangi verileri topluyor?", ["Sitemizde üyelik, çerezle takip ya da ziyaretçi istatistiği tutan bir sistem yoktur (ayrıntılar için <a href=\"cerez-politikasi.html\">çerez politikamıza</a> bakabilirsiniz). Sitedeki iletişim formu bilgilerinizi sunucumuza kaydetmez; yazdığınız mesaj yalnızca sizin onayınızla WhatsApp uygulamasında açılır ve gönder tuşuna bastığınızda bize ulaşır."]),
         ("Üçüncü taraf hizmetler", [{"liste": ["<b>Google Haritalar:</b> Konum haritası Google tarafından sunulur.",
              "<b>Google Fonts:</b> Yazı tipleri Google sunucularından yüklenir.",
              "<b>jsDelivr:</b> Marka logoları bu içerik dağıtım ağından yüklenir.",
              "<b>WhatsApp:</b> WhatsApp ile yazdığınızda mesajınız WhatsApp'ın kendi koşullarına tabidir."]},
              "Bu hizmetler, sayfayı görüntülemeniz için tarayıcınızın IP adresi gibi teknik bilgileri kendi gizlilik politikaları çerçevesinde işleyebilir."]),
         ("Servis işlemlerinde işlenen veriler", ["Aracınızı servisimize bıraktığınızda adınız, telefon numaranız ve araç bilgileriniz (plaka, şasi numarası, kilometre) yalnızca servis hizmetinin yürütülmesi, faturalandırma ve yasal yükümlülüklerimiz için işlenir; reklam amacıyla üçüncü kişilerle paylaşılmaz."]),
         ("Haklarınız", ["KVKK'nın 11. maddesi uyarınca kişisel verilerinizin işlenip işlenmediğini öğrenme, düzeltilmesini ya da silinmesini isteme gibi haklara sahipsiniz. Başvurularınız için " + f'<a href="tel:{TEL}">{TEL_YAZI}</a> numarasından ya da servisimize gelerek bize ulaşabilirsiniz.']),
        ]
    ic = "".join(f"<section><h2>{h}</h2>{''.join(blok_html(k) for k in x)}</section>" for h, x in b)
    govde = f"""{O.sayfa_bas(yol, "Gizlilik ve KVKK aydınlatma metni", "Kişisel verilerinizi nasıl işlediğimizi açıklıyoruz.", eylem=False)}
<section class="makale"><div class="kap"><div class="makale-govde" style="max-width:760px">{ic}</div></div></section>"""
    O.sayfa("gizlilik.html", "Gizlilik ve KVKK Aydınlatma Metni | Çelikel Oto Servis",
            "Çelikel Oto Servis web sitesi gizlilik politikası ve KVKK aydınlatma metni: hangi verilerin işlendiği, üçüncü taraf hizmetler ve haklarınız.",
            govde, ek_ld=O.kirinti_ld(yol))

def cerez_sayfasi():
    yol = [("Ana sayfa", "index.html"), ("Çerez politikası", None)]
    b = [("Çerez nedir?", ["Çerezler, ziyaret ettiğiniz web sitelerinin tarayıcınıza kaydettiği küçük metin dosyalarıdır. Benzer şekilde tarayıcının \"yerel depolama\" alanı da sitelerin küçük bilgileri cihazınızda saklamasına izin verir. Bu metin, Çelikel Oto Servis web sitesinde (celikeloto.com) bu teknolojilerin nasıl kullanıldığını açıklar."]),
         ("Sitemizin kendi çerezleri", ["Sitemiz kendi adına <b>hiçbir çerez oluşturmaz</b>. Ziyaretçi sayma, reklam, yeniden hedefleme ya da davranış takibi yapan bir araç (örneğin Google Analytics, Facebook Pikseli) kullanmıyoruz."]),
         ("Yerel depolama", ["Sitemiz tarayıcınızın yerel depolama alanına yalnızca tek bir bilgi kaydeder:",
              {"tablo": (["Ad", "Amaç", "Süre"], [["anma-10kasim-(yıl)", "10 Kasım anma ekranının size aynı gün içinde yalnızca bir kez gösterilmesi", "Siz tarayıcı verilerini silene kadar"]])},
              "Bu bilgi kişisel veri içermez, yalnızca cihazınızda tutulur ve bize gönderilmez."]),
         ("Üçüncü taraf hizmetlerin çerezleri", [
              {"tablo": (["Hizmet", "Nerede kullanılıyor?", "Çerez"], [
                ["Google Haritalar", "İletişim bölümündeki harita", "Harita görüntülendiğinde Google kendi çerezlerini oluşturabilir"],
                ["Google Fonts", "Yazı tipleri", "Çerez oluşturmaz; teknik bağlantı bilgisi (IP adresi) Google'a iletilir"],
                ["jsDelivr", "Marka logoları", "Çerez oluşturmaz; teknik bağlantı bilgisi iletilir"],
                ["WhatsApp", "Mesaj gönderme düğmeleri", "Düğmeye tıkladığınızda WhatsApp'ın kendi koşulları geçerlidir"]])},
              "Bu hizmetlerin çerez ve veri kullanımı, ilgili şirketlerin kendi gizlilik politikalarına tabidir. Google'ın politikasına policies.google.com adresinden ulaşabilirsiniz."]),
         ("Çerezleri nasıl kontrol edebilirsiniz?", ["Tarayıcınızın ayarlarından çerezleri ve yerel depolanan verileri görebilir, silebilir ya da engelleyebilirsiniz:",
              {"liste": ["<b>Chrome:</b> Ayarlar → Gizlilik ve güvenlik → Üçüncü taraf çerezleri",
                         "<b>Safari (iPhone):</b> Ayarlar → Safari → Geçmişi ve Web Sitesi Verilerini Temizle",
                         "<b>Firefox:</b> Ayarlar → Gizlilik ve Güvenlik → Çerezler ve site verileri",
                         "<b>Edge:</b> Ayarlar → Çerezler ve site izinleri"]},
              "Çerezleri engellemeniz sitemizin çalışmasını etkilemez; yalnızca harita görüntülenmeyebilir."]),
         ("Kişisel verileriniz", ['Kişisel verilerinizin nasıl işlendiğine dair ayrıntılar için <a href="gizlilik.html">Gizlilik ve KVKK aydınlatma metnimize</a> bakabilirsiniz. Sorularınız için ' + f'<a href="tel:{TEL}">{TEL_YAZI}</a> numarasından bize ulaşabilirsiniz.']),
        ]
    ic = "".join(f"<section><h2>{h}</h2>{''.join(blok_html(k) for k in x)}</section>" for h, x in b)
    govde = f"""{O.sayfa_bas(yol, "Çerez politikası", "Sitemizde çerez ve yerel depolamanın nasıl kullanıldığını açıklıyoruz.", eylem=False)}
<section class="makale"><div class="kap"><div class="makale-govde" style="max-width:760px">{ic}<p><small>Son güncelleme: 10 Kasım 2026</small></p></div></div></section>"""
    O.sayfa("cerez-politikasi.html", "Çerez Politikası | Çelikel Oto Servis",
            "Çelikel Oto Servis web sitesi çerez politikası: kullanılan çerezler, yerel depolama, üçüncü taraf hizmetler ve çerezleri nasıl kontrol edebileceğiniz.",
            govde, ek_ld=O.kirinti_ld(yol))

def hata_sayfasi():
    govde = f"""<section class="sayfa-bas"><div class="kap"><h1>Aradığınız sayfa bulunamadı</h1>
  <p>Bağlantı değişmiş ya da sayfa kaldırılmış olabilir. Aşağıdaki sayfalardan devam edebilir ya da bizi arayabilirsiniz.</p>
  <div class="eylemler"><a class="btn btn-sari" href="index.html">Ana sayfaya dön</a><a class="btn btn-wa" href="tel:{TEL}">{O.TEL_I} {TEL_YAZI}</a></div>
  <p style="margin-top:24px"><a href="hizmetler.html">Hizmetler</a> · <a href="rehber.html">Oto tamir rehberi</a> · <a href="iletisim.html">İletişim</a> · <a href="tel:{YOL}">7/24 yol yardım: {YOL_YAZI}</a></p></div></section>"""
    O.sayfa("404.html", "Sayfa bulunamadı | Çelikel Oto Servis", "Aradığınız sayfa bulunamadı.", govde)
    O.URLLER.remove("404.html")
    y = KOK / "404.html"; t = y.read_text(encoding="utf-8")
    t = t.replace('<meta charset="utf-8">', f'<meta charset="utf-8">\n<base href="{SITE_URL}">\n<meta name="robots" content="noindex">', 1)
    t = re.sub(r'<link rel="canonical"[^>]*>\n', "", t)
    y.write_text(t, encoding="utf-8")

def calistir():
    O.css(); O.ana(); O.hizmetler_sayfasi(); O.markalar_sayfasi(); O.hakkimizda(); O.iletisim()
    for h in HIZMETLER: O.hizmet_sayfasi(h)
    for m in MARKALAR: O.marka_sayfasi(m)
    rehber_ana(); bolgeler_ana(); kucukcekmece_sayfasi()
    for m in MAKALELER: rehber_sayfasi(m)
    for i in ILCELER: ilce_sayfasi(i)
    gizlilik_sayfasi(); cerez_sayfasi(); hata_sayfasi()
    O.llms(); llms_ek(); site_haritasi()
    print("Sayfalar üretildi:", len(set(O.URLLER)))
