import random

from VortexInterfaces import CompanionControllerInterfaces

class CompanionController(CompanionControllerInterfaces):
    
    def __init__(self):
        pass

    def readSensorsData(self):
        return {
            "depth": self.getDepth(),
            "PH": self.getPH(),
            "heading": self.getHeading(),
            "Pitch": self.getPitch(),
            "Roll": self.getRoll()
        }

    def getDepth(self):
        return round(random.uniform(0, 5), 2)
    
    def getPH(self):
        return round(random.uniform(0, 14), 1)
    
    def getHeading(self):
        return random.randint(0,359)
    
    def getPitch(self):
        return random.randint(-90,90)
    
    def getRoll(self):
        return random.randint(-180,359)