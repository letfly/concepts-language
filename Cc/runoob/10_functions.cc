#include <iostream>
using namespace std;

// 函数声明
int max(int num1, int num2);

int main(){
    // 局部变量声明
    int a = 100;
    int b = 200;
    int ret;

    // 调用函数来获取最大值
    ret = max(a, b);
    cout << "Max value is : " << ret << endl;
}
// 函数返回两个数中较大的那个数
int max(int num1, int num2){
    // 局部变量声明
    int ret;
    ret = num1>num2?num1:num2;
    return ret;
}
