class Translate(): 
    def __init__(self):
        pass
    def translateFrom(self, state):
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
            obskb += "1.0 :: obs(0,{},{},0,0).\n".format(obs[0],obs[1])
        conskb = self.getConstants()
        return conskb + poskb + dirkb + obskb
        

    def translateTo(self, labels):
        # from labels to reward
        sLabels = {}
        for label in labels:
            sLabels[str(label)] = labels[label]
        return sLabels["crashmaybe"]*0.05 + sLabels["crash"]*-0.1

    def getConstants(self):
        s = "1.0 :: speed(1).\n" + "1.0 :: acc(0).\n" + "1.0 :: time(0).\n" + "1.0 :: timestep(1).\n"
        return s