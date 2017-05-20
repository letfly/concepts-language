const fs = require('fs');
const https = require('https');
const WebSocketServer = require('ws').Server;


let options = {
  key: fs.readFileSync('./server.key'),
  ca: [fs.readFileSync('./ca.cert')],
  cert: fs.readFileSync('./server.cert')
};

let app = https.createServer(options, function(req, res) {
  res.end('Hello world\n');
}).listen(3000, '127.0.0.1');

let wsServer = new WebSocketServer({ server: app });

wsServer.on('connection', function connection(socket) {
  socket.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  socket.send('something');
});
