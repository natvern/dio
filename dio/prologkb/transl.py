import csv
from dio.prologkb.config import config


class Translate(): 
    time = 0
    def __init__(self):
        self.time = 0

    def translateFrom(self, state):
        self.time = state[4]
        position = state[0] # position
        poskb  = "1.0 :: atPos({}, {}).\n".format(position[0],position[1])
        direction = state[1] # direction
        if (direction == 0):
            dirkb = "1.0 :: direction({}).\n".format("right")
        elif (direction == 1):
            dirkb = "1.0 :: direction({}).\n".format("down")
        elif (direction == 2):
            dirkb = "1.0 :: direction({}).\n".format("left") 
        elif (direction == 3):
            dirkb = "1.0 :: direction({}).\n".format("up")
        else:
            raise "Unknown direction state"
        obstacles = state[2]
        obskb = ""
        for obs in obstacles:
            if obs[0] <= position[0]+2 and obs[0] >= position[0]-2:
                if obs[1] <= position[1]+2 and obs[1] >= position[1]-2:
                    obskb += "1.0 :: obs(0,{},{},1,0).\n".format(obs[0],obs[1])
        conskb = self.getConstants()
        goal = state[3]
        goalkb = "1.0 :: goal({},{}).\n".format(goal[0],goal[1])
        timekb = "1.0 :: time({}).\n".format(self.time)
        if obskb == "":
            obskb = "1.0 :: obs(0,-1,-1,1,0).\n"
        return conskb + poskb + dirkb + obskb + goalkb + timekb
        

    def translateTo(self, labels):
        # from labels to reward
        sLabels = {}
        for label in labels:
            sLabels[str(label)] = labels[label]
        myLabels = self.getInference()
        r = 0
        for label in sLabels.keys():
            #print(label + " has probability:" + str(sLabels[label]))
            r += myLabels[label]*sLabels[label]
        # Need to normalize feedback
        #print("Original feedback: " + str(r))
        r = r * config.normalize
        return r

    def normalize(self, r):
        zeroOne = (r - config.min_dio) / (config.max_dio - config.min_dio)
        return 2 * zeroOne - 1

    def getConstants(self):
        n = config.max_steps
        s = "1.0 :: speed(1).\n" + "1.0 :: acc(0).\n" + "1.0 :: timestep(1).\n" \
                + "1.0 :: max_steps({}).\n".format(n)
        return s

    def getInference(self):
        with open('../prologkb/inference.csv', mode='r') as inp:
            reader = csv.reader(inp)
            D = {rows[0]:float(rows[1]) for rows in reader}
        return D
