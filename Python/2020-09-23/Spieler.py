from Konto import Konto
from Spielfeld import Spielfeld

class Spieler(object):
    def __init__(self, wuerfel1, wuerfel2, wuerfel3, spielfeld):
        self.sKonto = Konto(50)
        self.wuerfel1 = wuerfel1
        self.wuerfel2 = wuerfel2
        self.wuerfel3 = wuerfel3
        self.spielfeld = spielfeld

    def spielen(self, zahl):
        self.spielfeld.setzen(zahl)
        self.sKonto.auszahlen(1)
        self.wuerfel1.werfen()
        self.wuerfel2.werfen()
        self.wuerfel3.werfen()
        
        
        
