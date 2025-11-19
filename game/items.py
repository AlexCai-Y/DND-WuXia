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


class Pants(Item):
	
	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False


class Helmet(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False
		

class Boots(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False


class Earring(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False


class Amulet(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False


class Ring(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
		self.equipted = False


class Medicine(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect


class	Food(Item):

	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect


class Drink(Item):	
	
	def __init__(self, name, effect=None):
		super().__init__(name)
		self.effect = effect
	
	