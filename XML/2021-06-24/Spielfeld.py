from Feld import *
from Spieler import *
from xml.dom.minidom import *
from xml.dom import minidom

document = minidom.parse('xml-spielstand.xml')


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
    
    def getFeldById(self, feldId):
        for f in self.felder:
            if f.getID() == feldId:
                return f
        return None

    def toXML(self):
        file = open("ausgabe.xml", "w")
        file.write('<?xml version="1.0" encoding="iso-8859-1"?><Spielstand>')
        for spieler in self.spieler:
            file.write(spieler.toXML())
        file.write('</Spielstand>')
        file.close()

    def fromXML(self, doc):
        self.spieler = []
        self.felder = []
        for i in range(40):
            self.felder.append(Feld(i))

        i = -1
        while i < len(self.felder)-2:
            self.felder[i].setNextFeld(self.felder[i+1])
            i += 1
            
        spielerXML = doc.getElementsByTagName('Spieler')
        for spieler in spielerXML:
            neuerSpieler = Spieler(spieler.getElementsByTagName('Name')[0].firstChild.nodeValue, self, spieler.getAttribute('id'))
            self.spieler.append(neuerSpieler)
            neuerSpieler.fromXML(spieler)
            #print(spieler.getElementsByTagName('Name')[0].firstChild.nodeValue, spieler.getAttribute('id'))


s = Spielfeld()
s.makeSpielfeld()
s.ausgabe()
#s.toXML()
s.fromXML(document)
s.ausgabe()
#s.toXML()


