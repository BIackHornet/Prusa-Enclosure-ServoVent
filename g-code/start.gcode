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