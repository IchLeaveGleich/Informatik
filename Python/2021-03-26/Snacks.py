class Snack(object):
    def __init__(self, name, preis, kasse):
        self.name = name
        self.preis = preis
        self.kasse = kasse
        self.stand = 0

    def auswaehlen(self, name):
        self.kasse.einkfauskorb.append()

    def getStand(self):
        return self.stand

    def getName(self):
        return self.name

    def getPreis(self):
        return self.preis.getPreis()


