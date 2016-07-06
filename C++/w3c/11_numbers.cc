#include <iostream>
/*// C++ 数学运算
#include <cmath>
using namespace std;

int main(){
    // 数字定义
    short s;
    int i;
    long l;
    float f;
    double d;

    // 数字赋值
    s = 10;
    i = 1000;
    l = 10000000;
    f = 230.47;
    d = 30949.374;

    // 数字输出
    cout << "sin(d) :" << sin(d) << endl;
    cout << "abs(i) :" << abs(i) << endl;
    cout << "floor(l) :" << floor(l) << endl;
    cout << "sqrt(f) :" << sqrt(f) << endl;
    cout << "pow(d, 2) :" << pow(d, 2) << endl;
}*/
// C++ 随机数
#include <ctime>
#include <cstdlib>
using namespace std;

int main(){
    int i;

    // 设置种子
    srand((unsigned) time(NULL));
    // 生成10个随机数
    for(i=0; i<10; i++){
        // 生成实际的随机数
        cout << "随机数：" << rand() << endl;
    }
}
