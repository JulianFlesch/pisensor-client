import config
from .sensor import Sensor
from picamera import PiCamera
import tempfile
import time
import os

class Camera(Sensor):
    name = "Camera"
    topic = "image"

    def __init__(self) -> None:
        self.value = None
        self.resolution = config.camera_resolution
        self.wait_time = config.camera_wait

    def get_outfile(self):
        timestamp = time.ctime().replace(" ", "_")
        prefix = "CAMERA_%s_" % timestamp
        out = tempfile.TemporaryFile(prefix)

        return out

    def check(self):
        _ = self.readout()
        self.cleanup()

    def take_picture(self):
        # get tempfile
        filename = self.get_outfile()
        
        # take picture
        camera = PiCamera()
        camera.resolution(self.resolution)
        camera.start_preview()
        time.sleep(self.wait_time)
        camera.capture(filename)
        camera.stop_preview()

        return filename

    def readout(self):
        self.value = self.take_picture()
        return self.value

    def cleanup(self):
        if os.path.exists(self.value):
            os.remove(self.value)

