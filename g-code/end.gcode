; --- Turn off vent outputs ---
M264 P0 B0 ; Exhaust OFF
M264 P1 B0 ; Recirculate OFF

; --- Simulate pressing FAN button (OFF) ---
M264 P2 B1 ; Toggle ON (pull low)
G4 S1       ; Wait 1 second
M264 P2 B0 ; Toggle OFF (release)