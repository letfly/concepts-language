#include <iostream>
using namespace std;

class Book{
    public:
        double get_cost(){
            return book_id*pop;
        }
        void set_book_id(int id){
            book_id = id;
        }
        void set_pop(int po){
            pop = po; // pop = pop;这种写法是错误的
        }
        // 重载＋运算符，用于把两个Box对象相加
        Book operator+(const Book &b){
            Book book;
            book.book_id = this->book_id + b.book_id;
            book.pop = this->pop + b.pop;
            return book;
        }
    private:
        int book_id;
        int pop;
};
int main(){
    Book book1;
    Book book2;
    Book book3;

    book1.set_book_id(6);
    book1.set_pop(10);
    book2.set_book_id(2);
    book2.set_pop(4);

    cout << book1.get_cost() << endl;

    book3 = book1+book2;
    cout << book3.get_cost() << endl;
}
