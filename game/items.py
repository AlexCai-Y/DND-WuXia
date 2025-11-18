class Item():

	def __init__(self, name):
		self.name = name 
		
	
	
class Weapon(Item):

	def __init__(self, name, attack, parry, effect):
		super().__init__(name)
		self.attack = attack
		self.parry = parry
		self.effect = effect
		self.equipted = False
		self.clas = "WEAPON"

class Armour(Item):

	def __init__(self, name, effect):
		super().__init__(name)
		self.equipted = False
		self.clas = "ARMOUR"

class Pants(Item):



class Helmet(Item):



class Boots(Item):



class Earring(Item):



class Amulet(Item):



class Ring(Item):




class Medicine(Item):




class	Food(Item):




class Drink(Item):	
	
	
	
	