const WebSocketServer = require('ws').Server;
let wsserver = new WebSocketServer({ port: 8080 });

wsserver.on('connection', function connection(socket) {
  socket.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  socket.send('something');
});
