from abc import ABC, abstractmethod
from .config import Config

class Sensor(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def topic(self):
        pass

    def __init__(self, config=None):
        
        self.config = config if isinstance(config, Config) else Config()

    @abstractmethod
    def readout(self):
        pass

    def cleanup(self):
        pass
