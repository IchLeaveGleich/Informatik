from Spieler import Spieler
from Wuerfel import Wuerfel
from Spielfeld import Spielfeld

class Spielanbieter(object):
    def __init__(self):
        self.wuerfel1 = Wuerfel()
        self.wuerfel2 = Wuerfel()
        self.wuerfel3 = Wuerfel()
        self.spielfeld = Spielfeld()
        self.spielerListe = []
        self.spielerAnReihe = 0
        self.wuerfelListe = [self.wuerfel1, self.wuerfel2, self.wuerfel3]
        
    def spielerErzeugen(self):
        self.spielerListe.append(Spieler(self.wuerfel1, self.wuerfel2, self.wuerfel3, self.spielfeld))

    def naechsterSpieler(self):
        self.spielerListe[self.spielerAnReihe].spielen()
        if len(self.spielerListe) >= spielerAnReihe + 1:
            self.spielerAnReihen = 0
        else:
            self.spielerAnReihe += 1
            
    def gewinnAuszahlen(self):
        richtige = 0
        for i in self.wuerfelListe:
            if i.getAugen() == self.spielfeld.getGesetzteZahl():
                richtige += 1
        self.spielerListe[self.spielerAnReihe].sKonto.einzahlen(1 * richtige)

#----------------------------------------
# Test
#----------------------------------------

# Erzeugung und Verbindung der Objekte
# ...
s = Spielanbieter()
s.spielerErzeugen()
s.spielerErzeugen()
s.spielerErzeugen()


# Ausgabe
print('Wuerfel: ', s.wuerfel1.getAugen(), s.wuerfel2.getAugen(), s.wuerfel3.getAugen())
print('Konto  : ', s.spielerListe[s.spielerAnReihe].sKonto.getStand())
print()

# Durchführung des Spiels 
for i in range(10):
    s.spielerListe[s.spielerAnReihe].spielen(2)
    s.gewinnAuszahlen()
    # Ausgabe
    print('Wuerfel: ', s.wuerfel1.getAugen(), s.wuerfel2.getAugen(), s.wuerfel3.getAugen())
    print('Konto  : ', s.spielerListe[s.spielerAnReihe].sKonto.getStand())
    print()
