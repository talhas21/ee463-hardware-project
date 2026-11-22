# KiCad PCB Analiz Raporu: `synchronous_buck.kicad_pcb`

## 1. Kart Boyutları ve Katman Yapısı
- **Kart Sınırı (Edge.Cuts):** 106.50 mm x 95.50 mm (X: 76.0..182.5, Y: 62.0..157.5)
- **Bakır Katmanlar (4):** F.Cu (signal), In1.Cu (power), In2.Cu (signal), B.Cu (signal)
- **Toplam Eleman:** 56 | **Yol Segmenti:** 223 | **Via:** 20 | **Zone:** 4

## 2. Bakır Dolgular (Copper Zones)
- **Net:** `GND` | **Katman:** F.Cu | **Durum:** Dolu (Filled)
- **Net:** `/V_OUT` | **Katman:** F.Cu | **Durum:** Dolu (Filled)
- **Net:** `GND` | **Katman:** In1.Cu | **Durum:** Dolu (Filled)
- **Net:** `GND` | **Katman:** In2.Cu | **Durum:** Dolu (Filled)

## 3. Net Bazlı Yol (Track) ve Via Özeti
| Net Adı | Pad Sayısı | Segment | Toplam Uzunluk (mm) | Yol Kalınlıkları (mm) | Kullanılan Katmanlar | Via Sayısı |
| :--- | :---: | :---: | :---: | :--- | :--- | :---: |
| `GND` | 43 | 27 | 61.9 | 0.25, 0.5, 0.8 | F.Cu | 14 |
| `+12V` | 10 | 26 | 180.2 | 1 | B.Cu, F.Cu | 1 |
| `/48V_BUS` | 10 | 23 | 88.0 | 1, 1.5, 2 | B.Cu, F.Cu | 1 |
| `Net-(Q2-SOURCE)` | 7 | 16 | 57.4 | 0.5, 0.8, 1, 2, 3 | F.Cu | 0 |
| `/HI_PWM` | 2 | 14 | 137.8 | 0.5 | B.Cu, F.Cu | 1 |
| `/V_SENSE` | 5 | 14 | 95.5 | 0.25, 0.3 | F.Cu | 0 |
| `/LO_PWM` | 2 | 12 | 95.0 | 0.5 | B.Cu, F.Cu | 1 |
| `/LOAD_RTRN` | 3 | 9 | 36.0 | 0.5, 4 | F.Cu | 0 |
| `+5V` | 4 | 8 | 40.1 | 1.5 | B.Cu, F.Cu | 0 |
| `/I_SENSE` | 3 | 8 | 76.3 | 0.3 | F.Cu | 0 |
| `Net-(R12-Pad2)` | 3 | 7 | 24.4 | 0.3 | F.Cu | 0 |
| `Net-(U3-HO)` | 3 | 7 | 15.8 | 0.5 | B.Cu, F.Cu | 2 |
| `Net-(D1-A)` | 4 | 6 | 15.4 | 0.3 | F.Cu | 0 |
| `Net-(D2-K)` | 3 | 5 | 26.1 | 1 | F.Cu | 0 |
| `Net-(D3-A)` | 3 | 5 | 30.7 | 0.5 | F.Cu, In2.Cu | 0 |
| `Net-(D4-A)` | 3 | 4 | 22.8 | 0.5 | B.Cu, F.Cu | 0 |
| `Net-(Q1-DRAIN)` | 2 | 4 | 14.2 | 2 | F.Cu | 0 |
| `Net-(U4A--)` | 3 | 4 | 6.3 | 0.3 | F.Cu | 0 |
| `Net-(U4B-+)` | 3 | 4 | 7.3 | 0.3 | F.Cu | 0 |
| `+48V` | 2 | 3 | 10.5 | 2 | F.Cu | 0 |
| `Net-(D3-K)` | 2 | 3 | 12.6 | 0.5 | F.Cu | 0 |
| `Net-(U3-LO)` | 3 | 3 | 7.6 | 0.5 | F.Cu | 0 |
| `Net-(U4B--)` | 3 | 3 | 8.1 | 0.3, 0.5 | F.Cu | 0 |
| `Net-(C11-Pad1)` | 2 | 2 | 4.1 | 0.8 | F.Cu | 0 |
| `Net-(D4-K)` | 2 | 2 | 7.4 | 0.5 | F.Cu | 0 |
| `Net-(D5-K)` | 2 | 2 | 13.5 | 1 | F.Cu | 0 |
| `Net-(U3-HB)` | 2 | 2 | 4.2 | 0.5 | F.Cu | 0 |
| `/V_OUT` | 8 | 0 | 0.0 | - | Yol Yok (Unrouted) | 0 |

