"""Teknik rehber makaleleri (4/4): müşteri rehberleri."""

MAKALELER_4 = [
dict(slug="garantili-arac-ozel-serviste-bakim", grup="Bakım ve muayene", hizmet="periyodik-bakim",
 baslik="Garantili araç özel serviste bakım yaptırabilir mi?",
 meta="Garantisi süren aracın bakımı özel serviste yapılırsa garanti bozulur mu? Rekabet düzenlemeleri, dikkat edilecek şartlar ve saklanacak belgeler.",
 ozet="Türkiye'de rekabet düzenlemeleri, garanti süresindeki araçların bakımının yalnızca yetkili serviste yapılması şartını sınırlar. Bakım üreticinin talimatlarına uygun yapılır, uygun kalitede parça kullanılır ve belgelenirse özel serviste yapılan bakım tek başına garantiyi geçersiz kılmaz. Yine de kesin şartlar için aracınızın garanti kitapçığına bakmanız gerekir.",
 bolumler=[
  ("Rekabet düzenlemeleri ne diyor?", [
   "Rekabet Kurumu'nun motorlu taşıtların dağıtım ve servis hizmetlerine ilişkin düzenlemeleri, üreticilerin garantiyi yalnızca yetkili serviste bakım yapılması şartına bağlamasını sınırlar. Bu, araç sahibine bakımını yetkili servis dışındaki bir serviste yaptırma serbestliği tanır.",
   "Ancak bu serbestlik koşulsuz değildir: üretici, kendi talimatlarına aykırı yapılan ya da uygun olmayan parçayla yapılan bir işlemden kaynaklanan arızayı garanti kapsamı dışında tutabilir."]),
  ("Dikkat edilmesi gerekenler", [
   {"liste": ["Bakım, üreticinin bakım planındaki kilometre ya da süreye uygun yapılmalı.",
              "Üreticinin istediği yağ sınıfı ve onayı kullanılmalı.",
              "Orijinal ya da orijinal kalitesinde (eşdeğer) parça kullanılmalı.",
              "Yapılan işler ve kullanılan parçalar faturada ayrıntılı yazmalı.",
              "Garanti kapsamındaki bir arıza (örneğin üretim hatası) için yetkili servise başvurulmalı; bu onarımlar ücretsizdir."]}]),
  ("Hangi belgeleri saklamalısınız?", [
   {"liste": ["Her bakımın tarihini, kilometresini ve yapılan işleri gösteren fatura",
              "Kullanılan parçaların marka ve parça numaraları",
              "Kullanılan yağın marka, viskozite ve onay bilgisi"]},
   "Bu belgeler, ileride bir garanti talebinde bakımın düzenli ve doğru yapıldığını göstermenin en kolay yoludur."]),
 ],
 sss=[("Özel serviste bakım yaptırdım, garantim bitti mi?", "Hayır, bakım üretici talimatlarına uygun yapıldı ve belgelendiyse garanti tek başına bu nedenle sona ermez. Kesin koşullar için garanti kitapçığınızı kontrol edin."),
      ("Garanti kapsamındaki arızayı özel servis onarabilir mi?", "Garanti kapsamındaki arızaların ücretsiz onarımı üreticinin yetkili servisleri tarafından yapılır. Bu tür bir arızada önce yetkili servise başvurmanız gerekir.")]),

dict(slug="orijinal-esdeger-muadil-parca", grup="Bakım ve muayene", hizmet="yedek-parca",
 baslik="Orijinal, eşdeğer ve muadil yedek parça farkı",
 meta="Orijinal (OEM), eşdeğer ve muadil yedek parça arasındaki farklar nelerdir? Hangi parçada hangisi tercih edilmeli, sahte parça nasıl anlaşılır?",
 ozet="Orijinal parça, aracın üreticisinin logosuyla satılan parçadır. Eşdeğer (OEM kalitesinde) parça, çoğu zaman aynı üreticinin ya da aynı standartlarda üretim yapan bir firmanın kendi markasıyla sattığı parçadır. Muadil parça ise farklı üreticilerin uyumlu ürünleridir; kalitesi markaya göre geniş bir aralıkta değişir.",
 bolumler=[
  ("Parça türleri", [
   {"tablo": (["Tür", "Ne demek?", "Avantaj", "Dikkat"], [
     ["Orijinal", "Araç üreticisinin ambalajı ve logosuyla satılan parça", "Birebir uyum, güvence", "En yüksek fiyat"],
     ["Eşdeğer (OEM kalitesinde)", "Üreticiye parça üreten firmanın kendi markasıyla sattığı parça", "Orijinale yakın kalite, daha uygun fiyat", "Doğru parça numarasıyla eşleştirilmeli"],
     ["Muadil", "Farklı üreticilerin uyumlu ürünü", "En ekonomik seçenek", "Kalite markaya göre çok değişir"]])}]),
  ("Hangi parçada ne tercih edilmeli?", [
   {"liste": ["<b>Güvenlik parçaları</b> (fren balatası, disk, rot, rotil, amortisör): orijinal ya da bilinen eşdeğer markalar.",
              "<b>Motor iç ve triger parçaları</b>: orijinal ya da eşdeğer; ucuz parça büyük hasara yol açabilir.",
              "<b>Sarf parçaları</b> (filtre, silecek, ampul): kaliteli eşdeğer ya da muadil ürünler yeterli olabilir.",
              "<b>Kaporta parçaları</b>: uyum ve kaplama kalitesi önemlidir; ucuz muadillerde boşluk ve renk farkı çıkabilir."]}]),
  ("Doğru parça nasıl seçilir?", [
   "Aynı model aracın farklı üretim yıllarında ya da motor seçeneklerinde farklı parçalar kullanılabilir. Bu yüzden parça, ruhsattaki şasi numarasıyla eşleştirilmelidir. Sahte ürün riskine karşı parçanın güvenilir tedarikçiden alınması, ambalajının ve etiketinin kontrol edilmesi gerekir."]),
 ],
 sss=[("Muadil parça garantiyi bozar mı?", "Garanti süresindeki araçlarda üreticinin istediği kaliteye uygun parça kullanılması gerekir. Bu araçlarda orijinal ya da eşdeğer parça tercih edilmelidir."),
      ("Hangi parçanın takıldığını nasıl bilirim?", "Faturada parçanın markası ve türü yazmalıdır. Değişen eski parçaları ve yeni parçanın ambalajını görmek isteyebilirsiniz.")]),

dict(slug="guvenilir-oto-servis-secimi", grup="Bakım ve muayene", hizmet="ucretsiz-on-kontrol",
 baslik="Güvenilir oto servis nasıl seçilir? 8 işaret",
 meta="Aracınızı hangi servise bırakmalısınız? Güvenilir servisin işaretleri: önceden fiyat, değişen parçayı göstermek, fatura, garanti ve doğru teşhis.",
 ozet="Güvenilir bir servis, ne yapılacağını ve tutarını işe başlamadan söyler, onayınızı almadan işe başlamaz, değişen parçaları gösterir, fatura ve işçilik garantisi verir. Arızayı tahminle değil, ölçüm ve kontrolle bulur.",
 bolumler=[
  ("Güvenilir servisin işaretleri", [
   {"liste": ["<b>Fiyatı önceden söyler:</b> Kontrolden sonra yapılacak işleri ve tutarı işe başlamadan bildirir.",
              "<b>Onay almadan işe başlamaz:</b> Onarım sırasında ek bir iş çıkarsa önce sizi arar.",
              "<b>Önce teşhis koyar:</b> Parça değiştirerek arıza aramaz; cihazla ve ölçümle sorunu bulur.",
              "<b>Değişen parçayı gösterir:</b> Eski parçayı ve yenisinin ambalajını görmek isteyebilirsiniz.",
              "<b>Fatura verir:</b> Yapılan işler ve parçalar faturada ayrıntılı yazar.",
              "<b>İşçiliğine garanti verir:</b> Yaptığı işin arkasında durur.",
              "<b>Parça seçeneğini size bırakır:</b> Orijinal ve muadil seçenekleri fiyatlarıyla anlatır.",
              "<b>Geçmişi ve yorumları vardır:</b> Uzun süredir aynı müşterilere hizmet veren servisler güven kazanmıştır."]}]),
  ("Servise giderken siz ne yapabilirsiniz?", [
   {"liste": ["Sorunu ne zaman, hangi koşulda yaşadığınızı not edin: soğukken mi, virajda mı, belli bir hızda mı?",
              "Varsa önceki bakım faturalarını götürün.",
              "Fiyatı ve yapılacak işleri yazılı ya da mesajla isteyin.",
              "İş bitince aracı teslim alırken yapılan işleri ve değişen parçaları sorun."]}]),
 ],
 sss=[("Ucuz servis her zaman kötü müdür?", "Hayır. Önemli olan fiyatın neden o kadar olduğunu açıkça anlatması, hangi parçanın kullanılacağını söylemesi ve yaptığı işin arkasında durmasıdır."),
      ("Arıza tespit ücretli mi olmalı?", "Servise göre değişir. Biz aracınızın genel durumunu ücretsiz ön kontrolle değerlendiriyor, yapılacak işleri ve tutarını önceden söylüyoruz.")]),

dict(slug="kasko-hasar-onarim-sureci", grup="Bakım ve muayene", hizmet="hasar-onarimi",
 baslik="Kaza sonrası hasar onarım süreci: kasko ve trafik sigortası",
 meta="Kaza yaptıktan sonra ne yapmalı? Kaza tespit tutanağı, sigortaya ihbar, eksper incelemesi, kasko ile trafik sigortası farkı ve hasar onarım süreci adım adım.",
 ozet="Kazadan sonra önce güvenliği sağlayın, ardından kaza tespit tutanağını doldurun ya da gerekiyorsa polisi çağırın ve sigortanıza en kısa sürede ihbarda bulunun. Sigorta şirketinin eksperi hasarı inceler; onarım, eksperin onayladığı kapsamda yapılır.",
 bolumler=[
  ("Kaza anında", [
   {"liste": ["Yaralı varsa 112'yi arayın; önce güvenliği sağlayın.",
              "Yaralanma yoksa ve taraflar anlaşıyorsa kaza tespit tutanağını birlikte doldurun; anlaşma yoksa polisi çağırın.",
              "Kazanın, araçların konumunun ve hasarların fotoğraflarını çekin.",
              "Karşı tarafın ehliyet, ruhsat ve sigorta poliçe bilgilerini alın."]}]),
  ("Kasko mu, trafik sigortası mı?", [
   {"tablo": (["", "Zorunlu trafik sigortası", "Kasko"], [
     ["Kimin hasarını karşılar?", "Kusurlu sürücünün, karşı tarafa verdiği zararı", "Kendi aracınızın hasarını (poliçe kapsamında)"],
     ["Zorunlu mu?", "Evet", "Hayır, isteğe bağlı"],
     ["Kusurlu sizseniz", "Kendi aracınızı karşılamaz", "Kapsam dahilinde karşılar"]])},
   "Karşı taraf kusurluysa aracınızın hasarı onun trafik sigortasından karşılanır. Kusurlu sizseniz kendi aracınızın onarımı için kaskonuz gerekir."]),
  ("Onarım süreci adım adım", [
   {"liste": ["Sigorta şirketine hasar ihbarı yapılır (çoğu zaman acente, çağrı merkezi ya da uygulama üzerinden).",
              "Araç servise getirilir; sigorta şirketi bir eksper görevlendirir.",
              "Eksper hasarı inceler, onarım ve değişecek parçaları belirler.",
              "Onarım, eksperin onayladığı kapsamda yapılır.",
              "Araç teslim edilir; ödeme süreci poliçe şartlarına göre tamamlanır."]},
   "Süreç sigorta şirketine ve poliçeye göre değişebilir. Bu aşamalarda evrak ve iletişim konusunda size yol gösteriyoruz."]),
 ],
 sss=[("Küçük bir hasar için sigortayı kullanmalı mıyım?", "Kasko kullanımı bir sonraki yılın prim indirimini etkileyebilir. Küçük hasarlarda onarım tutarını öğrenip poliçe şartlarıyla karşılaştırmak mantıklıdır."),
      ("Eksper gelmeden onarıma başlanır mı?", "Hayır. Sigorta kapsamında yapılacak onarımlarda eksper incelemesi ve onayı beklenmelidir.")]),
]
