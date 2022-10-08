import numpy
import csv


class Config:

    def __init__(self):
    ## Variables for tracking 
    ## Data during Training
        self.exhaust = 0

        ## Given rewards for RL 
        self.reward_succ = 1
        self.reward_fail = -1
        self.reward_life = -0.0001 
        self.reward_exhaust = -1
        self.max_steps = 10000

        ## Weight given to DIO
        self.weight_dio = 1
        self.min_dio = -2.84
        self.max_dio = 2.65

        ## Placement of Goal
        self.width = 100
        self.height = 100 
        self.goalX = numpy.random.randint(0, high=self.width-2)
        self.goalY = numpy.random.randint(0, high=self.height-2)

        self.minimal = 3
        self.intermediate = ((self.width-2) * (self.height-2))/3
        self.apocalyptic = 18


        self.currentFile = "normalized-alpha-onlycrash-0-intermediate-100x100-vf-v1-180000"
        self.alpha = 0 ## Weight for DIO
        self.obstacles = self.intermediate

        self.normalize = abs(self.reward_life / 0.75)



config = Config()

global Csucc 
global Cfail 
global Cexhaust


def increase_success():
    f = open("../prologkb/sfe/" + config.currentFile + ".csv", 'a')
    writer = csv.writer(f)
    writer.writerow([1]) 
    f.close()

def increase_failure():
    f = open("../prologkb/sfe/" + config.currentFile + ".csv", 'a')
    writer = csv.writer(f)
    writer.writerow([-1]) 
    f.close()

def increase_exhaust():
    f = open("../prologkb/sfe/" + config.currentFile + ".csv", 'a')
    writer = csv.writer(f)
    writer.writerow([0]) 
    f.close()

def count():
    success = 0
    failure = 0
    exhaustion = 0
    with open("../prologkb/sfe/" + config.currentFile + ".csv", 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[0] == "0": 
                exhaustion += 1
            if row[0] == "1":
                success += 1
            if row[0] == "-1":
                failure += 1 
    return [success, failure, exhaustion]
