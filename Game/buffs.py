import controllable as ctrl

class Buff():

	def __init__(self, name, time_left, apply_index):
		# apply_index: the index of play turn when the buff is applied.
		self.name = name
		self.time_left = time_left
		self.apply_index = apply_index


class DOT(Buff):
	# Buffs that periodically apply damage to a controllable.
	
	def __init__(self, name, time_left, apply_index, target, severity, trigger_time):
		# target = hp, mana, rage, etc.
		# trigger_time = start of the round (0) / end of the round (1)
		super().__init__(name, time_left, apply_index)
		self.target = target
		self.severity = severity
		self.trigger_time = trigger_time


	def trigger(self, controllable: ctrl.Controllable):
		# Apply the effect to the controllable
		if self.target in controllable.__dict__:
			current_value = getattr(controllable, self.target)

			setattr(controllable, self.target, current_value + self.severity)

class Effect(Buff):
	# Buffs that provide ongoing effects to a controllable.

	def __init__(self, name, time_left, apply_index, target, severity):
		super().__init__(name, time_left, apply_index)
		# target = strength, vital, etc.
		self.target = target
		self.severity = severity
		

class Status(Effect):
	# Buffs that does not have explicit effects on target.

	def __init__(self, name, time_left, apply_index):
		super().__init__(name, time_left, apply_index)
	

	
	
		
