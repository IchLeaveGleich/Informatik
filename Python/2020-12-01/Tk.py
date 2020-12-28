from tkinter import *

class GUI(object):
    def __init__(self):

        self.fenster = Tk()
        self.fenster.geometry("1200x600")
        self.fenster.title("Test")

        self.label1 = Label(master=self.fenster, bg="white")
        self.label1.place(x=50, y=50, width=1100, height=200)

        self.button1 = Button(master=self.fenster, bg="white", command=lambda: self.label1.config(text="Clicked"), text="Click Me" )
        self.button1.place(x=500, y=350, width=200, height=100)

        self.fenster.mainloop()


g = GUI()
