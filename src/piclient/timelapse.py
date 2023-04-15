from .sensor import Sensor
from picamera import PiCamera
import tempfile
import time
import os

class Camera(Sensor):
    name = "PiCamera"
    topic = "image"

    def __init__(self) -> None:
        self.value = None

    def get_outfile(self):
        timestamp = time.ctime().replace(" ", "_")
        prefix = "CAMERA_%s_" % timestamp
        out = tempfile.TemporaryFile(prefix)

        return out

    def take_picture(self):
        # get tempfile
        filename = self.get_outfile()
        
        # take picture
        camera = PiCamera()
        camera.start_preview()
        time.sleep(5)
        camera.capture(filename)
        camera.stop_preview()

        return filename

    def record(self):
        self.value = self.take_picture()
        return self.value

    def cleanup(self):
        if os.path.exists(self.value):
            os.remove(self.value)
