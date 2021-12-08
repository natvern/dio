import gym
import sys
import os
import time
import copy
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from PIL import Image as Image
import matplotlib.pyplot as plt
import matplotlib

# define colors
# 0: black; 1 : gray; 2 : blue; 3 : green; 4 : red
COLORS = {0:[0.0,0.0,0.0], 1:[0.5,0.5,0.5], \
          2:[0.0,0.0,1.0], 3:[0.0,1.0,0.0], \
          4:[1.0,0.0,0.0], 6:[1.0,0.0,1.0], \
          7:[1.0,1.0,0.0]}

class GridworldEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    num_env = 0
    def __init__(self):
        self._seed = 0
        self.action_names = ["Right", "Left", "Up", "UpP"]
        self.action_space = spaces.Discrete(4)
        self.rng, self.seed = seeding.np_random()
        this_file_path = os.path.dirname(os.path.realpath(__file__))
        self.img_path = os.path.join(this_file_path, 'gridimg')
        self.arr_img = [plt.imread(self.img_path + "_s{}.png".format(i), format='png') for i in range(6)]

        ''' set observation space / same as state space'''
        self.observation_space = spaces.Discrete(6)

        self.observation = 1
        matplotlib.use('TkAgg')

        ''' agent state: start, target, current state '''
        self.agent_start_state = 1
        self.agent_state = self.agent_start_state


        ''' set other parameters '''
        self.restart_once_done = False  # restart or not once done
        self.verbose = True # to show the environment or not

        GridworldEnv.num_env += 1
        self.this_fig_num = GridworldEnv.num_env
        #if self.verbose == True:
        #    self.fig = plt.figure(self.this_fig_num)
        #    plt.show(block=False)
        #    plt.axis('off')
        #    self.render()

    def _do_up_step(self, r):
        info = {}
        if self.agent_state in [4,5]: # bounces
            return (self.agent_state, r, False, info)
        if self.agent_state == 2:
            return (4, r, False, info)
        if self.agent_state == 3:
            return (5, r, False, info)
        if self.agent_state == 0:
            return (2, r, False, info)
        if self.agent_state == 1:
            return (3, r, False, info)
    def _do_left_step(self):
        info = {}
        info['success'] = True
        if self.agent_state in [0,2,4]:
            if self.agent_state == 2:
                return (2, -100, False, info)
            elif self.agent_state == 4:
                return (0, 10, False, info)
            else:  # bounces
                return (self.agent_state, -1, False, info)
        else:
            if self.agent_state == 1:
                return (0, 0, False, info)
            elif self.agent_state == 3:
                return (2, 0, False, info)
            elif self.agent_state == 5:
                return (4, 0, False, info)
    def _do_right_step(self):
        info = {}
        info['success'] = True
        if self.agent_state in [1,3,5]:  # bounces
            return (self.agent_state, -1, False, info)
        else:
            if self.agent_state == 0:
                return (1, 0, False, info)
            elif self.agent_state == 2:
                return (3, 0, False, info)
            elif self.agent_state == 4:
                return (5, 0, False, info)

    def step(self, action_id):
        ''' return next observation, reward, finished, success '''
        info = {}
        action = self.action_names[action_id]
        #print(action, self.agent_state)
        info['success'] = False
        if action == "Left": #
            ret = self._do_left_step()
        if action == "Right":
            ret = self._do_right_step()
        if action == "Up":
            ret = self._do_up_step(-1)
        if action == "UpP":
            val = self.rng.uniform()
            if val <= 0.8:
                ret = self._do_up_step(0)
            elif val <= 0.9:
                ret = self._do_left_step()
            else:
                ret = self._do_right_step()
        self.agent_state = ret[0]
        return ret

    def reset(self):
        self.agent_state = self.agent_start_state
        self.observation = self.agent_state
        #self.render()
        return self.observation

    def render(self, mode='human', close=False):
        #if self.verbose == False:
        #    return
        #img = self.arr_img[self.agent_state]
        #fig = plt.figure(self.this_fig_num)
        #plt.clf()
        #plt.imshow(img)
        #fig.canvas.draw()
        #plt.pause(0.00001)
        return


    def get_agent_state(self):
        ''' get current agent state '''
        return self.agent_state

    def get_start_state(self):
        ''' get current start state '''
        return self.agent_start_state
    def get_action_name(self, action_id):
        return self.action_names[action_id]
    def get_number_of_actions():
        return self.action_space.n


    def _close_env(self):
        plt.close(1)
        return
