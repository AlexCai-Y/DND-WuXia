import operator
from controllable import Player as character
from typing import Union
from ability import ability

comparators = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "==": operator.eq,
}


def triggered(
    target_attr_value: int, trigger_comparative: str, trigger_threshold: int
) -> bool:
    cmp_func = comparators.get(trigger_comparative)
    if not cmp_func:
        raise ValueError(f"Invalid comparator: {trigger_comparative}")
    elif cmp_func(target_attr_value, trigger_threshold):
        return True
    return False


class effect:
    pass


class attr_additive_effect(effect):
    def __init__(
        self,
        trigger_attr: str,
        trigger_comparative: str,
        trigger_threshold: str,
        additive_value: int,
    ):
        self.trigger_condition = trigger_attr
        self.trigger_comparative = trigger_comparative
        self.trigger_threshold = trigger_threshold

        self.additive_value = additive_value

    def effect_additive(self, target: character) -> bool:
        target_attr_value = target.get_stat(self.trigger_attr)

        if triggered(
            target_attr_value, self.trigger_comparative, self.trigger_threshold
        ):
            return self.additive_value
        return 0


class battle_additive(effect):
    def __init__(
        self,
        trigger_attr: str,
        trigger_comparative: str,
        trigger_threshold: str,
        additive_value: int,
    ):
        self.trigger_condition = trigger_attr
        self.trigger_comparative = trigger_comparative
        self.trigger_threshold = trigger_threshold
        self.additive_value = additive_value

    def take_effect(self, target: character) -> int:
        target_attr_value = target.get_stat(self.trigger_attr)

        if triggered(
            target_attr_value, self.trigger_comparative, self.trigger_threshold
        ):
            return self.additive_value
        return 0


class ability_additive(effect):
    """技能加成效果

    例如：当武學伤害类型为内功（internal)时，增加10点伤害
    effect = ability_additive(
        trigger_attr="dmg_type",        触发属性
        trigger_comparative="==",       触发比较符
        trigger_threshold="internal",   触发阈值
        additive_attr="internal",       加成属性
        additive_value=10               加成数值
    effect.take_effect(内功武學) -> ["internal_damage", 10]
    effect.take_effect（外功武學) -> []
    
    usage ex:
    当武學動作为主要動作时，暴擊骰-1
    effect = ability_additive(
        trigger_attr="action_type",     武學動作
        trigger_comparative="==",       为
        trigger_threshold="main",       主要動作时，
        additive_attr="crit",           暴擊骰
        additive_value= -1              -1
    """

    def __init__(
        self,
        trigger_attr: str,
        trigger_comparative: str,
        trigger_threshold: Union[str, int],
        additive_attr: str,
        additive_value: int,
    ):
        self.trigger_attr = trigger_attr
        self.trigger_comparative = trigger_comparative
        self.trigger_threshold = trigger_threshold
        self.additive_attr = additive_attr
        self.additive_value = additive_value

    def take_effect(self, ability) -> int:
        target_attr_value = ability.get_stat(self.trigger_attr)

        if triggered(
            target_attr_value, self.trigger_comparative, self.trigger_threshold
        ):
            return [self.additive_attr, self.additive_value]
        return []
