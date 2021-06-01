import gym
from gym import error, spaces, utils
import numpy as np
from gym_game.envs.drive_game import driveGame
from gym.utils import seeding

class DriveEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
        self.pygame = driveGame()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0, 0]), np.array([10, 10, 10, 10, 10]), dtype=np.int)

    def reset(self):
        del self.pygame
        self.pygame = driveGame()
        show = self.pygame.view()
        return show

    def step(self, action):
        self.pygame.action(action)
        show = self.pygame.view()
        reward = self.pygame.eval()
        comp = self.pygame.finish()
        return show, reward, comp, {}

    def render(self, mode="human", close=False):
        self.pygame.view()
