from problog.program import PrologString
from problog.core import ProbLog

from problog import get_evaluatable
from transl import Translate
from problog.engine import DefaultEngine

import copy

class Dio: 
    def __init__(self):
        self.rules = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/ruleskb", "r").read()
        self.world = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/worldkb", "r").read()
        self.labels = open("/Users/srahmoun/Documents/Thesis/dio/prologkb/labels", "r").read()
        self.transl = Translate()
        self.original = DefaultEngine().prepare(PrologString(self.rules+"\n"+self.labels+"\n"+self.world))
        self.know = self.original
        
    def getLabels(self):  
        label = (get_evaluatable().create_from(self.know).evaluate())
        self.know = copy.copy(self.original)
        return label

    def updateWorld(self,position,direction,obstacles,goal):
        ## Consider updating the initial file and make 
        ## log of world changes 
        kb = self.transl.translateFrom([position,direction,obstacles,goal])
        for statement in PrologString(kb):
            self.know += statement

    def getFeedback(self):
        return self.transl.translateTo(self.getLabels())
    
