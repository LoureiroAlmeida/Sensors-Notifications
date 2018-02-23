from .main import Sensor

class NumericSensor(object):
    """docstring for NumericSensor"""
    def __init__(self,name):
        super(BinarySensor, self).__init__(name)
        self.value = 0.0

    def get_state(self):
        return self.state

    def update_state(self):
        pass
