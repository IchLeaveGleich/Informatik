from Spieler import Spieler
from Spielfeld import Spielfeld
from Wuerfel import Wuerfel

class Spielanbieter(object):
    def __init__(self):
        self.wuerfelListe = [Wuerfel(), Wuerfel(), Wuerfel()]
        self.spielerListe = []
        self.spielfeld = Spielfeld()
        self.spielerAnReihe = 1


    def naechsterSpieler(self):
        tmp = self.spielerListe.pop()
        self.spielerListe.append(tmp)

    def spielerErstellen(self, anzahlSpieler):
        for i in range(anzahlSpieler):
            self.spielerListe.append(Spieler(self.spielfeld, self.wuerfelListe))

    def gewinnAuszahlen(self):
        richtige = 0
        for wuerfel in self.wuerfelListe:
            if wuerfel.getAugenzahl() == self.spielfeld.getGesetzteZahl():
                richtige += 1
        self.spielerListe[0].konto.einzahlen(richtige * self.spielerListe[0].getEinsatz())
