from gym.envs.registration import register

register(
    id='gridworld_hw-v0',
    entry_point='gym_hw.envs:GridworldEnv',
)

register(
    id='cartpole_hw-v0',
    entry_point='gym_hw.envs:CartPoleEnv',
)
