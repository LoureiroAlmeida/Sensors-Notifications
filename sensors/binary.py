from .main import Sensor

class BinarySensor(Sensor):
    """docstring for """
    def __init__(self,name):
        super(BinarySensor, self).__init__(name)
        self.state = False

    def get_state(self):
        return self.state

    def update_state(self):
        pass
