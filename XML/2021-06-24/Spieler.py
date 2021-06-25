from Figur import *
from random import *
from xml.dom.minidom import *


class Spieler(object):
    def __init__(self, name, spielfeld, Id):
        self.id = Id
        self.spielfeld = spielfeld
        self.name = name
        self.figuren = []
        for i in range(4):
            self.figuren.append(Figur(i, self))

    def setFiguren(self):
        for f in self.figuren:
            if randint(0,3) > 0:
                zufall = randint(0, len(self.spielfeld.getFelder())-1)
                while not self.spielfeld.getFelder()[zufall].frei():
                    zufall = randint(0, len(self.spielfeld.getFelder())-1)
                feld = self.spielfeld.getFelder()[zufall]
                feld.setFigur(f)
                f.setFeld(feld)

    def ausgabe(self):
        print(self.name)
        for f in self.figuren:
            f.ausgabe()
        print("")
        print("")

    def getID(self):
        return self.id
        

    def toXML(self):
        code = "<Spieler id='" + str(self.id) + "'>\n"
        code += "<Name>" + self.name + "</Name>\n"
        code += "<Figuren>\n"
        for figur in self.figuren:
            code += figur.toXML()
        code += "</Figuren>\n"
        code += "</Spieler>\n"
        return code

    def fromXML(self, spielerXML):
        self.figuren = []
        figurenXML = spielerXML.getElementsByTagName('Figur')
        for figur in figurenXML:
            neueFigur = Figur(figur.getAttribute('id'), self)
            self.figuren.append(neueFigur)
            neueFigur.fromXML(figur,self.spielfeld)

        """
     for spieler in spielerXML:
            neuerSpieler = Spieler(spieler.getElementsByTagName('Name')[0], self, spieler.getAttribute('id'))
            self.spieler.append(neuerSpieler)
            neuerSpieler.fromXML(spieler)
            #print(spieler.getElementsByTagName('Name')[0].firstChild.nodeValue, spieler.getAttribute('id'))
"""


