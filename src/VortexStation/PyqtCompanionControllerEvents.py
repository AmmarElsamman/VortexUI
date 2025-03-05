from PyQt5.QtCore import QObject
from VortexStation.VortexWidgetNamesEnums import Readings

class PyqtCompanionControllerEvents(QObject):

    def __init__(self, readingsLabelUpdater):
        super().__init__()
        self.readingsLabelUpdater = readingsLabelUpdater

    def depthEvent(self, value):
        print("depthEvent: value:{}.".format(value))
        self.readingsLabelUpdater(Readings.Depth, str(value))

    def PHEvent(self, value):
        print("PHEvent: value:{}.".format(value))
        self.readingsLabelUpdater(Readings.PH, str(value))

    def headingEvent(self, value):
        print("headingEvent: value:{}.".format(value))
        self.readingsLabelUpdater(Readings.Heading, str(value))
    
    def PitchEvent(self, value):
        print("PitchEvent: value:{}.".format(value))
        self.readingsLabelUpdater(Readings.Pitch, str(value))
    
    def RollEvent(self, value):
        print("RollEvent: value:{}.".format(value))
        self.readingsLabelUpdater(Readings.Roll, str(value))
