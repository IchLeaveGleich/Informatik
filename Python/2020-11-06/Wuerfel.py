import random 

class Wuerfel(object):
    def _init__(self):
        self.augenzahl = 0

    def wuerfeln(self):
        self.augenzahl = random.randint(1,6)

    def getAugen(self):
        return self.augenzahl
