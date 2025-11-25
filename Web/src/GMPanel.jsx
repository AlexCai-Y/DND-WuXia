import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://172.30.53.118:3001");

export default function GMPanel() {
  const [state, setState] = useState({ playerHP: 100, enemyHP: 100, turn: 1 });

  useEffect(() => {
    console.log("GMPanel mounted");
    socket.on("state", setState);

    socket.on("turnUpdate", (data) => {
    console.log("Turn updated:", data.turn);
    setState((prev) => ({ ...prev, turn: data.turn }));
    });

    socket.on("connect", () => {
      console.log("socket connected:", socket.id, "transport:", socket.io?.engine?.transport?.name);
    });

    socket.on("connect_error", (err) => {
      console.error("socket connect_error:", err);
    });

    socket.on("disconnect", (reason) => {
      console.log("socket disconnected:", reason);
    });

    return () => {
      socket.off("connect");
      socket.off("connect_error");
      socket.off("disconnect");
      socket.off("state");
      socket.off("turnUpdate");
    };
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
      <p>Turn: {state.turn}</p>

      <div className="flex space-x-4">
      <button onClick={() => changeHP("playerHP", -10)}>Damage Player</button>
      <button onClick={() => changeHP("enemyHP", -10)}>Damage Enemy</button>
      <button onClick={() => changeHP("playerHP", +10)}>Heal Player</button>
      <button onClick={() => changeHP("enemyHP", +10)}>Heal Enemy</button>
      </div>
      <button onClick={() => endTurn()}>End Turn</button>
    </div>
  );
}