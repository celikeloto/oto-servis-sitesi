"""Teknik rehber makaleleri (2/3): egzoz, aktarma organları, fren, süspansiyon, direksiyon, lastik."""

MAKALELER_2 = [
dict(slug="egzoz-dpf-egr-adblue", grup="Motor", hizmet="egzoz-dpf-egr",
 baslik="Egzoz sistemi, DPF, EGR ve AdBlue nedir?",
 meta="Dizel partikül filtresi (DPF) neden tıkanır, rejenerasyon nedir? EGR valfi, katalitik konvertör ve AdBlue sisteminin görevleri ile sık görülen arızalar.",
 ozet="Egzoz sistemi yanmış gazları dışarı atarken zararlı emisyonları da azaltır. Katalitik konvertör zehirli gazları dönüştürür, dizel partikül filtresi (DPF) isi tutar, EGR valfi egzozun bir kısmını tekrar yakarak azot oksitleri düşürür, AdBlue ise bazı dizellerde azot oksitleri suya ve azota çevirir.",
 bolumler=[
  ("Egzoz sistemindeki parçalar", [
   {"tablo": (["Parça", "Görevi"], [
     ["Egzoz manifoldu", "Silindirlerden çıkan gazları toplar"],
     ["Katalitik konvertör", "Karbon monoksit, hidrokarbon ve azot oksitleri daha zararsız gazlara dönüştürür"],
     ["DPF (dizel partikül filtresi)", "Dizel egzozundaki is (kurum) parçacıklarını tutar"],
     ["EGR valfi", "Egzoz gazının bir kısmını emmeye geri göndererek yanma sıcaklığını ve NOx'u düşürür"],
     ["Lambda (oksijen) sensörü", "Egzozdaki oksijeni ölçer; motor beyni karışımı buna göre ayarlar"],
     ["Susturucular", "Egzoz sesini azaltır"]])}]),
  ("DPF neden tıkanır? Rejenerasyon nedir?", [
   "DPF içinde biriken is, filtre belli bir doluluğa ulaşınca yüksek sıcaklıkta yakılır; buna <b>rejenerasyon</b> denir. Rejenerasyonun tamamlanması için motorun uzun süre çalışma sıcaklığında kalması gerekir. Sürekli kısa mesafe ve şehir içi dur-kalk kullanımda rejenerasyon yarım kalır ve filtre tıkanır.",
   {"liste": ["Göstergede DPF uyarı ışığı yanar.",
              "Araç güç azaltma (acil) moduna geçebilir.",
              "Yakıt tüketimi artar, motor fanı park halindeyken çalışmaya devam edebilir."]},
   "DPF uyarısı yandığında çoğu üretici, aracı birkaç kilometre boyunca sabit hızda ve orta devirde sürmeyi önerir. Uyarı sönmüyorsa servis rejenerasyonu ya da filtre temizliği gerekir. Doğru yağ kullanımı (düşük kül içerikli) DPF ömrünü uzatır."]),
  ("EGR arızası belirtileri", [
   {"liste": ["Rölantide titreme ve stop etme", "Hızlanırken güç kaybı", "Egzozdan siyah duman", "Motor arıza ışığı"]},
   "EGR valfi zamanla isle kaplanıp takılı kalabilir. Temizlik çoğu zaman yeterli olur; valf ya da motoru arızalıysa değişim gerekir."]),
  ("AdBlue nedir?", [
   "AdBlue, yüzde 32,5 oranında üre içeren saf su çözeltisidir. SCR sistemli dizel araçlarda ayrı bir depodan egzoza püskürtülür ve azot oksitleri azot ve su buharına çevirir. Depo boşalırsa ya da sistem arızalanırsa çoğu araç belirli bir süre sonra yeniden çalıştırmaya izin vermez; bu yüzden uyarı geldiğinde AdBlue eklenmelidir. AdBlue yakıt deposuna kesinlikle konmamalıdır."]),
 ],
 sss=[("DPF iptali yapılır mı?", "Hayır. DPF'nin sökülmesi ya da yazılımla devre dışı bırakılması yasal değildir, egzoz emisyon testinde aracın kalmasına yol açar ve çevreye zarar verir. Doğru çözüm temizlik ya da onarımdır."),
      ("Egzozdan su damlaması normal mi?", "Motor soğukken kısa süre su damlaması normaldir; yanma sırasında oluşan su buharı soğuk egzozda yoğunlaşır.")]),

dict(slug="debriyaj", grup="Aktarma organları", hizmet="debriyaj",
 baslik="Debriyaj nasıl çalışır? Debriyaj kaçırması ve ömrü",
 meta="Debriyaj seti hangi parçalardan oluşur, neden aşınır ve kaç km dayanır? Debriyaj kaçırma, sertleşme, titreme belirtileri ve debriyajı uzun ömürlü kullanma yolları.",
 ozet="Manuel vitesli araçlarda debriyaj, motor ile şanzıman arasındaki bağlantıyı kurup keser. Debriyaj seti; baskı, disk (balata) ve rulmandan oluşur. Kullanım şekline göre genellikle 100.000–150.000 km dayanır; şehir içi dur-kalk ve yokuş kalkışları ömrü kısaltır.",
 bolumler=[
  ("Debriyajın parçaları", [
   {"liste": ["<b>Volan:</b> Krank miline bağlı ağır disk; debriyajın sürtündüğü yüzeydir. Bazı araçlarda çift kütleli volan kullanılır.",
              "<b>Debriyaj diski (balata):</b> Volan ile baskı arasında sıkışarak gücü şanzımana iletir.",
              "<b>Baskı (balata baskısı):</b> Diski volana bastıran yaylı parça.",
              "<b>Debriyaj rulmanı:</b> Pedala basıldığında baskıyı iterek bağlantıyı keser.",
              "<b>Halat ya da hidrolik merkez:</b> Pedal hareketini rulmana iletir."]}]),
  ("Debriyaj bitiyor mu? Belirtiler", [
   {"tablo": (["Belirti", "Olası neden"], [
     ["Gaza basınca devir yükseliyor, araç hızlanmıyor", "Debriyaj diski aşınmış (kaçırma)"],
     ["Pedal çok yukarıda tutuyor", "Disk aşınması"],
     ["Pedal sertleşti", "Baskı ya da halat sorunu"],
     ["Pedala basınca vınlama sesi", "Debriyaj rulmanı"],
     ["Kalkışta titreme", "Disk, baskı ya da çift kütleli volan"],
     ["Yanık balata kokusu", "Debriyajın yarım basılı kullanılması ya da kaçırma"]])}]),
  ("Debriyajı uzun ömürlü kullanmak", [
   {"liste": ["Trafikte beklerken vitesi boşa alıp ayağınızı pedaldan çekin.",
              "Yokuşta aracı debriyajla tutmayın; el frenini ya da yokuş kalkış desteğini kullanın.",
              "Kalkışta gereğinden yüksek devirle debriyajı kaydırmayın.",
              "Sürüş sırasında ayağınızı debriyaj pedalının üzerinde dinlendirmeyin."]}]),
 ],
 sss=[("Debriyaj değişirken volan da değişmeli mi?", "Volan aşınmış, yüzeyi yanmış ya da çift kütleli volanda boşluk varsa değişmelidir. Debriyaj söküldüğünde volan mutlaka kontrol edilir."),
      ("Otomatik araçlarda debriyaj var mı?", "Tork konvertörlü otomatiklerde klasik debriyaj yoktur. Çift kavramalı (DSG, EDC, Powershift gibi) şanzımanlarda ise içerde iki debriyaj bulunur ve bunlar da aşınabilir.")]),

dict(slug="sanziman-turleri", grup="Aktarma organları", hizmet="sanziman",
 baslik="Şanzıman türleri: manuel, otomatik, çift kavramalı ve CVT",
 meta="Manuel, tork konvertörlü otomatik, çift kavramalı (DSG/EDC) ve CVT şanzıman arasındaki farklar. Şanzıman yağı değişimi ve şanzıman arızası belirtileri.",
 ozet="Şanzıman, motorun gücünü tekerleklere farklı oranlarda aktarır. Otomobillerde dört ana tip bulunur: manuel, tork konvertörlü otomatik, çift kavramalı (DSG, EDC, Powershift gibi) ve CVT. Hepsinin bakım ihtiyacı ve arıza belirtileri farklıdır.",
 bolumler=[
  ("Şanzıman türleri", [
   {"tablo": (["Tür", "Nasıl çalışır?", "Dikkat edilecekler"], [
     ["Manuel", "Vitesleri sürücü debriyajla değiştirir", "Debriyaj ve senkromeç aşınması"],
     ["Tork konvertörlü otomatik", "Hidrolik tork konvertörü ve planet dişlilerle çalışır", "Şanzıman yağı (ATF) değişimi"],
     ["Çift kavramalı (DSG/EDC vb.)", "Biri tek, biri çift vitesleri yöneten iki debriyaj", "Kavrama ve mekatronik ünite; kalkışta titreme"],
     ["CVT", "Kayış ya da zincir ve kasnaklarla kademesiz oran", "Özel CVT yağı; aşırı zorlamaya hassastır"],
     ["Robotize (yarı otomatik)", "Manuel şanzımanı ve debriyajı elektronik kumanda yönetir", "Debriyaj ayarı ve aktüatör"]])}]),
  ("Şanzıman yağı değişmeli mi?", [
   "Bazı üreticiler şanzıman yağını 'ömür boyu' olarak belirtse de yağ zamanla ısıyla bozulur. Özellikle otomatik, çift kavramalı ve CVT şanzımanlarda yağ ve filtre değişimi, üreticiye göre genellikle 60.000–100.000 km aralığında önerilir. Her şanzıman tipi için doğru yağın kullanılması şarttır; yanlış yağ ciddi arızaya yol açar."]),
  ("Şanzıman arızası belirtileri", [
   {"liste": ["Vites geçişlerinde gecikme, sert vuruntu ya da kayma",
              "Manuel viteste vites girerken ses, vitesten çıkma",
              "Şanzımandan uğultu ya da ıslık sesi",
              "Göstergede şanzıman uyarısı ya da aracın tek viteste kalması (acil mod)",
              "Araç altında kırmızımsı yağ lekesi (otomatik şanzıman yağı)"]},
   "Belirti başladığında erken kontrol, çoğu zaman pahalı bir revizyonun önüne geçer."]),
 ],
 sss=[("Otomatik araç çekiciyle nasıl çekilmeli?", "Otomatik vitesli araçların tekerlekleri yerde sürüklenerek uzun mesafe çekilmesi şanzımana zarar verebilir. Mümkünse platformlu çekici kullanılmalıdır."),
      ("DSG titremesi neden olur?", "Kalkışta titreme çoğunlukla kavrama aşınması, mekatronik ünite ya da yazılım ayarından kaynaklanır. Cihazla teşhis gerekir.")]),

dict(slug="aks-saft-diferansiyel", grup="Aktarma organları", hizmet="sanziman",
 baslik="Aks, şaft ve diferansiyel: dönüşte gelen tıkırtı",
 meta="Aks körüğü, aks kafası, şaft ve diferansiyel ne işe yarar? Dönüşlerde gelen tıkırtı, titreşim ve uğultu belirtileri ile aks körüğü yırtılmasının önemi.",
 ozet="Aks, şanzımandan gelen gücü tekerleğe taşır; tekerleğin hem dönmesine hem de direksiyonla yön değiştirmesine izin veren eklemleri (aks kafaları) vardır. Dönüşlerde gelen tıkırtı çoğunlukla aşınmış aks kafasının işaretidir.",
 bolumler=[
  ("Parçalar ve görevleri", [
   {"liste": ["<b>Aks mili:</b> Önden çekişli araçlarda şanzımandan tekerleğe giden mil.",
              "<b>Aks kafası (homokinetik mafsal):</b> Tekerlek dönerken ve yön değiştirirken gücün kesintisiz aktarılmasını sağlar.",
              "<b>Aks körüğü:</b> Aks kafasındaki gresi içeride, suyu ve tozu dışarıda tutan kauçuk kılıf.",
              "<b>Şaft:</b> Arkadan ya da dört çekişli araçlarda gücü arka diferansiyele taşır.",
              "<b>Diferansiyel:</b> Virajda iç ve dış tekerleklerin farklı hızlarda dönmesine izin verir."]}]),
  ("Aks körüğü neden önemli?", [
   "Yırtılan bir aks körüğünden gres dışarı kaçar, içeri toz ve su girer. Kısa sürede aks kafası aşınır. Körük erken fark edilirse yalnızca körük ve gres değişimiyle sorun çözülür; geç kalınırsa aks kafası ya da komple aks değişir. Tekerlek içinde gres sıçrantısı görmek erken bir işarettir."]),
  ("Belirtiler", [
   {"tablo": (["Belirti", "Olası neden"], [
     ["Tam dönüşte tık tık sesi", "Dış aks kafası aşınmış"],
     ["Hızlanırken titreşim", "İç aks kafası ya da motor takozu"],
     ["Belli hızda uğultu", "Teker rulmanı ya da diferansiyel"],
     ["Vites değişirken ya da kalkışta vuruntu", "Şaft mafsalı, takoz ya da diferansiyel boşluğu"]])}]),
 ],
 sss=[("Aks tıkırtısıyla yola devam edilir mi?", "Kısa süre devam edilebilir, ancak aşınma ilerledikçe aks kafası dağılabilir ve araç yolda kalabilir. Erken kontrol daha ucuzdur."),
      ("Teker rulmanı sesi nasıl anlaşılır?", "Hız arttıkça artan, virajda bir yöne dönünce değişen uğultu genellikle teker rulmanıdır.")]),

dict(slug="fren-sistemi", grup="Fren, süspansiyon ve direksiyon", hizmet="fren-yuruyen",
 baslik="Fren sistemi rehberi: balata, disk, hidrolik ve ABS",
 meta="Fren balatası kaç km'de değişir, fren diski ne zaman yenilenir? Fren hidroliği (DOT 4) değişim aralığı, ABS ve fren arızası belirtileri.",
 ozet="Fren sistemi, pedala basıldığında hidrolik basınçla kaliperleri sıkıştırarak balataları diske bastırır. Balatalar genellikle sürtünme malzemesi yaklaşık 3 mm'ye indiğinde, diskler ise üzerinde yazan minimum kalınlığın altına düştüğünde değiştirilir. Fren hidroliği nem çektiği için yaklaşık 2 yılda bir yenilenmelidir.",
 bolumler=[
  ("Fren sisteminin parçaları", [
   {"tablo": (["Parça", "Görevi", "Tipik ömür / kontrol"], [
     ["Balata", "Diske sürtünerek aracı yavaşlatır", "Kullanıma göre 20.000–60.000 km; yaklaşık 3 mm'de değişir"],
     ["Fren diski", "Balatanın sürtündüğü dönen disk", "Üzerindeki 'MIN TH' değerinin altına inince değişir; genellikle 2 balata ömrü"],
     ["Kaliper", "Hidrolik basınçla balatayı diske bastırır", "Sıkışma ve kaçak kontrolü"],
     ["Fren hidroliği", "Pedal kuvvetini kaliperlere taşır", "Genellikle 2 yılda bir (DOT 4 yaygın)"],
     ["Kampana ve pabuç", "Bazı araçların arka frenlerinde disk yerine kullanılır", "Aşınma ve ayar kontrolü"],
     ["ABS sensörleri", "Tekerlek hızını ölçer, frende kilitlenmeyi önler", "Arıza halinde ABS ışığı yanar"]])}]),
  ("Fren arızası belirtileri", [
   {"liste": ["<b>İnce, metalik gıcırtı:</b> Balata aşınma uyarı sacı diske değiyor olabilir.",
              "<b>Sürtünme, öğütme sesi:</b> Balata bitmiş, metal diske sürtüyor; acil kontrol gerekir.",
              "<b>Frende direksiyon titremesi:</b> Disk yüzeyinde eğrilik ya da düzensiz aşınma.",
              "<b>Araç frende bir tarafa çekiyor:</b> Kaliper sıkışması ya da tek taraflı aşınma.",
              "<b>Pedal derine gidiyor ya da süngerimsi:</b> Hidrolikte hava, kaçak ya da eskimiş hidrolik."]}]),
  ("Fren hidroliği neden değişmeli?", [
   "Fren hidroliği havadaki nemi çeker. İçindeki su oranı arttıkça kaynama noktası düşer; uzun yokuş inişlerinde ya da ardı ardına sert frenlerde hidrolik kaynayarak buhar kabarcığı oluşturur ve pedal boşa gider. Bu yüzden kilometre dolmasa da genellikle 2 yılda bir değiştirilmesi önerilir."]),
  ("ABS ve ESP nedir?", [
   "ABS, ani frende tekerleklerin kilitlenmesini önleyerek direksiyon hâkimiyetini korur; ABS devredeyken pedalda titreşim hissetmek normaldir. ESP ise aracın savrulmaya başladığını sezip tek tek tekerleklere fren uygulayarak aracı toparlar. Göstergede ABS ya da ESP ışığı sürekli yanıyorsa bu sistemler devre dışıdır; normal fren çalışır ama güvenlik desteği yoktur."]),
 ],
 sss=[("Balata değişince disk de değişmeli mi?", "Disk minimum kalınlığın üzerindeyse ve yüzeyi düzgünse değişmesi gerekmez. Ancak genellikle iki balata değişiminde bir disk değişimi gerekir. Diskler ve balatalar her zaman aynı aksta çift taraflı değiştirilir."),
      ("Fren sesi her zaman arıza mıdır?", "Hayır. Yağmurdan sonra ya da sabah ilk frenlerde diskteki ince pas nedeniyle kısa süreli ses normaldir. Sürekli ses ya da sürtünme kontrol gerektirir.")]),

dict(slug="suspansiyon", grup="Fren, süspansiyon ve direksiyon", hizmet="suspansiyon-direksiyon",
 baslik="Süspansiyon rehberi: amortisör, yay, salıncak ve rotil",
 meta="Amortisör ne zaman değişir, süspansiyon sesi neden gelir? Amortisör testi, salıncak burcu, rotil, viraj demiri ve süspansiyon arızası belirtileri.",
 ozet="Süspansiyon, yoldaki darbeleri emerek tekerleklerin yola temasını korur ve sürüş konforunu sağlar. Yaylar aracın ağırlığını taşır, amortisörler yayların salınımını söndürür. Aşınmış amortisör fren mesafesini uzatır ve yol tutuşunu azaltır.",
 bolumler=[
  ("Parçalar", [
   {"tablo": (["Parça", "Görevi"], [
     ["Helezon yay", "Aracın ağırlığını taşır, darbeyi karşılar"],
     ["Amortisör", "Yayın salınımını söndürür; aracın sekmesini engeller"],
     ["Amortisör takozu ve rulmanı", "Amortisörün gövdeye bağlantısı; direksiyonla döner"],
     ["Salıncak ve burçları", "Tekerleği gövdeye bağlar, hareketini yönlendirir"],
     ["Rotil", "Salıncak ile porya arasındaki küresel mafsal"],
     ["Viraj demiri ve bağlantı çubukları", "Virajda gövdenin yatmasını azaltır"]])}]),
  ("Amortisör bitti mi? Basit kontrol", [
   {"liste": ["Aracın bir köşesine sertçe bastırıp bırakın; araç bir kez yükselip durmalı. Birkaç kez sekiyorsa amortisör zayıflamıştır.",
              "Amortisör gövdesinde yağ sızıntısı olup olmadığına bakın.",
              "Lastiklerde dalgalı, testere dişi gibi düzensiz aşınma amortisör zayıflığına işaret edebilir.",
              "Frende aracın burnunun aşırı dalması da bir belirtidir."]},
   "Amortisörler kullanıma göre genellikle 80.000–100.000 km civarında kontrol edilmeli, aynı aks üzerinde çift olarak değiştirilmelidir."]),
  ("Süspansiyondan gelen sesler", [
   {"tablo": (["Ses", "Olası neden"], [
     ["Çukurlarda tok vuruntu", "Amortisör takozu, salıncak burcu ya da viraj demiri lastiği"],
     ["Direksiyonu çevirirken çıtırtı", "Amortisör rulmanı ya da yay oturağı"],
     ["Kasislerde gıcırtı", "Kuruyan burçlar"],
     ["Bozuk yolda takırtı", "Viraj demiri bağlantı çubukları ya da rotil"]])}]),
 ],
 sss=[("Tek amortisör değiştirilir mi?", "Önerilmez. Aynı akstaki iki amortisör farklı sönümleme yaparsa araç dengesiz davranır. Ön ya da arka çift olarak değiştirilmelidir."),
      ("Süspansiyon onarımından sonra rot ayarı gerekir mi?", "Salıncak, rot, rotil ya da amortisör gibi tekerlek açısını etkileyen parçalar değiştiğinde ön düzen (rot) ayarı yaptırılması gerekir.")]),

dict(slug="direksiyon-rot-ayari", grup="Fren, süspansiyon ve direksiyon", hizmet="suspansiyon-direksiyon",
 baslik="Direksiyon sistemi ve rot ayarı: araç neden bir tarafa çeker?",
 meta="Hidrolik ve elektrikli direksiyon farkı, rot ve rotil arızaları, rot (ön düzen) ayarı nedir ve ne zaman yapılır? Toe, kamber ve kaster açıları sade anlatımla.",
 ozet="Direksiyon sistemi, direksiyon simidinin hareketini rotlar aracılığıyla tekerleklere iletir. Rot (ön düzen) ayarı ise tekerleklerin açılarını üretici değerlerine getirir; ayarı bozuk araç bir tarafa çeker ve lastikleri düzensiz aşındırır.",
 bolumler=[
  ("Direksiyon sistemleri", [
   {"liste": ["<b>Hidrolik direksiyon:</b> Motorla çalışan bir pompa hidrolik basınçla direksiyonu hafifletir. Hidrolik yağı seviyesi ve kaçaklar kontrol edilmelidir.",
              "<b>Elektrikli direksiyon (EPS):</b> Elektrik motoruyla destek verir; yağ gerektirmez, arızası genellikle göstergede uyarı ve ağırlaşan direksiyon olarak görülür.",
              "<b>Direksiyon kutusu (kremayer):</b> Simidin dönme hareketini rotlara iletir.",
              "<b>Rot ve rot başı:</b> Kutudan tekerleğe giden bağlantı çubukları."]}]),
  ("Rot ayarı nedir?", [
   "Rot ayarı ya da ön düzen ayarı, tekerleklerin yola ve birbirine göre açılarının ölçülüp düzeltilmesidir. Temel açılar şunlardır:",
   {"tablo": (["Açı", "Ne demek?", "Bozuksa"], [
     ["Toe (yakınsama)", "Tekerleklerin yukarıdan bakınca içe ya da dışa dönüklüğü", "Lastik iç ya da dış kenardan hızlı aşınır"],
     ["Kamber", "Tekerleğin önden bakınca içe ya da dışa yatıklığı", "Lastik tek kenardan aşınır"],
     ["Kaster", "Direksiyon ekseninin yandan bakınca eğimi", "Direksiyon kendini toparlamaz, araç dengesiz gider"]])}]),
  ("Ne zaman rot ayarı yapılmalı?", [
   {"liste": ["Araç düz yolda bir tarafa çekiyorsa",
              "Düz giderken direksiyon simidi ortada durmuyorsa",
              "Lastikler kenarlardan düzensiz aşınıyorsa",
              "Sert bir çukura ya da kaldırıma çarptıktan sonra",
              "Rot, rotil, salıncak ya da amortisör değiştirildikten sonra",
              "Yeni lastik takıldığında (önerilir)"]}]),
  ("Rot ayarı ile balans ayarı aynı şey mi?", [
   "Hayır. Balans, tekerleğin kendi etrafında dengeli dönmesini sağlar; balansı bozuk tekerlek belli hızlarda direksiyonda titreme yapar. Rot ayarı ise tekerleklerin açısıyla ilgilidir; bozuksa araç çeker ve lastik aşınır. İkisi sıkça birlikte yapılır ama farklı işlemlerdir."]),
 ],
 sss=[("Direksiyon ağırlaştı, neden olabilir?", "Hidrolik direksiyonda yağ eksikliği ya da pompa arızası, elektrikli direksiyonda motor ya da sensör arızası, ayrıca lastik basıncının düşük olması direksiyonu ağırlaştırabilir."),
      ("Direksiyonda boşluk tehlikeli mi?", "Evet. Rot başı, rotil ya da direksiyon kutusundaki boşluk aracın hâkimiyetini azaltır. Gecikmeden kontrol ettirilmelidir.")]),

dict(slug="lastik-rehberi", grup="Fren, süspansiyon ve direksiyon", hizmet="lastik-balans",
 baslik="Lastik rehberi: ebat okuma, diş derinliği, basınç ve balans",
 meta="205/55 R16 91V ne demek? Lastik üretim tarihi, yasal diş derinliği (1,6 mm), doğru lastik basıncı, balans, lastik tamiri ve kış lastiği rehberi.",
 ozet="Lastik, aracın yolla temas eden tek parçasıdır. Türkiye'de yasal en düşük diş derinliği 1,6 mm'dir; güvenlik için yaz lastiğinde 3 mm, kış lastiğinde 4 mm altına inmeden değişim önerilir. Doğru basınç, aracın kapı direğindeki ya da yakıt kapağı içindeki etikette yazar ve lastik soğukken ölçülmelidir.",
 bolumler=[
  ("Lastik ebatı nasıl okunur?", [
   "Lastiğin yanağında örneğin <b>205/55 R16 91V</b> yazar:",
   {"tablo": (["Kod", "Anlamı"], [
     ["205", "Lastik genişliği (mm)"],
     ["55", "Yanak yüksekliğinin genişliğe oranı (%)"],
     ["R", "Radyal yapı"],
     ["16", "Jant çapı (inç)"],
     ["91", "Yük endeksi: lastik başına taşıyabileceği yük (91 = 615 kg)"],
     ["V", "Hız endeksi: izin verilen en yüksek hız (V = 240 km/s)"]])},
   "Lastiğin üretim tarihi, yanaktaki <b>DOT</b> kodunun son dört hanesinden okunur: <b>2423</b>, 2023 yılının 24. haftası demektir. Kullanılmasa bile lastik kauçuğu zamanla sertleşir; 5–6 yaşını geçen lastikler dikkatle kontrol edilmelidir."]),
  ("Diş derinliği ve mevsim lastiği", [
   {"liste": ["Yasal sınır 1,6 mm'dir; lastik oluklarındaki aşınma göstergesi (TWI) bu seviyeyi gösterir.",
              "Islak yolda tutuş 3 mm'nin altında belirgin şekilde azalır.",
              "Kış lastiği, 7 °C'nin altındaki sıcaklıklarda daha iyi tutunmak için yumuşak hamurla üretilir; 4 mm'nin altında kış performansı düşer.",
              "Dört lastiğin aynı tip ve mümkünse aynı aşınmada olması önerilir."]}]),
  ("Lastik basıncı", [
   "Doğru basınç değeri araca özeldir ve sürücü kapısı direğindeki, yakıt kapağının içindeki ya da kullanım kılavuzundaki etikette yazar. Basınç ayda bir ve uzun yola çıkmadan önce, lastik soğukken kontrol edilmelidir. Düşük basınç yakıt tüketimini artırır, lastiği kenarlardan aşındırır ve ısınarak patlama riskini yükseltir; yüksek basınç ise tutuşu azaltır ve lastiği ortadan aşındırır."]),
  ("Lastik tamiri: ne zaman tamir, ne zaman değişim?", [
   {"tablo": (["Durum", "Tamir edilebilir mi?"], [
     ["Diş bölgesinde çivi ya da vida deliği (küçük çaplı)", "Genellikle evet, içten yama ile kalıcı tamir"],
     ["Lastik yanağında kesik, şişlik ya da delik", "Hayır, lastik değişmeli"],
     ["Basıncı çok düşük ya da patlak halde uzun süre sürülmüş lastik", "Genellikle hayır; iç yapısı zarar görmüş olabilir"],
     ["Büyük yırtık ya da birden fazla yakın delik", "Hayır"]])},
   "Lastik tamir spreyi ya da kiti yalnızca en yakın servise ulaşmak için geçici çözümdür."]),
  ("Balans ayarı nedir?", [
   "Lastik ve jant üzerindeki ağırlık hiçbir zaman tam eşit dağılmaz. Balans makinesi bu dengesizliği ölçer, jantın uygun noktalarına küçük ağırlıklar takılarak tekerlek dengelenir. Balansı bozuk tekerlek genellikle 80–120 km/s arasında direksiyonda titremeye yol açar. Lastik değişiminde, tamirinden sonra ve titreme hissedildiğinde balans yapılmalıdır."]),
 ],
 sss=[("Lastikler kaç yılda değişmeli?", "Diş derinliği yeterli olsa bile üretim tarihinden itibaren 5–6 yılı geçen lastikler çatlak ve sertleşme açısından kontrol edilmeli, 8–10 yılı geçenler değiştirilmelidir."),
      ("Lastik patlarsa ne yapmalıyım?", "Direksiyonu sıkı tutun, sert fren yapmadan yavaşlayın ve güvenli bir yere çekin. Dörtlüleri yakın, reflektörü koyun. Stepne yoksa ya da değiştirmek güvenli değilse yol yardımı çağırın.")]),
]
