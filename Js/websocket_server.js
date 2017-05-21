const WebSocketServer = require('ws').Server;
const Koa = require('koa');

let app = new Koa();
let server = app.listen(3000);

let wsServer = new WebSocketServer({ server: server });
wsServer.on('connection', function(ws) {
  let i = 0;
  ws.on('message', function(msg) {
    console.log(msg, i++);
    console.log(i);
  });

  ws.send('server lai le ' + i);
});
app.wss = wsServer;
