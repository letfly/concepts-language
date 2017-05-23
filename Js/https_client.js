const https = require('https');
const fs = require('fs');

let options = {
  hostname: '127.0.0.1',
  port: 3000,
  path: '/',
  method: 'GET',
  ca: [fs.readFileSync('./ca.cert')],
  agent: false
};

options.agent = new https.Agent(options);
let req = https.request(options, function(res) {
  console.log("statusCode: ", res.statusCode);
  console.log("headers: ", res.headers);
  res.setEncoding('utf-8');
  res.on('data', function(d) {
    console.log(d);
  });
});

req.end();

req.on('error', function(e) {
  console.log(e);
});
