import time
import notifications
import sensors
import random
import pprint as pp


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
     #  self.notify = notifications.MockNotification()
        self.notify = notifications.TelegramNotification()
        self.already_n=[]

    def create_sensors(self):
        for name in self.numeric_sensors_names:
            self.numeric_sensors.append(
                sensors.mocksensors.MockNumericSensor(name)
            )
        for name in self.binay_sensors_names:
            self.binay_sensors.append(
                sensors.mocksensors.MockBinarySensor(name)
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
            self.get_state()

            for ns in self.sensors["numeric"]:
                if self.sensors["numeric"][ns] > 15.0 and ns not in self.already_n:
                    self.notify.notify(ns)
                    self.already_n.append(ns)

    #        pprint(self.sensors)
            time.sleep(0.2)
        pass

if __name__=='__main__':
    random.seed(1)
    guardian = Guardian()
    guardian.main
