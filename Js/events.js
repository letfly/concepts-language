EventEmitter.init = function() {};

function EventEmitter() {
  EventEmitter.init.call(this);
}

function _addListener(target, type, listener, prepend) {
  if (typeof listener != 'function')
    throw new TypeError('"listener" argument must be a function');

  let events = target._events;
  if (!events)
    events = target._events = Object.create(null);

  events[type] = listener;

  return target;
}
EventEmitter.prototype.addListener = function addListener(type, listener) {
  return _addListener(this, type, listener, false);
};
EventEmitter.prototype.on = EventEmitter.prototype.addListener;

function emitNone(handler, isFn, self) {
  if (isFn) handler.call(self);
}
EventEmitter.prototype.emit = function emit(type) {
  let events = this._events,
    handler = events[type];
  let isFn = typeof handler === 'function',
    len = arguments.length;
  switch (len) {
    // fast cases
    case 1:
      emitNone(handler, isFn, this);
      break;
  }

  return true;
};
module.exports = EventEmitter;
