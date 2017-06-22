const https = require('https');
const fs = require('fs');

const options = {
  host: '127.0.0.1',
  port: 8000,
  path: '/',
  method: 'GET',
  ca: [fs.readFileSync('./ca-cert.pem')],
  key: fs.readFileSync('./server-key.pem'),
  cert: fs.readFileSync('./server-cert.pem'),
  rejectUnauthorized: true,
};

const req = https.request(options, (res) => {
  console.log('statusCode:', res.statusCode);
  console.log('headers:', res.headers);

  res.on('data', (d) => {
    process.stdout.write(d);
  });
});
req.on('error', (e) => {
  console.error(e);
});
req.end();
