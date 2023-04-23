import os
from collections import UserDict
import configparser


class Config(UserDict):
    CONFIG_LOCATION = "/etc/raspiclient_conf.ini"
    DEFAULTS = [
        # general
        ("device_name", "Default_Device", lambda x: x),
        ("location", "Default_Location", lambda x: x),
        ("installed_sensors", "", lambda x: x.split(",")),
        ("installed_actors", "", lambda x: x.split(",")),
        
        # mqtt settings
        ("transport", "tcp", lambda x: x),
        ("broker", "192.169.0.34", lambda x: x),
        ("port", "443", lambda x: x),
        ("token", "", lambda x: x),
        ("user", "", lambda x: x), 
        ("password", "", lambda x: x),

        # camera settings
        ("camera_resolution", "1024,768", lambda x: [int(i) for i in x.split(",")]),
        ("camera_wait", "2", lambda x: int(x)),

        # binary soil humidity settings
        ("bin_soil_humidity_channel", "1", lambda x: int(x)),
    ]
    
    def __init__(self):
        
        super().__init__()

        self.read_from_environment()
        self.read_from_conf_file(self.CONFIG_LOCATION)

    def read_from_environment(self):
        env = os.environ
        for k, default, parse in self.DEFAULTS:
            self[k] = parse(env.get(k.upper(), default))

    def read_from_conf_file(self, config_file=None):
        if os.path.exists(config_file):
            cp = configparser.ConfigParser()
            cp.read(config_file)

            for s in cp.sections():
                for k, default, parse in self.DEFAULTS:
                    self[k] = parse(cp[s].get(k, default))
        else:
            pass
