import gym
from gym import error, spaces, utils
import numpy as np
from gym_game.envs.drive_game import driveGame
from gym.utils import seeding

class DriveEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
        self.drivezy = driveGame()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)

    def reset(self):
        del self.drivezy
        self.drivezy = driveGame()
        show = self.drivezy.view()
        return show

    def step(self, action):
        self.drivezy.action(action)
        show = self.drivezy.view()
        reward = self.drivezy.eval()
        comp = self.pygame.finish()
        return show, reward, comp, {}

    def render(self, mode="human", close=False):
        self.drivezy.view()
