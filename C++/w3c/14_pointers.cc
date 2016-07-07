#include <iostream>
using namespace std;

int main(){
    int var = 20;
    int *ip;

    ip = &var;

    // 访问var 中的值
    cout << var << endl;
    // 访问ip中存储地址
    cout << ip << endl;
    // 访问指针ip中地址的值
    cout << *ip << endl;
}
