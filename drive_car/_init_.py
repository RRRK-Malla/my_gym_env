from gym.envs.registration import register

register(
    id='Drivezy-v0',
    entry_point='my_gym_env.envs:DriveEnv',
)
