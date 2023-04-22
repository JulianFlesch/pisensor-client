import os
from collections import UserDict
import configparser


class Config(UserDict):
    CONFIG_LOCATION = "/etc/raspiclient.conf"
    DEFAULTS = [
        # general
        ("device_name", "Default_Pi_Client", lambda x: x),
        ("installed_sensors", "", lambda x: x.split(",")),
        ("installed_actors", "", lambda x: x.split(",")),
        
        # mqtt settings
        ("tranport", "tcp", lambda x: x),
        ("broker", "192.169.0.34", lambda x: x),
        ("port", "443", lambda x: x),
        ("token", "", lambda x: x),
        ("user", "", lambda x: x), 
        ("password", "", lambda x: x),

        # camera settings
        ("camera_resolution", "1024,768", lambda x: x.split(",")),
        ("camera_wait", "5", lambda x: int(x))
    ]
    
    def __init__(self):
        
        super(UserDict, self).__init__()

        self.read_from_environment()
        self.read_from_conf_file(self.CONFIG_LOCATION)

    def read_from_environment(self):
        env = os.environ
        for k, default, parse in self.DEFAULTS:
            self.data[k] = parse(env.get(k.to_upper, default))

    def read_from_conf_file(self, config_file=None):
        if os.path.exists(config_file):
            cp = configparser.ConfigParser()
            conf = cp.read(config_file)

            for s in conf.sections():
                for k, default, parse in self.DEFAULTS:
                    self.data[k] = parse(conf[s].get(k, default))
        else:
            pass
