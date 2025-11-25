// server/server.js
import express from 'express';
import cors from 'cors';
import { WebSocketServer } from 'ws';
import { db, initDB } from './db.js';

const app = express();
app.use(cors());
app.use(express.json());

// REST example
app.get('/api/battles', (req, res) => {
  const battles = db.prepare('SELECT * FROM battles').all();
  res.json(battles);
});

// Create battle
app.post('/api/battles', (req, res) => {
  const { name } = req.body;
  const stmt = db.prepare('INSERT INTO battles (name, state) VALUES (?, ?)');
  const result = stmt.run(name, JSON.stringify({ players: [], enemies: [], turn: 1 }));
  res.json({ id: result.lastInsertRowid });
});

const server = app.listen(3001, () => console.log('HTTP API on 3001'));

// WebSocket
const wss = new WebSocketServer({ server });
wss.on('connection', (ws) => {
  console.log('client connected');
  ws.on('message', (msg) => {
    const data = JSON.parse(msg);

    if (data.type === 'SYNC_BATTLE') {
      const battle = db.prepare('SELECT * FROM battles WHERE id = ?').get(data.battleId);
      ws.send(JSON.stringify({ type: 'BATTLE_STATE', battle }));
    }

    if (data.type === 'UPDATE_BATTLE') {
      db.prepare('UPDATE battles SET state = ? WHERE id = ?')
        .run(JSON.stringify(data.state), data.battleId);

      wss.clients.forEach((client) => {
        client.send(JSON.stringify({ type: 'BATTLE_STATE', battleId: data.battleId, state: data.state }));
      });
    }
  });
});

initDB();

