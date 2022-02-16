import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np




## Start with simple action choices 
## Either accelerate, constant or deaccelerate for vehicle 1 
## Similarly for vehicle 2. Thus, 9 possible actions. 

class PlatoonEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  
  def __init__(self):
    self.state = np.array([0,10,0,0])
    # deaccelerate lot + bit + constant + accelerate bit + lot
    self.action_space = spaces.Discrete(9)
    # possible rewards defined as the distance between the vehicles
    self.reward_range = (-200,200)
    # x-pos 1 + x-pos 2 + velocity v1 + v2
    self.observation_space = spaces.Box(low=np.array([-100,-100,-10,-10]), high=np.array([100,100,10,10]))
    self.MINGAP = 10

  def step(self, action):
    self.take_action(action)
    done = False 
    if self.state[1] < self.state[0]: 
        done = True
        return self.state, -200, done, dict()
    return self.state, self.get_reward(), done, dict()

  def reset(self):
    self.state = np.array([0,10,0,0])
    return self.state

  def render(self, mode='human', close=False):
    print(self.state)

  def take_action(self, action):
    state = self.state
    if action == 0: ## Accelerate + Accelerate
        velocity1 = state[2]+1 
        velocity2 = state[3]+1
    if action == 1: ## Accelerate + Constant
        velocity1 = state[2]+1 
        velocity2 = state[3]
    if action == 2: ## Accelerate + Deaccelerate
        velocity1 = state[2]+1 
        velocity2 = state[3]-1
    if action == 3: ## Deaccelerate + Accelerate
        velocity1 = state[2]-1 
        velocity2 = state[3]+1
    if action == 4: ## Deaccelerate + Constant
        velocity1 = state[2]-1 
        velocity2 = state[3]
    if action == 5: ## Deaccelerate + Deaccelerate
        velocity1 = state[2]-1 
        velocity2 = state[3]-1
    if action == 6: ## Constant + Deaccelerate
        velocity1 = state[2] 
        velocity2 = state[3]-1
    if action == 7: ## Constant + Accelerate
        velocity1 = state[2] 
        velocity2 = state[3]+1
    if action == 8: ## Constant + Constant
        velocity1 = state[2]
        velocity2 = state[3]
    self.state = np.array([self.state[0]+self.state[2], self.state[1]+self.state[3],velocity1,velocity2])

  def get_reward(self):
    if (self.state[1] - self.state[0] < self.MINGAP): 
        return -200
    return -(abs(self.state[1] - self.state[0]))
