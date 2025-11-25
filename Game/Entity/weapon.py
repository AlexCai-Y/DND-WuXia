from typing import int, List

class weapon():
    def __init__(self, name: str, type: str, attack_bonus: int, defense_bonus: int, attributes: List[str], effects: List[str]):
        self.name = name 
        self.type = type # 武器类型(刀...）
        self.attack_bonus = attack_bonus # 攻击加成
        self.defense_bonus = defense_bonus # 防御加成
        self.attributes = attributes # 属性加成
        self.effects = effects # 特殊效果
		

    def get_attack_bonus(self) -> int:
        return self.attack_bonus    
    
    def get_defense_bonus(self) -> int:
        return self.defense_bonus   
