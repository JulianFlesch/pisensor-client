import config
from camera import Camera

class Client:
    sensor_choices = dict(
        ("Camera", Camera),)

    def __init__(self):

        self._sensors = self._init_sensors()

    def _init_sensors(self):
        initialized = []

        for s in config.installed_sensors:
            if s in self.sensor_choices.keys():
                sensor = self.sensor_choices[s]()
                
                try:
                    sensor.check()
                    initialized.append(sensor)
                except Exception as e:
                    print("[Error] initializing sensor %s failed" % s)
                    print(e)

        return initialized

    def read_all(self):
        readouts = []
        for sensor in self._sensors:
            readouts.append((sensor.name, sensor.readout()))
            sensor.cleanup()

        return readouts
