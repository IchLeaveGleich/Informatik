import random

class Wuerfel(object):
    def __init__(self):
        self.augen = 0

    def werfen(self):
        self.augen = random.randint(1,6)

    def getAugen(self):
        return self.augen
