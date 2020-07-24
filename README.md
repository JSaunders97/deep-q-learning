# Deep Q-Learning

In this project Deep Q-Learning was explored for playing Atari Breakout. In particular Deep Q-Learning (DQN) [(Mnih et al. 2015)], Double Deep Q-Learning (DDQN) [(Van Hasselt et al. 2016)], Duelling Deep Q-Learning [(Wang et al. 2015)] and Double Deep Q-Learning with Prioritised Replay Memory (DDQN with PRM) [(Schaul et al. 2016)] were implemented. The project formed the final coursework for our Reinforcement Learning course. Madge Kelly, Joe Rosenberg and Joe Molyneux-Saudners (myself) made equal contributions to the project. A detailed explaination of the implementation and analysis can be found in the report PDF.

## Results



Method | Max Training Score | Average Test score (100 episodes)
--- | --- | ---
Deep Q-Learning  | **354** | 76.66
Double Deep Q-Learning  | 279 | 72.93
Duelling Deep Q-Learning  | 306 | **78.91**
Double Deep Q-Learning with Prioritised Replay Memory  | 335 | 29.80


[(Mnih et al. 2015)]: https://www.nature.com/articles/nature14236
[(Van Hasselt et al. 2016)]: https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/viewPaper/12389
[(Schaul et al. 2016)]: https://arxiv.org/abs/1511.05952
[(Wang et al. 2015)]: https://arxiv.org/abs/1511.06581

