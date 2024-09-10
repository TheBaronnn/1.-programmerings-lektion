from machine import Pin
from machine import sleep
import time
led1 = Pin(26, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(13, Pin.OUT)
while True:
    print("RED ON!")
    led1.on()
    time.sleep(5)
    print ("RED OFF, YELLOW ON!")
    led1.off()
    led2.off()
    time.sleep(1)
    print ("YELLOW OFF!")
    led2.on()
    print ("GREEN ON THEN OFF!")
    led3.on()
    time.sleep(5)
    led3.off()
    

