from gym_avoid_game.envs.resource.scene import Scene


class TaskManager():
    """
    ミッション中のクラスを保持して管理、記録の更新を行う
    """

    def __init__(self, task):
        self.task = task()
        self.task_number = int(''.join([ch for ch in self.task.__class__.__name__[-2:] if ch.isdecimal()]))
        self.task_number = 1

    def update(self, a, x_axis_only=False):
        self.task.update(a, x_axis_only)

        if self.task.return_value["status"] == "exit":
            return Scene.QUIT

        return Scene.NO_SCENE_CHANGE

    def draw(self, screen):
        self.task.draw(screen)
