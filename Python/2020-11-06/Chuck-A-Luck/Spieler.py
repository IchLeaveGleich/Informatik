from Konto import Konto

class Spieler(object):
    def __init__(self, inputSpielfeld, inputWuerfelListe):
        self.konto = Konto()
        self.spielfeld = inputSpielfeld
        self.wuerfelListe = inputWuerfelListe 
        self.einsatz = None

    def spielen(self, inputZahl):
        self.spielfeld.zahlSetzen(inputZahl)
        self.konto.auszahlen(inputEinsatz)
        for wuerfel in self.wuerfelListe:
            wuerfel.wuerfeln()

    def setEinsatz(self, inputEinsatz):
        self.einsatz = inputEinsatz

    def getEinsatz(self):
        return self.einsatz
