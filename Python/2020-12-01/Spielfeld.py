class Spielfeld(object):
    def __init__(self):
        self.spielfeld = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

    def zeichenSetzen(self, zeichen, spalte, reihe):
        self.spielfeld[reihe][spalte]

    def getSpielfeld(self):
        return self.spielfeld
        

                          
