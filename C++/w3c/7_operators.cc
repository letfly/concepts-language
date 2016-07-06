/* // 关系运算符
#include <iostream>
using namespace std;

int main(){
    int a = 21;
    int b = 10;
    int c;

    if( a == b ){
        cout << "Line 1 - a等于b" << endl;
    }else{
        cout << "Line 1 - a 不等于b" << endl;
    }
    if( a < b ){
        cout << "Line 2 - a小于b" << endl;
    }else{
        cout << "Line 2 - a不小于b" << endl;
    }
    if( a > b ){
        cout << "Line 3 - a大于b" << endl;
    }else{
        cout << "Line 3 - a不大于b" << endl;
    }
    // 改变a和b的值
    a = 5;
    b = 20;
    if( a <= b ){
        cout << "Line 4 - a小于或等于b" << endl;
    }
    if( b >= a ){
        cout << "Line 5 - b大于或等于a" << endl;
    }
}*/
/*// 逻辑运算符
#include <iostream>
using namespace std;

int main(){
    int a = 5;
    int b = 20;
    int c;
    if( a && b ){
        cout << "Line 1 - 条件为真" << endl;
    }
    if( a || b ){
        cout << "Line 2 - 条件为真" << endl;
    }
    // 改变a 和b的值
    a = 0;b=10;
    if( a && b ){
        cout << "Line 3 - 条件为真" << endl;
    }else{
        cout << "Line 4 - 条件不为真" << endl;
    }
    if( !(a && b) ){
        cout << "Line 5 - 条件为真" << endl;
    }
}*/
/*// 位运算符
#include <iostream>
using namespace std;

int main(){
    unsigned int a = 60; // 60 = 0011 1100
    unsigned int b = 13; // 13 = 0000 1101
    int c = 0;

    c = a & b; // 12 = 0000 1100
    cout << "Line 1 - c 的值是" << c << endl;

    c = a | b; // 61 = 0011 0000
    cout << "Line 2 - c 的值是" << c << endl;

    c = a ^ b; // 49 = 0011 0001
    cout << "Line 3 - c 的值是" << c << endl;

    c = ~a; // -61 = 1100 0011
    cout << "Line 4 - c的值是" << c << endl;

    c = a << 2; // 240 = 1111 0000
    cout << "Line 5 - c的值是" << c << endl;

    c = a >> 2; // 15 = 0000 1111
    cout << "Line 6 - c的值是" << c <<endl;
}*/
/*// 赋值运算符
#include <iostream>
using namespace std;

int main(){
    int a = 21;
    int c;
    c = a;
    cout << "Line 1 - = 运算符实例，c的值＝：" << c << endl;

    c += a;
    cout << "Line 2 - +=运算符实例，" << c <<endl;

    c -= a;
    cout << c << endl;

    c *= a;
    cout << c << endl;

    c /= a;
    cout << c << endl;
}*/
// C++ 中的运算符优先级
#include <iostream>
using namespace std;

int main(){
    int a = 20; int b = 10; int c = 15; int d = 5; int e;
    e = (a + b)*c/d;
    cout << e << endl;

    e = ((a+b)*c)/d; // (30 * 15)/5
    cout << e << endl;

    e = (a + b) * (c / d); // (30)*(15/5)
    cout << e << endl;
}
