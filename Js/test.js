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
function Car()
{
  this.num = 0;
  this.color = 'red';
  this.run = function()
  {
    console.log(this.num+";;"+this.color);
  };
}
var c = new Car();
c.run();
// 5匿名函数
var sum = function(arg1, arg2)
{
  return arg1 + arg2;
};
console.log("Value of total:" + sum(10, 20));
// 8构造函数
function Car(num)
{
  this.num = num;
  this.color = 'red';
  this.run = function()
  {
    console.log(this.num+";;"+this.color);
  };
}
var c = new Car(2017);
console.log(c.run());*/
//
function Car(model, year, miles)
{
  this.model = model;
  this.year = year;
  this.miles = miles;
}
//注意：这里我们使用了object.prototype.方法名，而不是object.prototype
//主要是用来避免重写定义原型prototype对象
Car.prototype.output = function()
{
  return this.model + "走了" + this.miles + '公里';
};
var tom = new Car("大叔", 2009, 20000);
console.log(tom.output());
/*// 10.this对象
// 作为对象方法调用
var point =
{
  x : 0,
  y : 0,
moveTo :
  function(x, y)
  {
    this.x = this.x + x;
    this.y = this.y + y;
  }
};
point.moveTo(1, 1);*/
