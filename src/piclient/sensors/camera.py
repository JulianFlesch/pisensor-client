from .base import Sensor
from picamera import PiCamera
import tempfile
import time
import os

class Camera(Sensor):
    name = "Camera"
    topic = "image"

    def __init__(self, config=None):
        super().__init__(config)
        self.value = None
        self.resolution = self.config["camera_resolution"]
        self.wait_time = self.config["camera_wait"]

    def get_outfile(self):
        timestamp = time.ctime().replace(" ", "_")
        prefix = "CAMERA_%s_" % timestamp
        tmp = tempfile.NamedTemporaryFile(prefix=prefix, suffix=".jpg")

        return tmp.name

    def check(self):
        _ = self.readout()
        self.cleanup()

    def take_picture(self):
        # get tempfile
        filename = self.get_outfile()
        
        # take picture
        camera = PiCamera()
        camera.resolution = self.resolution
        camera.start_preview()
        time.sleep(self.wait_time)
        camera.capture(filename)
        camera.stop_preview()
        camera.close()
        
        return filename

    def readout(self):
        self.value = self.take_picture()

        with open(self.value, "rb") as f:
            data = f.read()

        return data

    def cleanup(self):
        if os.path.exists(self.value):
            os.remove(self.value)

