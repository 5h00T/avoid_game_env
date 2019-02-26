from ..enemy import enemy1
from . import task


class Task1(task.Task):

    def __init__(self):
        self.enemy = enemy1.Enemy1(30, 10, 12, 12, 240, 8)
        super().__init__()

    def update(self, a):
        super().update(a)

    def draw(self, screen):
        super().draw(screen)

    def collision_detection(self):
        super().collision_detection()
