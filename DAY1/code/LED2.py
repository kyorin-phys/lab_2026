from machine import Pin
from time import sleep_ms

LED = Pin(15, Pin.OUT) # GPIOピンにLEDと抵抗を直列につないでGNDに接続
# value = 1 : HIGH 3.3V  
# value = 0 : LOW GND(0V)
# N回点滅
N = 10
TS = 200
for i in range(N):
    LED.value(1)
    sleep_ms(TS)
    LED.value(0)
    sleep_ms(TS)
