import RPi.GPIO as IO
import time as time

BARCODE_GPIO = 14
COFFEE_GPIO = 15

BARCODE_TO_COFFEE_TIME = 10

IO.setwarnings(False)
IO.setmode(IO.BCM)
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