from Kasse import *
from Spielfeld import *

class Spieler(object):
    def __init__(self, wliste, sf):
        self.kasse = Kasse()
        self.wuerfel = wliste
        self.spielfeld = sf
        self.name = ""

    def werfen(self):
        for i in self.wuerfel:
            i.werfen()

    def auszahlen(self):
        self.kasse.auszahlen()
        
    def einzahlen(self, gewinn):
        self.kasse.einzahlen(gewinn)



