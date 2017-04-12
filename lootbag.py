import sys
import uuid

class LootBag():

	def write_child_to_file(self, child_name, action):
		with open('children', action) as children:
			child_id = uuid.uuid4()
			children.write("{},{}\n".format(child_id, child_name))

		return child_id

	def write_toy_to_file(self, toy_name, child_id, action):
		with open('toylist', action) as toys:
			toy_id = uuid.uuid4()
			toys.write("{},{},{}\n".format(toy_id, toy_name, child_id))

	def add_to_bag(self, toy, child_name):
		'''Add a toy and assign it to a child. Both the toy and
		the child will be written to disk in the 'toylist' or 'children'
		file, respectively

		Attributes:
			toy (string)
			child_name (string)
		'''

		# Determine whether child already exists
		try:
			with open('children', 'r') as children:
				all_children = children.readlines()

				for child in all_children:
					current_child_id, current_child_name = child.split(",")
					if current_child_name == child_name:
						self.write_toy_to_file(toy, current_child_id, 'a')
						return

				new_child_id = self.write_child_to_file(child_name, 'a')
				self.write_toy_to_file(toy, new_child_id, 'a')

		except FileNotFoundError:
			new_child_id = self.write_child_to_file(child_name, 'w')
			self.write_toy_to_file(toy, new_child_id, 'a')

	def list_toys_for_child(self, child_name):
		'''Returns a list of toys for a specific child

		Attributes:
			child_name (string)
		'''
		child_id_on_toylist = list()
		toy_list_for_child = list()
		with open('children', 'r') as children:
			all_children = children.readlines()
    	
			for child in all_children:
				current_child_id,current_child_name = child.split(",")
				if child_name == current_child_name.replace('\n',''):
					child_id_on_toylist = current_child_id
    	
		with open('toylist', 'r') as toys:
			all_toys = toys.readlines()
			for toy in all_toys:
				toy_id, toy_name, child_id = toy.split(",")
				if child_id_on_toylist == child_id.replace('\n',''):
					toy_list_for_child.append(toy_name)
		return toy_list_for_child

	def remove_toy_from_child(self, toy, child_name):

		'''Removes a toy from the toy list

		Attributes:
			toy (string)
			child_name (string)
		'''

		child_id_on_toylist = list()
		revised_toy_list = list()
		with open('children', 'r') as children:
			all_children = children.readlines()
			for child in all_children:
				current_child_id,current_child_name = child.split(",")
				if child_name == current_child_name.replace('\n',''):
					child_id_on_toylist = current_child_id

		with open('toylist', 'r') as toys:
			all_toys = toys.readlines()
       
		with open('toylist', 'w') as toys:
			for toy_line in all_toys:
				toy_id, toy_name, child_id = toy_line.split(",")
				if child_id_on_toylist != child_id.replace('\n',''):
					if toy != toy_name.replace('\n',''):
						toys.write(toy_line)

	def get_single_child(self, child_name):
		return {
			'delivered': False
		}

	def deliver_toys_to_child(self, child_name):
		return {
			'delivered': True
		}

	def get_kids(self):
		return ['Vincent']

# if __name__ == "__main__":
#     if sys.argv[1] == "add":
#         bag = LootBag()
#         bag.add_to_bag(sys.argv[2], sys.argv[3])









