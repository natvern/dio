from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

class Dio: 
    def __init__(self):
        self.rules = open("ruleskb", "r").read()
        self.world = open("worldkb", "r").read()
        self.labels = open("labels","r").read()
        self.p = PrologString(self.world+"\n"+self.rules+"\n"+self.labels)

    def getLabels(self):
        return get_evaluatable().create_from(p).evaluate()

    def updateWorld(self,state):
        ## Should consider translation here or elsewhere?
        ## Consider updating the initial file and make 
        ## log of world changes 
        self.world = state
        self.updatePrologString()

    def updatePrologString(self):
        self.p = PrologString(self.world+"\n"+self.rules+"\n"+self.labels)
    
