const EventEmitter = require('events');
const util = require('util');

function Server(options, connectionListener) {
  if (!(this instanceof Server))
    return new Server(options, connectionListener);

  EventEmitter.call(this);

  if (typeof options === 'function') {
    connectionListener = options;
    options = {};
    this.on('connection', connectionListener);
  }
}
util.inherits(Server, EventEmitter);
Server.prototype.listen = function() {};

exports.createServer = function(options, connectionListener) {
  return new Server(options, connectionListener);
};





const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
