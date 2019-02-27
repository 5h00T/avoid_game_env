import numpy as np
from .resource.scene import Scene
from .resource.task import task1
from .resource import task_manager
import gym
import gym.spaces
import os
import pygame

# os.environ["SDL_VIDEODRIVER"] = "dummy"


class ShootingEnv(gym.Env):
    def __init__(self):
        self.screen = None
        self.action_space = gym.spaces.Discrete(9)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(60, 60, 3), dtype=np.uint8)
        self.task_manager = None
        self.done = None

    def step(self, a):
        pygame.event.get()

        reward = 1

        result = self.task_manager.update(a)
        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        if result == Scene.QUIT:
            self.done = True
            reward = 0

        pixelarray = pygame.PixelArray(self.screen)
        rgb_pixels = [[[(j >> 16) & 255, (j >> 8) & 255, j & 255] for j in i] for i in pixelarray]
        # time.sleep(1)

        return np.asarray(rgb_pixels, dtype=np.uint8), reward, self.done, {}

    def render(self, mode='human'):
        pygame.display.update()

    def reset(self):
        self.done = False
        pygame.init()
        self.task_manager = task_manager.TaskManager(task1.Task1)
        try:
            self.screen = pygame.display.set_mode((60, 60))
        except:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.screen = pygame.display.set_mode((60, 60), flags=0, depth=32)
        pygame.display.set_caption("shooting_env")

        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        pixelarray = pygame.PixelArray(self.screen)
        rgb_pixels = [[[(j >> 16) & 255, (j >> 8) & 255, j & 255] for j in i] for i in pixelarray]

        return np.asarray(rgb_pixels, dtype=np.uint8)

    def close(self):
        pygame.quit()

    def seed(self, seed=None):
        pass
