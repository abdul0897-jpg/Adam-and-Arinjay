from machine import Pin, PWM, ADC 
from time import sleep, ticks_ms 
 
# --- Components --- 
button = Pin(14, Pin.IN, Pin.PULL_DOWN) # Button 
pot = ADC(26) # Potentiometer 
buzzer = PWM(Pin(15)) # Buzzer 
green = Pin(16, Pin.OUT) # Flashing LED 
red = Pin(17, Pin.OUT) # Constant LED 
red.value(1) # Turn red LED ON 
 
# RGB LED (PWM) 
r = PWM(Pin(18)) 
g = PWM(Pin(19)) 
b = PWM(Pin(20)) 
for led in [r, g, b]: 
led.freq(1000) 
 
# --- Helper: Colour wheel for smooth RGB cycling --- 
def wheel(pos): 
"""Return (r,g,b) PWM 0–65535 from pos (0–255).""" 
if pos < 85: 
return (65535 - pos * 257, pos * 257, 0) 
elif pos < 170: 
pos -= 85 
return (0, 65535 - pos * 257, pos * 257) 
else: 
pos -= 170 
return (pos * 257, 0, 65535 - pos * 257) 
 
# --- Variables --- 
last_flash = ticks_ms() 
flash_state = False 
hue = 0 
 
print("System ready! Press the button to start the full system.") 
 
# --- Main Loop --- 
while True: 
if button.value() == 1: # Button pressed 
pot_value = pot.read_u16() 
scaled = pot_value / 65535 # Scale 0–1 
 
# --- Green LED flashing --- 
flash_delay = 50 + (1 - scaled) * 450 # 50–500 ms range 
now = ticks_ms() 
if now - last_flash >= flash_delay: 
flash_state = not flash_state 
green.value(flash_state) 
last_flash = now 
 
# --- RGB LED colour cycling --- 
hue = (hue + 1 + int(scaled * 5)) % 256 
r_val, g_val, b_val = wheel(hue) 
r.duty_u16(r_val) 
g.duty_u16(g_val) 
b.duty_u16(b_val) 
 
# --- Buzzer --- 
freq = int(200 + scaled * 1800) 
buzzer.freq(freq) 
buzzer.duty_u16(30000) 
 
sleep(0.02) # Smooth updates 
else: 
# Button not pressed — turn everything off 
buzzer.duty_u16(0) 
green.value(0) 
for led in [r, g, b]: 
led.duty_u16(0) 
sleep(0.05) 
