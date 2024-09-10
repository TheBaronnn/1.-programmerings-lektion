from machine import Pin
from machine import sleep
led1 = Pin(26, Pin.OUT)
led1.on()
led2 = Pin(12, Pin.OUT)
led2.off()
led3 = Pin(13, Pin.OUT)
led3.on
while True:
    print("ALL ON!")
    led1.on()
    sleep(1)
    led2.off()
    sleep(1)
    led3.on()
    sleep(1)
    print("ALL OFF!")
    led1.off()
    sleep(1)
    led2.on
    sleep(1)
    led3.off()
    sleep(1)
    

