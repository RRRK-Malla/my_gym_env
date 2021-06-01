from gym.envs.registration import register

register(
    id='Drivezy-v0',
    entry_point='drive-car.envs:DriveEnv',
)
