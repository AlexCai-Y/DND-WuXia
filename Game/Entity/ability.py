from typing import int, List, Union


class ability:

    def __init__(
        self,
        name: str,
        level: int,
        mastery: int,
        upgraded_damange: int,
        inner_attribute: str,
        attributes: List[Union[str, None]],
        factors: List[float],
        dmg_types: List[str],
        weapon: str,
        effect: str,
        action: str,
        mana_cost: int,
        rage_cost: int,
    ):
        self.name = name  # 技能名称
        self.level = level  # 技能級別 (人地天，2-4)
        self.mastery = mastery  # 技能熟练度 1-4
        self.upgraded_damange = upgraded_damange  # 升级伤害

        self.inner_attribute = inner_attribute  # 阴阳属性 (yin, soft, yang, hard, neutral)

        self.attributes = attributes  # 加成属性(力量...)
        self.factors = factors  # 加成係數
        self.dmg_types = dmg_types  # 伤害类型 (internal, external)

        self.weapon = weapon  # 武器
        self.effect = effect  # 技能效果()
        self.action_type = action  # 动作类型
        self.mana_cost = mana_cost  # 内力消耗
        self.rage_cost = rage_cost  # 怒气消耗

    def get_attributes(self) -> List[Union[str, None]]:
        return self.attributes

    def get_factors(self) -> List[float]:
        return self.factors

    def get_dmg_typeS(self) -> List[str]:
        return self.dmg_types

    def get_feint_additive(self) -> int:
    
        return self.mastery * self.level

    def inner_practice_additive(self, inner_practice) -> float:
        if self.inner_attribute == inner_practice:
            return 0.2
        elif self.inner_attribute == "neutral" or inner_practice == "neutral":
            return 0.1
        else:
            return 0.0
