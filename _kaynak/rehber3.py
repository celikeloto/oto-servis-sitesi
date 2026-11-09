"""Teknik rehber makaleleri (3/3): elektrik, klima, kaporta, bakım takvimi, muayene, yolda kalma."""

MAKALELER_3 = [
dict(slug="aku-sarj-sistemi", grup="Elektrik ve konfor", hizmet="oto-elektrik",
 baslik="Akü ve şarj sistemi: akü voltajı, şarj dinamosu, marş motoru",
 meta="Akü kaç volt olmalı, ne kadar dayanır? Şarj dinamosu ve marş motoru arızaları, akü bitme nedenleri ve akü takviyesi nasıl yapılır.",
 ozet="12 voltluk bir otomobil aküsü tam doluyken, motor kapalı ve dinlenmişken yaklaşık 12,6 volt gösterir; 12,0 voltun altı boşalmış demektir. Motor çalışırken şarj dinamosu sistemi genellikle 13,8–14,7 volt arasında besler. Aküler kullanıma ve iklime göre çoğunlukla 3–5 yıl dayanır.",
 bolumler=[
  ("Akü voltajı ne anlatır?", [
   {"tablo": (["Ölçüm (motor kapalı, dinlenmiş)", "Durum"], [
     ["12,6 V ve üzeri", "Tam dolu"],
     ["Yaklaşık 12,4 V", "Yaklaşık %75 dolu"],
     ["Yaklaşık 12,2 V", "Yaklaşık yarı dolu"],
     ["12,0 V ve altı", "Boşalmış; şarj ya da test gerekir"]])},
   "Motor çalışırken 13,8–14,7 V arası bir değer şarj sisteminin çalıştığını gösterir. Bu değerin altı şarj dinamosu ya da bağlantı sorununa, belirgin üstü ise regülatör arızasına işaret edebilir."]),
  ("Akü neden biter?", [
   {"liste": ["Akünün yaşlanması; özellikle sıcak yazlardan sonra kışın ilk soğuklarda biter.",
              "Sürekli kısa mesafe kullanım; akü yeterince dolmaz.",
              "Araç kapalıyken akım çeken bir arıza (kaçak akım).",
              "Şarj dinamosunun yetersiz şarj etmesi.",
              "Far, iç aydınlatma ya da müzik sisteminin açık unutulması."]}]),
  ("Marş motoru ve şarj dinamosu belirtileri", [
   {"tablo": (["Belirti", "Olası neden"], [
     ["Marşa basınca tık sesi, motor dönmüyor", "Akü boş, bağlantı gevşek ya da marş motoru"],
     ["Motor yavaş, zorlanarak dönüyor", "Zayıf akü ya da soğuk havada yaşlı akü"],
     ["Sürüş sırasında akü ışığı yanıyor", "Şarj dinamosu ya da V kayışı"],
     ["Farlar rölantide sönükleşiyor", "Şarj sistemi yetersiz"]])}]),
  ("Akü takviyesi nasıl yapılır?", [
   {"liste": ["İki aracın da kontağını kapatın.",
              "Kırmızı kabloyu önce boş akünün artı (+) kutbuna, sonra dolu akünün artı kutbuna bağlayın.",
              "Siyah kabloyu dolu akünün eksi (−) kutbuna, diğer ucunu ise boş aracın motorunda boyasız bir metal noktaya bağlayın.",
              "Yardım eden aracı çalıştırın, birkaç dakika bekleyin, sonra diğer aracı çalıştırın.",
              "Kabloları bağladığınız sıranın tersiyle sökün."]},
   "Akü sık sık bitiyorsa takviye kalıcı çözüm değildir; akü ve şarj sistemi test edilmelidir."]),
 ],
 sss=[("Start-stop özellikli araçlara normal akü takılır mı?", "Hayır. Start-stop sistemli araçlar EFB ya da AGM tipi akü ister. Normal akü bu araçlarda kısa sürede bozulur."),
      ("Akü değişiminden sonra ayar gerekir mi?", "Bazı araçlarda yeni akünün araç beynine tanıtılması gerekir; aksi halde şarj sistemi aküyü doğru şarj etmeyebilir.")]),

dict(slug="ariza-kodlari-obd", grup="Elektrik ve konfor", hizmet="ariza-tespit",
 baslik="Arıza kodları (OBD) nedir? P0300, P0420 gibi kodlar ne anlatır?",
 meta="OBD-II arıza kodları nasıl okunur? P, C, B, U kodlarının anlamı, sık görülen P0300, P0420, P0171 kodları ve arıza tespit cihazının yapabildikleri.",
 ozet="Modern araçlar motor ve diğer sistemlerdeki sorunları arıza kodu olarak hafızaya kaydeder. Bu kodlar OBD soketine bağlanan bir arıza tespit cihazıyla okunur. Kod sorunun nerede olduğunu gösterir ama tek başına hangi parçanın bozuk olduğunu söylemez; kesin teşhis için ölçüm ve kontrol gerekir.",
 bolumler=[
  ("Kod yapısı", [
   "OBD-II kodları bir harf ve dört rakamdan oluşur. Harf, arızanın hangi sistemde olduğunu gösterir:",
   {"tablo": (["Harf", "Sistem"], [
     ["P", "Motor ve şanzıman (powertrain)"],
     ["C", "Şasi: fren, ABS, süspansiyon, direksiyon"],
     ["B", "Gövde: hava yastığı, klima, kapılar, aydınlatma"],
     ["U", "Ağ: modüller arası haberleşme"]])},
   "İlk rakam 0 ise kod tüm üreticilerde ortaktır; 1 ise üreticiye özeldir."]),
  ("Sık görülen kodlar", [
   {"tablo": (["Kod", "Anlamı", "Sık nedenler"], [
     ["P0300", "Rastgele/çoklu silindir teklemesi", "Buji, bobin, enjektör, vakum kaçağı"],
     ["P0301–P0304", "Belirli silindirde tekleme", "O silindirin bujisi, bobini ya da enjektörü"],
     ["P0171", "Karışım fakir (benzinli)", "Vakum kaçağı, hava debimetresi, yakıt basıncı"],
     ["P0420", "Katalitik konvertör verimi düşük", "Katalizör, oksijen sensörü, egzoz kaçağı"],
     ["P0401", "EGR akışı yetersiz", "İs tutmuş EGR valfi ya da kanalları"],
     ["P2002", "DPF verimi düşük (dizel)", "Tıkalı ya da hasarlı partikül filtresi, sensör"]])}]),
  ("Kodu silmek arızayı çözer mi?", [
   "Hayır. Kod silindiğinde uyarı ışığı geçici olarak söner ama sorun duruyorsa kod kısa sürede geri gelir. Doğru yaklaşım; kodu okumak, canlı verileri incelemek ve ilgili parçayı ölçerek arızayı doğrulamaktır. Bu sayede gereksiz parça değişiminin önüne geçilir."]),
 ],
 sss=[("Motor arıza ışığı yanınca araç kullanılır mı?", "Işık sabit yanıyorsa araç dikkatle kullanılabilir ama en kısa sürede kontrol ettirilmelidir. Işık yanıp sönüyorsa ciddi tekleme vardır; aracı zorlamadan servise götürün."),
      ("Arıza tespit ne kadar sürer?", "Kod okuma birkaç dakika sürer. Sorunun kaynağını doğrulamak için yapılan ölçüm ve kontroller arızaya göre değişir.")]),

dict(slug="gosterge-uyari-isiklari", grup="Elektrik ve konfor", hizmet="ariza-tespit",
 baslik="Gösterge paneli uyarı ışıkları: kırmızı, sarı ve yeşil ne demek?",
 meta="Araç göstergesindeki uyarı ışıklarının anlamı: yağ basıncı, hararet, akü, fren, motor arıza, ABS, DPF ve lastik basıncı ışıkları. Hangi ışıkta durmalı?",
 ozet="Gösterge ışıkları renklerine göre aciliyet bildirir: kırmızı ışık hemen durulması gereken ciddi bir sorunu, sarı veya turuncu ışık kısa sürede kontrol gerektiren bir arızayı, yeşil ve mavi ışıklar ise bir sistemin çalıştığını gösterir.",
 bolumler=[
  ("Kırmızı ışıklar: güvenli yerde durun", [
   {"tablo": (["Işık", "Anlamı", "Ne yapmalı?"], [
     ["Yağ kabı (yağ basıncı)", "Motor yağ basıncı düşük", "Hemen durun, motoru kapatın, yağ seviyesine bakın; seviye normalse çalıştırmayın"],
     ["Termometre (hararet)", "Motor aşırı ısınıyor", "Durun, motoru kapatın; soğumadan kapak açmayın"],
     ["Akü", "Şarj sistemi çalışmıyor", "Gereksiz elektrik tüketicilerini kapatıp servise gidin"],
     ["Ünlem içinde daire (fren)", "El freni çekili ya da fren hidroliği düşük", "El frenini kontrol edin; sönmüyorsa sürmeyin"],
     ["Hava yastığı", "Hava yastığı sisteminde arıza", "Kaza anında yastık açılmayabilir; kontrol ettirin"]])}]),
  ("Sarı/turuncu ışıklar: yakın zamanda kontrol", [
   {"tablo": (["Işık", "Anlamı"], [
     ["Motor silueti", "Motor ya da emisyon sisteminde arıza; yanıp sönüyorsa ciddi tekleme"],
     ["ABS", "ABS devre dışı; normal fren çalışır"],
     ["ESP / kayan araba", "Denge kontrolü devre dışı ya da arızalı"],
     ["Lastik kesiti ve ünlem", "Lastik basıncı düşük"],
     ["DPF (noktalı kutu)", "Partikül filtresi doluyor"],
     ["Spiral (kızdırma)", "Dizel kızdırma sistemi; sürekli yanıyor ya da yanıp sönüyorsa arıza"],
     ["Direksiyon simidi", "Direksiyon destek sistemi arızası"]])}]),
  ("Yeşil ve mavi ışıklar", [
   "Kısa far, sis farı, sinyal ve hız sabitleyici gibi ışıklar yalnızca bilgi verir. Mavi ışık uzun farın açık olduğunu gösterir; karşıdan araç geldiğinde kapatılmalıdır."]),
 ],
 sss=[("Kontak açılınca bütün ışıkların yanması normal mi?", "Evet. Kontak açıldığında araç ampul ve sistem testi yapar; motor çalıştıktan sonra birkaç saniye içinde sönmeleri gerekir."),
      ("Işık yanıp sönüp kayboldu, yine de kontrol ettirmeli miyim?", "Evet. Aralıklı yanan ışıklar çoğu zaman başlangıç aşamasındaki bir arızanın habercisidir ve arıza kodu hafızada kalır.")]),

dict(slug="klima-sistemi", grup="Elektrik ve konfor", hizmet="klima",
 baslik="Araç kliması nasıl çalışır? Klima gazı, kompresör ve bakım",
 meta="Araç kliması neden soğutmaz? Klima gazı (R134a, R1234yf), kompresör, kondenser ve polen filtresinin görevleri, kötü koku nedenleri ve klima bakımı.",
 ozet="Araç kliması, kompresörün sıkıştırdığı soğutucu gazın genleşirken ısı çekmesi prensibiyle çalışır. Soğutmayan klimanın en sık nedenleri gaz eksikliği (çoğu zaman bir kaçak), kompresör arızası ve tıkalı polen filtresidir. Klimanın yılda bir kontrol ettirilmesi ve kışın da ara ara çalıştırılması önerilir.",
 bolumler=[
  ("Sistemin parçaları", [
   {"liste": ["<b>Kompresör:</b> Motor tarafından döndürülür, gazı sıkıştırır.",
              "<b>Kondenser:</b> Aracın önünde, radyatörün yanında; sıcak gazı soğutup sıvılaştırır.",
              "<b>Kurutucu:</b> Sistemdeki nemi tutar.",
              "<b>Genleşme valfi:</b> Basıncı düşürür; gaz genleşerek soğur.",
              "<b>Evaporatör:</b> Torpidonun arkasında; kabine üflenen havayı soğutur.",
              "<b>Polen filtresi:</b> Kabine giren havayı temizler."]},
   "Daha eski araçlarda R134a, yeni araçların çoğunda ise R1234yf gazı kullanılır; iki gaz birbirinin yerine kullanılamaz."]),
  ("Klima neden soğutmaz?", [
   {"tablo": (["Belirti", "Olası neden"], [
     ["Hiç soğutmuyor", "Gaz bitmiş (kaçak), kompresör devreye girmiyor, sigorta ya da basınç sensörü"],
     ["Az soğutuyor", "Gaz eksik, kondenser kirli ya da fan çalışmıyor"],
     ["Hava zayıf üflüyor", "Tıkalı polen filtresi ya da kalorifer fanı"],
     ["Kötü koku", "Evaporatörde nem ve bakteri birikmesi, eski polen filtresi"]])},
   "Gaz kendiliğinden bitmez; eksiliyorsa bir yerden kaçak vardır. Kaçak bulunmadan yapılan gaz dolumu kısa sürede tekrar boşalır."]),
  ("Klimayı sağlıklı kullanmak", [
   {"liste": ["Kışın da ayda birkaç kez kısa süre çalıştırın; contalar yağlanır ve camlar daha çabuk açılır.",
              "Varış noktasına birkaç dakika kala klimayı kapatıp fanı açık bırakın; evaporatör kurur, koku oluşumu azalır.",
              "Polen filtresini yılda bir değiştirin."]}]),
 ],
 sss=[("Klima yakıt tüketimini artırır mı?", "Evet, kompresör motordan güç aldığı için bir miktar artırır. Yüksek hızda camları açık sürmek de hava direnci nedeniyle tüketimi artırır."),
      ("Klima gazı kaç yılda bir yenilenir?", "Sağlam bir sistemde gaz çok yavaş azalır. Soğutma zayıfladığında ya da genel olarak 2–3 yılda bir kontrol ettirilmesi yeterlidir.")]),

dict(slug="kaporta-boya-pas", grup="Elektrik ve konfor", hizmet="kaporta-boya",
 baslik="Kaporta, boya ve pas: göçük, çizik ve korozyon rehberi",
 meta="Araç kaportasındaki göçük, çizik ve pas nasıl onarılır? Boyasız göçük düzeltme, rötuş, lokal boya, pasın nedenleri ve kaportayı korumanın yolları.",
 ozet="Kaporta hasarları üç ana grupta ele alınır: göçük, boya çiziği ve pas. Küçük göçükler çoğu zaman boyaya dokunmadan düzeltilebilir; derin çizikler ve pas ise yayılmadan önce onarılmalıdır, çünkü metale ulaşan nem korozyonu hızla ilerletir.",
 bolumler=[
  ("Hasar türleri ve onarım", [
   {"tablo": (["Hasar", "Onarım yöntemi"], [
     ["Boyası çatlamamış küçük göçük", "Boyasız göçük düzeltme (PDR)"],
     ["Vernikte yüzeysel çizik", "Pasta ve cila"],
     ["Boyaya inen çizik", "Rötuş ya da lokal boya"],
     ["Metale inen çizik veya pas başlangıcı", "Zımpara, astar ve boya"],
     ["Delinmiş ya da ağır hasarlı parça", "Parça onarımı ya da değişimi"]])}]),
  ("Pas neden oluşur?", [
   "Pas, metalin nem ve oksijenle tepkimesidir. Taş sıçramasıyla açılan küçük boya yaraları, kışın yollara dökülen tuz, kapı altlarında ve çamurluk içlerinde biriken çamur pasın en sık nedenleridir. Kabarcık şeklinde görünen boya, altında pasın ilerlediğinin işaretidir."]),
  ("Kaportayı korumak için", [
   {"liste": ["Kışın düzenli yıkama yapın ve aracın altını da yıkatın.",
              "Taş izlerini ve küçük boya yaralarını rötuşla kapatın.",
              "Kapı altlarındaki su tahliye deliklerinin açık olduğundan emin olun.",
              "Yılda bir ya da iki kez cila, boyayı güneşe ve kire karşı korur."]}]),
 ],
 sss=[("Boyalı parça aracın değerini düşürür mü?", "Kaza kaydı ve boya durumu ikinci el değerini etkileyebilir. Küçük göçüklerde boyasız düzeltme, orijinal boyayı korumanın yoludur."),
      ("Lokal boya rengi tutar mı?", "Doğru renk kodu ve uygun karışımla yapılan lokal boyada renk farkı en aza indirilir; geçişler parlatılarak belirsizleştirilir.")]),

dict(slug="periyodik-bakim-takvimi", grup="Bakım ve muayene", hizmet="periyodik-bakim",
 baslik="Periyodik bakım takvimi: hangi parça kaç kilometrede değişir?",
 meta="Araç bakım takvimi: motor yağı, filtreler, buji, triger, fren hidroliği, antifriz, şanzıman yağı ve diğer parçaların tipik değişim kilometreleri tek tabloda.",
 ozet="Bakım aralıkları araçtan araca değişir ve kesin değerler kullanım kılavuzunda yazar. Yine de çoğu otomobil için genel bir takvim çıkarılabilir: yağ ve yağ filtresi her 10.000–15.000 km'de ya da yılda bir, fren hidroliği 2 yılda bir, triger kayışı ise genellikle 60.000–120.000 km arasında değişir.",
 bolumler=[
  ("Genel bakım tablosu", [
   {"tablo": (["Parça / işlem", "Tipik aralık", "Not"], [
     ["Motor yağı ve yağ filtresi", "10.000–15.000 km ya da 1 yıl", "Ağır kullanımda daha sık"],
     ["Hava filtresi", "15.000–30.000 km", "Tozlu ortamda daha sık"],
     ["Polen filtresi", "15.000 km ya da 1 yıl", ""],
     ["Yakıt filtresi", "30.000–60.000 km", "Dizelde daha önemli"],
     ["Buji (bakır/nikel)", "20.000–30.000 km", "Platin/iridyumda 60.000–100.000 km"],
     ["Fren hidroliği", "2 yıl", "Kilometreden bağımsız"],
     ["Balata", "Kontrolle; ~3 mm'de değişim", "Her bakımda ölçülür"],
     ["Antifriz", "2–5 yıl", "Antifriz tipine göre"],
     ["Triger kayışı seti", "60.000–120.000 km ya da 4–6 yıl", "Üreticiye göre kesin değer"],
     ["V kayışı", "Kontrolle; çatlak varsa", "Triger ile birlikte değişebilir"],
     ["Şanzıman yağı (otomatik/DSG/CVT)", "60.000–100.000 km", "Üretici önerisine göre"],
     ["Akü", "3–5 yıl", "Yılda bir test"],
     ["Silecek lastikleri", "Yılda bir", "İz bırakıyorsa"]])}]),
  ("Ağır kullanım nedir?", [
   "Pek çok üretici, aşağıdaki koşulları 'ağır kullanım' sayar ve bu durumda bakım aralıklarının kısaltılmasını önerir:",
   {"liste": ["Çoğunlukla 10 km'den kısa yolculuklar", "Yoğun şehir içi trafik ve sık dur-kalk", "Tozlu ya da toprak yollar", "Römork çekme, yüklü kullanım", "Taksi, servis ya da ticari kullanım"]}]),
  ("Bakım kaydı neden önemli?", [
   "Düzenli ve belgeli bakım, hem arızaları erken yakalar hem de aracınızı satarken değerini korur. Bakımdan sonra hangi parçanın ne zaman değiştiğini yazılı olarak saklamak, bir sonraki bakımı planlamayı kolaylaştırır."]),
 ],
 sss=[("Yetkili servis dışında bakım garantiyi bozar mı?", "Garanti koşulları üreticiye göre değişir. Garanti süresindeki araçlarda üreticinin şartlarına ve onaylı parça kullanımına dikkat edilmelidir; garanti kitapçığını kontrol edin."),
      ("Araç az kullanılıyorsa bakım ertelenebilir mi?", "Kilometre dolmasa bile yağ ve fren hidroliği gibi sıvılar zamanla bozulur. Yılda en az bir bakım önerilir.")]),

dict(slug="arac-muayenesi-hazirlik", grup="Bakım ve muayene", hizmet="muayene-oncesi-kontrol",
 baslik="Araç muayenesine hazırlık: muayeneden kalmamak için kontrol listesi",
 meta="Araç muayenesinde nelere bakılır? Fren, far, lastik, egzoz, rot ve rotil kontrolleri; muayeneden kusurla dönmemek için muayene öncesi kontrol listesi.",
 ozet="Araç muayenesinde güvenlikle ilgili sistemler kontrol edilir: frenler, aydınlatma, lastikler, direksiyon ve süspansiyon, egzoz ve emisyon, camlar ve görüş. Muayeneden önce bu noktaları kontrol ettirmek, ağır kusurla dönüp ikinci kez gitme zahmetini önler.",
 bolumler=[
  ("Muayene öncesi kontrol listesi", [
   {"tablo": (["Kontrol", "Dikkat edilecek nokta"], [
     ["Frenler", "Sağ-sol fren dengesi, el freni tutuşu, hidrolik kaçağı"],
     ["Aydınlatma", "Far ayarı, kısa-uzun far, stop, sinyal, plaka lambası"],
     ["Lastikler", "Diş derinliği, yanak hasarı, aynı aksta aynı ebat"],
     ["Direksiyon ve süspansiyon", "Rot, rotil ve salıncak boşluğu, amortisör kaçağı"],
     ["Egzoz", "Sızıntı, aşırı ses ve emisyon değerleri"],
     ["Görüş", "Ön camda görüşü engelleyen çatlak, silecekler, aynalar"],
     ["Güvenlik donanımı", "Emniyet kemerleri, korna, hava yastığı uyarı ışığı"],
     ["Gösterge ışıkları", "Motor arıza, ABS ve hava yastığı ışığının sönmesi"]])}]),
  ("Sık görülen kusurlar", [
   {"liste": ["Fren dengesizliği ya da el freninin zayıf tutması",
              "Yanmayan ampuller ve hatalı far ayarı",
              "Rotil ve rot başlarında boşluk",
              "Egzoz sızıntısı ya da yüksek emisyon",
              "Yanan motor arıza ya da hava yastığı ışığı"]},
   "Bu kusurların çoğu muayene öncesi bir kontrolle kolayca giderilebilir."]),
 ],
 sss=[("Muayeneden önce ne zaman kontrol ettirmeliyim?", "Muayene randevusundan bir-iki hafta önce kontrol ettirmek, gerekirse parça temini için zaman bırakır."),
      ("Gösterge ışığı yanıyorsa muayeneden geçer mi?", "Hava yastığı ve ABS gibi güvenlik sistemlerine ait uyarı ışıkları kusur sebebi olabilir. Muayeneden önce arızanın giderilmesi önerilir.")]),

dict(slug="yolda-kalinca-ne-yapmali", grup="Bakım ve muayene", hizmet="lastik-balans",
 baslik="Yolda kalınca ne yapmalı? Lastik patlaması, akü ve hararet",
 meta="Araç yolda kaldığında ne yapmalı? Lastik patlaması, akü bitmesi, hararet ve yakıt bitmesinde adım adım yapılacaklar ve yol yardım ne zaman çağrılır.",
 ozet="Araç yolda kaldığında önce güvenlik gelir: aracı mümkünse yolun en sağına ya da emniyet şeridine çekin, dörtlüleri yakın, reflektörü aracın 30–150 metre gerisine koyun ve yolcularla birlikte bariyerin arkasında güvenli bir yerde bekleyin. Sorunu güvenle çözemiyorsanız yol yardım çağırın.",
 bolumler=[
  ("İlk adımlar", [
   {"liste": ["Aracı trafikten olabildiğince uzağa, düz ve görünür bir yere çekin.",
              "Dörtlüleri yakın; karanlıkta park lambalarını da açık bırakın.",
              "Reflektif yeleğinizi giyin, reflektörü yola koyun.",
              "Otoyolda aracın içinde ya da önünde beklemeyin; bariyerin arkasına geçin.",
              "Konumunuzu belirleyin: yol adı, yön, yakındaki tabela ya da kilometre levhası."]}]),
  ("Duruma göre ne yapmalı?", [
   {"tablo": (["Durum", "Ne yapmalı?"], [
     ["Lastik patladı", "Güvenli yerdeyseniz stepneyi takın; yanak hasarı, gece ya da yoğun trafik varsa yol yardım çağırın"],
     ["Akü bitti", "Takviye kablosu ve yardım edecek araç varsa takviye yapın; yoksa yol yardım"],
     ["Hararet yaptı", "Motoru kapatın, kapağı açmayın, soğumasını bekleyin; kaçak varsa sürmeyin"],
     ["Yakıt bitti", "Dizel araçlarda yakıt sistemine hava girebilir; yakıt eklendikten sonra çalışmazsa zorlamayın"],
     ["Yağ basıncı ışığı yandı", "Hemen motoru kapatın, tekrar çalıştırmayın"],
     ["Triger koptu (motor aniden stop etti, marşta farklı ses)", "Tekrar çalıştırmayı denemeyin; çekici ya da yol yardım"]])}]),
  ("Yol yardım çağırırken", [
   {"liste": ["Tam konumunuzu ve gidiş yönünüzü söyleyin.",
              "Aracın markasını, modelini ve rengini bildirin.",
              "Sorunu tarif edin: patlak lastik, çalışmayan motor, duman, ses.",
              "Stepne, takviye kablosu gibi donanımınız olup olmadığını belirtin."]}]),
  ("Araçta bulunması gerekenler", [
   {"liste": ["Reflektör ve reflektif yelek", "İlk yardım çantası ve yangın söndürücü", "Kullanılabilir durumda stepne, kriko ve bijon anahtarı", "Takviye kablosu", "El feneri"]}]),
 ],
 sss=[("Stepne yoksa ne yapmalıyım?", "Bazı araçlarda stepne yerine lastik tamir kiti bulunur; bu kit yalnızca küçük delikler için geçici çözümdür. Yanak hasarında ya da kit yetersiz kalırsa yol yardım çağırın."),
      ("Patlak lastikle sürmeye devam edilir mi?", "Hayır. Kısa mesafede bile jant ve lastik onarılamayacak şekilde zarar görür, araç kontrolü zorlaşır. Güvenli yere çekip durun.")]),
]
