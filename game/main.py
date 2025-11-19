import game.battle as battle
import game.items as item
import game.core as core
import game.abilities as abi
import game.style as style
import game.buffs as buff
import game.controllable as ctrl
import pickle

try:
    characters = pickle.load(open("save/characters.pkl", "rb"))
except FileNotFoundError:
    characters = []

battle = battle.Battle()




