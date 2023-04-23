from .base import Sensor
import os

class Temperature(Sensor):

    name = "DS18B20-Temperature"
    topic = "temperature"

    def __init__(self, config=None):
        super().__init__(config)
        self.value = None
        self._w1_devices_dir = "/sys/bus/w1/devices/"
        self._ds18b20_dir_prefix = "28"
        self._readout_file = "w1_slave"

    def check(self):
        # check sensor prerequisites
        with open("/boot/config.txt", "r") as f:
            one_wire_installed = f.read().find("dtoverlay=w1-gpio")

        if not one_wire_installed:
            return False

        # check sensor readout
        _ = self.readout()
        self.cleanup()

    def readout(self):
        # read the sensors
        os.system("modprobe w1-gpio")
        os.system("modprobe w1-therm")

        # find the directory with temperature measurements
        # inside the one-wire devices directory
        w1_temp = list(filter(lambda x: x.startswith(self._ds18b20_dir_prefix),
                              os.listdir(self._w1_devices_dir)))
        
        if len(w1_temp) != 1:
            raise RuntimeError("DS18B20 temperature readout directory not found")
        
        else:
            readout_file = os.path.join(self._w1_devices_dir, w1_temp[0], self._readout_file)
            with open(readout_file, "r") as f:
                content = f.read()
                readout = content[content.find("t=") + 2:]
                readout = readout.strip()
                readout = int(readout)
                # convert to celsius
                readout = readout / 1000
                self.value = readout
            return readout

    def cleanup(self):
        pass
