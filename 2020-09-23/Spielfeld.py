class Spielfeld(object):
    def __init__(self):
        self.gesetzteZahl = 0

    def setzten(self, zahl):
        self.gesetzteZahl = zahl

    def getGesetzteZahl(self):
        return self.gesetzteZahl
