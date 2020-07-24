from sum_tree import SumTree
import numpy as np

class PrioritisedMemory(object):

	def __init__(self, alpha, beta, beta_end, epsilon, num_steps, replay_size):

		self.alpha = alpha
		self.beta_start = beta
		self.beta_end = beta_end
		self.beta = beta 
		self.epsilon = epsilon
		self.num_steps = num_steps

		self.memory = SumTree(replay_size)
		self.replay_size = replay_size

	def proprotional_priority(self, td_error):

		return (np.abs(td_error) + self.epsilon)**self.alpha

	def add_memory(self, td_error, data):

		priority = self.proprotional_priority(td_error)

		self.memory.add_memory(data, priority)

		self.beta = np.min([1.0, self.beta + (self.beta_end-self.beta_start)/self.num_steps])

	def update_priority(self, index, td_error):

		new_priority = self.proprotional_priority(td_error)
		self.memory.update_priority(index, new_priority)

	def minibatch_sample(self, minibatch_size):

		samples = []
		priorities = []
		priority_indexes = []

		interval = self.memory.priority_total()/minibatch_size

		for i in range(minibatch_size):

			sample = np.random.uniform(i*interval, (i+1)*interval)

			priority_index, priority, data = self.memory.get(sample)

			samples.append(data)

			priorities.append(priority)

			priority_indexes.append(priority_index)

		sampling_probabilities = priorities/self.memory.priority_total()
		importance_weights = np.power(self.memory.replay_size * sampling_probabilities, -self.beta)
		importance_weights /= np.max(is_weight)

		return priority_indexes, samples, importance_weights 
