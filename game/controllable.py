import random
import game.items as item

EQUIPMENTS = item.EQUIPMENTS

class Controllable():
	
	def __init__(self, name: str):
		self.name = name 
		
		self.talent = 0
		self.skill = 0
		self.knowledge = 0

		self.strength = 1
		self.vital = 1
		self.movement = 1 
		self.spirit = 1
		self.perception = 1
		self.appearance = 1
		
		self.counter = 0
		self.break_ability = 0
		self.evade = 0
		self.parry = 0
		self.max_life = 0
		self.life = 0
		self.max_mana = 0
		self.mana = 0
		
		self.def_out = 0
		self.def_in = 0
		self.crit_out = 20
		self.crit_in = 20
		self.hit_out = 0
		self.hit_in = 0
		
		self.initiative = 0
		self.rage = 0
		
		self.action = True
		self.sec_action = True
		self.re_action = True
		self.simple_action = True
		
		self.inventory = []
		self.equipted_item = {}
		
		for equipment in EQUIPMENTS:
			self.equipted_item[equipment] = None
			
		self.abilities = []
		self.core = []
		self.perm_buffs = []
		self.temp_buffs = []
		self.speed = 0
		
		self.status = "Alive"
	
	
	def compute_attributes(self):
		self.counter = self.skill
		self.max_life = self.vital * 4 + self.strength
		self.max_mana = self.spirit
		self.speed = 5
		self.evade = 10 + self.movement//4
		self.initiative = self.movement//10
		self.def_out = self.vital//5
		self.def_in = self.spirit//3
		self.crit_out -= self.strength//20
		self.crit_in -= self.perception//20
		self.hit_out += self.movement//2
		self.hit_in += self.perception//2
	
	
	def parrying(self, break_ab):
		rolled_counter = random.randint(0, 20)
		if self.counter + rolled_counter >= break_ab:
			print("看破{0} vs. 虚招{1}: 看破成功。".format(self.counter + rolled_counter, break_ab))
			return True
			
		else:
			self.status = "Alive"
			print("看破{0} vs. 虚招{1}: 架招被破。".format(self.counter + rolled_counter, break_ab))
			return False
		
	def equip(self, item):
		self.equipted_item[item.clas] = item
		self.compute_attributes()
	
	
	def unequip(self, clas):
		self.equipted_item[clas] = None
		self.compute_attributes()

	
	def add_buff(self, buff):
		self.temp_buffs.append(buff)
			
	
	def remove_buff(self, buff):
		if buff in self.temp_buffs:
			self.temp_buffs.remove(buff)
		
		
class Human(Controllable):
		
	def __init__(self, name):
		super().__init__(name)
		
		
	def attack(self, ability, target):
		if ability.dmg_type == "IN":
			hit_score = self.hit_in + random.randint(0, 20)
		elif ability.dmg_type == "OUT":
			hit_score = self.hit_out + random.randint(0, 20)
		else:
			hit_score = max(self.hit_in, self.hit_out) + random.randint(0, 20)
		
		if target.evade >= hit_score:
			print("闪避{0} vs. 命中{1}: {2}闪避成功。".format(target.evade, hit_score, target.name))
		else:
			print("闪避{0} vs. 命中{1}: {2}被命中。".format(target.evade, hit_score, target.name))
			if ability.type == "Real" or ability.type == "Ult" or ability.type == "Basic":
				return damage
			elif ability.type == "Fake":
				result = target.parry(self.break_ab + random.randint(0, 20))
				if result:
					target.counter_attack()
				else:
					return damage
	
	
	def defend(self, damage):
		hp_reduction = 0
		print("造成{0}点伤害。".format(damage))
		if self.life >= hp_reduction:
			self.life -= hp_reduction
		else:
			self.life = 0
			self.mana -= (hp_reduction - self.life)//5
			print("{0}倒地，请投伤残鉴定。".format(self.name))
			inj_result = self.injury_check()
			print("伤残鉴定结果：{0}.".format(inj_result))
			if self.mana <= 0:
				print("{0}内力归零，请投死亡鉴定。".format(self.name))
				death_result = self.death_check()
				print("死亡鉴定结果：{0}".format(death_result))

	
	def guard_up(self, guard):
		self.status = "Guarded"
				
	
	def injury_check(self):
		result = random.randint(0, 100)
		return result
			
		
	def death_check(self):
		result = random.randint(0, 20)
		return result
			
	
class Animal(Controllable):
		
	def __init__(self, name, protection):
		super().__init__(name)
		self.protection = protection
		
		
	def attack(self, ability, target):
		return hit_score, damage
	
	
	def defend(self, hit_score, damage):
		if self.evade >= hit_score:
			print("闪避{0} vs. 命中{1}: 闪避成功。".format(self.evade, hit_score))
		else:
			print("闪避{0} vs. 命中{1}: 闪避失败。".format(self.evade, hit_score))
			if damage > self.protection:
				print("造成1点伤害。")
				if self.life >= 2:
					self.life -= 1
				else:
					self.life = 0
					self.status = "Dead"
					print("{0}永远的离开了。".format(self.name))
			else:
				print("未能破防。")
			
		
		