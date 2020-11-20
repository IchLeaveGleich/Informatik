from AmpelSteuerung import *
from Gui import *

class Controller(object):
    def __init__(self):
        self.model = AmpelSteuerung()
        self.gui = GUI(self.model.makeListOfProcedure())

c = Controller()
