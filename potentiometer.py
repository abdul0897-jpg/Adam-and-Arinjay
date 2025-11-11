from machine import Pin, PWM, ADC 
from time import sleep 
 
# --- Components --- 
button = Pin(14, Pin.IN, Pin.PULL_DOWN) # Button input 
buzzer = PWM(Pin(15)) # Buzzer output 
pot = ADC(26) # Potentiometer input 
 
print("System ready! Press the button to ring the buzzer.") 
 
# --- Main loop --- 
while True: 
if button.value() == 1: # Button pressed 
pot_value = pot.read_u16() 
# Map potentiometer to frequency range 200 Hz → 2000 Hz 
freq = int(200 + (pot_value / 65535) * 1800) 
buzzer.freq(freq) 
buzzer.duty_u16(30000) # Turn buzzer on 
print(f"🔊 Button pressed! Frequency: {freq} Hz") 
else: 
buzzer.duty_u16(0) # Turn buzzer off 
sleep(0.05) 
