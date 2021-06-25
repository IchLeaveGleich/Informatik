from xml.dom.minidom import *

class Figur(object):
    def __init__(self, Id, spieler):
        self.id = Id
        self.spieler = spieler
        self.feld = None

    def setFeld(self,feld):
        self.feld = feld

    def ausgabe(self):
        if self.feld != None:
            feld = self.feld.id
        else:
            feld = "None"
        
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
        code += "</Figur>"
        return code

    def fromXML(self, figurXML, spielfeld):
        
        feldIdStr = figurXML.getElementsByTagName('Feld')[0].firstChild.nodeValue
        if feldIdStr != "None":
            self.feld = spielfeld.getFeldById(int(feldIdStr))
        else:
            self.feld = None





