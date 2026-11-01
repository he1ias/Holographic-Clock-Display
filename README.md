## Holographic Display
### A 'floating' display for your bedside table

![3D View of PCB](https://raw.githubusercontent.com/he1ias/Holographic-Clock-Display/refs/heads/main/Images/3D.jpeg)

A Holographic Clock Display for your bedside table, powered by the ESP32. Using the Pepper's Ghost visual effect, this display appears to 'float' in mid-air.

Comes with a wide range of pre-programmed clock-faces, visual effects, and relaxing animations. Works best when used in a dark room.

Made for HackClub's Half Life event.

Onshape URL: [click here](https://cad.onshape.com/documents/4a07292fcf3ec5a261f2cd78/w/7a4fcc3ff990e21e98229a03/e/6ea8dd64a432b46748776d14)

### What can it do?

It can display a wide variety of clock faces & relaxing visual effects. The Pepper's Ghost 'illusion' gives the images a 3D effect. Simply connected to the ESP32 via a USB-C cable. The display comes with a builtin effect selection button and brightness knob for ease of use.

### How does it?

4 displays sit hidden inside the 3D-printed casing, pointed up at the transparent material. The material then reflects the light back at the viewer, as if the material was the source of the light itself.

### How was it made?

Using KiCad & Onshape.

I first tested the effect by cutting some acrylic:

![Testing Phase](https://raw.githubusercontent.com/he1ias/Holographic-Clock-Display/refs/heads/main/Images/Testing.jpeg)

I then selected my parts, and wired the schematic in KiCad:

![Schematic](https://raw.githubusercontent.com/he1ias/Holographic-Clock-Display/refs/heads/main/Images/Schematic.jpeg)

I then arranged my PCB and routed my wires:

![PCB](https://raw.githubusercontent.com/he1ias/Holographic-Clock-Display/refs/heads/main/Images/PCB.jpeg)

I then used online CAD program Onshape to design the 3D-printed casing for my piece. The slots hold the transparent material securely into place, and screw holes live inside the case so the PCB can be attached:

![Casing](https://raw.githubusercontent.com/he1ias/Holographic-Clock-Display/refs/heads/main/Images/Casing.png)

### How do I build it?

First, order the materials located in `BOM.csv` and below, 3D-print the casing (STEP and STL files are located in this repository) and print the PCB using an online service such as JLCPCB.

To assemble, solder the parts onto the PCB, screw it into place in the casing, and put the lid over the top. Cut out 4 equally sized trapeziums with `base = 3cm, top = 9cm, and height = 3√2 ~= 4.25cm`, and insert into the slots marked out.

That's it! Simply connect to the ESP32 via USB-C and the clock will turn itself on!

### Bill of Materials (BOM)

| Item | Qty | Supplier | Cost/item | Total Cost | Link |
|------|----:|----------|----------:|-----------:|------|
| XIAO RP2040 ESP32 | 1 | seeedstudio | $3.90 | $3.90 | [Link](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) |
| Display | 4 | LCSC | $2.22 | $8.88 | [Link](https://www.lcsc.com/product-detail/C7471924.html) |
| Button | 10 | LCSC | $0.06 | $0.60 | [Link](https://www.lcsc.com/product-detail/C49393619.html) |
| Thumbwheel Potentiometer | 1 | LCSC | $1.08 | $1.08 | [Link](https://www.lcsc.com/product-detail/C470643.html) |
| Male pin headers | 5 | LCSC | $0.16 | $0.80 | [Link](https://www.lcsc.com/product-detail/C2337.html) |
| JLCPCB | 1 | JLC | $4.00 | $4.00 | [Link](https://jlcpcb.com/) |
| JLC3DP | 1 | JLC | $6.50 | $6.50 | [Link](https://www.jlc3dp.com) |
| Reflective material (eg. acrylic sheet) (Already owned) | 1 | Amazon | $0.01 | $0.01 | [Link](https://www.amazon.com.au/Pack-Clear-Acrylic-Sheets-Transparent/dp/B0H6PXC3K6) |
| M2 Screws (Already owned) | 4 | AliExpress | $0.01 | $0.04 | [Link](https://www.aliexpress.com/item/4000056753202.html) |
| Estimated total shipping | 1 | | | $13.00 | |
| **Total** | | | | **$38.81** | |