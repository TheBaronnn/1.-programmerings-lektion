from machine import Pin
from machine import sleep
import time

pb1 = Pin(4, Pin.IN)
led1 = Pin(26, Pin.OUT)

while True:
    first = pb1.value()
    time.sleep(0.01)
    second = pb1.value()
    
    if first == 1 and second == 0:
        led1.on()
        print("Knappen er blevet trykket, så er der lys")
        
    if first == 0 and second == 1:
        led1.off()
        print("Knappen er ikke længere trykket, så er den slukket")
    
    