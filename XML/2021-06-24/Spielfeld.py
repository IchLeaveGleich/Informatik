from Feld import *
from Spieler import *
from xml.dom.minidom import *


class Spielfeld(object):
    def __init__(self):
        self.felder = []
        for i in range(40):
            self.felder.append(Feld(i))

        i = -1
        while i < len(self.felder)-2:
            self.felder[i].setNextFeld(self.felder[i+1])
            i += 1

        self.spieler = []
        i = 0
        for name in ["Rot", "Gelb", "Blau", "Grün"]:
            self.spieler.append(Spieler(name, self, i))
            i += 1
        


    def getFelder(self):
        return self.felder

    def makeSpielfeld(self):
        for s in self.spieler:
            s.setFiguren()

    def ausgabe(self):
        for s in self.spieler:
            s.ausgabe()

    def toXML(self):
        file = open("ausgabe.xml", "w")
        file.write('<?xml version="1.0" encoding="iso-8859-1"?><Spielstand>')
        for spieler in self.spieler:
            file.write(spieler.toXML())
        file.write('</Spielstand>')
        file.close()

    def fromXML(self):
        for spieler in self.spieler:
            spieler.fromXML()
        
        

#				<Feld>15<Feld>
#			</Figur>
#		</Figuren>
##	</Spieler> </Spielstand>'''
        


s = Spielfeld()
s.makeSpielfeld()
s.ausgabe()
s.fromXML()
