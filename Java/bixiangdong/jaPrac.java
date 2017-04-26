class HelloWorld
{
  public static void main(String []args)
  {
    System.out.println("x=");
  }
}
//2
/**
a=(x>y)?x:y;
//3
if (x==3||x==4||x==5)
  sop(x+"春季");
else if (x==6||x==7||x==8)
  sop(x+"夏季")
else
  sop("月份不存在")
//4
int x=4
switch(x){
  case 4:
    sop("a");break;
  case 6:
    sop("b");break;
  default:
    sop("c");
}
//5
int x=1;
while(x<3){
  sop("x="+x);
  x++;
}
int x=1;
do{
  sop("do:x="+x);
  x++;
}while(x<3);
//6
for(int x=0;x<3;x++){
  sop(x);
}
//7
for(int x=0;x<3;x++){
  for(int y=0;y<4;y++){
    sop("*");
  }
  System.out.println();
}
//8
//break,continue
//9
//没有pass语句
//10函数
public static void getResult(int num){
  return num*3+5;
  }
//11元组(数组)
int[] arr=new int[5];
int[] arr=new int[]{1,2,3};
int[] arr={3,5,1};
for(int x=0;x<arr.length;x++){
  sop("arr["+x+"]"+arr[x]+";");
}
//
////二，面向对象
class Car{
  int num=0;
  String color="red";
  public void run(){
    System.out.println(num+"::"+color)
  }
}
class CarDemo{
  public static void main(String[] args){
    Car c=new Car();
    c.run();
  }
}
//5匿名对象
class Car{}
class CarDemo{
  public static void main(String[] args){
    show(new Car());
  }
  public static void show(Car()){
  }
}
//8构造函数
class Person(){
  Person(){}
  Person(String n,int s){
    name=n;salary=s;
  }
}
//9构造代码块
class Person{
  {}
}
//10this关键字【代表本类对象】
//11this应用
//当定义类中功能时，该函数内部要用到该函数的对象时，这时用this来表示这个对象


// day06
//1，static关键字
//2，main()函数[作为程序的入口]
//Java:可以被jvm调用
public static void main(String[] args){}
//3，静态什么时候用[对象共享数据，与特有数据(名字)不一样]
//无论创建多少个对象，静态字段也只占用一份存储空间。
//4，静态的应用-工具类
//将ArrayTool抽取出来为一个文件，由于ArrayTool类没有特有数据，因此可将其内部函数都静态化。节约内存空间。类名.函数()
//5，帮助文档制作javadoc
//接下来，将ArrayTool.class文件发送给其他人，其他人只需将该文件设置到classpath路径下，就可使用
//6，静态代码块[随着类的加载而执行，只执行一次用于给类初始化]
class StaticCode{
  static{sop("a");}
}
class StaticCodeDemo{
  static{sop("b");}
  public static void main(String[] args){
    new StaticCode();
    new StaticCode();
    sop("over");
    static{sop("c");}
  }
}
//7，对象的初始化过程
class Person{
  private String name="hh";private int age;
  private static String country="cn";
  Person(String name,int age){
    this.name=name;this.age=age;
  }{sop(name+".."+age);}
  public void setName(String name){this.name=name;}
}
//9，单例设计模式：[偏思想]
class Single{
  private Single(){}
  static Single s=new Single();
  public static Single getInstance(){return s;}
  public void show(){sop("haha");}
}
class SingleDemo{
  public static void main(String[] args){
    Single s=Single.getInstance();s.show();
  }
}


//day07
//1，继承-概述[为了提高代码的复用性，提出类类之间关系所属关系 is a]
//只支持单继承，不支持多继承，多继承不安全例：
class A{
  void show(){
    sop("A");
  }
}
class B{
  void show(){
    sop("B");
  }
}
class C extends A,B{
  C c=new C();
  c.show();
}
//4，子父类中变量特点
class Fu{
  int num=4;
}
class Zi extends Fu{
  int num=5;
  void show(){
    sop(super.num);
  }
}
Zi z=new Zi();
z.show();
//5，子父类覆盖
class Fu{
  void show(){
    sop("Fu");
  }
}
class Zi extends Fu{
  void show(){
    sop("Zi");
  }
}
class ShowDemo{
  public static void main(String[] args){
    Zi z=new Zi();
    z.show();
  }
}

//day11
class Test extends Thread{
  private String name;
  Test(String name){
    this.name=name;
  }
  public void run(){
    for(int x=0;x<50;x++){
      sop(this.getName()+"test..."+x);//获取线程名称
    }
  }
}
class Test extends Thread{
  Test(String name){
    super(name)
  }
  public void run(){
    for(int x=0;x<60;x++){
      sop(Thread.currentThread().getName()+"test"+x);//Thread.currentThread():获取当前线程对象。getName()：获取线程名称。设置县城名称：setName或者构造函数。
    }
  }
}
class ThreadTest{
  public static void main(String[] args){
    Test t1=new Test("one");
    Test t2=new Test("two");
    t1.start();
    t2.start();
    for(int x=0;x<60;x++){
      sop("main...."+x);
    }
  }
}
//售票的例子
class Ticket extends Thread{
  static  private int tick=100;
  public void run(){
    while(true){
      if(tick>0)  {
        sop(currentThread().getName()+"sale:"+tick--);
      }
    }
  }
}
class TicketDemo{
  public static void main(String[] args)  {
    Ticket t1=new Ticket();
    //Ticket t2=new Ticket();
    //Ticket t3=new Ticket();
    //Ticket t4=new Ticket();
    t1.start();
    t1.start();
    t1.start();
    t1.start();
  }
}*/
