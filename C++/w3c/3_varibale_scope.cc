#include <iostream>
using namespace std;

int g; // 全局变量声明
int main(){
    // 局部变量声明
    int a, b;

    // 实际初始化
    int g = 10;
    a = 10;
    b = 20;
    // g = a + b;

    cout << g << endl;
}
