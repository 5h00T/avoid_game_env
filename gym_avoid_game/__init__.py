from gym.envs.registration import register

register(
    id='avoid_game_t1-v0',
    entry_point='gym_avoid_game.envs:v0AvoidGameTask1Env'
)

register(
    id='avoid_game_t1-v1',
    entry_point='gym_avoid_game.envs:v1AvoidGameTask1Env'
)

register(
    id='avoid_game_t2-v0',
    entry_point='gym_avoid_game.envs:v0AvoidGameTask2Env'
)

register(
    id='avoid_game_t2-v1',
    entry_point='gym_avoid_game.envs:v1AvoidGameTask2Env'
)

register(
    id='avoid_game_t3-v0',
    entry_point='gym_avoid_game.envs:v0AvoidGameTask3Env'
)

register(
    id='avoid_game_t3-v1',
    entry_point='gym_avoid_game.envs:v1AvoidGameTask3Env'
)
