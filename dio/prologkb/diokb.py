from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable
from dio.prologkb.transl import Translate
import os
import dio.prologkb.config as config

class Dio: 
    def __init__(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        ruleskb = os.path.join(dir, 'ruleskb')
        worldkb = os.path.join(dir, 'worldkb')
        labels = os.path.join(dir, 'labels')
        self.rules = open(ruleskb, "r").read()
        self.world = open(worldkb, "r").read()
        self.labels = open(labels,"r").read()
        self.transl = Translate()
        self.alpha = config.config.alpha
        self.steps = 1
        self.p = PrologString(self.world+"\n"+self.rules+"\n"+self.labels)

    def getLabels(self):
        return get_evaluatable().create_from(self.p).evaluate()

    def updateWorld(self,position,direction,obstacles,goal,time):
        ## Consider updating the initial file and make 
        ## log of world changes 
        kbt = self.transl.translateFrom([position,direction,obstacles,goal,time])
        self.world = kbt
        self.p = self.updatePrologString()

    def updatePrologString(self):
        return PrologString(self.world+"\n"+self.rules+"\n"+self.labels)

    def getFeedback(self):
        return self.alpha * (self.transl.translateTo(self.getLabels()))
    
    
