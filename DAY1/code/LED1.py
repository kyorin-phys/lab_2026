from machine import Pin
from time import sleep_ms

LED = Pin(15, Pin.OUT) # GPIO15 にLEDと抵抗を直列につないで、GNDに落とす

LED.value(1)
sleep_ms(1000)
LED.value(0)
