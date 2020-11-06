class Gewinnkarte(object):
    def __init__(self, wuerfelListe):
        self.wuerfelListe = wuerfelListe

    def wuerfelAuswerten(self):
        for wuerfel in self.wuefelListe:
            augenzahl = wuefel.getAugenzahl()
            
