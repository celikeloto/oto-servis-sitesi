// Ayarlar: saatleri veya numarayı değiştirmek için burayı düzenleyin
var AYAR = { acilis: 8, kapanis: 19, kapaliGunler: [0] /* 0 = Pazar */, wa: "905421401974" };

(function(){
  var yil = document.getElementById("yil");
  if (yil) yil.textContent = new Date().getFullYear();

  // Mobil menü
  var dugme = document.querySelector(".menu-dugme"), nav = document.getElementById("ana-menu");
  if (dugme && nav) dugme.addEventListener("click", function(){
    var acik = nav.classList.toggle("acik");
    dugme.setAttribute("aria-expanded", acik ? "true" : "false");
    dugme.setAttribute("aria-label", acik ? "Menüyü kapat" : "Menüyü aç");
  });
  // Açılır menü (dokunmatik ve klavye)
  document.querySelectorAll(".acilir > button").forEach(function(b){
    b.addEventListener("click", function(){
      var li = b.parentElement, acik = li.classList.toggle("acik");
      b.setAttribute("aria-expanded", acik ? "true" : "false");
    });
  });
  document.addEventListener("keydown", function(e){
    if (e.key !== "Escape") return;
    document.querySelectorAll(".acilir.acik").forEach(function(li){ li.classList.remove("acik"); li.querySelector("button").setAttribute("aria-expanded","false"); });
  });

  // Şu an açık mı? (Türkiye saatine göre)
  var el = document.getElementById("durum");
  if (el) try{
    var yazi = el.querySelector("span");
    var p = new Intl.DateTimeFormat("en-GB",{timeZone:"Europe/Istanbul",weekday:"short",hour:"2-digit",minute:"2-digit",hour12:false}).formatToParts(new Date());
    var g = {}; p.forEach(function(x){ g[x.type]=x.value; });
    var gunler = {Sun:0,Mon:1,Tue:2,Wed:3,Thu:4,Fri:5,Sat:6};
    var saat = parseInt(g.hour,10) % 24 + parseInt(g.minute,10)/60, bugun = gunler[g.weekday];
    var acik = AYAR.kapaliGunler.indexOf(bugun) === -1 && saat >= AYAR.acilis && saat < AYAR.kapanis, sonraki;
    if (saat < AYAR.acilis && AYAR.kapaliGunler.indexOf(bugun) === -1) sonraki = "bugün 08:00'de";
    else { var d = (bugun + 1) % 7; while (AYAR.kapaliGunler.indexOf(d) !== -1) d = (d + 1) % 7;
      sonraki = (d === (bugun + 1) % 7 ? "yarın" : ["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"][d]) + " 08:00'de"; }
    el.classList.add(acik ? "acik" : "kapali");
    yazi.textContent = acik ? "Şu an açığız, 19:00'a kadar" : "Şu an kapalıyız, " + sonraki + " açılıyoruz";
  }catch(e){}

  // Form → WhatsApp mesajı
  var form = document.getElementById("form");
  if (form){
    var etiket = document.getElementById("aciklama-etiket"), aciklama = document.getElementById("aciklama"), hata = document.getElementById("hata");
    form.addEventListener("change", function(e){
      if (e.target.name !== "tur") return;
      if (e.target.value === "randevu"){ etiket.textContent = "Sorun ne, ne zaman gelmek istersiniz?"; aciklama.placeholder = "Örn. Frenden ses geliyor, cumartesi sabah uygun"; }
      else { etiket.textContent = "Hangi parça lazım?"; aciklama.placeholder = "Örn. Ön balata ve disk"; }
    });
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var tur = form.tur.value, arac = form.arac.value.trim(), ack = aciklama.value.trim();
      if (!arac || !ack){ hata.classList.add("goster"); (arac ? aciklama : form.arac).focus(); return; }
      hata.classList.remove("goster");
      var mesaj = (tur === "randevu" ? "Merhaba, servis randevusu almak istiyorum." : "Merhaba, parça fiyatı sormak istiyorum.")
        + "\nAraç: " + arac + "\n" + (tur === "randevu" ? "Sorun / gün: " : "Parça: ") + ack;
      window.open("https://wa.me/" + AYAR.wa + "?text=" + encodeURIComponent(mesaj), "_blank", "noopener");
    });
  }
})();

