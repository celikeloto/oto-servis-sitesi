"""Teknik rehber makaleleri (1/3): motor ve motor çevresi.
Biçim: bolumler = [(alt başlık, [paragraf | {"liste": [...]} | {"tablo": (başlıklar, satırlar)}]), ...]"""

MAKALELER_1 = [
dict(slug="motor-nasil-calisir", grup="Motor", hizmet="motor-mekanik",
 baslik="Motor nasıl çalışır? Dört zamanlı motorun temelleri",
 meta="Dört zamanlı benzinli ve dizel motor nasıl çalışır? Emme, sıkıştırma, iş ve egzoz zamanı ile motorun temel parçalarını sade bir dille anlatıyoruz.",
 ozet="Otomobil motorları, yakıtı silindir içinde yakarak pistonu iter; pistonun ileri geri hareketi krank mili sayesinde dönme hareketine çevrilir ve tekerleklere aktarılır. Bu iş dört zamanda tamamlanır: emme, sıkıştırma, iş (yanma) ve egzoz.",
 bolumler=[
  ("Dört zaman: motorun bir çevrimi", [
   "Bugün yollardaki benzinli ve dizel otomobillerin neredeyse tamamı dört zamanlı motor kullanır. Her silindirde aynı dört adım sırayla ve çok hızlı biçimde tekrarlanır:",
   {"liste": ["<b>Emme:</b> Piston aşağı iner, emme supabı açılır, silindire hava (benzinlide hava-yakıt karışımı) dolar.",
              "<b>Sıkıştırma:</b> Supaplar kapanır, piston yukarı çıkarak karışımı sıkıştırır.",
              "<b>İş (yanma):</b> Benzinli motorda buji kıvılcım çakar; dizelde ise yakıt, sıkıştırılarak ısınmış havaya püskürtülünce kendiliğinden tutuşur. Genleşen gazlar pistonu aşağı iter. Gücün üretildiği tek zaman budur.",
              "<b>Egzoz:</b> Egzoz supabı açılır, piston yukarı çıkarak yanmış gazları dışarı atar."]}]),
  ("Benzinli ve dizel motorun farkı", [
   "İki motor da dört zamanlıdır ama yakıtı tutuşturma şekli farklıdır. Benzinli motor karışımı bujiyle ateşler. Dizel motor ise havayı çok daha yüksek oranda sıkıştırır; sıkışan havanın sıcaklığı yakıtı kendiliğinden tutuşturur. Bu yüzden dizel motorlarda buji yoktur, soğuk havada ilk çalıştırmaya yardım eden kızdırma bujileri bulunur.",
   "Dizel motorlar genelde düşük devirde daha yüksek tork üretir ve daha az yakıt tüketir; benzinli motorlar ise daha sessiz çalışır ve yüksek devirlere daha kolay çıkar."]),
  ("Motorun temel parçaları", [
   {"tablo": (["Parça", "Görevi"], [
     ["Silindir bloğu", "Silindirlerin bulunduğu ana gövde"],
     ["Piston ve segmanlar", "Yanma basıncını karşılar; segmanlar sızdırmazlık sağlar ve yağı kontrol eder"],
     ["Biyel kolu", "Pistonu krank miline bağlar"],
     ["Krank mili", "Pistonun doğrusal hareketini dönme hareketine çevirir"],
     ["Silindir kapağı", "Supapların, eksantrik milinin ve (benzinlide) bujilerin bulunduğu üst bölüm"],
     ["Eksantrik mili ve supaplar", "Havanın girişini ve egzozun çıkışını doğru zamanda açıp kapatır"],
     ["Triger kayışı/zinciri", "Krank ve eksantrik millerini birbirine senkron bağlar"],
     ["Silindir kapak contası", "Blok ile kapak arasında yağ, su ve yanma basıncının sızmasını engeller"]])}]),
  ("Motor sağlığını korumak için", [
   {"liste": ["Motor yağını ve filtresini zamanında değiştirin; yağ motorun hem yağlayıcısı hem soğutucusudur.",
              "Motor soğukken yüksek devirde zorlamayın; yağın tüm parçalara ulaşması birkaç dakika sürer.",
              "Triger değişim kilometresini kaçırmayın.",
              "Hararet göstergesini ve yağ basıncı ışığını takip edin; ikisi de yanarsa motoru hemen durdurun."]}]),
 ],
 sss=[("Motor neden tıkırtı yapar?", "Düşük yağ seviyesi, aşınmış supap itecekleri, hatalı yakıt ya da motor içi aşınma tıkırtı yapabilir. Ses yeni başladıysa önce yağ seviyesini kontrol edin ve aracı bir ustaya gösterin."),
      ("Dizel motorda buji var mı?", "Hayır. Dizel motorlarda yakıt sıkıştırma ısısıyla tutuşur. Soğuk çalıştırmaya yardım eden kızdırma bujileri vardır ama bunlar kıvılcım çakmaz.")]),

dict(slug="motor-yagi", grup="Motor", hizmet="periyodik-bakim",
 baslik="Motor yağı rehberi: 5W-30 ne demek, ne zaman değişir?",
 meta="Motor yağındaki 5W-30, 10W-40 gibi değerler ne anlama gelir? Yağ değişim aralığı, yağ seviyesi kontrolü ve doğru yağ seçimi hakkında bilmeniz gerekenler.",
 ozet="Motor yağı, hareketli parçaları yağlar, soğutur ve temiz tutar. Çoğu otomobilde yağ ve yağ filtresi 10.000–15.000 km'de ya da yılda bir değiştirilir; kesin aralık ve doğru yağ sınıfı aracın kullanım kılavuzunda yazar.",
 bolumler=[
  ("Yağ kodları nasıl okunur?", [
   "Yağ kutusundaki <b>5W-30</b> gibi bir kod yağın akışkanlığını (viskozitesini) anlatır:",
   {"liste": ["<b>5W:</b> Soğuk havadaki akışkanlık. W kış (winter) demektir; sayı küçüldükçe yağ soğukta daha kolay akar ve motor ilk çalıştırmada daha çabuk yağlanır.",
              "<b>30:</b> Motor çalışma sıcaklığındaki (yaklaşık 100 °C) kalınlık. Sayı büyüdükçe yağ sıcakta daha kalın kalır."]},
   "Kodun yanı sıra üreticinin istediği <b>onay ve standartlar</b> (örneğin ACEA sınıfları ya da üreticiye özel onay numaraları) da önemlidir. Özellikle partikül filtreli dizel araçlarda düşük kül içerikli yağ kullanılması gerekir."]),
  ("Ne sıklıkla değiştirilmeli?", [
   {"tablo": (["Kullanım", "Tipik değişim aralığı"], [
     ["Normal şehir içi ve şehirlerarası kullanım", "10.000–15.000 km ya da yılda bir"],
     ["Uzun ömürlü yağ ve üreticinin izin verdiği esnek bakım", "Üreticiye göre 20.000–30.000 km"],
     ["Ağır kullanım (kısa mesafe, sık dur-kalk, taksi, çekme)", "Normal aralığın yaklaşık yarısı"]])},
   "Az kullanılan araçlarda bile yağ zamanla bozulur; bu yüzden kilometre dolmasa da yılda bir değişim önerilir. Yağ değiştirilirken yağ filtresi de mutlaka değiştirilmelidir."]),
  ("Yağ seviyesi nasıl kontrol edilir?", [
   {"liste": ["Aracı düz bir zemine park edin; motor çalıştıysa 5–10 dakika bekleyin.",
              "Yağ çubuğunu çekin, silin, tamamen geri takıp tekrar çekin.",
              "Yağ izi MIN ve MAX çizgileri arasında olmalı. MIN'e yakınsa aynı yağdan ekleyin; MAX'ı aşmayın.",
              "Yağ çok koyu ve kıvamsızsa, içinde metal parlaklığı ya da süt gibi açık renk varsa ustaya gösterin."]}]),
  ("Yağ eksiltiyorsa", [
   "Bir miktar yağ tüketimi normaldir; ancak iki bakım arasında sık sık ekleme yapıyorsanız yağ kaçağı, segman aşınması ya da turbo sorunu olabilir. Egzozdan mavimsi duman çıkması yağ yandığına işaret eder."]),
 ],
 sss=[("Farklı marka yağlar karıştırılır mı?", "Aynı viskozite ve standarttaki yağlar acil durumda eklenebilir, ancak ilk bakımda tek tip yağla değişim yapılması en doğrusudur."),
      ("Yağ değişimi ne kadar sürer?", "Yağ ve filtre değişimi genellikle yarım saat ile bir saat arasında tamamlanır; diğer filtreler ve kontroller de yapılıyorsa süre uzayabilir.")]),

dict(slug="filtreler", grup="Motor", hizmet="periyodik-bakim",
 baslik="Araç filtreleri: yağ, hava, polen ve yakıt filtresi",
 meta="Araçta hangi filtreler var, ne işe yarar ve ne zaman değişir? Yağ filtresi, hava filtresi, polen (kabin) filtresi ve yakıt filtresi rehberi.",
 ozet="Araçta dört temel filtre bulunur: yağ, hava, polen (kabin) ve yakıt filtresi. Yağ filtresi her yağ değişiminde, hava ve polen filtresi genellikle yılda bir ya da 15.000–30.000 km'de, yakıt filtresi ise yakıt tipine göre 30.000–60.000 km'de değiştirilir.",
 bolumler=[
  ("Hangi filtre ne işe yarar?", [
   {"tablo": (["Filtre", "Görevi", "Tipik değişim"], [
     ["Yağ filtresi", "Motor yağındaki metal tozunu ve kirleri tutar", "Her yağ değişiminde"],
     ["Hava filtresi", "Motora giren havadaki toz ve kumu tutar", "15.000–30.000 km (tozlu yolda daha sık)"],
     ["Polen (kabin) filtresi", "Kabine giren havadaki polen, toz ve kokuyu tutar", "Yılda bir ya da 15.000 km"],
     ["Yakıt filtresi", "Yakıttaki su ve parçacıkları tutar; dizelde çok önemlidir", "Dizelde 30.000–60.000 km; benzinlide üreticiye göre"]])}]),
  ("Tıkalı filtre neye yol açar?", [
   {"liste": ["<b>Hava filtresi tıkanırsa</b> motor yeterince hava alamaz; güç düşer, yakıt tüketimi artar.",
              "<b>Polen filtresi tıkanırsa</b> klima ve kalorifer zayıf üfler, camlar daha çok buğulanır, kötü koku oluşur.",
              "<b>Yakıt filtresi tıkanırsa</b> araç zor çalışır, yokuşta ya da hızlanırken teklemeye başlar. Dizel araçlarda filtredeki su enjektörlere zarar verebilir.",
              "<b>Yağ filtresi zamanında değişmezse</b> kirli yağ motor parçalarını aşındırır."]}]),
  ("Ucuz filtre tasarruf mu?", [
   "Filtre, motoru koruyan en ucuz parçadır. Kalitesiz bir filtre ya tozu yeterince tutmaz ya da erken tıkanır. Orijinal ya da kaliteli muadil filtre kullanmak uzun vadede daha ekonomiktir."]),
 ],
 sss=[("Hava filtresini temizleyip tekrar takabilir miyim?", "Kâğıt hava filtreleri basınçlı havayla kısa süreli temizlenebilir ama bu kalıcı çözüm değildir; bakım zamanında yenisi takılmalıdır."),
      ("Polen filtresi değişmezse ne olur?", "Klima verimi düşer, kabinde koku oluşur ve alerjisi olan yolcular rahatsız olur. Ucuz ve hızlı değişen bir parçadır.")]),

dict(slug="triger-kayisi-zinciri", grup="Motor", hizmet="triger-seti",
 baslik="Triger kayışı ve zinciri: ne zaman değişmeli?",
 meta="Triger kayışı ne işe yarar, kaç kilometrede değişir, koparsa ne olur? Triger zinciri ile kayışı arasındaki farklar ve triger setinde değişen parçalar.",
 ozet="Triger kayışı ya da zinciri, krank mili ile eksantrik milini senkron döndürür; supapların doğru anda açılıp kapanmasını sağlar. Kayışlı motorlarda değişim genellikle 60.000–120.000 km ya da 4–6 yılda bir yapılır; kesin değer aracın bakım kılavuzunda yazar.",
 bolumler=[
  ("Triger neden bu kadar önemli?", [
   "Pek çok motorda piston ve supaplar aynı boşluğu farklı zamanlarda kullanır. Triger kayışı koparsa senkron bozulur; pistonlar açık kalan supaplara çarpabilir. Sonuç çoğu zaman silindir kapağı onarımı ya da motor revizyonudur. Bu yüzden triger değişimi, arıza beklenmeden kilometre ve yaşa göre yapılır."]),
  ("Kayış mı, zincir mi?", [
   {"tablo": (["", "Triger kayışı", "Triger zinciri"], [
     ["Malzeme", "Takviyeli kauçuk", "Metal"],
     ["Ömür", "Belirli km/yılda değişir", "Uzun ömürlüdür, ama uzayabilir"],
     ["Belirti", "Genelde belirti vermeden kopar", "Uzayınca ilk çalıştırmada metalik şıkırtı yapar"],
     ["Bakım", "Gergi, avara ve çoğu zaman devirdaim ile birlikte değişir", "Uzama ya da ses varsa gergi ve kızaklarla değişir"]])}]),
  ("Triger setinde neler değişir?", [
   {"liste": ["Triger kayışı",
              "Gergi rulmanı ve avara (yönlendirme) rulmanları",
              "Devirdaim pompası (kayışla çalışıyorsa genellikle birlikte değiştirilir)",
              "Gerekiyorsa V kayışı ve gergisi"]},
   "Yalnızca kayışı değiştirip eski rulmanları bırakmak risklidir: kayıştan önce bir rulman dağılırsa sonuç aynıdır."]),
  ("Değişim zamanı geldiğini nasıl anlarım?", [
   {"liste": ["Bakım kılavuzundaki kilometre ya da yıl sınırına ulaşıldıysa",
              "Aracı ikinci el aldıysanız ve son triger değişimi belgelenmemişse",
              "Motorun ön kısmından ötme, hışırtı ya da sürtünme sesi geliyorsa",
              "Devirdaim bölgesinden su sızıntısı varsa"]}]),
 ],
 sss=[("Triger kayışı koparsa araç çalışır mı?", "Hayır. Motor hemen stop eder ve çoğu motorda supaplar zarar görür. Aracı tekrar çalıştırmayı denemeyin, çekici ya da yol yardımı çağırın."),
      ("Triger değişimi ne kadar sürer?", "Motora göre değişmekle birlikte genellikle birkaç saat sürer; parça hazırsa aynı gün teslim edilebilir.")]),

dict(slug="sogutma-sistemi-hararet", grup="Motor", hizmet="sogutma-sistemi",
 baslik="Soğutma sistemi ve hararet: antifriz, radyatör, termostat",
 meta="Araç neden hararet yapar? Antifriz oranı, radyatör, termostat ve devirdaimin görevleri, hararet anında yapılması gerekenler ve bakım aralıkları.",
 ozet="Soğutma sistemi motoru yaklaşık 90 °C civarındaki çalışma sıcaklığında tutar. Antifriz-su karışımı motorda ısınır, radyatörde soğur; termostat akışı ayarlar, devirdaim pompası sıvıyı dolaştırır. Hararet göstergesi yükselirse aracı güvenli bir yerde durdurup motoru kapatmak gerekir.",
 bolumler=[
  ("Sistem nasıl çalışır?", [
   {"liste": ["<b>Devirdaim (su pompası):</b> Soğutma sıvısını motor ve radyatör arasında dolaştırır.",
              "<b>Termostat:</b> Motor soğukken kapalı kalır, motor ısınınca açılarak sıvıyı radyatöre gönderir.",
              "<b>Radyatör:</b> Sıvının ısısını havaya verir.",
              "<b>Fan:</b> Araç dururken ya da yavaşken radyatöre hava üfler.",
              "<b>Genleşme kabı:</b> Isınan sıvının fazlasını toplar; seviye buradan kontrol edilir."]}]),
  ("Antifriz neden önemli?", [
   "Antifriz yalnızca donmayı önlemez; kaynama noktasını yükseltir ve sistemdeki metalleri paslanmaya karşı korur. Yaygın kullanımda antifriz ile su yaklaşık yarı yarıya karıştırılır; bu oran donmaya karşı yaklaşık -35 °C'ye kadar koruma sağlar. Antifriz tipine göre 2–5 yılda bir yenilenmelidir. Farklı tip antifrizleri karıştırmamak gerekir."]),
  ("Hararet yaparsa ne yapmalı?", [
   {"liste": ["Klimayı kapatın, kaloriferi en sıcakta ve fanı en yüksekte açın; bu motorun ısısını bir miktar alır.",
              "Güvenli bir yerde durun ve motoru kapatın.",
              "<b>Motor sıcakken radyatör ya da genleşme kabının kapağını kesinlikle açmayın;</b> basınçlı kaynar sıvı yanığa neden olur.",
              "Motor soğuduktan sonra seviyeyi kontrol edin; kaçak varsa aracı sürmeye devam etmeyin, yol yardımı çağırın."]},
   "Hararetle sürmeye devam etmek silindir kapak contasını yakabilir ve kapağı eğebilir; bu, basit bir hortum değişiminin motor onarımına dönüşmesi demektir."]),
  ("Sık görülen arızalar", [
   {"tablo": (["Belirti", "Olası neden"], [
     ["Antifriz sürekli eksiliyor", "Hortum, radyatör ya da devirdaim kaçağı; ileri durumda kapak contası"],
     ["Kalorifer ısıtmıyor", "Termostat açık kalmış, sıvı eksik ya da sistemde hava var"],
     ["Trafikte hararet yükseliyor", "Fan ya da fan müşiri çalışmıyor"],
     ["Egzozdan beyaz, tatlı kokulu duman", "Soğutma sıvısı yanma odasına geçiyor (kapak contası)"]])}]),
 ],
 sss=[("Antifriz yerine su koyabilir miyim?", "Acil durumda kısa süreli olarak su eklenebilir; ancak en kısa sürede doğru oranda antifrizle tamamlanmalıdır. Kışın yalnızca su donarak motora zarar verebilir."),
      ("Hararet göstergesi normalde nerede durur?", "Motor ısındıktan sonra çoğu araçta göstergenin ortasında sabit durur. Ortanın üzerine çıkıyorsa sorun var demektir.")]),

dict(slug="buji-atesleme", grup="Motor", hizmet="periyodik-bakim",
 baslik="Buji ve ateşleme sistemi: tekleme neden olur?",
 meta="Buji ne işe yarar, ne zaman değişir? Bobin, buji kablosu ve ateşleme sistemi arızaları, tekleme belirtileri ve dizel araçlardaki kızdırma bujileri.",
 ozet="Benzinli motorlarda buji, sıkıştırılmış hava-yakıt karışımını kıvılcımla ateşler; kıvılcım için gereken yüksek voltajı bobin üretir. Bakır/nikel bujiler genellikle 20.000–30.000 km'de, platin ve iridyum bujiler 60.000–100.000 km'de değiştirilir.",
 bolumler=[
  ("Ateşleme sisteminin parçaları", [
   {"liste": ["<b>Buji:</b> Silindir içinde kıvılcım çakar.",
              "<b>Bobin:</b> Akünün 12 voltunu binlerce volta yükseltir. Modern araçlarda her bujinin üstünde ayrı bobin bulunur.",
              "<b>Buji kabloları:</b> Tek bobinli eski sistemlerde voltajı bujilere taşır.",
              "<b>Motor beyni:</b> Kıvılcımın zamanlamasını sensörlerden gelen bilgiye göre ayarlar."]}]),
  ("Bozuk buji ya da bobin belirtileri", [
   {"liste": ["Rölantide titreme ve sarsıntı",
              "Hızlanırken tekleme, güç kaybı",
              "Yakıt tüketiminde artış",
              "Motor arıza ışığının yanması ya da yanıp sönmesi (P0300–P0304 gibi tekleme kodları)",
              "Zor çalışma"]},
   "Motor arıza ışığı yanıp sönüyorsa ciddi tekleme vardır; yanmayan yakıt egzoza gidip katalitik konvertöre zarar verebilir. Bu durumda aracı zorlamadan servise getirin."]),
  ("Dizel araçlarda kızdırma bujisi", [
   "Dizel motorlarda kıvılcım bujisi yoktur. Kızdırma bujileri, motor soğukken yanma odasını ısıtarak ilk çalıştırmayı kolaylaştırır. Kızdırmalardan biri bozulduğunda araç soğuk havada zor çalışır ve ilk dakikalarda beyaz duman ve titreme görülür."]),
 ],
 sss=[("Bujilerin hepsi birlikte mi değişmeli?", "Evet. Bujiler aynı sürede aşındığı için set halinde değiştirilmesi motorun dengeli çalışmasını sağlar."),
      ("Tekleme her zaman buji kaynaklı mıdır?", "Hayır. Bobin, enjektör, vakum kaçağı ya da kompresyon kaybı da tekleme yapabilir. Doğru teşhis için arıza kodu okunmalı ve test yapılmalıdır.")]),

dict(slug="yakit-sistemi-enjektor", grup="Motor", hizmet="yakit-enjektor",
 baslik="Yakıt sistemi ve enjektör: tekleme, duman ve yakıt tüketimi",
 meta="Yakıt pompası, enjektör, common rail ve gaz kelebeğinin görevleri. Enjektör arızası belirtileri, siyah duman, yüksek yakıt tüketimi ve bakım önerileri.",
 ozet="Yakıt sistemi, depodaki yakıtı pompa ile motora taşır ve enjektörler aracılığıyla doğru miktarda, doğru anda silindirlere püskürtür. Enjektör ya da pompa arızaları tekleme, zor çalışma, güç kaybı ve yüksek yakıt tüketimi olarak kendini gösterir.",
 bolumler=[
  ("Sistemin parçaları", [
   {"liste": ["<b>Yakıt pompası:</b> Depodaki yakıtı basınçla motora gönderir.",
              "<b>Yakıt filtresi:</b> Yakıttaki parçacıkları ve (dizelde) suyu tutar.",
              "<b>Enjektörler:</b> Yakıtı silindire ya da emme kanalına çok ince zerreler halinde püskürtür.",
              "<b>Yüksek basınç pompası ve rail:</b> Modern dizel (common rail) ve doğrudan enjeksiyonlu benzinli motorlarda yakıtı çok yüksek basınca çıkarır.",
              "<b>Gaz kelebeği ve hava sensörleri:</b> Motora giren hava miktarını ölçer ve ayarlar; motor beyni yakıtı buna göre belirler."]}]),
  ("Enjektör arızası belirtileri", [
   {"tablo": (["Belirti", "Ne anlama gelebilir?"], [
     ["Egzozdan siyah duman", "Fazla yakıt püskürtülüyor ya da yakıt iyi yanmıyor"],
     ["Rölantide titreme, sarsıntı", "Bir ya da birkaç enjektör düzgün püskürtmüyor"],
     ["Zor çalışma, özellikle sıcakken", "Enjektör kaçırıyor ya da basınç düşüyor"],
     ["Yakıt tüketiminde belirgin artış", "Enjektör, sensör ya da kaçak sorunu"],
     ["Motordan tak tak sesi (dizel)", "Enjektör püskürtme düzensizliği"]])}]),
  ("Yakıt sistemini korumak için", [
   {"liste": ["Güvenilir istasyonlardan yakıt alın; kirli ya da sulu yakıt enjektörlerin en büyük düşmanıdır.",
              "Dizel araçlarda yakıt filtresini zamanında değiştirin.",
              "Depoyu sürekli rezervde dolaşmayın; dipteki tortu pompaya ve filtreye yük bindirir.",
              "Belirti başladığında erken müdahale, pahalı enjektör ya da pompa değişimini önleyebilir."]}]),
 ],
 sss=[("Enjektör temizliği işe yarar mı?", "Hafif kirlenmede faydalı olabilir; ancak mekanik olarak aşınmış ya da kaçıran enjektör temizlikle düzelmez. Önce test yapılıp sorunun kaynağı belirlenmelidir."),
      ("Yanlış yakıt aldım, ne yapmalıyım?", "Aracı çalıştırmayın. Benzinli araca dizel ya da dizele benzin konduysa depo boşaltılmadan motoru çalıştırmak pompaya ve enjektörlere ciddi zarar verir. Yol yardımı çağırın.")]),

dict(slug="turbo", grup="Motor", hizmet="turbo",
 baslik="Turbo nasıl çalışır? Turbo arızası belirtileri ve korunma",
 meta="Turbo şarj nasıl çalışır, neden arızalanır? Islık sesi, mavi duman ve güç kaybı gibi turbo arızası belirtileri ile turboyu uzun ömürlü kullanmanın yolları.",
 ozet="Turbo, egzoz gazının enerjisiyle dönen bir türbin sayesinde motora daha fazla hava basar; böylece küçük hacimli motordan daha yüksek güç elde edilir. Turbonun en büyük düşmanları kötü ya da eksik yağ ve motor kapatılırken turbonun sıcakken yağsız kalmasıdır.",
 bolumler=[
  ("Turbo nasıl çalışır?", [
   "Turbonun bir tarafında egzoz gazının döndürdüğü türbin, diğer tarafında aynı mile bağlı kompresör bulunur. Kompresör havayı sıkıştırarak motora basar. Sıkışan hava ısındığı için çoğu araçta önce <b>intercooler</b> denilen bir soğutucudan geçirilir. Turbo mili dakikada yüz binlerce devire çıkabildiği için yağlama hayati önemdedir."]),
  ("Turbo arızası belirtileri", [
   {"liste": ["Belirgin güç kaybı, aracın çekişten düşmesi",
              "Gaza basınca ıslık ya da siren benzeri ses",
              "Egzozdan mavimsi duman, yağ tüketimi",
              "Göstergede güç azaltma (acil mod) uyarısı",
              "Turbo hortumlarında yağlanma"]},
   "Bu belirtilerin hepsi turbonun bozulduğu anlamına gelmez. Patlak bir turbo hortumu, intercooler kaçağı ya da arızalı bir sensör de aynı belirtileri verebilir. Turbo değiştirmeden önce bu bağlantılar mutlaka kontrol edilmelidir."]),
  ("Turboyu uzun ömürlü kullanmak", [
   {"liste": ["Motor yağını ve filtresini zamanında, doğru sınıf yağla değiştirin.",
              "Soğuk motorla yüksek devirde zorlamayın.",
              "Uzun ve yüklü bir sürüşten sonra motoru kapatmadan önce 30–60 saniye rölantide bekletin.",
              "Hava filtresini temiz tutun; içeri giren toz turbo kanatlarını aşındırır."]}]),
 ],
 sss=[("Turbo arızası motoru etkiler mi?", "Evet. Dağılan bir turbo, parçalarını ya da yağını motora gönderebilir. Belirti başladığında aracı zorlamadan kontrol ettirmek gerekir."),
      ("Benzinli araçlarda da turbo var mı?", "Evet. Son yıllarda küçük hacimli benzinli motorların çoğu turboludur ve aynı bakım kurallarına tabidir.")]),
]
