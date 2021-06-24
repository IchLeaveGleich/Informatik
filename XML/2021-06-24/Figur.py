from xml.dom.minidom import *

class Figur(object):
    def __init__(self, Id, spieler):
        self.id = Id
        self.spieler = spieler
        self.feld = None

    def setFeld(self, feld):
        self.feld = feld

    def ausgabe(self):
        if self.feld != None:
            feld = self.feld.id
        else:
            feld = None

        print(self.id, self.spieler.id, feld)
        return([self.id, self.spieler.id, feld])

    def toXML(self):
        code = "<Figur id='" + str(self.id) + "'>\n"
        code += "<Feld>"
        if self.feld == None:
            code += "None"
        else:
            code += str(self.feld.id)
        code += "</Feld>\n"
        code += "</Figur>\n"
        return code

    def fromXML(self):
        dokument = parse("eingabe.xml")
        alleFigur = dokument.getElementsByTagName("Figur")
        for figur in alleFigur:
            if int(figur.getAttribute("id")) == self.id:
                self.setFeld(figur.getElementsByTagName("Feld")[0].firstChild.nodeValue)
                #print(figur.getElementsByTagName("Feld")[0].firstChild.nodeValue)