// Yukarı çık düğmesi
(function(){
  var b = document.querySelector(".yukari"); if (!b) return;
  var guncelle = function(){ b.classList.toggle("goster", window.scrollY > 600); };
  window.addEventListener("scroll", guncelle, {passive:true}); guncelle();
  b.addEventListener("click", function(){
    var azHareket = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({top:0, behavior: azHareket ? "auto" : "smooth"});
  });
})();

// Hareket azaltma tercihi olanlarda arka plan videosunu durdur
(function(){
  var v = document.querySelector(".giris-video"); if (!v) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches){ v.removeAttribute("autoplay"); v.pause(); }
})();

/* Bugünün tarihi (İstanbul saatiyle, YYYY-AA-GG). Önizleme için adrese ?gun=2026-12-10 eklenebilir. */
function bugunIstanbul(){
  var m = /[?&]gun=(\d{4}-\d{2}-\d{2})/.exec(location.search); if (m) return m[1];
  return new Intl.DateTimeFormat("en-CA",{timeZone:"Europe/Istanbul",year:"numeric",month:"2-digit",day:"2-digit"}).format(new Date());
}

/* 10 Kasım anma ekranı: yalnızca 10 Kasım günü (İstanbul saatiyle), her ziyaretçiye bir kez */
(function(){
  try {
    var p = bugunIstanbul();
    if (p.slice(5) !== "11-10") return;
    var anahtar = "anma-10kasim-" + p.slice(0,4);
    try { if (localStorage.getItem(anahtar)) return; } catch(e){}
    var d = document.createElement("div");
    d.className = "anma"; d.setAttribute("role","dialog"); d.setAttribute("aria-modal","true"); d.setAttribute("aria-label","10 Kasım Atatürk'ü anma");
    d.innerHTML = '<div class="anma-ic"><img class="anma-gorsel" src="assets/img/10-kasim.jpg" alt="10 Kasım: Cumhuriyetimizin kurucusu Gazi Mustafa Kemal Atatürk\'ü sevgi, saygı ve özlemle anıyoruz." width="724" height="1024">'
      + '<div class="anma-alt"><img src="assets/logo/logo-yatay-acik.png?v=2" alt="Çelikel Oto Servis" height="34"><button type="button" class="anma-kapat">Siteye geç</button></div></div>';
    function kapat(){ d.remove(); document.documentElement.style.overflow=""; document.removeEventListener("keydown", tus); }
    function tus(e){ if (e.key === "Escape") kapat(); }
    d.addEventListener("click", function(e){ if (e.target === d || e.target.classList.contains("anma-kapat")) kapat(); });
    document.addEventListener("keydown", tus);
    document.documentElement.style.overflow = "hidden";
    document.body.appendChild(d);
    d.querySelector(".anma-kapat").focus();
    try { localStorage.setItem(anahtar, "1"); } catch(e){}
  } catch(e){}
})();

/* Önemli günler şeridi: resmî bayramlar, anma günleri, kandiller ve dinî bayramlar.
   Dinî günler her yıl değişir; tarihler Diyanet İşleri Başkanlığı dinî günler takviminden alınmıştır.
   Yeni yılın tarihleri DINI listesine eklenmelidir (son eklenen: 2027 sonu). */
