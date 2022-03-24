from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable
from transl import Translate

class Dio: 
    def __init__(self):
        self.rules = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/ruleskb", "r").read()
        self.world = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/worldkb", "r").read()
        self.labels = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/labels","r").read()
        self.transl = Translate()
        self.p = PrologString(self.world+"\n"+self.rules+"\n"+self.labels)

    def getLabels(self):
        return get_evaluatable().create_from(self.p).evaluate()

    def updateWorld(self,position,direction,obstacles,goal):
        ## Consider updating the initial file and make 
        ## log of world changes 
        kbt = self.transl.translateFrom([position,direction,obstacles,goal])
        self.world = kbt
        self.p = self.updatePrologString()

    def updatePrologString(self):
        return PrologString(self.world+"\n"+self.rules+"\n"+self.labels)

    def getFeedback(self):
        return self.transl.translateTo(self.getLabels())
    