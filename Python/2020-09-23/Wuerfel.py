from random import randint

class Wuerfel(object):
    def __init__(self):
        self.augen = 0

    def werfen(self):
        self.augen = randint(1,6)

    def getAugen(self):
        return self.augen
