#include <iostream>
using namespace std;

// 基类
class Book{
    protected:
        int book_id, pop;
    public:
        void set_book_id(int id){
            book_id = id;
        }
        void set_pop(int po){
            pop = po; // pop = pop;这种写法是错误的
        }
};
// 基类
class BookCost{
    public:
        int get_cost(int pop_book){
            return pop_book*70;
        }
};
// 派生类
class PopBook: public Book, public BookCost{
    public:
        int get_pop_book(){
            return book_id * pop;
        }
};
int main(){
    PopBook Pop;
    int pop_book;

    Pop.set_book_id(10);
    Pop.set_pop(200);

    pop_book = Pop.get_pop_book();

    // 输出对象的面积
    cout << pop_book << endl;

    // 输出总花费
    cout << Pop.get_cost(pop_book) << endl;
}
