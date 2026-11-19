EE463 - IRFB4110 MOSFET'e seri R + harici Schottky diyot testi
===============================================================
Kullanim:
  1. ZIP icindeki tum dosyalari AYNI klasore cikar.
  2. LTspice ile asagidaki .asc dosyalarindan birini ac.
  3. Run, sonra akim ve gerilimleri ayni calisma noktasinda karsilastir.

Dosyalar:
  IRFB4110_Parasitics_Snubber_BASELINE.asc         Orijinal parasitikli + RC snubber'li devre.
  IRFB4110_Parasitics_Snubber_Diode_R_LOW.asc      Yalnizca LOW-SIDE X2'ye R + Schottky.
  IRFB4110_Parasitics_Snubber_Diode_R_BOTH.asc     X1 ve X2'nin ikisine de R + Schottky.
  IRFB4110_Snubber_BASELINE_NoL.asc                Tum parasitik L'ler temizce silinmis referans.
  IRFB4110_Snubber_Diode_R_BOTH_NoL.asc            Tum parasitik L'ler silinmis + iki diyot.

Yeni elemanlar:
  RLS_EXT = 0.02 ohm seri DLS_EXT (low-side MOSFET)
  RHS_EXT = 0.02 ohm seri DHS_EXT (high-side MOSFET, BOTH varyantinda)
  DSH_TEST = dusuk reverse-recovery davranisini taklit eden idealize edilmis
             Schottky diode modeli (GERCEK PARCA MODELI DEGIL).
  Diyotlarin KATOTU MOSFET DRAIN'e, ANOTU MOSFET SOURCE'a bakar.
  Her diyot MOSFET'in kendi D-S pinlerine baglidir; harici L parasitikleri
  diyot dalinin disindadir. D-S arasinda direncli paralel serbest-donus yolu.

Aynen korunanlar:
  IRFB4110PBF Infineon model, UCC27282 surucu, 24 V giris, 12 V surucu,
  100 kHz, HS %50 duty, 150 ns nominal dead-time,
  Rgon=22 ohm ve Roff=2.2 ohm (iki MOSFET),
  LHD=5 nH, LHS=3 nH, LLD=3 nH, LLS=5 nH,
  CIN=4.7 uF, RSN=4.7 ohm, CSN=1 nF, L1=68 uH, C2=100 uF, R1=2.4 ohm.

Karsilastirma icin:
  Ix(X1:D) ve Ix(X2:D): MOSFET drain akimlari
  I(DLS_EXT) ve I(DHS_EXT): harici diyot akimlari (BOTH varyantinda ikisi)
  V(HGATE,HSOURCE) ve V(LGATE,LSOURCE): gercek Vgs
  V(SW), V(VOUT), I(L1)
  Simulasyon penceresi: 1.8 ms - 2.0 ms (kararli durum yaklasimi)

UYARI:
  - Harici Schottky, body diode'un akimini azaltabilirse reverse recovery'yi
    azaltabilir; her durumda garanti degildir.
  - Bu modelin Tt=0 parametresi, minority carrier recovery icermedigini
    varsayar. Junction capacitance ve PCB parasitikleri hala onemlidir.
  - 0.02 ohm ornek seri direnctir; cok buyuk R, harici diyodu etkisiz kilar.
  - Gercek devre icin 48 V giris ve olasi overshoot'a gore yeterli Vrrm,
    surge akimi, termal ve PCB yerlesimi icin GERCEK diyot secilmelidir.
  - Bu dosyalar LTspice calistirilip dogrulanamadi; baglanti/netlist
    kontrolleri yapildi. Sonucu osiloskop benzeri grafikte teyit et.
