import random

import math

from gym_avoid_game.envs.resource.enemy import enemy


class Enemy3(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.set_shot_function(self.shot_positions[0].pattern3(3, 11, 2.3, 50))

    def update(self):
        super().update()

        if self.count > 130 and self.count % 90 == 0 and len(self.bits) < 5:
            bit = enemy.Bit(self.x, self.y, 10, 10, 0, 0, 15, (190, 100, 230), {
                "move_speed": random.uniform(0.02, 0.04),
                "direction": 1 if random.random() > 0.5 else -1})
            bit.set_move_function(bit.move_pattern1(bit.const_parameter["direction"], 1, 2, 3, math.pi / 2,
                                                    bit.const_parameter["move_speed"], 0, math.inf))
            shot_angle_direction = 1 if random.random() > 0.5 else -1
            bit.set_shot_function(bit.shot_position.pattern14(1, 90, 30, 0.9, 1.2, 60, 1, 0, 0, 10, 40, 20, math.inf,
                                                              lambda x: shot_angle_direction * x, 4, (120, 50, 45)))
            bit.set_shot_function(bit.shot_position.pattern14(1, 90, -30, 0.9, 1.2, 60, 1, 0, 0, 10, 40, 20, math.inf,
                                                              lambda x: shot_angle_direction * x, 4, (120, 50, 45)))
            self.bits.append(bit)

    def draw(self, screen):
        super().draw(screen)
