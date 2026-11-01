## Holographic Display
### A 'floating' display for your bedside table

...

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

...

I then selected my parts, and wired the schematic in KiCad:

...

I then arranged my PCB and routed my wires:

...

I then used online CAD program Onshape to design the 3D-printed casing for my piece. The slots hold the transparent material securely into place, and screw holes live inside the case so the PCB can be attached:

...

### How do I build it?

First, order the materials located in `BOM.csv` and below, 3D-print the casing (STEP and STL files are located in this repository) and print the PCB using an online service such as JLCPCB.

To assemble, solder the parts onto the PCB, screw it into place in the casing, and put the lid over the top. Cut out 4 equally sized trapeziums with `base = 3cm, top = 9cm, and height = 3√2 ~= 4.25cm`, and insert into the slots marked out.

That's it! Simply connect to the ESP32 via USB-C and the clock will turn itself on!

### Bill of Materials (BOM)

...