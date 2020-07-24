class SumTree(object):

	def __init__(self, replay_size):

		self.replay_size = replay_size
		self.priority_size = 2*replay_size-1
		self.priority = [0.0 for _ in range(2*replay_size-1)]
		self.memory = [0 for _ in range(replay_size)]
		self.cursor = 0
		self.cur_size = 0

	def sum_up(self, index, delta):

		parent_ind = (index - 1) // 2

		self.priority[parent_ind] += delta

		if not self.is_root(parent_ind):
			self.sum_up(parent_ind, delta)

	def update_priority(self, index, new_priority):

		delta = new_priority - self.priority[index]

		self.priority[index] = new_priority

		self.sum_up(index, delta)

	def add_memory(self, data, priority):

		self.memory[self.cursor] = data

		priority_index = self.cursor + (self.replay_size - 1)
		self.priority[priority_index] = priority

		self.cursor = (self.cursor + 1) % self.replay_size

		if self.cur_size < self.replay_size:
			self.cur_size += 1 

	def is_root(self, index):

		if index == 0:
			return True

	def priority_total(self):

		return self.priority[0]

	def get_priority(self, index, sample):

		left_child = 2*index + 1
		right_child = 2*index + 2

		if left_child > self.priority_size:

			return index

		elif sample < self.priority[left_child]:

			return self.get_priority(left_child, sample)

		else:

			return self.get_priority(right_child, sample - self.priority[left_child])

	def get(self, sample):

		priority_index = self.get_priority(0, sample)

		memory_index = priority_index - self.replay_size + 1

		return priority_index, self.priority[priority_index], self.memory[memory_index]

