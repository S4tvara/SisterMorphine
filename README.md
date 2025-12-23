# SisterMorphine


| Band/Freq Range         | Modulation Type              | Equipment              | Typical Data Rate           | Why Used?                                        | Range                             |
| ----------------------- | ---------------------------- | ----------------------------------- | --------------------------- | ------------------------------------------------ | --------------------------------- |
| HF (2-30 MHz)           | SSB-SC (USB/LSB)             | BEL MHS 355, LHP 265DI, R&S M3UR    | 2.4-9.6 kbps voice          | Long-range ship-shore/sat, 50% BW savings        | 1000-5000 km (skywave) bel-india​ |
| VHF (30-300 MHz)        | FM (16TONE), AM, Digital SDR | SDR on MH-60R, Link-II VHF          | 16 kbps voice, 64 kbps data | Short-range ship-ship/helo, encrypted voice/data | 50-200 km LOS idrw​               |
| UHF (300 MHz-3 GHz)     | FM, Digital (HAVEQUICK II)   | Rohde & Schwarz NAVAL VHF/UHF       | 16-75 kbps                  | Anti-jam tactical voice/data                     | 100-400 km LOS rohde-schwarz​     |
| VLF (3-30 kHz)          | Advanced Digital (MSK/F SK)  | BEL VLF Modulator (INS Kattabomman) | 50-400 bps                  | Submarine comms through seawater                 | Global (submerged) bel-india​     |
| LF (30-300 kHz)         | CW, Narrowband FSK           | Legacy submarine wake detection     | 50 bps                      | Emergency buoy comms                             | 1000 km                           |
| Satellite (L/S/C bands) | BPSK/QPSK, DAMA              | INMARSAT, Link-II SATCOM            | 64 kbps-2 Mbps              | Beyond LOS, high data rate, imagery              | Global idrw​                      |



| Type | β (Mod Index) | Deviation | Bandwidth    | Navy Use Case                         |
| ---- | ------------- | --------- | ------------ | ------------------------------------- |
| NBFM | β < 0.3       | ±2.5 kHz  | ~4 kHz       | VHF ship-ship voice (25 kHz channels) |
| WBFM | β > 1-10      | ±75 kHz   | ~200 kHz     | Audio broadcast (not tactical)        |
| PM   | Fixed phase   | N/A       | Depends on β | Digital precursors (BPSK/QPSK)        |