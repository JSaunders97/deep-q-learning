# Deep Q-Learning

In this project Deep Q-Learning was explored for playing Atari Breakout. In particular Deep Q-Learning (DQN) [(Mnih et al. 2015)], Double Deep Q-Learning (DDQN) [(Van Hasselt et al. 2016)], Duelling Deep Q-Learning [(Wang et al. 2015)] and Double Deep Q-Learning with Prioritised Replay Memory (DDQN with PRM) [(Schaul et al. 2016)] were implemented. The project formed the final coursework for a Reinforcement Learning course. Madge Kelly, Joe Rosenberg and Joe Molyneux-Saunders (myself) made equal contributions to the project. A detailed explaination of the implementations and discussion of the results can be found in the [report PDF].

Double Deep Q-Learning Agent Playing Breakout.

![alt text][play]

## Results

Learning curves for each of the 4 deep reinforcement learning methods implemented showing the moving average reward (100 episodes) per training epoch (100 episodes).

![alt text][results]

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
[results]: https://github.com/JSaunders97/deep-q-learning/blob/master/results.png "Learning curves"
[play]: https://github.com/JSaunders97/deep-q-learning/blob/master/ddqn_5000_episodes.gif
[report PDF]: https://github.com/JSaunders97/deep-q-learning/blob/master/report.pdf

