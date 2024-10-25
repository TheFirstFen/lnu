import utime

count = 0
start_time = utime.ticks_ms()
last_press = 0

def buttonEventCallback():
    global count, start_time, last_press
    delta_t = utime.ticks_ms() - start_time
    if delta_t >= 1000:
        print(f"Button was pressed: {count} time(s). Time since last {delta_t}ms")
        count += 1
        start_time = utime.ticks_ms()  # Reset the start time after processing a button press
    else:
        time_left = 1000 - delta_t
        print(f"Ignored button press: Time left for next press is {time_left}ms")
        last_press = delta_t

button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        buttonEventCallback()