from .binary import BinarySensor
from .numeric import NumericSensor

import random
import Adafruit_DHT
import RPi.GPIO as GPIO


class MockBinarySensor(BinarySensor):
    """MockBinarySensor"""
    def __init__(self, name):
        super(MockBinarySensor, self).__init__(name)

    def update_state(self):
        if random.randint(1,100) == 98:
            self.state = not self.state

class MockNumericSensor(NumericSensor):
    """MockNumericSensor"""
    def __init__(self, name):
        super(MockNumericSensor, self).__init__(name)


    def update_value(self):
        self.value += random.uniform(-0.1,0.1)
        if random.randint(1,100) == 98:
            self.value += 10.0
