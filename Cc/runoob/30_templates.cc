#include <iostream>

/*// 函数模板
using std::cout;
using std::endl;
using std::string;

template <typename T>
T Max (T  a, T  b){
    return a < b ? b:a;
}
int main (){
    int i = 39;
    int j = 20;
    cout << "Max(i, j): " << Max(i, j) << endl;

    double f1 = 13.5;
    double f2 = 20.7;
    cout << "Max(f1, f2): " << Max(f1, f2) << endl;

    string s1 = "Hello";
    string s2 = "World";
    cout << "Max(s1, s2): " << Max(s1, s2) << endl;

    return 0;
}*/
// 类模板
#include <vector>
#include <cstdlib>
#include <stdexcept>

using std::cout;
using std::endl;
using std::cerr;
using std::exception;
using std::string;
using std::out_of_range;

template <class T>
class Stack {
private:
    vector<T> elems;     // 元素

public: 
    void push(T const&);  // 入栈
    void pop();               // 出栈
    T top() const; // 返回栈顶元素
    bool empty() const{       // 如果为空则返回真。
        cout << "ddd" << endl;
        return elems.empty();
    }
};

template <class T>
void Stack<T>::push (T const& elem){
    // 追加传入元素的副本
    elems.push_back(elem);
}

template <class T>
void Stack<T>::pop(){
    if (elems.empty()){
        throw out_of_range("Stack<>::pop(): empty stack");
    }
    // 删除最后一个元素
    elems.pop_back();
}

template <class T>
T Stack<T>::top()const{
    if (elems.empty()){
        throw out_of_range("Stack<>::top(): empty stack");
    }
    // 返回最后一个元素的副本
    return elems.back();
}

int main(){
    try{
        Stack<int> int_stack;  // int 类型的栈
        Stack<string> string_stack;    // string 类型的栈

        // 操作 int 类型的栈
        int_stack.push(7);
        int_stack.push(3);
        cout << int_stack.top() <<endl;

        // 操作 string 类型的栈
        string_stack.push("hello");
        cout << string_stack.top() << std::endl;
        string_stack.pop();
        string_stack.pop();
    }
    catch (exception const& ex){
        cerr << "Exception: " << ex.what() <<endl;
        return -1;
    }
}
