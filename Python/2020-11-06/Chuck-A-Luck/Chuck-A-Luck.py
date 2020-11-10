from tkinter import *
from Spielanbieter import Spielanbieter

class ChuckALuck(object):
    def __init__(self):
        self.tkFenster = Tk()
        self.spielanbieter = Spielanbieter()

    def createWindow(self):
        self.tkFenster.title("Chuck A Luck")
        self.tkFenster.geometry("1200x600")

    def feldAuswaehlen(self):
        pass

    def createTitleLabel(self):
        labelTitle = Label(master=self.tkFenster, bg="white", text = "Chuck A Luck", font = ("Arial", 36))
        labelTitle.place(x=10, y=5, width = 1180, height = 75)

    def createGrid(self):
        labelGrid = Label(master=self.tkFenster, bg="white")
        labelGrid.place(x=10, y=90, width=1180, height = 450)

        button1 = Button(master=labelGrid, bg="white", text="1", command=self.spielanbieter.spielfeld.zahlSetzen(1))
        button1.place(x=10, y=20, width=320, height=150)

        button2 = Button(master=labelGrid, bg="white", text="2", command=self.spielanbieter.spielfeld.zahlSetzen(2))
        button2.place(x=(1160/2)-160, y=20, width=320, height=150)

        button3 = Button(master=labelGrid, bg="white", text="3", command=self.spielanbieter.spielfeld.zahlSetzen(3))
        button3.place(x=850, y=20, width=320, height=150)

        button4 = Button(master=labelGrid, bg="white", text="4", command=self.spielanbieter.spielfeld.zahlSetzen(4))
        button4.place(x=10, y=280, width=320, height=150)

        button5 = Button(master=labelGrid, bg="white", text="5", command=self.spielanbieter.spielfeld.zahlSetzen(5))
        button5.place(x=(1160/2)-160, y=280, width=320, height=150)

        button6 = Button(master=labelGrid, bg="white", text="6", command=self.spielanbieter.spielfeld.zahlSetzen(6))
        button6.place(x=850, y=280, width=320, height=150)

    def createButtonLabel(self):
        labelButton = Label(master=self.tkFenster, bg="white")
        labelButton.place(x=10, y=550, width=1180, height=45)

        buttonVerlassen = Button(master=labelButton, bg="grey", text="Verlassen")
        buttonVerlassen.place(x=5, y=5, width=150, height=35)
        buttonWuerfeln = Button(master=labelButton, bg="grey", text="Wuerfeln")
        buttonWuerfeln.place(x=440, y=5, width=300, height=35)
        buttonWeiter = Button(master=labelButton, bg="grey", text="Weiter")
        buttonWeiter.place(x=1025, y=5, width=150, height=35)

    def spielVerlassen(self):
        pass

    def mainLoop(self):
        pass


cal = ChuckALuck()
cal.createWindow()
cal.createGrid()
cal.createTitleLabel()
cal.createButtonLabel()

cal.tkFenster.mainloop()
