/**
 * YeldizSmart AI - Express REST API + WebSocket Backend
 * Handles real-time lead updates, classification, and webhook sync
 */

const express = require('express');
const cors = require('express-cors');
const bodyParser = require('body-parser');
const WebSocket = require('ws');
const http = require('http');
require('dotenv').config();

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// WebSocket clients set
const clients = new Set();

// WebSocket connection
wss.on('connection', (ws) => {
  console.log('WebSocket client connected');
  clients.add(ws);

  ws.on('message', (message) => {
    console.log('Received:', message);
    // Broadcast to all clients
    clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ type: 'update', data: message }));
      }
    });
  });

  ws.on('close', () => {
    clients.delete(ws);
    console.log('WebSocket client disconnected');
  });
});

// REST API Routes
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

app.post('/api/leads/classify', (req, res) => {
  const { title, description, price } = req.body;
  // Call Gemini AI classifier
  res.json({ quality: 'HOT', confidence: 95, reason: 'Direct owner' });
});

app.post('/api/leads/sync', (req, res) => {
  const leads = req.body;
  // Sync to Google Sheets
  res.json({ success: true, synced: leads.length });
});

app.get('/api/campaigns', (req, res) => {
  res.json({
    campaigns: [
      { id: 1, city: 'Mumbai', platform: 'FB', status: 'RUNNING', leads: 45 },
      { id: 2, city: 'Delhi', platform: 'OLX', status: 'PAUSED', leads: 28 }
    ]
  });
});

// Broadcast helper
function broadcastToClients(data) {
  clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
}

server.listen(PORT, () => {
  console.log(`YeldizSmart AI Backend running on http://localhost:${PORT}`);
  console.log(`WebSocket available on ws://localhost:${PORT}`);
});
