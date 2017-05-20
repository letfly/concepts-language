const WebSocket = require('ws');

let socket = new WebSocket("ws://127.0.0.1:3000/");
socket.on('open', function open() {
  socket.send('message');
});
