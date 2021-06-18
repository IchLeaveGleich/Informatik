class Feld(object):
    def __init__(self, Id):
        self.id = Id        
        self.figur = None
        self.nextFeld = None

    def setNextFeld(self,feld):
        self.nextFeld = feld

    def setFigur(self, figur):
        self.figur = figur

    def frei(self):
        return self.figur == None
