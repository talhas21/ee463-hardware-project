EE463 - IRFB4110PBF URETICI MODELI ILE LTspice DEVRESI
========================================================

1) ZIP dosyasindaki tum dosyalari TEK klasore cikart.
2) LTspice > File > Open > GateDriver_recreated.asc
3) Run. .include IRFB4110PBF.spi ve .include UCC27282_LTspice.lib ayni klasorden okunur.
4) V(SW), V(VOUT), I(L1) ve -I(V2) incele.

Degisiklikler:
- Infineon'un kullanicinin indirdigi orijinal IRFB4110PBF.spi eklendi.
- Elle yazilan yaklasik .model IRFB4110 VDMOS(...) KALDIRILDI.
- M1/M2 yerine X1/X2 kullanildi: .SUBCKT irfb4110pbf 1 2 3
- Buck_NMOS_Subckt.asy yeni sembol; Prefix=X, pin sirasi D(1), G(2), S(3).
- Harici gate direncleri R2=R3=4.7 ohm, diger devre parametreleri ayni.

DOGRUDAN MOSFET DRAIN AKIMI ICIN:
- .SUBCKT modeline gecince eski Id(M1) ve Id(M2) izleri kullanilamaz.
- GateDriver_manufacturer_with_sense.cir dosyasini LTspice'ta acip Run yap.
- Burada VSH ve VSL isimli IDEAL 0V akim sensorleri vardir.
- I(VSH) = high-side drain akimi (VIN -> M1 drain),
  I(VSL) = low-side drain akimi (SW -> M2 drain).
- Netlist devresi, sema ile elektriksel olarak aynidir; 0V sensorler ideal olarak gerilim dusurmez.
- Karsilastirma icin ayni zaman araligi ve ayni PWM/gate direnci kullan.

MODELE ILISKIN:
- Modelin dahili RG direnci 5.39883 ohm; harici R2/R3 buna ilave olur.
- Body diode modelindeki TT=1e-07 (100 ns); bu deger fiziki reverse recovery suresiyle
  birebir esdeger olarak yorumlanmamalidir.
- Dosyada irfb4110pbft adli AYRI bir termal RC alt devresi vardir.
  Elektriksel MOSFET modeline otomatik bagli bir elektrotermal sim. degildir.
- Infineon modeli 2005 tarihli SPICE3 formatindadir; LTspice ile burada
  calistirilip dogrulanamadi. Olası uyumluluk hatalarini kontrol et.
- Devrenin bootstrap/driver modeli de fiziksel donanimda dogrulanmalidir.

GitHub'a *.asc, *.asy, *.lib, *.spi, *.cir ekle; *.raw dosyalarini ekleme.
