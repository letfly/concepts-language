#include <iostream>

/* //static 存储类
// 函数声明
void func(void);
static int count = 10; //全局变量
int main(){
    while(count--){
        func();
    }
}
// 函数定义
void func(){
    static int i = 5; //局部静态变量
    i++;
    std::cout << "变量i为" << i;
    std::cout << " ，变量count 为" << count <<count << std::endl;
}*/

//extern 存储类
int count;
extern void write_extern();

int main(){
    count = 5;
    write_extern();
}
