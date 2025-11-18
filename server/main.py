from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles


app = FastAPI()


current_attacker: str | None = None
current_defender: str | None = None


app.mount("/", StaticFiles(directory="static", html=True), name="static")


class NamePayload(BaseModel):
    name: str


@app.post("/set_attacker")
async def set_attacker(payload: NamePayload):
    global current_attacker
    current_attacker = payload.name
    return {"status": "ok", "current_attacker": current_attacker}


@app.post("/set_defender")
async def set_defender(payload: NamePayload):
    global current_defender
    current_defender = payload.name
    return {"status": "ok", "current_defender": current_defender}


@app.get("/state")
async def get_state():
    return {"current_attacker": current_attacker, "current_defender": current_defender}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")