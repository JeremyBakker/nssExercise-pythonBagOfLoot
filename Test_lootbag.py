import unittest
from lootbag import *

class TestLootbag(unittest.TestCase):

	@classmethod # tells unit tests to avoid testing the following def
	def setUpClass(self):
		self.bag = LootBag()

	def test_add_toy_to_bag(self):
		self.bag.add_to_bag('Ball', 'Vincent')
		vincents_toys = self.bag.list_toys_for_child('Vincent')

		self.assertIsInstance(vincents_toys, list)
		self.assertIn('Ball', vincents_toys)

	def test_remove_toy_of_child(self):
		toy = 'Slinky'
		self.bag.add_to_bag(toy, 'Vincent')

		self.assertIn('Vincent', self.bag.get_kids())

		self.bag.remove_toy_from_child(toy, 'Vincent')
		vincents_toys = self.bag.list_toys_for_child('Vincent')

		self.assertNotIn(toy, vincents_toys)

	def test_list_of_good_kids(self):
		toy = 'Silly Putty'
		self.bag.add_to_bag(toy, 'Vincent')
		good_kids = self.bag.get_kids()

		self.assertIsInstance(good_kids, list)
		self.assertIn('Vincent', good_kids)

	def test_toys_in_bag_for_specific_child(self):
		toy = 'Slime'
		self.bag.add_to_bag(toy, 'Vincent')
		vincents_toys = self.bag.list_toys_for_child('Vincent')

		self.assertIsInstance(vincents_toys, list)
		self.assertIn('Slime', vincents_toys)

	def test_child_toys_are_delivered(self):
		toy = 'Pony'
		self.bag.add_to_bag(toy, 'Vincent')
		vincent = self.bag.get_single_child('Vincent')
		
		self.assertIsintance(vincent, dict)
		self.asserFalse(vincent['delivered'])

		self.bag.deliver_toys_to_child('Vincent')
		self.asserTrue(vincent['delivered'])

if __name__ == '__main__':
    unittest.main()