#------------------------------------------------------------------------------
# GUI
#------------------------------------------------------------------------------
import time
from tkinter import *

black = "black"
red = "red"
yellow = "gold"
green = "green"
grey = "grey"

class GUI(object):
    def __init__(self, listOfProcedure):
        #Laden der Prozeduren
        self.anzeigenAmpel1 = listOfProcedure[0]
        self.anzeigenAmpel2 = listOfProcedure[1]
        self.naechsteSchaltung = listOfProcedure[2]
        
        #Fenster Erzeugung
        self.ampel1_fenster = Tk()
        self.ampel2_fenster = Tk()
        self.schalten_fenster = Tk()
        #Titel
        self.ampel1_fenster.title('Ampel 1')
        self.ampel2_fenster.title('Ampel 2')
        self.schalten_fenster.title("Schaltfenster")
        #Fenster Groesse
        self.ampel1_fenster.geometry('200x600')
        self.ampel2_fenster.geometry('200x600')
        self.schalten_fenster.geometry('200x200')
        #Background Frame
        self.frameBackground1 = Frame(master=self.ampel1_fenster, background=black)
        self.frameBackground1.place(x=0, y=0, width=200, height=600)

        self.frameBackground2 = Frame(master=self.ampel2_fenster, background=black)
        self.frameBackground2.place(x=0, y=0, width=200, height=600)

        #Button zum schalten
        self.buttonAmpelSchalten = Button(master=self.schalten_fenster, text="SCHALTEN", bg='white', font= ("Times New Roman",20),command = self.buttonSchaltenKlick )
        self.buttonAmpelSchalten.place(x=10, y=10, width=180, height=180)

        self.anzeigeAktualisieren()

    def buttonSchaltenKlick(self):
        self.naechsteSchaltung()
        self.anzeigeAktualisieren()

    def anzeigeAktualisieren(self):
        ampel1 = self.anzeigenAmpel1()
        ampel2 = self.anzeigenAmpel2()

        if ampel1[0]:
            self.A1L1()
        else:
            self.A1L1_off()

        if ampel1[1]:
            self.A1L2()
        else:
            self.A1L2_off()

        if ampel1[2]:
            self.A1L3()
        else:
            self.A1L3_off()

        if ampel2[0]:
            self.A2L1()
        else:
            self.A2L1_off()

        if ampel2[1]:
            self.A2L2()
        else:
            self.A2L2_off()

        if ampel2[2]:
            self.A2L3()
        else:
            self.A2L3_off()
    
        #Ampel 1
    def A1L1(self):
        #Licht 1 an
        self.canvas1 = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas1.place(x=0, y=0, width=200, height=200)
        self.id_rot = self.canvas1.create_oval(10, 10, 190, 190, fill=red)

    def A1L1_off(self):
        #Licht 1 aus
        self.canvas1_off = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas1_off.place(x=0, y=0, width=200, height=200)
        self.id_grey = self.canvas1_off.create_oval(10, 10, 190, 190, fill=grey)
        
    def A1L2(self):
        #Licht 2 an
        self.canvas2 = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas2.place(x=0, y=200, width=200, height=200)
        self.id_yellow = self.canvas2.create_oval(10, 10, 190, 190, fill=yellow)

    def A1L2_off(self):
        #Licht 2 aus
        self.canvas2_off = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas2_off.place(x=0, y=200, width=200, height=200)
        self.id_grey = self.canvas2_off.create_oval(10, 10, 190, 190, fill=grey)
        
    def A1L3(self):
        #Licht 3 an
        self.canvas3 = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas3.place(x=0, y=400, width=200, height=200)
        self.id_yellow = self.canvas3.create_oval(10, 10, 190, 190, fill=green)

    def A1L3_off(self):
        #Licht 3 aus
        self.canvas3_off = Canvas(master=self.ampel1_fenster, background=black)
        self.canvas3_off.place(x=0, y=400, width=200, height=200)
        self.id_grey = self.canvas3_off.create_oval(10, 10, 190, 190, fill=grey)

        #Ampel 2
    def A2L1(self):
        #Licht 1 an
        self.canvas1 = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas1.place(x=0, y=0, width=200, height=200)
        self.id_rot = self.canvas1.create_oval(10, 10, 190, 190, fill=red)
        
    def A2L1_off(self):
        #Licht 1 aus
        self.canvas1_off = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas1_off.place(x=0, y=0, width=200, height=200)
        self.id_grey = self.canvas1_off.create_oval(10, 10, 190, 190, fill=grey)
        
    def A2L2(self):
        #Licht 2 an
        self.canvas2 = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas2.place(x=0, y=200, width=200, height=200)
        self.id_yellow = self.canvas2.create_oval(10, 10, 190, 190, fill=yellow)
        
    def A2L2_off(self):
        #Licht 2 aus
        self.canvas2_off = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas2_off.place(x=0, y=200, width=200, height=200)
        self.id_grey = self.canvas2_off.create_oval(10, 10, 190, 190, fill=grey)
        
    def A2L3(self):
        #Licht 3 an
        self.canvas3 = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas3.place(x=0, y=400, width=200, height=200)
        self.id_yellow = self.canvas3.create_oval(10, 10, 190, 190, fill=green)

    def A2L3_off(self):
        #Licht 3 aus
        self.canvas3_off = Canvas(master=self.ampel2_fenster, background=black)
        self.canvas3_off.place(x=0, y=400, width=200, height=200)
        self.id_grey = self.canvas3_off.create_oval(10, 10, 190, 190, fill=grey)


        
