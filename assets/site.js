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

/* 10 Kasım anma ekranı: yalnızca 10 Kasım günü (İstanbul saatiyle), her ziyaretçiye bir kez */
(function(){
  try {
    var p = new Intl.DateTimeFormat("en-CA",{timeZone:"Europe/Istanbul",year:"numeric",month:"2-digit",day:"2-digit"}).format(new Date());
    if (p.slice(5) !== "11-10") return;
    var anahtar = "anma-10kasim-" + p.slice(0,4);
    try { if (localStorage.getItem(anahtar)) return; } catch(e){}
    var d = document.createElement("div");
    d.className = "anma"; d.setAttribute("role","dialog"); d.setAttribute("aria-modal","true"); d.setAttribute("aria-label","10 Kasım Atatürk'ü anma");
    d.innerHTML = '<div class="anma-ic"><img class="anma-gorsel" src="assets/img/10-kasim.jpg" alt="10 Kasım: Cumhuriyetimizin kurucusu Gazi Mustafa Kemal Atatürk\'ü sevgi, saygı ve özlemle anıyoruz." width="724" height="1024">'
      + '<div class="anma-alt"><img src="assets/logo/logo-yatay-acik.svg" alt="Çelikel Oto Servis" height="34"><button type="button" class="anma-kapat">Siteye geç</button></div></div>';
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
