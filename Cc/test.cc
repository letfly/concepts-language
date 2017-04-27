#include <cstdio>

class Car
{
  int num = 0;
  char color[10] = "red";
public:
  static int static_n;
  Car(int n)
  {
    num = n;
  }
  void run()
  {
    printf("%d;;%s", num, color);
  }
  void output(int num)
  {
    this->num = num;
    run();
  }
};
void run()
{
  printf("%d;;%s", 0, "red");
}
int main()
{
  /*// 1.打印
  printf("d");
  // 2.三元运算符
  int a = (1 > 2) ? 1 : 2;
  printf("%d", a);
  // 3.条件语句
  int x = 5;
  if (x == 3 || x == 4 || x == 5)
    printf("%d+春季", x);
  else if (x == 6 || x == 7 || x == 8)
    printf("%d+夏季", x);
  // 4.选择语句
  switch (x)
  {
  case 4:
    printf("a");
    break;
  case 5:
    printf("b");
    break;
  case 6:
    printf("c");
    break;
  }
  // 5.while循环
  while (x < 3)
  {
    ++x;
    printf("%d", x);
  }
  // 6.for循环
  for (int x = 0; x < 3; ++x) printf("%d", x);
  // 10.函数
  // run()
  // 11. 数组
  // 指针方式
  //int *arr = new int[5]; // 每个元素都没有初始化
  //arr = new int[5](); // 每个元素初始化为0
  // 标准方式
  //int arr[5]; // arr[i]的值不确定，没有初始化
  int arr[5] = {1, 2, 3, 4, 8};
  for (unsigned long i = 0; i < sizeof(arr) / sizeof(int);
       ++i) printf("%d ", arr[i]);
  // 二，面向对象
  Car c;
  c.run();
  Car *c = new Car();
  c->run();
  // 5.匿名函数
  auto sum = [](int x, int y) {return x+y;};
  printf("%d", sum(10, 20));
  // 8.构造函数
  Car *c = new Car(2017);
  c->run();
  // 9构造代码块(没有)
  // 10.this关键字(防止命名冲突而修改私有成员)
  Car *c = new Car(2017);
  c->output(2018);*/
  // day06
  // 1，static关键字(每一次声明类都是同一变量)
  Car *c = new Car(2017);
  c->output(2018);
  printf("%d\n", Car::static_n);
  printf("%d\n", Car::static_n);
}
