# avoid_game_env
Learning Environment for OpenAI Gym

# Description
Move the player (yellow object) to avoid the bullet from the enemy (blue object). The goal is to keep the bullets avoid.
v0 moves in the vicinity of 8. v1 only moves horizontally.

## Observation: 
numpy array  
    shape(200, 200, 3) dtype=np.uint8
    Min 0  
    Max 255

## Actions
### v0
Type: Discrete(9) 

| Num | Action |
----|----
| 0 | Player don't move |
| 1 | Player moves to the up |
| 2 | Player moves to the up right |
| 3 | Player moves to the right |
| 4 | Player moves to the down right |
| 5 | Player moves to the down |
| 6 | Player moves to the down left |
| 7 | Player moves to the left |
| 8 | Player moves to the up left |

### v1
Type: Discrete(3)

| Num | Action |
----|----
| 0 | Player don't move |
| 1 | Player moves to the left |
| 2 | Player moves to the right |

## Reward
Reward 1 per step survival

## Episode Termination
The episode ends when the player is hit

# Download and Installation
```
git clone https://github.com/5h00T/avoid_game_env/
cd avoid_game_env/
pip install -e .
```

# Usage
```Python
import time

import gym_avoid_game
import gym


env = gym.make("avoid_game_1-v1")
obs = env.reset()
done = False
while not done:
    env.render()
    # time.sleep(0.016)
    
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
```
