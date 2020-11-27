class Kasse(object):
    def __init__(self):
        self.kontostand = 50

    def einzahlen(self, gewinn):
        self.kontostand += gewinn

    def auszahlen(self):
        if self.kontostand-1 <= 0:
            return False
        else:
            self.kontostand -= 1
            return True

    def getKontostand(self):
        return self.kontostand
