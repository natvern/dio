#!/bin/bash 

echo "Starting Training" 
cd "prologkb" 
alpha=$(python config.py)
cd "../rl-starter-files"
python -m scripts.train --env MiniGrid-ProbGrid-100x100-v0 --model alpha-$alpha-dio-test --algo ppo --frames 20
cd "../prologkb" 
python cumulative.py 
python failures.py
echo "Training Done"


