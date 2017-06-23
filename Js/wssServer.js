const fs = require('fs');
const https = require('https');
const WebSocketServer = require('ws').Server;


let options = {
  ca: [fs.readFileSync('./ca-cert.pem')],
  key: fs.readFileSync('./server-key.pem'),
  cert: fs.readFileSync('./server-cert.pem'),
  rejectUnauthorized: true,
  requestCert: true,
};

let app = https.createServer(options).listen(3000, '127.0.0.1');

let wsServer = new WebSocketServer({ server: app });

wsServer.on('connection', function connection(socket) {
  socket.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  socket.send('something');
});
wsServer.on('connection', (ws) => {
  ws.on('message', (msg) => {
    console.log('next', msg);
  });
});
