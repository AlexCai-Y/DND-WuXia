class Item():

	def __init__(self, name):
		self.name = name 
		
	
class Weapon(Item):

	def __init__(self, name, attack, parry, effect=None):
		super().__init__(name)
		self.attack = attack
		self.parry = parry
		self.effect = effect
		self.equipted = False


class Armour(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.equipted = False