## 4. Bağlantısız (Unconnected) Pinler
- A1-Pin4 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO2-Pad4)`
- A1-Pin5 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO3-Pad5)`
- A1-Pin6 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO4-Pad6)`
- A1-Pin7 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO5-Pad7)`
- A1-Pin9 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO6-Pad9)`
- A1-Pin10 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO7-Pad10)`
- A1-Pin11 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO8-Pad11)`
- A1-Pin12 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO9-Pad12)`
- A1-Pin14 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO10-Pad14)`
- A1-Pin15 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO11-Pad15)`
- A1-Pin16 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO12-Pad16)`
- A1-Pin17 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO13-Pad17)`
- A1-Pin19 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO14-Pad19)`
- A1-Pin20 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO15-Pad20)`
- A1-Pin21 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO16-Pad21)`
- A1-Pin22 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO17-Pad22)`
- A1-Pin24 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO18-Pad24)`
- A1-Pin25 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO19-Pad25)`
- A1-Pin26 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO20-Pad26)`
- A1-Pin27 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO21-Pad27)`
- A1-Pin29 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO22-Pad29)`
- A1-Pin30 (RaspberryPi_Pico) -> `unconnected-(A1-RUN-Pad30)`
- A1-Pin34 (RaspberryPi_Pico) -> `unconnected-(A1-GPIO28_ADC2-Pad34)`
- A1-Pin35 (RaspberryPi_Pico) -> `unconnected-(A1-ADC_VREF-Pad35)`
- A1-Pin36 (RaspberryPi_Pico) -> `unconnected-(A1-3V3-Pad36)`
- A1-Pin37 (RaspberryPi_Pico) -> `unconnected-(A1-3V3_EN-Pad37)`
- A1-Pin40 (RaspberryPi_Pico) -> `unconnected-(A1-VBUS-Pad40)`

## 5. Via Ölçü Dağılımı
- **Çap/Delik:** 0.8 mm / 0.4 mm (F.Cu->B.Cu) — **20 adet**

## 6. Komponent Listesi ve Yerleşim
| Ref | Değer | Footprint | Katman | Konum (X, Y) | Rot | Pin Bağlantıları |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **A1** | RaspberryPi_Pico | `RaspberryPi_Pico_Common_THT` | F.Cu | (78.1, 148.5) | 90° | 1:/HI_PWM, 2:/LO_PWM, 3:GND, 4:unconnected-(A1-GPIO2-Pad4), 5:unconnected-(A1-GPIO3-Pad5), 6:unconnected-(A1-GPIO4-Pad6), 7:unconnected-(A1-GPIO5-Pad7), 8:GND, 9:unconnected-(A1-GPIO6-Pad9), 10:unconnected-(A1-GPIO7-Pad10), 11:unconnected-(A1-GPIO8-Pad11), 12:unconnected-(A1-GPIO9-Pad12), 13:GND, 14:unconnected-(A1-GPIO10-Pad14), 15:unconnected-(A1-GPIO11-Pad15), 16:unconnected-(A1-GPIO12-Pad16), 17:unconnected-(A1-GPIO13-Pad17), 18:GND, 19:unconnected-(A1-GPIO14-Pad19), 20:unconnected-(A1-GPIO15-Pad20), 21:unconnected-(A1-GPIO16-Pad21), 22:unconnected-(A1-GPIO17-Pad22), 23:GND, 24:unconnected-(A1-GPIO18-Pad24), 25:unconnected-(A1-GPIO19-Pad25), 26:unconnected-(A1-GPIO20-Pad26), 27:unconnected-(A1-GPIO21-Pad27), 28:GND, 29:unconnected-(A1-GPIO22-Pad29), 30:unconnected-(A1-RUN-Pad30), 31:/I_SENSE, 32:/V_SENSE, 33:GND, 34:unconnected-(A1-GPIO28_ADC2-Pad34), 35:unconnected-(A1-ADC_VREF-Pad35), 36:unconnected-(A1-3V3-Pad36), 37:unconnected-(A1-3V3_EN-Pad37), 38:GND, 39:+5V, 40:unconnected-(A1-VBUS-Pad40) |
| **C1** | 100uF 100V Electrolytic | `CP_Radial_D12.5mm_P5.00mm` | F.Cu | (116.7, 80.0) | 0° | 1:/48V_BUS, 2:GND |
| **C10** | 4.7uF 100V | `CP_Radial_D6.3mm_P2.50mm` | F.Cu | (117.8, 91.5) | 0° | 1:/48V_BUS, 2:GND |
| **C11** | 1nF 100V | `C_1206_3216Metric` | F.Cu | (161.0, 86.0) | -90° | 1:Net-(C11-Pad1), 2:GND |
| **C12** | 100nF 25V | `C_1206_3216Metric` | F.Cu | (166.5, 81.5) | 180° | 1:/V_OUT, 2:GND |
| **C13** | 100nF 25V | `C_1206_3216Metric` | F.Cu | (134.0, 98.5) | 90° | 1:+12V, 2:GND |
| **C14** | 4.7uF 25V | `CP_Radial_D10.0mm_P5.00mm` | F.Cu | (126.6, 115.0) | 0° | 1:+12V, 2:GND |
| **C15** | 100uF 25V | `CP_Radial_D6.3mm_P2.50mm` | F.Cu | (163.0, 66.0) | 0° | 1:/V_OUT, 2:GND |
| **C16** | 1nF 25V | `C_1206_3216Metric` | F.Cu | (97.5, 126.5) | 180° | 1:/V_SENSE, 2:GND |
| **C17** | 100nF 50V | `C_1206_3216Metric` | F.Cu | (165.5, 111.5) | -90° | 1:+12V, 2:GND |
| **C18** | 100nF 50V Ceramic | `C_1206_3216Metric` | F.Cu | (165.5, 103.0) | -90° | 1:Net-(U4B-+), 2:GND |
| **C19** | 100uF 25V | `CP_Radial_D6.3mm_P2.50mm` | F.Cu | (162.8, 75.0) | 0° | 1:/V_OUT, 2:GND |
| **C2** | 100nF Ceramic | `C_1206_3216Metric` | F.Cu | (130.5, 69.5) | -90° | 1:/48V_BUS, 2:GND |
| **C20** | 100nF 25V | `C_1206_3216Metric` | F.Cu | (166.5, 84.5) | 180° | 1:/V_OUT, 2:GND |
| **C21** | 100uF 25V | `CP_Radial_D6.3mm_P2.50mm` | F.Cu | (173.0, 82.3) | -90° | 1:/V_OUT, 2:GND |
| **C3** | 100uF 100V Electrolytic | `CP_Radial_D12.5mm_P5.00mm` | F.Cu | (106.5, 80.5) | 180° | 1:/48V_BUS, 2:GND |
| **C4** | 100nF 100V Ceramic | `C_1206_3216Metric` | F.Cu | (106.0, 88.5) | 180° | 1:/48V_BUS, 2:GND |
| **C5** | 470uF 25V Electrolytic | `CP_Radial_D10.0mm_P5.00mm` | F.Cu | (83.5, 85.9) | 90° | 1:+12V, 2:GND |
| **C6** | 100nF 50V Ceramic | `C_1206_3216Metric` | F.Cu | (91.0, 109.0) | -90° | 1:+12V, 2:GND |
| **C7** | 10uF 16V Electrolytic | `CP_Radial_D10.0mm_P5.00mm` | F.Cu | (82.5, 100.4) | 90° | 1:+5V, 2:GND |
| **C8** | 100nF 50V Ceramic | `C_1206_3216Metric` | F.Cu | (81.5, 112.0) | 90° | 1:+5V, 2:GND |
| **C9** | 0.1uF 25-50V Ceramic | `C_1206_3216Metric` | F.Cu | (129.5, 99.5) | 180° | 1:Net-(U3-HB), 2:Net-(Q2-SOURCE) |
| **D1** | BZX55C12-HT | `D_DO-35_SOD27_P7.62mm_Horizontal` | F.Cu | (127.0, 65.2) | -90° | 1:/48V_BUS, 2:Net-(D1-A) |
| **D2** | SR3100-HT | `D_DO-201AD_P15.24mm_Horizontal` | F.Cu | (119.5, 113.1) | 90° | 1:Net-(D2-K), 2:GND |
| **D3** | 1N5819-HT | `D_DO-41_SOD81_P10.16mm_Horizontal` | F.Cu | (145.5, 121.6) | 90° | 1:Net-(D3-K), 2:Net-(D3-A) |
| **D4** | 1N5819-HT | `D_DO-41_SOD81_P10.16mm_Horizontal` | F.Cu | (145.5, 108.1) | 90° | 1:Net-(D4-K), 2:Net-(D4-A) |
| **D5** | SR5100 | `D_DO-201AD_P15.24mm_Horizontal` | F.Cu | (157.1, 92.5) | 180° | 1:Net-(D5-K), 2:GND |
| **D6** | BZX55C3V3 | `D_DO-35_SOD27_P7.62mm_Horizontal` | F.Cu | (101.7, 121.5) | 0° | 1:/V_SENSE, 2:GND |
| **D7** | BZX55C3V3 | `D_DO-35_SOD27_P7.62mm_Horizontal` | F.Cu | (101.7, 125.5) | 0° | 1:/I_SENSE, 2:GND |
| **F1** | Fuse ?A Slow-Blow | `Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open` | F.Cu | (87.4, 67.6) | 0° | 1:+48V, 2:Net-(Q1-DRAIN) |
| **J1** | Screw_Terminal_01x02 | `TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal` | F.Cu | (78.5, 71.0) | 90° | 1:+48V, 2:GND |
| **J2** | Screw_Terminal_01x02 | `TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal` | F.Cu | (179.8, 67.0) | -90° | 1:/V_OUT, 2:/LOAD_RTRN |
| **L1** | 150uH | `L_12x12mm_H8mm` | F.Cu | (104.0, 108.0) | 180° | 1:Net-(D2-K), 2:+12V |
| **L2** | 68uH | `L_Toroid_Vertical_L24.6mm_W15.5mm_P11.44mm_Pulse_KM-4` | F.Cu | (146.0, 76.7) | 180° | 1:Net-(Q2-SOURCE), 2:/V_OUT |
| **Q1** | IRF5210PBF | `TO-220-3_Vertical` | F.Cu | (116.3, 68.8) | 0° | 1:Net-(D1-A), 2:Net-(Q1-DRAIN), 3:/48V_BUS |
| **Q2** | IRFB4110 | `TO-220-3_Vertical` | F.Cu | (138.5, 84.0) | 180° | 1:Net-(D4-A), 2:/48V_BUS, 3:Net-(Q2-SOURCE) |
| **Q3** | IRFB4110 | `TO-220-3_Vertical` | F.Cu | (130.5, 94.0) | 0° | 1:Net-(D3-A), 2:Net-(Q2-SOURCE), 3:GND |
| **R1** | 10k | `R_1206_3216Metric` | F.Cu | (115.0, 72.4) | 0° | 1:/48V_BUS, 2:Net-(D1-A) |
| **R10** | 10k | `R_1206_3216Metric` | F.Cu | (166.5, 96.0) | 0° | 1:/V_SENSE, 2:GND |
| **R11** | 0.005 | `R_2512_6332Metric` | F.Cu | (179.5, 83.5) | -90° | 1:/LOAD_RTRN, 2:GND |
| **R12** | 68k | `R_1206_3216Metric` | F.Cu | (180.0, 108.0) | -90° | 1:Net-(U4A--), 2:Net-(R12-Pad2) |
| **R13** | 1k | `R_1206_3216Metric` | F.Cu | (180.0, 102.5) | 90° | 1:Net-(U4A--), 2:GND |
| **R14** | 1k | `R_1206_3216Metric` | F.Cu | (161.5, 103.0) | -90° | 1:Net-(U4B-+), 2:Net-(R12-Pad2) |
| **R15** | 1k | `R_1206_3216Metric` | F.Cu | (162.0, 107.5) | 0° | 1:/I_SENSE, 2:Net-(U4B--) |
| **R2** | 15k | `R_1206_3216Metric` | F.Cu | (122.2, 72.4) | 0° | 1:Net-(D1-A), 2:GND |
| **R3** | 22 | `R_1206_3216Metric` | F.Cu | (138.5, 99.0) | 180° | 1:Net-(D4-A), 2:Net-(U3-HO) |
| **R4** | 22 | `R_1206_3216Metric` | F.Cu | (138.5, 108.0) | 180° | 1:Net-(D3-A), 2:Net-(U3-LO) |
| **R5** | 2.2 | `R_1206_3216Metric` | F.Cu | (138.5, 112.5) | 180° | 1:Net-(D3-K), 2:Net-(U3-LO) |
| **R6** | 2.2 | `R_1206_3216Metric` | F.Cu | (138.5, 103.5) | 180° | 1:Net-(D4-K), 2:Net-(U3-HO) |
| **R7** | 0.02 | `R_1206_3216Metric` | F.Cu | (145.5, 84.5) | 180° | 1:Net-(D5-K), 2:Net-(Q2-SOURCE) |
| **R8** | 4.7 | `R_2512_6332Metric` | F.Cu | (154.0, 84.5) | 180° | 1:Net-(C11-Pad1), 2:Net-(Q2-SOURCE) |
| **R9** | 56k | `R_1206_3216Metric` | F.Cu | (166.5, 91.0) | 180° | 1:/V_OUT, 2:/V_SENSE |
| **U1** | LM2596HVT-12 | `TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical` | F.Cu | (107.4, 92.0) | 180° | 1:/48V_BUS, 2:Net-(D2-K), 3:GND, 4:+12V, 5:GND |
| **U2** | L7805CV-DG | `TO-220-3_Vertical` | F.Cu | (85.5, 108.0) | -90° | 1:+12V, 2:GND, 3:+5V |
| **U3** | UCC27211DR | `SOIC-8_3.9x4.9mm_P1.27mm` | F.Cu | (132.0, 105.5) | -90° | 1:+12V, 2:Net-(U3-HB), 3:Net-(U3-HO), 4:Net-(Q2-SOURCE), 5:/HI_PWM, 6:/LO_PWM, 7:GND, 8:Net-(U3-LO) |
| **U4** | LM358 | `DIP-8_W7.62mm_Socket` | F.Cu | (176.3, 109.3) | 180° | 1:Net-(R12-Pad2), 2:Net-(U4A--), 3:/LOAD_RTRN, 4:GND, 5:Net-(U4B-+), 6:Net-(U4B--), 7:Net-(U4B--), 8:+12V |