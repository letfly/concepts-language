#include <iostream>

using namespace std;

class Book{
    protected:
        int book_id, pop;
    public:
        Book(int a=0, int b=0){
            book_id = a; pop = b;
        }
        virtual void cost(){
            cout << "Parent class cost :" << endl;
        }
};
class MathBook: public Book{
    public:
        MathBook(int a=0, int b=0):Book(a, b){}
        void cost(){
            cout << "MathBook class cost :" << endl;
        }
};
class ProgBook: public Book{
    public:
        ProgBook(int a=0, int b=0):Book(a, b){}
        void cost(){
            cout << "ProgBook class cost :" << endl;
        }
};
int main(){
    Book *book;
    MathBook mat(10,7);
    ProgBook pro(10,5);

    // 存储数学的地址
    book = &mat;
    // 调用数学的求成本函数
    book->cost();

    book = &pro;
    book->cost();
}
