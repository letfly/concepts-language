#include <iostream>
using namespace std;

/*// C 风格字符串
int main(){
    char greeting[6] = {'H', 'e', 'l', 'l', 'o'};

    cout << "Greeing message" << greeting << endl;
}*/
/*// 使用字符串函数库
int main(){
    char str1[10] = "Hello";
    char str2[10] = "World";
    char str3[10];
    int len;

    // 复制str1到str3
    strcpy(str3, str1);
    cout << "复制str1到str3 " << str3 << endl;
    // 连接str1和str2
    strcat(str1, str2);
    cout << "连接str1和str2 " << str1 << endl;
    // 连接后，str1的总长度
    len = strlen(str1);
    cout << "strlen(str1): " << len << endl;
}*/
// C++ 中的 String 类
int main(){
    string str1 = "Hello";
    string str2 = "World";
    string str3;
    int len;

    // 复制str1到str3
    str3 = str1;
    cout << "复制str1到str3 " << str3 << endl;
    // 连接str1和str2
    str1 = str1 + str2;
    cout << "连接str1和str2 " << str1 << endl;
    // 连接后，str1的总长度
    len = str1.size();
    cout << "连接后，str1的总长度 " << len << endl;
}
