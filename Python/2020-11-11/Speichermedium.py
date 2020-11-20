class Speichermedium(object):
    def __init__(self):
        self.__kapazitaet = 0.0

    def setKapazitaet(self, kap):
        self.kapazitaet = kap

    def getKapazitaet(self):
        return self.kapazitaet

class CD(Speichermedium):
    def __init__(self):
        super().__init__()
        self.__titel = ""
        self.__anazahlLieder = 0
        self.__liednummer = 0

    def getTitle(self):
        return self.__titel

    def naechstesLied(self):
        pass

    def voherigesLied(self):
        pass

    def getLiednummer(self):
        return self.liednummer

    def setLiednummer(self, nr):
        self.liednummer = nr


class DVD(Speichermedium):
    def __init__(self):
        super().__init__()
        self.aufloesung = ""
        self.laserfarbe = ""

    def setLaserfarbe(self, neueFarbe):
        self.laserfarbe = neueFarbe

    def getLaserfarbe(self):
        return self.laserfarbe
