#include <iostream>
using namespace std;

/*
// 字符常量
int main(){
    cout << "Hello\tWorld\n";
}*/
/*
// define预处理器
#define LENGTH 10
#define WIDTH 5
#define NEWL '\n'

int main(){
    int area;
    area = LENGTH*WIDTH;
    cout << area;
    cout << NEWL;
}*/
int main(){
    const int LENGTH = 10;
    const int WIDTH = 5;
    const char NEWL = '\n';
    int area;
    LENGTH = 10;

    area = LENGTH * WIDTH;
    cout << area;
    cout << NEWL;
}
