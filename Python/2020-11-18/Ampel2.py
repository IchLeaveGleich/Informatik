class Ampel(object):
    def __init__(self):
        self.zustand = 1
     

    def naechsterZustand(self):
        if self.zustand + 1 >= 5:
            self.zustand = 1
        else:
            self.zustand += 1

    def anzeige(self):
        if self.zustand == 1:
            return [True, False, False] #An,Aus,Aus
        
        elif self.zustand == 2:
            return [True, True, False] #An,An,Aus
           
        elif self.zustand == 3:
            return [False, False, True] #Aus,Aus,an 
        else:
            return [False, True, False] #Aus,An,Aus



class Ampelsteuerung(object):
    def __init__(self):
        self.ampel1 = Ampel()#Rot
        self.ampel2 = Ampel()#Rot
        self.ampel2.naechsterZustand() #RotGelb
        self.ampel2.naechsterZustand() #Grün

    def weiterSchalten(self):
        if self.ampel2.zustand==1:
            self.ampel1.naechsterZustand()
        elif self.ampel1.zustand==1:     
            self.ampel2.naechsterZustand()


    def makeListOfProcedure(self):
        liste = [self.ampel1.anzeige, self.ampel2.anzeige, self.weiterSchalten]
        return liste




















    
