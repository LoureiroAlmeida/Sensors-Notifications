from .binary import BinarySensor
from .numeric import NumericSensor

class MockBinarySensor(BinarySensor):
    """MockBinarySensor"""
    def __init__(self):
        super(MockBinarySensor,BinarySensor.__init__(name)

    def update_state(self):
        self.state = not self.state

class MockNumericSensor(BinarySensor):
    """MockNumericSensor"""
    def __init__(self):
        super(MockBinarySensor,BinarySensor.__init__(name)

    def update_state(self):
        self.value = 23.5
