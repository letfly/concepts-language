let http = require('http');

http.createServer(function(req, res) {
  let content = "";

  req.on('data', function(chunk) {
    content += chunk;
    console.log(content);
  });

  req.on('end', function() {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.write("You've sent: " + content);
    res.end();
  });

}).listen(3000);
