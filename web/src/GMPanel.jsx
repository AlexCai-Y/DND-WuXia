import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://172.30.55.166:3001");

export default function GMPanel() {
  const [state, setState] = useState({ playerHP: 100, enemyHP: 100 });

  useEffect(() => {
    console.log("GMPanel mounted");
    socket.on("state", setState);
  }, []);

  const changeHP = (key, amount) => {
    socket.emit("gmUpdate", { [key]: state[key] + amount });
  };

  const endTurn = () => {
    console.log("END TURN CLICKED - emitting to server");
    socket.emit("endTurn");
  };

  return (
    <div>
      <h1>GM Panel</h1>
      <p>Player HP: {state.playerHP}</p>
      <p>Enemy HP: {state.enemyHP}</p>

      <button onClick={() => changeHP("playerHP", -10)}>Damage Player</button>
      <button onClick={() => changeHP("enemyHP", -10)}>Damage Enemy</button>
      <button onClick={() => changeHP("playerHP", +10)}>Heal Player</button>
      <button onClick={() => changeHP("enemyHP", +10)}>Heal Enemy</button>
      <button onClick={() => endTurn()}>End Turn</button>
    </div>
  );
}