from . import bullet_pool
import math
import pygame

class Player():
    x = -10
    y = -10

    def __init__(self, x, y, width, height, collision_radius, speed):
        Player.x = x
        Player.y = y
        self.width = width
        self.height = height
        self.view_start_x = self.x - self.width / 2  # 長方形の始点
        self.view_start_y = self.y - self.height / 2  # 長方形の始点
        self.collision_radius = collision_radius  # あたり判定
        self.speed = speed
        self.slow_speed = 0.5  # 低速移動したときのスピード
        self.count = 0
        self.bullet_pool = bullet_pool.PlayerBulletPool(30)
        self.bullets = []

    @classmethod
    def getPosition(cls):
        return cls.x, cls.y

    def update(self, a):
        self.count += 1

        for b in self.bullets:
            b.update()
            if not b.is_active:
                self.bullets.remove(b)

        self.move(a)

    def draw(self, screen):
        pygame.draw.rect(screen, (249, 155, 69), pygame.Rect(self.view_start_x, self.view_start_y, self.width, self.height))
        # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 1, 1))
        for b in self.bullets:
            b.draw()

    def move(self, a):
        is_slanting = False
        slanting_speed = 0.71
        is_slow = False

        up = False
        down = False
        right = False
        left = False
        """
        0:○
        1:↑
        2:↗
        3:→
        4:↘
        5:↓
        6:↙
        7:←
        8:↖
        """
        if a is 0:
            pass
        elif a is 1:
            up = True
        elif a is 2:
            up = True
            right = True
        elif a is 3:
            right = True
        elif a is 4:
            down = True
            right = True
        elif a is 5:
            down = True
        elif a is 6:
            down = True
            left = True
        elif a is 7:
            left = True
        elif a is 8:
            up = True
            left = True

        # 上または下と左または右が押されたとき移動量を0.71倍する
        if (right or left) and \
            (up or down):
            is_slanting = True

        if right:
            Player.x += self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)
        elif left:
            Player.x -= self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)

        if up:
            Player.y -= self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)
        elif down:
            Player.y += self.speed * (slanting_speed if is_slanting else 1) * (self.slow_speed if is_slow else 1)

        self.view_start_x = Player.x - self.width / 2
        self.view_start_y = Player.y - self.height / 2

        # 画面外に行かないように移動制限
        width = height = 60
        if self.view_start_x < 0:
            Player.x = self.width / 2
        elif self.view_start_x + self.width >= width:
            Player.x = width - self.width / 2

        if self.view_start_y < 0:
            Player.y = self.height / 2
        elif self.view_start_y + self.height >= height:
            Player.y = height - self.height / 2

        self.view_start_x = Player.x - self.width / 2
        self.view_start_y = Player.y - self.height / 2

    def shot(self, way, start_angle, delta_angle, speed, radius, color):
        angle = start_angle
        _bullets = []
        for i in range(way):
            b = self.bullet_pool.get_bullet(radius, Player.x, Player.y, math.cos(math.radians(angle)),
                                            math.sin(math.radians(angle)), speed, color)
            angle += delta_angle
            if b:
                _bullets.append(b)
            else:
                for _b in _bullets:
                    _b.is_active = False
                break
        else:
            self.bullets.extend(_bullets)
