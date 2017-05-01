console.log(1 + "2" + "2");
console.log(1 + +"2" + "2");
console.log("A" - "B" + "2");
console.log("A" - "B" + 2);

var net = require('net');

var server = net.createServer(function(socket)
{
  // 新的连接
  socket.on('data', function()
  {
    console.log('连接断开');
  });
  socket.on('end', function()
  {
    console.log('连接断开');
  });
  socket.write("欢迎光临《深入浅出Node.js》示例：\n");
});

server.listen(10003, function()
{
  console.log('server bound');
});
