from typing import Union

from weapon import weapon
from ability import ability

unarmed = weapon("unarmed", "fist", 0, 0, [], [])


class controllable:
    def __init__(self, name: str, max_health: int):
        self.is_alive = True

        self.name = name
        self.max_health = max_health  # 气血
        self.current_health = 0  # 假设初始生命值为0


class Player(controllable):

    def __init__(self, name: str, health: int):
        super().__init__(name, health)
        
        self.max_mana = 0  # 最大内力
        self.current_mana = 0  # 当前内力

        # 基本屬性
        self.strength = 1  # 力量
        self.vital = 1  # 体魄
        self.agility = 1  # 身法
        self.spirit = 1  # 内息
        self.perception = 1  # 气感
        self.appearance = 1  # 神采
        self.comprehension = 1  # 悟性

        # 戰鬥屬性
        self.internal_resistance = 0  # 内功防御
        self.external_resistance = 0  # 外功防御
        self.interal_accuracy = 0  # 内功命中
        self.external_accuracy = 0  # 外功命中
        self.internal_crit = 0  # 内功暴击
        self.external_crit = 0  # 外功暴击
        self.evation = 0  # 闪避

        # 武学
        self.guard = None  # 架招
        self.inner_practice = []  # 内功
        self.current_inner_practice = None  # 当前内功
        self.styles = []  # 武学招式

        # 装备
        self.equipped_weapon = unarmed  # 装备武器

        # 武器熟练度
        self.weapon_mastery = {
            "sword": 0,
            "dagger": 0,
            "staff": 0,
            "special": 0,
            "hidden": 0,
            "musical": 0,
            "fist": 0,
        }

        # 属性技能
        self.skills = {
            "internal": 0,  # 内功
            "gossip": 0,  # 八卦
            "power": 0,  # 实力
            "appraisal": 0,  # 鉴定
            "Wrestling": 0,  # 角力
            "escape": 0,  # 挣脱
            "throw": 0,  # 抛掷
            "grapple": 0,  # 擒抱
            "stealth": 0,  # 潜行
            "handwork": 0,  # 巧手
            "footwork": 0,  # 轻功
            "equestrianism": 0,  # 骑术
            "tenacity": 0,  # 韧性
            "apnea": 0,  # 闭气
            "endurance": 0,  # 忍耐
            "coagulation": 0,  # 凝血
            "medicine": 0,  # 医术
            "acupoint_breach": 0,  # 忍耐
            "concealment": 0,  # 敛息
            "qi_transfer": 0,  # 渡气
            "acupressure": 0,  # 点穴
            "tracking": 0,  # 追踪
            "search": 0,  # 探查
            "Insight": 0,  # 洞察
            "trading": 0,  # 交易
            "beguile": 0,  # 欺瞒
            "convince": 0,  # 说服
            "determination": 0,  # 定力
        }

    # 架招开启/破防 （None)
    def set_guard(self, guard: Union[ability, None]) -> None:
        self.guard = guard

    # Weapon related methods
    def equip_weapon(self, weapon) -> None:
        self.equipped_weapon = weapon
        return None



