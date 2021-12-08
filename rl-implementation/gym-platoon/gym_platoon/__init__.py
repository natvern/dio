from gym.envs.registration import register

register(
    id='platoon-v1',
    entry_point='gym_platoon.envs:PlatoonEnv',
)