import game.abilities as abi

class Style():

	def __init__(self, name, level):
		self.name = name 
		self.level = level
		self.abilities = []
		
		
	def add_ability(self, ability: abi.Ability):
		self.abilities.append(ability)