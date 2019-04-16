import random

import math
from gym_avoid_game.envs.resource.enemy import enemy


class Enemy2(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        first_angle = random.randint(0, 30)
        for start_angle in range(first_angle, first_angle + 360, 30):
            self.set_shot_function(
                self.shot_positions[0].pattern19(start_angle, 3.3, 10, 0, math.inf, 1, 0, 40,
                                                 lambda count: -math.sin(self.count / 120) * 20,
                                                 lambda count: math.sin(self.count / 120) * 3.5)
            )

    def update(self):
        super().update()

    def draw(self, screen):
        super().draw(screen)
