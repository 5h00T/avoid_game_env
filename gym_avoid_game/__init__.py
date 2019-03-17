from gym.envs.registration import register

register(
    id='avoid_game-v0',
    entry_point='gym_avoid_game.envs:ShootingEnv'
)

register(
    id='avoid_game-v1',
    entry_point='gym_avoid_game.envs:SimpleShootingEnv'
)