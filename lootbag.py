class LootBag():
	
	def add_to_bag(self, toy, child):
		with open('{}.log'.format(child), 'a') as toy_file:
			toy_file.write('{}\n'.format(toy))

	def list_toys_for_child(self, child):
		with open('{}.log'.format(child), 'r') as toy_file:
			toy_list = []
			for line in toy_file:
				toy_list.append(line.replace('\n', ''))
			return toy_list

	def remove_toy_from_child(self, toy, child):
		with open('{}.log'.format(child), 'r') as toy_file:
			toy_list = []
			for line in toy_file:
				toy_list.append(line.replace('\n', ''))
			toy_list.remove(toy)
		with open('{}.log'.format(child), 'w') as toy_file:
			toy.file.write(toy_list)
			return(toy_list)

	def get_kids(self):
		with open('good_kids.log', 'r') as kids:
			
