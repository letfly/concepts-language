const EventEmitter = require('./events');

let emitter = new EventEmitter();
// 1.概述
emitter.on('someEvent', function(){
  console.log('event has occured');
});

function f() {
  console.log('start');
  emitter.emit('someEvent');
  console.log('end');
}
f();
