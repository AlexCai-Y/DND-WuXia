from typing import *

class Core():
	
	def __init__(self, name: str, level: str, mastery: int, attr: List[List[int]], effect: List[List[str]]):
		self.name = name 
		self.level = level
		self.attr = attr 
		self.effect = effect
		self.mastery = 0
		
		