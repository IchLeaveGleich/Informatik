class Spielfeld(object):
    def __init__(self):
        self.gesetzteZahl = 0

    def setzen(self, zahl):
        self.gesetzteZahl = zahl

    def getGesetzteZahl(self):
        return self.gesetzteZahl
