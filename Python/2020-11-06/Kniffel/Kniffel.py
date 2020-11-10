from Wuerfel import Wuerfel
from Spieler import Spieler
from Gewinnkarte import Gewinnkarte

class Kniffel(object):
    def __init__(self):
        self.spielerListe = []
        self.spielerAnzahl = 0
        self.wuerfelListe = [Wuerfel(),Wuerfel(),Wuerfel(),Wuerfel(),Wuerfel()]
        self.spielerAnReihe = 0
        
    #Spieler erzeugen
    def spielerErzeugen(self):
        self.spielerListe.append(Spieler())

    #Nächsten Spieler spielen lassen
    def naechsterSpieler(self):
        self.spielerListe.remove(0).append()

    #Spieleranzhal setzten
    def setSpielerAnzahl(self, spielerAnzahlInput):
        self.spielerAnzahl = spielerAnzahlInput

    #Spieleranzahl zurückgeben
    def getSpielerAnzahl(self):
        return self.spielerAnzahl

    #Hauptspiel durchlaufen
    def spielen(self):
        for wuerfel in self.wuerfelListe:
            if wuerfel.istGesichert() == True:
                continue
            else:
                wuerfel.wuerfeln()

    #Wuerfel zuruecksetzten
    def wuerfelNeu(self):
        for wuerfel in self.wuerfelListe:
            wuerfel.__init__()

#Testabschnitt
k = Kniffel()

