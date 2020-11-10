from Gewinnkarte import Gewinnkarte

class Spieler(object):
    def __init__(self,wuerfelListe):
        self.name = ""
        self.wuerfelListe = wuerfelListe
        self.gewinnkarte = Gewinnkarte(self.wuerfelListe)
        
    def setName(self, nameInput):
        self.name = nameInput

    def getName(self):
        return self.name

    def wuerfelSichern(self,inputWuerfel):
        inputWuerfel.istGesichert()
        
