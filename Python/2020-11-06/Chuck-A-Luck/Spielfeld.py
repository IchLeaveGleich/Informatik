class Spielfeld(object):
    def __init__(self):
        self.gesetzteZahl = None

    def zahlSetzen(self, inputGesetzteZahl):
        self.gesetzteZahl = inputGesetzteZahl

    def getGesetzteZahl(self):
        return self.gesetzteZahl
