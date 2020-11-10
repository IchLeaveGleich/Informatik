class Gewinnkarte(object):
    def __init__(self, wuerfelListe):
        self.wuerfelListe = wuerfelListe

    #Gewürfeltes Auswerten
    def wuerfelAuswerten(self):
        augenzahlListe = [0,0,0,0,0,0]
        for wuerfel in self.wuerfelListe:
            augenzahl = wuerfel.getAugenzahl()
            for i in range(6):
                if augenzahl == i+1:
                    augenzahlListe[i] += 1
        
        #Dreierpasch Abfrage (Oberer Teil)
        for zahl, augen in enumerate(augenzahlListe):
            if augen == 3:
                gesamtOben += zahl+1 * augen
        #Bonus bei 63

