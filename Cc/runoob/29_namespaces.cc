#include <iostream>

/*// 定义命名空间
// 第一个命名空间
namespace first_space{
    void func(){
        std::cout << "Inside first_space" << std::endl;
    }
}
// 第二个命名空间
namespace second_space{
    void func(){
        std::cout << "second_space" << std::endl;
    }
}
int main(){
    // 调用第一个命名空间中的函数
    // 您可以通过使用 :: 运算符来访问命名空间中的成员
    first_space::func();

    // 调用第二个
    second_space::func();
}*/
// using 指令
using std::cout;

int main(){
    cout << "std::endl is used with std!" << std::endl;
}
