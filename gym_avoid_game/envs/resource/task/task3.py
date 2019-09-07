from gym_avoid_game.envs.resource.enemy import enemy3
from gym_avoid_game.envs.resource.task import task


class Task3(task.Task):

    def __init__(self):
        self.enemy = enemy3.Enemy3(100, 70, 20, 20, 240, (0, 0, 255))
        super().__init__()

    def update(self, a, x_axis_only=False):
        super().update(a, x_axis_only)

    def draw(self, screen):
        super().draw(screen)

    def collision_detection(self):
        super().collision_detection()
