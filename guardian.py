import time

import sensors


class Guardian(object):
    """HomeGuardian is a security system for python"""
    def __init__(self):
        super(Guardian,self).__init__()
        self.binay_sensors_names = [
            "bsensor1", "bsensor2", "bsensor3"
        ]
        self.numeric_sensors_names = [
            "nsensor1", "nsensor2", "nsensor3"
        ]
        self.numeric_sensors = []
        self.binay_sensors = []
        self.sensors = {}
        self.sensors["binary"] = {}
        self.sensors["numeric"] = {}

    def create_sensors(self):
        for name in self.numeric_sensors_names:
            self.numeric_sensors.append(
                self.sensors.mocksensors.MockNumericSensor(name)
            )
        for name in self.binay_sensors_names:
            self.binay_sensors.append(
                self.sensors.mocksensors.MockBinarySensor(name)
            )
        pass

    def get_state(self):
        #update
        for sensor in self.binay_sensors:
            sensor.update_state()
            self.sensors["binary"][sensor.name] = sensor.get_state()

        for sensor in self.numeric_sensors:
            sensor.update_value()
            self.sensors["numeric"][sensor.name] = sensor.get_value()

        return self.sensors

    def main(self):
        # crearsensores
        self.create_sensors()
        while True:
            state = self.get_state()
        #        if condiciones:
        #           notificar()
        #        sleep(1)
            print(state)
            time.sleep(1)
        pass

if __name__=='__main__':
    guardian = Guardian()
    guardian.main
