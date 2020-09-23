class Konto(object):
    def __init__(self, startbetrag):
        self.stand = startbetrag

    def einzahlen(self, betrag):
        self.stand += betrag

    def auzahlen(self, betrag):
        if (self.stand - betrag) >= 0:
            self.stand -= betrag
        else:
            self.stand = 0
            
    def getStand(self):
        return self.stand
