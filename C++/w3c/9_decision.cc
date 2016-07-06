#include <iostream>
using namespace std;

/*// conditional-operator
int main(){
    // 局部变量声明
    int x, y = 10;
    x = (y<10)?30:40;

    cout << "Value of x: " << x << endl;
}*/
int main(){
    // 局部变量声明
    char grade = 'A';
    switch(grade){
        case 'A':
            cout << "很棒！" << endl;
            break;
        case 'B':
        case 'C':
            cout << "做得好！" << endl;
            break;
        case 'D':
            cout << "您通过了" << endl;
            break;
        case 'F':
            cout << "最好再试一下" << endl;
            break;
        default:
            cout << "无效的成绩" << endl;
    }
    cout << "您的成绩" << grade << endl;
}
