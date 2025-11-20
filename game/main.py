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

battle.roll_initiatives()

battle.battle_start()

def frontend():

    while True:
        cmd = input("Enter a command: ")
        commands.put(cmd) 

threading.Thread(target=frontend, daemon=True).start()


while True:
    end_turn = False
    # The list of actions a player can do.
    available_action = battle.possible_actions()

    # Wait until the player press end_turn.
    while not end_turn:
        try:
            cmd = commands.get_nowait()

            if cmd == "end turn":
                end_turn = True
            else:
                battle.current_player.act(cmd)
                available_action = battle.possible_actions()

        except queue.Empty:
            pass

        time.sleep(0.1)
    
    battle.next_turn()



