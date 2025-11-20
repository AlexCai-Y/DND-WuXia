import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://localhost:3001");

export default function GMPanel() {
  const [state, setState] = useState({ playerHP: 100, enemyHP: 100 });

  useEffect(() => {
    socket.on("state", setState);
  }, []);

  const changeHP = (key, amount) => {
    socket.emit("gmUpdate", { [key]: state[key] + amount });
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
    </div>
  );
}