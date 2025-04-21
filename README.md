*This is a work in progress and not currently functional*

Summary:
I am trying to create an automated way of controlling the exhaust vent and fan on my Original Prusa Enclosure. PrusaSlicer has variables that will know what filament
type is being used, that variable will be used in the start and end gcode. Based on the type of filament, the vent will be rotated by a servo and the fan turned on.

Related Articles:
https://forum.prusa3d.com/forum/user-and-hardware-mods/further-information-on-basic-board-and-psu-for-original-prusa-enclosure-for-filtration-unit-and-custom-led/
https://forum.prusa3d.com/forum/project-oni-general-discussion-announcements-and-releases/basic-board-connectors/
https://help.prusa3d.com/article/gpio-module_734695
https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4s-add-ons/gpio-how-to-article/
https://forum.prusa3d.com/forum/english-forum-original-prusa-i3-mk4s-add-ons/gpio-question/
https://web.archive.org/web/20241101203306/https://help.prusa3d.com/article/gpio-module_734695

Topology:
Raspberry Pi Pico running MicroPython
Prusa Basic Board connected to Pico GPIO with extension cable
Buck Convertor stepping down voltage (24v to 5v) from Basic Board to Pico
PrusaSlicer inserts Start and End G-code to control vent state (open or closed)
Original Prusa MK4/S, MK3.9/S, or MK3.5/S running firmware 6.2.0-alpha1 or newer.

![alt text](https://github.com/BIackHornet/Prusa-Enclosure-ServoVent/blob/main/images/TOPOLOGY.png?raw=true)

Hardware List:
MG90S Micro Servo - https://www.amazon.com/dp/B09BV5D7MD
Basic Board Extension Cable - https://www.digikey.com/en/products/detail/molex/0151350406/6830170
Raspberry Pi Pico - https://www.amazon.com/Raspberry-Pi-Pico/dp/B09KVB8LVR
Prusa Basic Board - https://www.prusa3d.com/product/basic-board-and-psu-for-original-prusa-enclosure-for-filtration-unit-and-led/
Buck Converter - https://www.amazon.com/dp/B0DBVYP91F
Servo Tester (Optional: Assist in calibrating servo for script) - https://www.amazon.com/dp/B07FQNZHG4le
3.5mm TRRS Jack - https://www.amazon.com/dp/B07L3P93ZD
2.5mm to 3.5mm TRRS Cable - https://www.amazon.com/dp/B0B9RF28W3

3D Printed Parts:
Advanced Filtration System Adjustable Exhaust (v3) for the Original Prusa Enclosure - https://www.printables.com/model/964245-advanced-filtration-system-adjustable-exhaust-v3-f
Larger Prusa GPIO "Hackerboard" Cover for Sticker - https://www.printables.com/model/1265425-larger-prusa-gpio-hackerboard-cover-for-sticker

BASIC BOARD EXTENSION PORT PINOUT:
1: GND
2: 24 VDC
3: GND (switched by FAN button)
4: GND (switched by LED button)

Software:
[MicroPython code and G-Code from my GitHub](https://github.com/BIackHornet/Prusa-Enclosure-ServoVent/)



🔧 PrusaSlicer Start G-code:

; --- Setup GPIO modes ---
M262 P0 B0 ; Pin 0: Exhaust
M262 P1 B0 ; Pin 1: Recirculate
M262 P2 B0 ; Pin 2: Fan toggle output

; --- Reset all outputs ---
M264 P0 B0 ; Exhaust OFF
M264 P1 B0 ; Recirculate OFF
M264 P2 B0 ; Ensure fan toggle is LOW

; --- Simulate pressing FAN button (ON) ---
M264 P2 B1 ; Toggle ON (pull low)
G4 S1       ; Wait 1 second
M264 P2 B0 ; Toggle OFF (release)

; --- Set venting mode based on filament ---
{if initial_filament_type == "PLA"}
  M264 P0 B1 ; Exhaust ON
{elsif initial_filament_type == "PETG"}
  M264 P0 B1 ; Exhaust ON
{elsif initial_filament_type == "TPU"}
  M264 P0 B1 ; Exhaust ON
{elsif initial_filament_type == "ABS"}
  M264 P1 B1 ; Recirculate ON
{elsif initial_filament_type == "ASA"}
  M264 P1 B1 ; Recirculate ON
{elsif initial_filament_type == "Nylon"}
  M264 P1 B1 ; Recirculate ON
{elsif initial_filament_type == "PC"}
  M264 P1 B1 ; Recirculate ON
{else}
  M117 ⚠ Unknown filament type – check vent manually



🧹 PrusaSlicer End G-codes:

; --- Turn off vent outputs ---
M264 P0 B0 ; Exhaust OFF
M264 P1 B0 ; Recirculate OFF

; --- Simulate pressing FAN button (OFF) ---
M264 P2 B1 ; Toggle ON (pull low)
G4 S1       ; Wait 1 second
M264 P2 B0 ; Toggle OFF (release)
