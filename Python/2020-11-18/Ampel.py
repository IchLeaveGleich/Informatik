class Ampel(object):
    def __init__(self):
        self.zustand = 1

    def naechsterZustand(self):
        if self.zustand+1 >= 5:
            self.zustand = 1
        else:
            self.zustand += 1

        #self.zustand = (self.zustand % 4) + 1
    def anzeige(self):
        if self.zustand == 1:
            return [True, False, False]
        elif self.zustand == 2:
            return [True, True, False]
        elif self.zustand == 3:
            return [False, False, True]
        else:
            return [False, True, False]


