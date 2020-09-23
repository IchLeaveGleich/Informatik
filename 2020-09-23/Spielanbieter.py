from Spieler import Spieler
from Wuerfel import Wuerfel
from Spielfeld import Spieler

class Spielanbieter(object):
    def __init__(self):
        self.wuerfel1 = Wuerfel()
        self.wuerfel2 = Wuerfel()
        self.wuerfel3 = Wuerfel()
        self.spielfeld = Spielfeld()
        self.spielerListe = []
        self.spielerAnReihe = 0
        
    def spielerErzeugen(self):
        self.spielerListe.append(Spieler(self.wuerfel1, self.wuerfel2, self.wuerfel3, self.spielfeld))

    def naechsterSpieler(self):
        self.spielerListe[self.spielerAnReihen].spielen()
        if len(self.spielerListe) >= spielerAnReihe + 1:
            self.spielerAnReihen = 0
        else:
            self.spielerAnReihe += 1
            
    def gewinnAuszahlung(self):
        pass
