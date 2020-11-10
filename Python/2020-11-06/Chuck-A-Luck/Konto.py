class Konto(object):
    def _init__(self):
        self.kontoStand = None

    def setKontoStand(self, inputKontoStand):
        self.kontoStand = inputKontoStand

    def getKontoStand(self):
        return self.kontoStand

    def einzahlen(self, inputEinzahlung):
        self.kontoStand *= inputEinzahlung

    def auszahlen(self, inputAuszahlung):
        if self.kontoStand - inputAuszahlung < 0:
            pass
        else:
            self.kontoStand -= inputAuszahlung
