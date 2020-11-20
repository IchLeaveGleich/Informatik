from Ampel import *

class AmpelSteuerung(object):
    def __init__(self):
        self.ampel1 = Ampel() #Rot
        self.ampel2 = Ampel() 
        self.ampel2.naechsterZustand() #Grün
        self.ampel2.naechsterZustand()
    
    def weiterSchalten(self):
        if self.ampel2.zustand >= 3:
            self.ampel2.naechsterZustand()
        self.ampel1.naechsterZustand()
        self.ampel2.naechsterZustand()

    def makeListOfProcedure(self):
        listOfProcedure = [self.ampel1.anzeige, self.ampel2.anzeige, self.weiterSchalten]
        return listOfProcedure
