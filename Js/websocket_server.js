const Koa = require('koa');
const WebSocketServer = require('ws').Server;

let app = new Koa();

let wsServer = new WebSocketServer({ port: 3000, server: app });
wsServer.on('connection', function(ws) {
  let i = 0;
  ws.on('message', function(msg) {
    console.log(msg, i++);
    console.log(i);
  });

  ws.send('server lai le ' + i);
});
