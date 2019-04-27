import numpy as np
from gym_avoid_game.envs.resource.scene import Scene
from gym_avoid_game.envs.resource.task import task1, task2
from gym_avoid_game.envs.resource import task_manager
from gym_avoid_game.envs.resource.config import WINDOW_HEIGHT, WINDOW_WIDTH
import gym
import gym.spaces
import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class v0AvoidGameTask1Env(gym.Env):
    def __init__(self):
        self.screen = None
        self.action_space = gym.spaces.Discrete(9)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(200, 200, 3), dtype=np.uint8)
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

        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8), reward, self.done, {}

    def render(self, mode='human'):
        pygame.display.update()

    def reset(self):
        self.done = False
        pygame.init()
        self.task_manager = task_manager.TaskManager(task1.Task1)
        try:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        except:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("avoid_game_env")

        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8)

    def close(self):
        pygame.quit()

    def seed(self, seed=None):
        pass


class v1AvoidGameTask1Env(gym.Env):
    def __init__(self):
        self.screen = None
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(60, 60, 3), dtype=np.uint8)
        self.task_manager = None
        self.done = None

    def step(self, a):
        pygame.event.get()

        reward = 1

        result = self.task_manager.update(a, True)
        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        if result == Scene.QUIT:
            self.done = True
            reward = 0

        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8), reward, self.done, {}

    def render(self, mode='human'):
        pygame.display.update()

    def reset(self):
        self.done = False
        pygame.init()
        self.task_manager = task_manager.TaskManager(task1.Task1)
        try:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        except:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("avoid_game_env")

        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8)

    def close(self):
        pygame.quit()

    def seed(self, seed=None):
        pass


class v0AvoidGameTask2Env(gym.Env):
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

        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8), reward, self.done, {}

    def render(self, mode='human'):
        pygame.display.update()

    def reset(self):
        self.done = False
        pygame.init()
        self.task_manager = task_manager.TaskManager(task2.Task2)
        try:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        except:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("avoid_game_env")

        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8)

    def close(self):
        pygame.quit()

    def seed(self, seed=None):
        pass


class v1AvoidGameTask2Env(gym.Env):
    def __init__(self):
        self.screen = None
        self.action_space = gym.spaces.Discrete(3)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(60, 60, 3), dtype=np.uint8)
        self.task_manager = None
        self.done = None

    def step(self, a):
        pygame.event.get()

        reward = 1

        result = self.task_manager.update(a, True)
        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        if result == Scene.QUIT:
            self.done = True
            reward = 0

        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8), reward, self.done, {}

    def render(self, mode='human'):
        pygame.display.update()

    def reset(self):
        self.done = False
        pygame.init()
        self.task_manager = task_manager.TaskManager(task2.Task2)
        try:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        except:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("avoid_game_env")

        self.screen.fill((255, 255, 255))
        self.task_manager.draw(self.screen)
        rgb_array = pygame.surfarray.array3d(self.screen)

        return np.asarray(rgb_array, dtype=np.uint8)

    def close(self):
        pygame.quit()

    def seed(self, seed=None):
        pass
