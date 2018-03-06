#!/usr/bin/env python
import time
import notifications
import sensors
import random
import pprint as pp
import Adafruit_DHT
import RPi.GPIO as GPIO




class Guardian(object):
    """HomeGuardian is a security system for python"""
    def __init__(self):
        super(Guardian, self).__init__()
        self.binary_sensors_names = [
            "bsensor1", "bsensor2", "bsensor3"
        ]
        self.numeric_sensors_names = [
            "nsensor1", "nsensor2", "nsensor3"
        ]
        #self.Temperature_sensor = "DHT"
        self.numeric_sensors = []
        self.binary_sensors = []
        self.sensors = {}
        self.sensors["binary"] = {}
        self.sensors["numeric"] = {}
     #  self.notify = notifications.MockNotification()
        self.notify = notifications.TelegramNotification()
        self.already_n=[]
        #self.DHTpin = 16

    def create_sensors(self):
        for name in self.numeric_sensors_names:
            self.numeric_sensors.append(
                sensors.mocksensor.MockNumericSensor(name)
            )
        for name in self.binary_sensors_names:
            self.binary_sensors.append(
                sensors.mocksensor.MockBinarySensor(name)
            )
        self.numeric_sensors.append(sensors.mocksensor.DHT("DHT"))
        pass

    def get_state(self):
        #update
        for sensor in self.binary_sensors:
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
            print self.sensors["numeric"]["DHT"]
            for ns in self.sensors["numeric"]:
                if self.sensors["numeric"][ns] > 25.0 \
                    and ns not in self.already_n:
                    self.notify.notify(ns)
                    self.already_n.append(ns)

            time.sleep(1)
        pass

if __name__=='__main__':
    random.seed(1)
    guardian = Guardian()
    guardian.main()
