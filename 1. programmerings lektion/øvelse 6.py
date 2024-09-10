from machine import Pin
from machine import sleep
import time

pb1 = Pin(4, Pin.IN)
led1 = Pin(26, Pin.OUT)
led_state = False
last_button_state = pb1.value()

while True:
    current_button_state = pb1.value()
    
    if last_button_state == 1 and current_button_state == 0:
        led_state = not led_state
        led1.value(led_state)  
        if led_state:
            print("LED ON!")
        else:
            print("LED OFF!")
        
    last_button_state = current_button_state

    
    