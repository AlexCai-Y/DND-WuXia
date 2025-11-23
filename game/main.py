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
import asyncio
import queue
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

clients = set()

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
    clients.add(sid)
    await sio.emit("turnUpdate", {"turn": battle.turn}, to=sid)

@sio.event
async def disconnect(sid, environ=None):
    print("Client disconnected:", sid)
    clients.discard(sid)

@sio.event
async def endTurn(sid):
    print("Frontend requested END TURN from", sid)
    await commands.put("endTurn")

@sio.event
async def action(sid, data):
    print("Frontend action:", data)
    await commands.put(data)


async def game_loop():
    while True:
        end_turn = False
        available_actions = battle.possible_actions()

        while not end_turn:
            try:
                cmd = await asyncio.wait_for(commands.get(), timeout=0.1)

            except asyncio.TimeoutError:
                # no command this tick, run other periodic logic if needed
                await asyncio.sleep(0)   # yield control
                continue

            if isinstance(cmd, str) and cmd == "endTurn":
                end_turn = True
            else:
                try:
                    battle.current_player.act(cmd)
                except Exception as e:
                    print("Error processing cmd:", cmd, e)
                available_actions = battle.possible_actions()

        battle.next_turn()
        print("Next turn:", battle.turn, "connected clients:", clients)

        try:
            await sio.emit("turnUpdate", {"turn": battle.turn})
        except Exception as e:
            print("Emit error:", e)

commands = None

async def start_background_tasks(app):
    global commands
    commands = asyncio.Queue()
    sio.start_background_task(game_loop)

app.on_startup.append(start_background_tasks)

if __name__ == "__main__":
    web.run_app(app,  host="0.0.0.0", port=3001)