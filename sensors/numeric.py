from .main import Sensor

class NumericSensor(Sensor):
    """NumericSensor"""
    def __init__(self, name):
        super(NumericSensor, self).__init__(name)
        self.value = 0.0

    def get_value(self):
        return self.value

    def update_value(self):
        pass
