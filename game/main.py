import battle as battle
import items as item
import core as core
import abilities as abi
import style as style
import buffs as buff
import controllable as ctrl
import pickle
import socketio
from aiohttp import web
import queue
import threading
import time


# try:
#     characters = pickle.load(open("save/characters.pkl", "rb"))
# except FileNotFoundError:
#     characters = []

battle = battle.Battle()

player = ctrl.Human("Player")
enemy1 = ctrl.Human("Enemy1")
enemy2 = ctrl.Human("Enemy2")

battle.add_participant(player)
battle.add_participant(enemy1)
battle.add_participant(enemy2)

battle.roll_initiatives()

battle.battle_start()

commands = queue.Queue()

sio = socketio.AsyncServer(
    async_mode="aiohttp",
    cors_allowed_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ]
)
app = web.Application()
sio.attach(app)

print("ACCEPTED ORIGINS:", sio.eio.cors_allowed_origins)

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid, "Origin:", environ.get("HTTP_ORIGIN"))

@sio.event
async def endTurn(sid):
    print("Frontend requested END TURN from", sid)
    commands.put("endTurn")

@sio.event
async def action(sid, data):
    print("Frontend action:", data)
    commands.put(data)


def game_loop():
    while True:
        end_turn = False
        available_actions = battle.possible_actions()

        while not end_turn:
            try:
                cmd = commands.get_nowait()

                if cmd == "endTurn":
                    end_turn = True
                else:
                    battle.current_player.act(cmd)
                    available_actions = battle.possible_actions()

            except queue.Empty:
                pass

            time.sleep(0.1)

        battle.next_turn()

threading.Thread(target=game_loop, daemon=True).start()


if __name__ == "__main__":
    web.run_app(app, port=3001)