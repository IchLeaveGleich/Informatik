from tkinter import *

class GUI(object):
    def __init__(self, wb):
        self.tkFenster = Tk()
        self.wb = wb
        
        self.tkFenster.title("Chuck A Luck")
        self.tkFenster.geometry("1200x600")
        
        self.labelTitle = Label(master=self.tkFenster, bg="white", text = "Chuck A Luck", font = ("Arial", 36))
        self.labelTitle.place(x=10, y=5, width = 1180, height = 75)

        self.labelGrid = Label(master=self.tkFenster, bg="white")
        self.labelGrid.place(x=10, y=90, width=1180, height = 450)

        self.button1 = Button(master=self.labelGrid, bg="white", text="1", font=("Arial",50), command=lambda:self.refresh(1))
        self.button1.place(x=10, y=20, width=320, height=150)

        self.button2 = Button(master=self.labelGrid, bg="white", text="2", font=("Arial",50), command=lambda:self.refresh(2))
        self.button2.place(x=(1160/2)-160, y=20, width=320, height=150)

        self.button3 = Button(master=self.labelGrid, bg="white", text="3", font=("Arial",50), command=lambda:self.refresh(3))
        self.button3.place(x=850, y=20, width=320, height=150)

        self.wuerfel1 = Label(master=self.labelGrid, bg="white", font=("Arial", 18), text="Wuerfel 1: {}".format(wb["augen"]()[0]))
        self.wuerfel1.place(x=70, y=200, width=200, height=50)

        self.wuerfel2 = Label(master=self.labelGrid, bg="white",font=("Arial", 18), text="Wuerfel 2: {}".format(wb["augen"]()[1]))
        self.wuerfel2.place(x=(1160/2)-100, y=200, width=200, height=50)

        self.wuerfel3 = Label(master=self.labelGrid, bg="white", font=("Arial", 18), text="Wuerfel 3: {}".format(wb["augen"]()[2]))
        self.wuerfel3.place(x=920, y=200, width=200, height=50)

        self.button4 = Button(master=self.labelGrid, bg="white", text="4", font=("Arial",50), command=lambda:self.refresh(4))
        self.button4.place(x=10, y=280, width=320, height=150)

        self.button5 = Button(master=self.labelGrid, bg="white", text="5", font=("Arial",50), command=lambda:self.refresh(5))
        self.button5.place(x=(1160/2)-160, y=280, width=320, height=150)

        self.button6 = Button(master=self.labelGrid, bg="white", text="6", font=("Arial",50),command=lambda:self.refresh(6))
        self.button6.place(x=850, y=280, width=320, height=150)

        self.labelButton = Label(master=self.tkFenster, bg="white")
        self.labelButton.place(x=10, y=550, width=1180, height=45)

        #buttonVerlassen = Button(master=labelButton, bg="grey", text="Verlassen")
        #buttonVerlassen.place(x=5, y=5, width=150, height=35)

        #buttonWuerfeln = Button(master=labelButton, bg="grey", text="Wuerfeln")
        #buttonWuerfeln.place(x=440, y=5, width=300, height=35)
        
        #buttonWeiter = Button(master=labelButton, bg="grey", text="Weiter")
        #buttonWeiter.place(x=1025, y=5, width=150, height=35)
        
        self.tkFenster.mainloop()

    def refresh(self, gesetzteZahl):
        self.wb["spielen"](gesetzteZahl)
        self.wuerfel1.config(text="Wuerfel 1:{}".format(self.wb["augen"]()[0]))
        self.wuerfel2.config(text="Wuerfel 2:{}".format(self.wb["augen"]()[1]))
        self.wuerfel3.config(text="Wuerfel 3:{}".format(self.wb["augen"]()[2]))
        

    
