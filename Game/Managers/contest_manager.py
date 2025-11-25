from backend.game_logic.Entities.controllable import controllable as character
from backend.game_logic.Entities.ability import ability


def if_hit(
    attacker: character,
    defender: character,
    rolled_accuracy: int,
    ability_used: ability,
) -> bool:
    accuracy = rolled_accuracy + attacker.get_accuracy(ability_used.get_dmg_type())
    agility = defender.get_attr("evation")

    if accuracy >= agility:
        print("命中率{0} vs. 命中{1}: 命中成功。".format(accuracy, agility))
        return True
    else:
        print("命中率{0} vs. 命中{1}: 命中失败。".format(accuracy, agility))
        return False


def break_through(
    attacker: character,
    defender: character,
    ability_used: ability,
    rolled_feint: int,
    rolled_see_through: int,
) -> bool:

    # 虚招值 = D20+[武器技能等级+招式层数*虚招系数]#
    feint_value = (
        rolled_feint
        + attacker.get_weapon_mastery(ability_used.weapon)
        + ability_used.get_feint_additive()
    )

    # 看破值 = D20+悟性#
    see_through_value = rolled_see_through + defender.get_comprehension()

    if feint_value >= see_through_value:
        print("看破{0} vs. 虚招{1}: 看破成功。".format(feint_value, see_through_value))
        return True
    else:
        defender.set_stance(None)
        print("看破{0} vs. 虚招{1}: 架招被破。".format(feint_value, see_through_value))
        return False


def attribute_contest(
    attacker: character,
    defender: character,
    rolled_attribute_value: int,
    attack_attribute: str,
    defend_attribute: str,
) -> bool:

    attack_attribute_value = (
        getattr(attacker, attack_attribute) + rolled_attribute_value
    )
    defend_attribute_value = getattr(defender, defend_attribute)

    if attack_attribute_value >= defend_attribute_value:
        print(
            "{0}{1} vs. {2}{3}: 属性对抗成功。".format(
                attack_attribute,
                attack_attribute_value,
                defend_attribute,
                defend_attribute_value,
            )
        )
        return True
    else:
        print(
            "{0}{1} vs. {2}{3}: 属性对抗失败。".format(
                attack_attribute,
                attack_attribute_value,
                defend_attribute,
                defend_attribute_value,
            )
        )
        return False
