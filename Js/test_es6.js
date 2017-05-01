class Car {
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
}
// 1，static关键字(es5没有该关键字)
/*Car.static_func();
var c = new Car();
c.output();
console.log(c.num);
//day07
//1，继承-概述[为了提高代码的复用性，提出类类之间关系所属关系 is a]
//只支持单继承，不支持多继承，多继承不安全：
class Car1 extends Car {
}
var c1 = new Car1();
c1.output();
//4，子父类中变量特点
class Car1 extends Car
{
  output()
  {
    console.log("dd");
  }
}
var c1 = new Car();
c1.output();*/

// 17.1.2回调函数
/*var fs = require('fs');
var readFile = function(fileName) {
  return new Promise(function(resolve, reject){
    fs.readFile(fileName, function(err, data){
      if (err) return reject(err);
      resolve(data);
    });
  });
};*/
var readFile = require('fs-readfile-promise');

var fileA = 'a.txt';
var fileB = 'b.txt';
/*readFile(fileA, function(err, data) {
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
  });*/
// 17.3.5 Generator
function* gen() {
  var r1 = yield readFile(fileA);
  console.log(r1.toString());
  var r2 = yield readFile(fileB);
  console.log(r2.toString());
}
/*var thunkify = require('thunkify');
var readFile = thunkify(readFile);

var g = gen();
g.next().value(function(err, data) {
  if (err) throw err;
  var r2 = g.next(data);
  r2.value(function(err, data) {
    if (err) throw err;
    g.next(data);
  });
});
// 17.3.6 Thunk函数的自动流程管理
var thunkify = require('thunkify');
var readFile = thunkify(readFile);

function run(fn) {
  var gen = fn();

  function next(err, data) {
    var result = gen.next(data);
    if (result.done) return;
    result.value(next);
  }
  next();
}

run(gen);
// 17.4 co模块
// 17.4.1 基本用法
var co = require('co');
co(gen);
// 17.4.3 基于Promise对象的自动执行
var g = gen();
g.next().value.then(function(data) {
  g.next(data).value.then(function(data) {
    g.next(data);
  });
});*/

function run(gen) {
  var g = gen();

  function next(data) {
    var result = g.next(data);
    if (result.done) return result.value;
    result.value.then(function(data) {
      next(data);
    });
  }

  next();
}

run(gen);
