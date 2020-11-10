import random 

class Wuerfel(object):
    def _init__(self):
        self.augenzahl = 0
        self.zustand = False

    def wuerfeln(self):
        self.augenzahl = random.randint(1,6)

    def getAugen(self):
        return self.augenzahl

    def istGesichert(self):
        if self.zustand == True:
            return self.zustand
        else:
            self.zustand = True
