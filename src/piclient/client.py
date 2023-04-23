from .config import Config
from .camera import Camera
from .temperature import Temperature

class Client:
    sensor_choices = dict([
        ("Camera", Camera),
        ("Temperature", Temperature)
    ])
    
    actor_choices = dict()

    def __init__(self, config=None):

        if isinstance(config, Config):
            self.config = config
        else:
            print("[Warning] Falling back to default config")
            self.config = Config()
        
        self._sensors = self._init_sensors()
        self._actors = self._init_actors()

    def _init_sensors(self):
        initialized = []

        for s in self.config["installed_sensors"]:
            if s in self.sensor_choices.keys():
                sensor = self.sensor_choices[s](self.config)
                
                try:
                    sensor.check()
                    initialized.append(sensor)
                except Exception as e:
                    print("[Error] initializing sensor %s failed" % s)
                    print(e)

        return initialized

    def _init_actors(self):
        initialized = []

        for a in self.config["installed_actors"]:
            if a in self.actor_choices.keys():
                actor = self.actor_choices[a]()

                try:
                    actor.check()
                    initialized.append(actor)
                except Exception as e:
                    print("[Error] initializing actor %s failed" % a)
                    print(e)
        
        return initialized

    def read_all_sensors(self):
        readouts = []
        for sensor in self._sensors:
            print("[Info] Reading %s" % sensor.name)
            readouts.append((sensor.topic, sensor.readout()))
            sensor.cleanup()

        return readouts

    def actor_callback(self, mqtt_client, userdata, msg):
        pass
