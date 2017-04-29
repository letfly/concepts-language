class Car
{
  constructor()
  {
    this.num = 0;
    this.color = 'red';
  }
  run()
  {
    console.log(this.num + ";;" + this.color);
  }
  output(n)
  {
    this.num = n;
    this.run();
  }
  static static_func()
  {
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
c1.output();*/
//4，子父类中变量特点
class Car1 extends Car
{
  output()
  {
    console.log("dd");
  }
}
var c1 = new Car();
c1.output();
