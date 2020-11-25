from Wuerfel import *
from Spieler import *
from Spielfeld import *

class Spielmanager(object):
    def __init__(self):
        self.w1 = Wuerfel()
        self.w2 = Wuerfel()
        self.w3 = Wuerfel()
        self.spielfeld = Spielfeld()
        self.spieler = Spieler([self.w1, self.w2, self.w3], self.spielfeld)

    def spielen(self, zahl):
        self.spieler.kasse.auszahlen()
        self.spieler.werfen()
        self.auswerten()
        self.gewinnAuszahlung()

    def gewinnAuszahlung(self):
        for i in range(self.auswerten):
            self.spieler.kasse.einzahlen(1)

    def auswerten(self):
        counter = 0
        for i in [self.w1, self.w2, self.w3]:
            if i.getAugen() == self.spielfeld.getGestzteZahl():
                counter += 1
        return counter

    def getDictOfProcedure(self):
        return {"spielen": self.spielen(self.spielfeld.getGestzteZahl()), "augen": self.getAugen(), "kassenInhalt": self.spieler.kasse.getKontostand()}

    def getAugen(self):
        return [self.w1.getAugen(), self.w2.getAugen(), self.w3.getAugen()]
