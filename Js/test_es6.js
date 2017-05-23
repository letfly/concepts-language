/*class Car {
  constructor() {
    this.num = 0;
    this.color = 'red';
  }
  run() {
    console.log(this.num + ";;" + this.color);
  }
  output(n) {
    this.num = n;
    this.run();
  }
  static static_func() {
    console.log("static_func");
  }
}*/
/*// 1，static关键字(es5没有该关键字)
Car.static_func();
let c = new Car();
c.output();
console.log(c.num);
//day07
//1，继承-概述[为了提高代码的复用性，提出类类之间关系所属关系 is a]
//只支持单继承，不支持多继承，多继承不安全：
class Car1 extends Car {}
let c1 = new Car1();
c1.output();
//4，子父类中变量特点
class Car1 extends Car {
  output() {
    console.log("dd");
  }
}
let c1 = new Car1();
c1.output();*/
// this关键字
// bind this关键字
class Logger {
  constructor() {
    this.printName = this.printName.bind(this);
  }
  printName(name = 'there') {
    this.print(`Hello ${name}`);
  }
  print(text) {
    console.log(text);
  }
}
const logger = new Logger();
//logger.printName();
const { printName } = logger;
printName(); // TypeError: Cannot read property 'print' of undefined

// 17.1.2回调函数
let fs = require('fs');
let readFile = function(fileName) {
  return new Promise(function(resolve, reject) {
    fs.readFile(fileName, function(err, data) {
      if (err) return reject(err);
      resolve(data);
    });
  });
};
//let readFile = require('fs-readfile-promise');

let fileA = 'a.txt';
let fileB = 'b.txt';
readFile(fileA, function(err, data) {
  if (err) throw err;
  console.log(data);
  readFile(fileB, function(err, data) {
    if (err) throw err;
    console.log(data);
  });
});
// 17.1.3 Promise
readFile(fileA)
  .then(function(data) {
    console.log(data.toString());
  })
  .then(function() {
    return readFile(fileB);
  })
  .then(function(data) {
    console.log(data.toString());
  })
  .catch(function(err) {
    console.log(err);
  });
// 17.3.5 Generator
/*function* gen() {
  let r1 = yield readFile(fileA);
  console.log(r1.toString());
  let r2 = yield readFile(fileB);
  console.log(r2.toString());
}*/
/*let thunkify = require('thunkify');
let readFile = thunkify(readFile);

let g = gen();
g.next().value(function(err, data) {
  if (err) throw err;
  let r2 = g.next(data);
  r2.value(function(err, data) {
    if (err) throw err;
    g.next(data);
  });
});
// 17.3.6 Thunk函数的自动流程管理
let thunkify = require('thunkify');
let readFile = thunkify(readFile);

function run(fn) {
  let gen = fn();

  function next(err, data) {
    let result = gen.next(data);
    if (result.done) return;
    result.value(next);
  }
  next();
}

run(gen);
// 17.4 co模块
// 17.4.1 基本用法
let co = require('co');
co(gen);
// 17.4.3 基于Promise对象的自动执行
let g = gen();
g.next().value.then(function(data) {
  g.next(data).value.then(function(data) {
    g.next(data);
  });
});

// 
function run(gen) {
  let g = gen();

  function next(data) {
    let result = g.next(data);
    if (result.done) return result.value;
    result.value.then(function(data) {
      next(data);
    });
  }

  next();
}

run(gen);*/
