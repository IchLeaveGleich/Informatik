from Wuerfel import Wuerfel
from Spieler import Spieler
from Gewinnkarte import Gewinnkarte

class Kniffel(object):
    def __init__(self):
        self.spielerListe = []
        self.spielerAnzahl = 0
        self.wuerfelListe = [Wuerfel(),Wuerfel(),Wuerfel(),Wuerfel(),Wuerfel()]
        self.spielerAnReihe = 0
        
    def spielerErzeugen(self):
        self.spielerListe.append(Spieler())

    def naechsterSpieler(self):
        self.spielerListe.remove(0).append(a)

    def setSpielerAnzahl(self, spielerAnzahlInput):
        self.spielerAnzahl = spielerAnzahlInput

    def getSpielerAnzahl(self):
        return self.spielerAnzahl

    def spielen(self):
        pass

    
