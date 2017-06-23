const fs = require('fs');
const WebSocket = require('ws');

let options = {
  key: fs.readFileSync('./client-key.pem'),
  cert: fs.readFileSync('./client-cert.pem'),
  ca: [fs.readFileSync('./ca-cert.pem')],
  requestCert: true,
  rejectUnauthorized: true,
};

let ws = new WebSocket('wss://127.0.0.1:3000/', options);
ws.on('open', function op() {
  ws.send('client lai le');

  ws.on('message', function mess(messa) {
    console.log(messa);
  });
});