(function(){
  try {
    var bugun = bugunIstanbul(), yil = +bugun.slice(0,4), ag = bugun.slice(5);
    var YOL = '<a href="tel:+905380648205">0538 064 82 05</a>';
    var RESMI = {
      "01-01": ["resmi", "Yeni yılınız kutlu olsun! Sağlıklı, huzurlu ve bol kazasız bir yıl dileriz."],
      "03-18": ["anma",  "18 Mart Çanakkale Zaferi'nin yıl dönümünde aziz şehitlerimizi rahmet ve minnetle anıyoruz."],
      "04-23": ["resmi", "23 Nisan Ulusal Egemenlik ve Çocuk Bayramımız kutlu olsun!"],
      "05-01": ["resmi", "1 Mayıs Emek ve Dayanışma Günü kutlu olsun."],
      "05-19": ["resmi", "19 Mayıs Atatürk'ü Anma, Gençlik ve Spor Bayramımız kutlu olsun!"],
      "07-15": ["anma",  "15 Temmuz Demokrasi ve Millî Birlik Günü'nde şehitlerimizi rahmetle anıyoruz."],
      "08-30": ["resmi", "30 Ağustos Zafer Bayramımız kutlu olsun!"],
      "10-29": ["resmi", "Cumhuriyetimizin " + (yil - 1923) + ". yılı kutlu olsun! 29 Ekim Cumhuriyet Bayramımız kutlu olsun."],
      "11-10": ["anma",  "Cumhuriyetimizin kurucusu Gazi Mustafa Kemal Atatürk'ü sevgi, saygı ve özlemle anıyoruz."]
    };
    var RB = "Ramazan Bayramınız mübarek olsun! 7/24 yol yardım hattımız bayramda da açık: " + YOL;
    var KB = "Kurban Bayramınız mübarek olsun! 7/24 yol yardım hattımız bayramda da açık: " + YOL;
    var DINI = {
      "2026-12-10": "Regaip Kandiliniz mübarek olsun. Üç ayların hayırlara vesile olmasını dileriz.",
      "2027-01-04": "Miraç Kandiliniz mübarek olsun.",
      "2027-01-22": "Berat Kandiliniz mübarek olsun.",
      "2027-02-08": "Hayırlı Ramazanlar! Ramazan ayının bereketli geçmesini dileriz.",
      "2027-03-05": "Kadir Geceniz mübarek olsun.",
      "2027-03-08": RB, "2027-03-09": RB, "2027-03-10": RB, "2027-03-11": RB,
      "2027-05-15": KB, "2027-05-16": KB, "2027-05-17": KB, "2027-05-18": KB, "2027-05-19": KB,
      "2027-08-13": "Mevlid Kandiliniz mübarek olsun.",
      "2027-11-29": "Üç aylar başladı. Hayırlara vesile olmasını dileriz.",
      "2027-12-02": "Regaip Kandiliniz mübarek olsun.",
      "2027-12-24": "Miraç Kandiliniz mübarek olsun."
    };
    var mesajlar = [], tur = null;
    if (DINI[bugun]) { mesajlar.push(DINI[bugun]); tur = "dini"; }
    if (RESMI[ag]) { mesajlar.push(RESMI[ag][1]); tur = tur || RESMI[ag][0]; if (RESMI[ag][0] === "anma") tur = "anma"; }
    if (!mesajlar.length) return;
    var anahtar = "gun-serit-" + bugun;
    try { if (localStorage.getItem(anahtar)) return; } catch(e){}
    var ay = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M14.5 3.2A9 9 0 1 0 20.8 15 7.2 7.2 0 0 1 14.5 3.2Z"/></svg>';
    var bayrak = '<svg viewBox="0 0 30 20" width="30" height="20" aria-hidden="true"><rect width="30" height="20" rx="2" fill="#e30a17"/><circle cx="11" cy="10" r="5" fill="#fff"/><circle cx="12.3" cy="10" r="4" fill="#e30a17"/><path fill="#fff" d="m17.6 10 4.6 1.5-2.9-3.9v4.8l2.9-3.9z"/></svg>';
    var s = document.createElement("div");
    s.className = "gun-serit gun-" + tur; s.setAttribute("role", "region"); s.setAttribute("aria-label", "Özel gün mesajı");
    s.innerHTML = '<div class="kap"><span class="gun-ikon">' + (tur === "dini" ? ay : bayrak) + '</span><p>'
      + mesajlar.join(' <span aria-hidden="true">·</span> ') + ' <span class="gun-imza">Çelikel Oto Servis</span></p>'
      + '<button type="button" class="gun-kapat" aria-label="Mesajı kapat">&times;</button></div>';
    s.querySelector(".gun-kapat").addEventListener("click", function(){ s.remove(); try { localStorage.setItem(anahtar, "1"); } catch(e){} });
    document.body.insertBefore(s, document.body.firstChild);
  } catch(e){}
})();
