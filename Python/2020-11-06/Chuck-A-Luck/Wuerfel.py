import random

class Wuerfel(object):
    def __init__(self):
        self.augenzahl = None

    def wuerfeln(self):
        self.augenzahl = random.randint(1,6)

    def getAugenzahl(self):
        return self.augenzahl

