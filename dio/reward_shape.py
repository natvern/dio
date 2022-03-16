from dio.prologkb.diokb import Dio

## Difference between utilization state vs. observation
## State is easier, obs is harder to implement
## Observation gives more options [unknown variables to state]

## Observation defined as dictionaries containing
 # - an image (partially observable view of the environment)
 # - the agent's direction/orientation (acting as a compass)
 # - a textual mission string (instructions for the agent)

## Pick up goal(X,Y) 
def findGoal(image):
    pass 

## Pick up obstacles(X,Y)
def findObstacles(image):
    pass 

## Pick up agent(X,Y)
def findAgent(image): 
    pass

## Turn left, turn right, move forward
 # left = 0
 # right = 1
 # forward = 2
def getAction(action):
    ## Notice that we're not making use of action yet
    pass 

def reward_shape(obs, action, reward, done):
    image = obs["image"]
    D = Dio()
    # Dio to take [position, direction, obsPositions, goal]
    position = findAgent(image)
    direction = obs['direction']
    obstacles = findObstacles(image)
    goal = findGoal(image)
    D.updateWorld(position,direction,obstacles,goal)
    rr = D.getFeedback()
    ## Do we care about done?
    return rr + reward