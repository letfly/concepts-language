#include <cstdio>

class Car
{
  int num = 0;
  char color[10] = "red";
public:
  Car(int n) { num=n; }
  void run() {
    printf("%d;;%s", num, color);
  }
};
void run() {
  printf("%d;;%s", 0, "red");
}
int main()
{
  /*// 10.函数
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
  c->run();*/
}
