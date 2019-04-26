# avoid_game_env
OpenAI Gym 用の環境

# Description
敵(青い物体)から撃たれる弾をプレイヤー(黄色い物体)を動かして避けます。目標は弾をよけ続けることです。
## Observation: 
ゲーム画面のRGB画素値 numpy array shape(200, 200, 3) dtype=np.uint8

## Actions
Type: Discrete(9)
Num	Action
0	Push cart to the left
1	Push cart to the right
2
3
4
5
6
7
8

# Download and Installation
```
git clone https://github.com/5h00T/avoid_game_env/
cd avoid_game_env/
pip install -e .
```

# Usage
```
import time

import gym_avoid_game
import gym


env = gym.make("avoid_game_1-v1")
obs = env.reset()
done = False
while not done:
    env.render()
    # time.sleep(0.016)

    obs, reward, done, _ = env.step(env.action_space.sample())
```
