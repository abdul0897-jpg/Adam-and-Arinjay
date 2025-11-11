
from machine import Pin, PWM 
from time import sleep 
 
button = Pin(14, Pin.IN, Pin.PULL_DOWN) 
buzzer = PWM(Pin(15)) 
buzzer.duty_u16(0) 
 
print("Button pressed! Buzzer ON.") 
while True: 
if button.value() == 1: 
buzzer.freq(1000) 
buzzer.duty_u16(30000) 
else: 
buzzer.duty_u16(0) 
sleep(0.05) 
