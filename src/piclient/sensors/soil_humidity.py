from .base import Sensor
from RPi import GPIO

class BinarySoilHumidty(Sensor):

    name = "Bin-Soil-Humidity"
    topic = "bin-soild-humidity"

    def __init__(self, config=None):
        super().__init__(config)
        self.value = None
        self.channel = self.config["bin_soil_humidity_channel"]

    def check(self):
        _ = self.readout()

    def readout(self):
        # read the sensors
        GPIO.set_mode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.IN)
        return GPIO.input(self.channel)

    def cleanup(self):
        pass
