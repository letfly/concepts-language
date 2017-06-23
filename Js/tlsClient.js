const tls = require('tls');
const fs = require('fs');

const options = {
  key: fs.readFileSync('./server-key.pem'),
  cert: fs.readFileSync('./server-cert.pem'),
  ca: [fs.readFileSync('./ca-cert.pem')],
  rejectUnauthorized: true,
  host: '127.0.0.1'
};
const socket = tls.connect(8000, options, () => {
  console.log('client connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  process.stdin.pipe(socket);
  process.stdin.resume();
});
socket.setEncoding('utf8');
socket.on('data', (data) => {
  console.log(data);
});
socket.on('end', () => {
});
