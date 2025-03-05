from abc import ABCMeta, abstractmethod, ABC
from PyQt5.QtCore import QObject

class CompanionControllerMeta(type(QObject), ABCMeta):
    pass


class CompanionControllerInterfaces(ABC, metaclass=CompanionControllerMeta):

    abstractmethod
    def readSensorsData(self):
        pass
