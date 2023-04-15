from abc import ABC, abstractmethod

class Sensor(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def topic(self):
        pass

    @abstractmethod
    def readout(self):
        pass

    def cleanup(self):
        pass
