class Spieler(object):
    def __init__(self, spielfeld):
        self.spielfeld = spielfeld
        self.zeichen = ""

    def spielen(self, spalte, reihe):
        pass

    def getZeichen(self):
        return self.zeichen

    def setZeichen(self, zeichen):
        self.zeichen = zeichen
