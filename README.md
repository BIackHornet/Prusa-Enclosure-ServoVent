> [!WARNING]
> # *This is a work in progress and not currently functional*

## Summary:
I am trying to create an automated way of controlling the exhaust vent and fan on my Original Prusa Enclosure. PrusaSlicer has variables that will know what filament
type is being used, that variable will be used in the Start and End G-code. Based on the type of filament, the vent will be rotated by a servo and the fan turned on.

## Related Articles:
- [Prusa Article - GPIO Module](https://help.prusa3d.com/article/gpio-module_734695)
- [Prusa Forum - Further information on Basic Board and PSU for Original Prusa Enclosure (for Filtration unit and *custom* LED)](https://forum.prusa3d.com/forum/user-and-hardware-mods/further-information-on-basic-board-and-psu-for-original-prusa-enclosure-for-filtration-unit-and-custom-led/)
- [Prusa Forum - Basic Board Connectors](https://forum.prusa3d.com/forum/project-oni-general-discussion-announcements-and-releases/basic-board-connectors/)
- [Prusa Forum - GPIO how to article](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4s-add-ons/gpio-how-to-article/)
- [Prusa Forum - GPIO Project Question - Filter control](https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4s-add-ons/gpio-question/)
- [Wayback Machine - Sample Connection of GPIO Module to Addon Controller (Fan Filter and LED) (Scroll Down)](https://web.archive.org/web/20241101203306/https://help.prusa3d.com/article/gpio-module_734695)

## Topology:
- Raspberry Pi Pico running MicroPython
- Prusa Basic Board connected to Pico GPIO with extension cable
- Buck Convertor stepping down voltage (24v to 5v) from Basic Board to Pico
- PrusaSlicer inserts Start and End G-code to control vent state (open or closed)
- Original Prusa MK4/S, MK3.9/S, or MK3.5/S running firmware 6.2.0-alpha1 or newer.

![alt text](https://github.com/BIackHornet/Prusa-Enclosure-ServoVent/blob/main/images/topology.png?raw=true)

## Hardware List:
- MG90S Micro Servo (This model has metal gears) - https://www.amazon.com/dp/B09BV5D7MD
- Basic Board Extension Cable - https://www.digikey.com/en/products/detail/molex/0151350406/6830170
- Raspberry Pi Pico - https://www.amazon.com/Raspberry-Pi-Pico/dp/B09KVB8LVR
- Prusa Basic Board - https://www.prusa3d.com/product/basic-board-and-psu-for-original-prusa-enclosure-for-filtration-unit-and-led/
- Buck Converter - https://www.amazon.com/dp/B0DBVYP91F
- Servo Tester (Optional: Assist in calibrating servo for script) - https://www.amazon.com/dp/B07FQNZHG4le
- 3.5mm TRRS Jack - https://www.amazon.com/dp/B07L3P93ZD
- 2.5mm to 3.5mm TRRS Cable - https://www.amazon.com/dp/B0B9RF28W3

## 3D Printed Parts:
- [Advanced Filtration System Adjustable Exhaust (v3) for the Original Prusa Enclosure by DaHouzKat](https://www.printables.com/model/964245-advanced-filtration-system-adjustable-exhaust-v3-f)
- [Larger Prusa GPIO "Hackerboard" Cover for Sticker by Horbit](https://www.printables.com/model/1265425-larger-prusa-gpio-hackerboard-cover-for-sticker)
- I need to create a model to house hardware above and hold the servo in position above exhaust selector

## Software:
[MicroPython code and G-Code from my GitHub](https://github.com/BIackHornet/Prusa-Enclosure-ServoVent)
