import random

class Battle():

	def __init__(self):
	
		self.rounds = 0
		self.turn = 0
		self.participants = []
		self.initiatives = []
		self.current_player = None 
		self.status = "Not Started"
	
	
	def add_participant(self, player):
		if self.status == "Not Started":
			self.participants.append(player)
		elif self.status == "Paused":
			self.participants.append(player)
			self.roll_initiatives(player)
		else:
			print("战斗已经开始，无法加入新成员。")

		
	def roll_initiatives(self, new_member = None):
		if self.status == "Not Started":
			initiatives = {}
			for participant in self.participants:
					if participant not in initiatives:
						rolled_initiative = random.randint(0, 20)
						initiatives[participant] = rolled_initiative + participant.initiative
			for key in initiatives:
				self.initiative.append((key, initiatives[key]))
				
			self.initiatives.sort(key=lambda x: x[1], reverse=True)
			for initiative in self.initiatives:
				print("{0}先攻为{1}。".format(initiative[0].name, initiative[1]))
		
		elif self.status == "Resumed":
			new_initiative = random.randint(0, 20) + new_member.initiative
			self.initiatives.append((new_member, new_initiative))
			self.initiatives.sort(key=lambda x: x[1], reverse=True)
				
	
	def battle_start(self):
		self.status = "Started"
		self.rounds = 1
		self.roll_initiatives()
		self.turn = 0
		self.current_player = self.initiatives[self.turn][0]

	
	def battle_pause(self):
		self.status = "Paused"
		
	
	def battle_resume(self):
		self.status = "Resumed"
		for initiative in self.initiatives:
			print("{0}先攻为{1}。".format(initiative[0].name, initiative[1]))


	def next_turn(self):
		# Move to the next player in initiative order
		# Check if the previous player has DOT buffs to trigger at end of round
		for buff in self.current_player.temp_buffs:
			if type(buff).__name__ == 'DOT' and buff.trigger_time == 1:  # end of round
				buff.trigger(self.current_player)
		
		self.turn += 1
		if self.turn >= len(self.initiatives):
			self.rounds += 1
			self.turn = 0
		self.current_player = self.initiatives[self.turn][0]
		# Check if the current player has DOT buffs to trigger at start of round
		for buff in self.current_player.temp_buffs:
			if type(buff).__name__ == 'DOT' and buff.trigger_time == 0:  # start of round
				buff.trigger(self.current_player)
		
