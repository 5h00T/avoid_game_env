from . import enemy


class Enemy1(enemy.Enemy):
    def __init__(self, x, y, width, height, hp, color):
        super().__init__(x, y, width, height, hp, color)
        self.shot_positions.append(enemy.ShotPosition(self.x, self.y))
        self.shot_functions.append(self.shot_positions[0].pattern4(15, 24, 0.5, 20))
        print("DD")

    def update(self):
        super().update()

    def draw(self, screen):
        super().draw(screen)
