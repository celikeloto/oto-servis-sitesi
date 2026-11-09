"""Bölge sayfaları içeriği. Mesafeler servisimizden ilçe merkezine kuş uçuşu yaklaşık değerlerdir."""

KUCUKCEKMECE_MAHALLELER = ["Atakent", "Atatürk", "Beşyol", "Cennet", "Cumhuriyet", "Fatih", "Fevzi Çakmak",
    "Gültepe", "Halkalı Merkez", "İnönü", "İstasyon", "Kanarya", "Kartaltepe", "Kemalpaşa", "Mehmet Akif",
    "Söğütlü Çeşme", "Sultan Murat", "Tevfikbey", "Yarımburgaz", "Yeni Mahalle", "Yeşilova"]

ILCELER = [
 dict(slug="basaksehir", ad="Başakşehir", km=7,
  baslik="Başakşehir oto servis ve araç bakım",
  meta="Başakşehir'e yakın oto servis: periyodik bakım, arıza tespit, motor, şanzıman, fren, lastik ve yedek parça. Aracınızı adresinizden alıyoruz. Fiyat işe başlamadan.",
  giris="Servisimiz Küçükçekmece'nin Yarımburgaz Mahallesi'nde, Başakşehir sınırına çok yakın. Başakşehir'den bize ulaşmak kısa sürer; vaktiniz yoksa aracınızı adresinizden alıp iş bitince geri getiriyoruz.",
  ozel=("Başakşehir'den gelen sürücüler için", [
   "Başakşehir'de yeni ve genç araçların oranı yüksek. Bu araçlarda en sık ihtiyaç duyulan işler periyodik bakım, arıza tespit ve lastik değişimidir. Garanti süresi devam eden araçlarda bakımın üreticinin istediği yağ ve parça sınıfıyla yapılmasına dikkat ediyoruz; garanti kitapçığınızı getirmeniz yeterli.",
   "Turbolu küçük hacimli benzinli motorlarda yağın zamanında ve doğru sınıfla değişmesi motor ve turbo ömrü için kritik. Bakım geçmişinizi birlikte gözden geçirip eksik kalan işleri söylüyoruz."]),
  sss=[("Başakşehir'den aracımı alabilir misiniz?", "Evet. Aracınızı adresinizden alıyor, işi bitince yine adresinize getiriyoruz. Uygun günü birlikte belirlemek için arayın."),
       ("Başakşehir'e en yakın neredesiniz?", "Servisimiz Yarımburgaz Mahallesi'nde, Başakşehir ilçe merkezine kuş uçuşu yaklaşık 7 km uzaklıkta.")]),
 dict(slug="avcilar", ad="Avcılar", km=8,
  baslik="Avcılar oto servis ve araç bakım",
  meta="Avcılar'a yakın oto tamir ve bakım servisi: motor, şanzıman, fren, süspansiyon, klima, lastik ve yedek parça. Aracınızı adresinizden alıyoruz.",
  giris="Avcılar'a kuş uçuşu yaklaşık 8 km uzaklıktayız. Avcılar'dan gelen müşterilerimiz için bakım, onarım ve parça temini tek serviste; isterseniz aracınızı adresinizden alıyoruz.",
  ozel=("Avcılar'daki araçlar için öneriler", [
   "Avcılar ve çevresinde E-5 trafiğinde sık dur-kalk sürüş yaygın. Bu kullanım şekli üreticilerin 'ağır kullanım' olarak tanımladığı koşullara girer: yağ ve filtre değişimini normal aralığın biraz önünde yapmak, fren balatası ve debriyajı her bakımda kontrol etmek mantıklı olur.",
   "Göl ve deniz kıyısına yakın bölgelerde nem, kaporta altında ve fren disklerinde paslanmayı hızlandırabilir. Kış aylarında aracın altını da yıkatmanızı öneririz."]),
  sss=[("Avcılar'dan aracımı getiremiyorum, ne yapabilirim?", "Bizi arayın; aracınızı adresinizden almak için gün ayarlayalım."),
       ("Avcılar'da yolda kaldım, yol yardım gönderiyor musunuz?", "Yol yardım hattımız Küçükçekmece'nin tamamında hizmet veriyor. Avcılar için durumunuzu ve konumunuzu söyleyin, size en hızlı çözümü birlikte bulalım.")]),
 dict(slug="esenyurt", ad="Esenyurt", km=7,
  baslik="Esenyurt araç bakım ve oto tamir",
  meta="Esenyurt'a yakın araç bakım ve oto tamir servisi: periyodik bakım, triger, debriyaj, fren, lastik ve balans, klima ve yedek parça. Fiyat işe başlamadan.",
  giris="Esenyurt'a kuş uçuşu yaklaşık 7 km uzaklıktayız. Esenyurt'tan araç bakımı ve oto tamiri için bize gelebilir ya da aracınızı adresinizden aldırabilirsiniz. Ne yapılacağını ve tutarını işe başlamadan söylüyoruz.",
  ozel=("Esenyurt'ta yoğun trafik ve aracınız", [
   "Esenyurt'ta günlük kullanımın büyük kısmı kısa mesafe ve yoğun trafikte geçiyor. Bu kullanımda motor yağı daha çabuk yıpranır, debriyaj ve frenler daha hızlı aşınır, dizel araçlarda partikül filtresi (DPF) rejenerasyonu yarım kalabilir.",
   "Önerimiz: yağ değişimini 10.000 km'yi geçirmeden yaptırın, DPF uyarısı yanarsa aracı birkaç kilometre sabit hızla sürün, uyarı sönmüyorsa gecikmeden kontrol ettirin. Detaylar için rehberimizdeki DPF ve periyodik bakım takvimi yazılarına bakabilirsiniz."]),
  sss=[("Esenyurt'tan araç bakım için randevu nasıl alırım?", "Telefonla ya da WhatsApp'tan aracınızın marka, model ve yılını yazmanız yeterli; uygun günü birlikte belirleyelim."),
       ("Esenyurt'tan aracımı alıyor musunuz?", "Evet, aracınızı adresinizden alıp iş bitince geri getiriyoruz.")]),
 dict(slug="beylikduzu", ad="Beylikdüzü", km=12,
  baslik="Beylikdüzü oto servis ve araç bakım",
  meta="Beylikdüzü'ne yakın oto servis: bakım, arıza tespit, motor ve mekanik, şanzıman, egzoz-DPF, lastik ve yedek parça. Aracınızı adresinizden alıyoruz.",
  giris="Beylikdüzü'ne kuş uçuşu yaklaşık 12 km uzaklıktayız. Beylikdüzü'nden bakım ve onarım için bize gelen müşterilerimiz için aracı adresinden alma imkânı sunuyoruz; böylece işinizden ya da evinizden ayrılmanız gerekmez.",
  ozel=("Otoyol ve uzun yol kullananlar için", [
   "Beylikdüzü'nden şehir merkezine ve şehir dışına uzun yol kullanımı yaygın. Uzun yolda en önemli kontroller lastik basıncı ve diş derinliği, fren sistemi, soğutma sıvısı ve motor yağı seviyesidir.",
   "Uzun yola çıkmadan önce kısa bir kontrol, yolda kalma riskini büyük ölçüde azaltır. Bakım takvimi ve lastik rehberimiz bu kontrollerin nasıl yapılacağını anlatıyor."]),
  sss=[("Beylikdüzü'nden aracımı alabilir misiniz?", "Evet. Arayın, bölgenize göre uygun alma ve teslim gününü birlikte ayarlayalım."),
       ("Uzun yol öncesi kontrol yapıyor musunuz?", "Evet. Lastik, fren, sıvı seviyeleri, aydınlatma ve akü kontrolünü yapıp eksikleri size söylüyoruz.")]),
 dict(slug="bakirkoy", ad="Bakırköy", km=13,
  baslik="Bakırköy oto servis ve araç bakım",
  meta="Bakırköy'deki eski müşterilerimizin tercih ettiği oto servis: bakım, onarım, arıza tespit ve yedek parça. Aracınızı adresinizden alıyoruz, fiyat işe başlamadan.",
  giris="Çelikel Oto Servis uzun yıllar Bakırköy'de hizmet verdi. Bakırköy'den birçok müşterimiz, Yarımburgaz'daki yeni yerimize de gelmeye devam ediyor. Bakırköy'e kuş uçuşu yaklaşık 13 km uzaklıktayız; mesafe sorun olmasın diye aracınızı adresinizden alıyoruz.",
  ozel=("Bakırköy'deki müşterilerimize", [
   "Aracınızın bakım geçmişini biliyorsak kaldığımız yerden devam ediyoruz; bilmiyorsak ilk ziyarette genel bir kontrolle aracın durumunu çıkarıyoruz.",
   "Yeni adresimize gelmek yerine aracınızı aldırmak isterseniz arayın; alma ve teslim gününü birlikte planlayalım."]),
  sss=[("Eski Bakırköy dükkânınız kapandı mı?", "Servisimiz Küçükçekmece'nin Yarımburgaz Mahallesi'ne taşındı. Aynı ustamızla, aynı anlayışla hizmet vermeye devam ediyoruz."),
       ("Bakırköy'den aracımı alıyor musunuz?", "Evet, aracınızı adresinizden alıp iş bitince geri getiriyoruz.")]),
]
