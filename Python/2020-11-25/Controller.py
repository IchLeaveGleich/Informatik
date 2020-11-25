from Spielmanager import *
from GUI import *

class Controller(object):
    def __init__(self):
        self.spielmanager = Spielmanager()
        self.gui = GUI(self.spielmanager.getDictOfProcedure())
