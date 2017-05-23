const fs = require('fs');
const https = require('https');
const Koa = require('koa');
const WebSocketServer = require('ws').Server;


let options = {
  key: fs.readFileSync('./server.key'),
  cert: fs.readFileSync('./server.cert')
};

let server = new Koa();
let app = https.createServer(options, server.callback()).listen(3000, '127.0.0.1');

let wsServer = new WebSocketServer({ server: app });

wsServer.on('connection', function connection(socket) {
  socket.on('message', function incoming(message) {
    console.log('received: %s', message);
  });

  socket.send('something');
});
