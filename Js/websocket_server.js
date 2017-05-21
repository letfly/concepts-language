const WebSocketServer = require('./ws').Server;
let wsServer = new WebSocketServer({ port: 3000 });

wsServer.on('connection', function connection(socket) {
  socket.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
});
