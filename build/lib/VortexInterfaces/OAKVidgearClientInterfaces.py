from abc import ABCMeta, abstractmethod, ABC
from PyQt5.QtCore import QObject

# Define a metaclass that inherits both from PyQt's QObject and ABCMeta for abstract classes
class OAKVidgearClientMeta(type(QObject), ABCMeta):
    pass

class OAKVidgearClientInterfaces(ABC, metaclass=OAKVidgearClientMeta):
    @abstractmethod
    def startOAKVidgearThread(self):
        pass

    @abstractmethod
    def stopOAKVidgearThread(self):
        pass
    
    @abstractmethod
    def getFrame(self):
        pass