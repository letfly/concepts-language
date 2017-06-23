const https = require('https');
const fs = require('fs');

let options = {
  key: fs.readFileSync('./server-key.pem'),
  cert: fs.readFileSync('./server-cert.pem'),
  ca: [fs.readFileSync('./ca-cert.pem')],
  requestCert: true,
  rejectUnauthorized: true,
};

https.createServer(options, function(req, res) {
  res.writeHead(200);
  res.end('hello world\n');
}).listen(8000, '127.0.0.1');
