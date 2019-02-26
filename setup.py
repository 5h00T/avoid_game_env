from setuptools import setup, find_packages

setup(name="gym_avoid_game",
      version="0.0.1",
      packages=find_packages("avoid_game_env"),
      install_requires=["gym", "pygame"]
)