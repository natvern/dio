# DEADLINES
- [x] **Abstract and Problem Statement** Aug 27th 
- [x] **Prospectus** Oct 1st
- [x] **Mid-Semester Presentation** Oct 18th
- [x] **Public Poster Presentation** Dec 8th
- [x] **Mid-Year Report** Dec 10th

--------------------------------------

- [x] **Mid-Semester Presentation** Mar 7th
- [ ] **Thesis Draft** Mar 25th
- [ ] **MOTM Presentation** Apr 22nd
- [ ] **Final Thesis** Apr 28th
- [ ] **Final Presentation** Apr 28th

--------------------------------------

This repository has submodules. To clone it, use:

```
git clone --recurse-submodules git@github.com:natvern/Thesis.git
```

--------------------------------------
# Dynamic Obstacles in a Gridworld 
There should be two files of interest in the gym-minigrid environment: *dynamicobstacles.py* for the environment only with the Reinforcement Learning and *probgrid.py* to include dio. 

All the files are in the dio folder.
First, set up the required conda environment. There is **.yml** file. You can initiate the environment with: 
```
conda env create -f dio.yml
conda activate dio
```

Before running the implementation, run the required installations. 
```
cd gym-minigrid 
pip3 install -e .
cd ../torch-ac
pip3 install -e .
cd ../rl-starter-files 
pip3 install -r requirements.txt 
```

You can now train the implementation without dio and with dio by:
```
python3 -m scripts.train --env MiniGrid-Dynamic-Obstacles-8x8-v0 --model DynamicObstacles --algo ppo --save-interval 10 --frames 80000
python3 -m scripts.train --env MiniGrid-ProbGrid-8x8-v0 --model DioDynamicObstacles --algo ppo --save-interval 10 --frames 80000
```
To visualize:
```
python3 -m scripts.visualize --env MiniGrid-Dynamic-Obstacles-8x8-v0 --model DynamicObstacles
python3 -m scripts.visualize --env MiniGrid-ProbGrid-8x8-v0 --model DioDynamicObstacles 
```
And finally, to evaluate:
```
python3 -m scripts.evaluate --env MiniGrid-Dynamic-Obstacles-8x8-v0 --model DynamicObstacles
python3 -m scripts.evaluate --env MiniGrid-Dynamic-Obstacles-8x8-v0 --model DioDynamicObstacles 
```
You should find more details on the parameters in rl-starter-files README. 

--------------------------------------
# TODO
- Adapt for SARSA/Q-Learning
- Consider mix-matching between number of steps ahead and number of steps to query
- Testing meta-learning through how well the two policies adapt
- Read on reward evolution 
- Run RL on Carla
- Make rules and labels for Carla environment in dio
