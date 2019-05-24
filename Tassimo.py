import RPi.GPIO as IO
import time as time

gpio_mode = IO.getmode()

BARCODE_GPIO = 8
COFFEE_GPIO = 10

BARCODE_TO_COFFEE_TIME = 3

IO.setwarnings(False)

if gpio_mode == -1:
    IO.setmode(IO.BOARD)


IO.setup(COFFEE_GPIO, IO.OUT)
IO.setup(BARCODE_GPIO, IO.OUT)


class Tassimo:
    def make_coffee(self):
        IO.output(BARCODE_GPIO, IO.HIGH)
        time.sleep(0.5)
        IO.output(BARCODE_GPIO, IO.LOW)
        time.sleep(BARCODE_TO_COFFEE_TIME)
        IO.output(COFFEE_GPIO, IO.HIGH)
        time.sleep(0.5)
        IO.output(COFFEE_GPIO, IO.LOW)
        time.sleep(0.5)