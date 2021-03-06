from gym_avoid_game.envs.resource import player
from gym_avoid_game.envs.resource.scene import Scene
from gym_avoid_game.envs.resource import bullet_pool


class Task():

    def __init__(self):
        self.player = player.Player(100, 180, 15, 15, 3, 3)
        self.enemy_max_hp = self.enemy.hp
        self.return_value = {"status": Scene.NO_SCENE_CHANGE}
        self.is_clear = False
        self.count = 0
        self.bullet_pool = bullet_pool.EnemyBulletPool
        self.bullet_pool.all_reset_bullet()
        self.is_player_active = True

    def update(self, a, x_axis_only=False):
        if self.is_player_active:
            self.player.update(a, x_axis_only)
        if not self.is_clear and self.is_player_active:
            self.count += 1
            self.enemy.update()
            self.collision_detection()
        else:
            self.return_value["status"] = "exit"

    def draw(self, screen):
        if self.is_player_active:
            self.player.draw(screen)
        if not self.is_clear:
            self.enemy.draw(screen)
            for bit in self.enemy.bits:
                bit.shot_position.draw(screen)

    def enemy_playerbullet_detection(self):
        x1 = self.enemy.view_start_x
        y1 = self.enemy.view_start_y
        x2 = self.enemy.view_start_x + self.enemy.width
        y2 = self.enemy.view_start_y + self.enemy.height
        for player_bullet in self.player.bullets:
            x = player_bullet.x
            y = player_bullet.y
            r = player_bullet.collision_radius

            C1 = x > x1 and x < x2 and y > y1 - r and y < y2 + r
            C2 = x > x1 - r and x < x2 + r and y > y1 and y < y2
            C3 = (x1 - x) ** 2 + (y1 - y) ** 2 < r ** 2
            C4 = (x2 - x) ** 2 + (y1 - y) ** 2 < r ** 2
            C5 = (x2 - x) ** 2 + (y2 - y) ** 2 < r ** 2
            C6 = (x1 - x) ** 2 + (y2 - y) ** 2 < r ** 2

            if C1 or C2 or C3 or C4 or C5 or C6:
                self.enemy.hp -= 1
                if self.enemy.hp <= 0:
                    self.mission_clear()
                player_bullet.is_active = False

    def bit_playerbullet_detection(self):
        for bit in self.enemy.bits:
            x1 = bit.view_start_x
            y1 = bit.view_start_y
            x2 = bit.view_start_x + bit.width
            y2 = bit.view_start_y + bit.height
            for player_bullet in self.player.bullets:
                x = player_bullet.x
                y = player_bullet.y
                r = player_bullet.collision_radius

                C1 = x > x1 and x < x2 and y > y1 - r and y < y2 + r
                C2 = x > x1 - r and x < x2 + r and y > y1 and y < y2
                C3 = (x1 - x) ** 2 + (y1 - y) ** 2 < r ** 2
                C4 = (x2 - x) ** 2 + (y1 - y) ** 2 < r ** 2
                C5 = (x2 - x) ** 2 + (y2 - y) ** 2 < r ** 2
                C6 = (x1 - x) ** 2 + (y2 - y) ** 2 < r ** 2

                if (C1 or C2 or C3 or C4 or C5 or C6) and bit.is_active:
                    bit.hp -= 1

                    if bit.hp <= 0:
                        bit.is_active = False
                    player_bullet.is_active = False

    def player_enemybullet_detection(self):
        player_x = self.player.x
        player_y = self.player.y
        player_r = self.player.collision_radius
        for shot_position in self.enemy.shot_positions:
            for enemy_bullet in shot_position.bullets:
                x = enemy_bullet.x
                y = enemy_bullet.y
                r = enemy_bullet.collision_radius
                if (player_x - x) ** 2 + (player_y - y) ** 2 <= (player_r + r) ** 2:
                    enemy_bullet.is_active = False
                    return True
        return False

    def player_bitbullet_detection(self):
        player_x = self.player.x
        player_y = self.player.y
        player_r = self.player.collision_radius
        for bit in self.enemy.bits:
            for bit_bullet in bit.shot_position.bullets:
                x = bit_bullet.x
                y = bit_bullet.y
                r = bit_bullet.collision_radius
                if (player_x - x) ** 2 + (player_y - y) ** 2 <= (player_r + r) ** 2:
                    bit_bullet.is_active = False
                    return True
        return False

    def collision_detection(self):
        self.enemy_playerbullet_detection()
        self.bit_playerbullet_detection()
        if self.player_enemybullet_detection() or self.player_bitbullet_detection():
            self.bullet_pool.all_reset_bullet()
            self.is_player_active = False
            self.return_value["status"] = "exit"

    def mission_clear(self):
        self.is_clear = True
