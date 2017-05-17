var https = require('https');
var fs = require('fs');

var options = {
	key: fs.readFileSync('./server.key'),
	ca: [fs.readFileSync('./ca.cert')],
	cert: fs.readFileSync('./server.cert')
};

https.createServer(options,function(req,res){
	res.writeHead(200);
	res.end('hello world\n');
}).listen(5000,'127.0.0.1');

