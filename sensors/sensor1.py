from .numeric import NumericSensor
from .binary import BinarySensor
import time  # Importamos time
from time import gmtime, strftime  # importamos gmtime y strftime
import Adafruit_DHT
import RPi.GPIO as GPIO

class DHT(NumericSensor):
    """DHT."""
    def __init__(self, name):
        super(DHT, self).__init__(name)


    def update_value(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin=23, retries=6, delay_seconds=2)
        self.value = temperature


class PIR(BinarySensor):
    """PIR"""
    def __init__(self, name):
        super(PIR, self).__init__(name)
        GPIO.setmode(GPIO.BCM)
        self.PIR_PIN = 23
        GPIO.setup(self.PIR_PIN, GPIO.IN)

    def update_state(self):
        try:
            while True:
                if GPIO.input(self.PIR_PIN):
                    time.sleep(1)
                    timex = strftime("%d-%m-%Y %H:%M:%S", gmtime())
                    print timex + " MOVIMIENTO DETECTADO"
                    time.sleep(1)
                time.sleep(1)
        except KeyboardInterrupt:
            print "quit"
            GPIO.cleanup()
