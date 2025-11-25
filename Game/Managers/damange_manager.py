from backend.game_logic.Entities.controllable import Player as character
from backend.game_logic.Entities.ability import ability

damange_resistance = {
    "internal": "internal_resistance",
    "external": "external_resistance",
    "bleeding": "coagulation",
    "poison": "tenacity",
    "mental": None,
    "blood_loss": None,
    "fire": None,
}


def medigated_damage(
    defender: character,
    premid_damage: float,
    dmg_type: str,
) -> float:
    resistance_attr = damange_resistance[dmg_type]
    if resistance_attr is not None:
        resistance = getattr(defender, resistance_attr)
        mitigated_damage = premid_damage - resistance
    else:
        mitigated_damage = premid_damage  # No resistance applied

    return max(mitigated_damage, 0)  # Damage cannot be negative


def get_ability_damage(attacker: character, defender: character, ability_used: ability):
    damage = 0.0

    # 武學係數
    attributes = ability_used.get_attributes()
    factors = ability_used.get_factors()
    dmg_types = ability_used.get_dmg_typeS()

    # 内功係數加成
    ratio_additive = ability_used.inner_practice_additive(attacker.inner_practice)

    for i in range(len(attributes)):
        if attributes[i] is None:
            damange += medigated_damage(defender, factors[i], dmg_types[i])
        else:
            premed_dmg = getattr(attacker, attributes[i]) * (
                factors[i] + ratio_additive
            )
            damage += medigated_damage(defender, premed_dmg, dmg_types[i])

    # 武器及熟練度加成
    damange += (
        attacker.get_mastery_additive(ability_used.weapon)
        + attacker.get_weapon_additive()
    )

    return max(1,damange)

