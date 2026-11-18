UCC27282 - LTspice starter package (Turkce)
=============================================

KAYNAK
- Yukledigin TI UCC27282 PSpice Transient Model (2018, unencrypted).
- Original dosya UCC27282_TI_original.lib, hicbir satiri degistirilmedi.
- UCC27282_LTspice.lib, PSpice -> LTspice sozdizimi uyarlamasi.
- UCC27282.asy, 9 girisli sembol.

BASLATMA (ONCELIKLE BUNU YAP)
1) ZIP'i Windows'ta bir klasore cikart. Butun dosyalar ayni klasorde kalsin.
2) LTspice 26 > File > Open > UCC27282_gate_test.cir.
3) Run'a bas. V(HI), V(LI), V(HO,HS), V(LO), V(GH,HS), V(GL), V(HB,HS) izle.
4) Hata varsa View > SPICE Error Log'u kopyala ve bana gonder.
5) Test basariliysa UCC27282_Rg_sweep.cir dosyasini ac; 2.2/4.7/10/22 ohm karsilastir.

GORSEL SEMATIK
- UCC27282_gate_test.asc dosyasi model sembolunu ve pin etiketlerini icerir.
- Test elemanlari alttaki SPICE direktifleriyle eklenmistir.
- LTspice sembolu bulamazsa UCC27282.asy'yi LTspice'in user symbol klasorune
  (or. Documents\LTspice\lib\sym) kopyalayip semayi yeniden ac.
- Sembolun 9 pin sirasi: LI HI EN VDD VSS HB HO HS LO.

DIKKAT
- Model 9 pinlidir; EN burada aktif (3.3V) tutulur. Fiziksel SOIC-8 UCC27282D'de
  EN pini yoktur. PCB pin numaralarini BU sembolden degil, TI datasheet'ten al.
- Testte HS=0, gercek MOSFET yerine 10nF dummy gate yukleri var.
- UCC27282'nin icinde bootstrap diyodu modellenmistir. CBOOT=470nF, HB-HS arasinda.
- Testte VDD=12V, f=100kHz, HI/LI icin 150ns komut dead time var.
- 150ns komut dead time = gercek MOSFET akim dead time demek degildir;
  gate plateau, propagation delay ve parasitikler nedeniyle dogrulanmalidir.
- Modelin PSpice'dan LTspice'a uyarlamasi yapildi fakat gercek LTspice
  motorunda calistirilamadi. Simulasyon sonucu kesin olarak dogrulanmis DEGIL.
- 48V -> 12V / 5A buck ve switching loss icin IRFB4110'un gercek SPICE
  modelini ve 47/68uH enduktor, 100uF cikis kapasitorunu ekleyecegiz.
- Sadece 10nF dummy gate testi ile Eon/Eoff, Vds overshoot veya verim bulunmaz.

SENTAKS UYARLAMASI
- Davranissal E/G VALUE kaynaklari LTspice B kaynaklarina donusturuldu.
- Ic ice parametre suslu parantezleri B ifadelerinde duzlestirildi.
- Bos 'PARAMS:' ifadesi dahili bootstrap diyotundan kaldirildi.
- Kullanilmayan yardimci alt devreler cikartildi. Ana model topolojisi korunuyor.

TASARIM NOTU
- Bu modelin EN girisi sadece makromodelin bir parcasidir; SOIC-8 fiziksel
  parcanin pin numaralariyla karistirma.
