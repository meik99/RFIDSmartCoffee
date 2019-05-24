# Most parts of this code are taken from
# https://pimylifeup.com/raspberry-pi-rfid-rc522/
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
is_reading = True

try:
        print("RFID-SmartCoffee started")
        while is_reading is True:
                from Tassimo import Tassimo
                tassimo = Tassimo()

                id, text = reader.read()
                print("Making coffee for %s" % id)
                tassimo.make_coffee()
finally:
        GPIO.cleanup()