from machine import Pin
import time
import random

button = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

results = []
#while True:
for i in range(10):
    print("準備してください")

    # ボタンを離した状態で開始
    while button.value() == 0:
        time.sleep_ms(10)

    # ランダム待機
    delay = random.uniform(2, 5)
    time.sleep(delay)

    # LED点灯
    led.on()

    start = time.ticks_ms()

    # 押されるまで待つ
    while button.value() == 1:
        pass

    reaction = time.ticks_diff(
        time.ticks_ms(),
        start
    )

    led.off()

    print("反応時間 =", reaction, "ms")
    results.append(reaction)

    # ボタンが離されるまで待つ
    while button.value() == 0:
        time.sleep_ms(10)

    time.sleep(1)
print("avg = ", sum(results)/len(results))
print("min = ", min(results))
print("max = ", max(results))
