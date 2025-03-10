from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from VortexCompanionController import CompanionController

class PyqtCompanionController(QObject, CompanionController):
    depthEvent = pyqtSignal(float)      # Signal for depth data
    PHEvent = pyqtSignal(float)         # Signal for PH data
    headingEvent = pyqtSignal(int)      # Signal for heading Event
    PitchEvent = pyqtSignal(int)        # Signal for Pitch data
    RollEvent = pyqtSignal(int)         # Signal for Roll Event

    def __init__(self):
        super().__init__()
        # Timer to periodically fetch sensor readings
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.getData)
        self.timer.start(500)  # Update every 500 ms

    def getData(self):
        sensorReadings = self.readSensorsData()
        self.processReadings(sensorReadings)

    def processReadings(self, sensorReadings):
        for dataType, value in sensorReadings.items():
            if dataType == "depth":
                self.depthEvent.emit(value)
            elif dataType == "PH":
                self.PHEvent.emit(value)
            elif dataType == "heading":
                self.headingEvent.emit(value)
            elif dataType == "Pitch":
                self.PitchEvent.emit(value)
            elif dataType == "Roll":
                self.RollEvent.emit(value)
    
    def connect(self, eventsObject):
        self.depthEvent.connect(eventsObject.depthEvent)
        self.PHEvent.connect(eventsObject.PHEvent)
        self.headingEvent.connect(eventsObject.headingEvent)
        self.PitchEvent.connect(eventsObject.PitchEvent)
        self.RollEvent.connect(eventsObject.RollEvent)
