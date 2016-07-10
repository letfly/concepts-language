#include <iostream>

class Book{
    public:
        Book(){
            std::cout << "调用构造函数！" << std::endl;
        }
        ~Book(){
            std::cout << "～调用析构函数！" << std::endl;
        }
};
int main(){
    Book *my_book = new Book[4];

    delete [] my_book; // delete Book
}
