/*function Car(n = 0) {
  var num = n; // 私有成员
  var color = 'red';
  this.run = function() // 有this，公有成员
  {
    console.log(num + ";;" + color);
  };
  this.output = function(n) {
    num = n;
    this.run();
  };
  this.static_output = function() {
    ++Car.static_n;
    ++num;
    console.log(Car.static_n + "," + num);
  };
}*/
/*// 1.打印
console.log("d")
// 2.三元运算符
var a = (1 > 2) ? 1 : 2
        console.log(a)
// 3.条件语句
        var x = 5
                if (x == 3 || x == 4 || x == 5) console.log(x + "春季");
else if (x = 6 || x == 7 || x == 8) console.log(x + "夏季");
// 4.选择语句
var x = 4;
switch (x)
{
case 4:
  console.log("a");
  break;
case 5:
  console.log('b');
  break;
case 6:
  console.log('c');
  break;
}
// 5.while循环
var x = 1
        while (x < 3)
{
  x++;
  console.log(x);
}
// 6.for循环
for (var x = 0; x < 3; x++)
  console.log(x);
// 7.for嵌套
var dic = {fname: "John", lname: "Don"}
          var arr = ['a', 'b', 'c']
                    for (x in dic)
{
  console.log(dic[x]);
  for (x in arr)
    console.log(arr[x]);
}
// 8.break,continue语句
for (i = 0; i < 10; i++)
{
  if (i == 3)
  {
    // break;
    continue;
  }
  console.log(i);
}
// 9.没有pass语句
// 10.函数
function get_result(num)
{
  console.log(num);
}
get_result(3);
// 11.数组
var arr = new Array(5); // 创建一个空数组
var arr = new Array('a', 'b');
var arr = ['a', 'b'];
console.log(arr);
// 二，面向对象
var c = new Car();
c.run();
// 5匿名函数
var sum = function(arg1, arg2)
{
  return arg1 + arg2;
};
console.log("Value of total:" + sum(10, 20));
// 8构造函数
function Car(n)
{
  var num = n;
  var color = 'red';
  this.run = function()
  {
    console.log(num+";;"+color);
  };
}
var c = new Car(2017);
c.run();
//
//注意：这里我们使用了object.prototype.方法名，而不是object.prototype
//主要是用来避免重写定义原型prototype对象
Car.prototype.add = function()
{
  return this.run();
};
var c = new Car();
c.add();
// 9构造代码块(没有)
// 10.this关键字(防止命名冲突以及定义公有成员)
var c = new Car();
c.output(2017);
// day06
// 1，static关键字(es5没有该关键字)
Car.static_n = 0; // static变量
var c = new Car();
c.static_output();
var c1 = new Car();
c1.static_output();
Car.static_func = function() {
  console.log("static_func");
};
Car.static_func();
//day07
//1，继承-概述[为了提高代码的复用性，提出类类之间关系所属关系 is a]
//只支持单继承，不支持多继承，多继承不安全：
function Car1(){
  Car.call(this, []);
}
Car1.prototype = Object.create(Car.prototype, {
});
var c1 = new Car1();
c1.output(1);*/
//4，子父类中变量特点
/*function Car1() {
  output() {
    console.log("dd");
  }
}*/
// 异步机制
for (var i = 0; i < 5; i++) {
  setTimeout(function() {
    console.log(i);
  }, 0);
}
console.log(i);
let start = +new Date();

setTimeout(function() {
  console.log('time: ' + (new Date().getTime() - start));
}, 10);
