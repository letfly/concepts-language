const WebSocket = require('ws');

let ws = new WebSocket("ws://127.0.0.1:3000/");
ws.on('open', function op() {
  ws.send('client lai le');

  ws.on('message', function mess(messa) {
    console.log(messa);
  });
});
