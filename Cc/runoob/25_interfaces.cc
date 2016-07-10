#include <iostream>

// 基类
class Book{
    protected:
        int book_id, pop;
    public:
        // 提供接口框架的纯虚函数
        virtual int get_cost() = 0;
        void set_book_id(int b){
            book_id = b;
        }
        void set_pop(int p){
            pop = p;
        }
};

// 派生类
class MathBook: public Book{
    public:
        int get_cost(){
            return book_id * pop;
        }
};
class ProgBook: public Book{
    public:
        int get_cost(){
            return book_id * pop;
        }
};
int main(){
    MathBook Math;
    ProgBook Prog;

    Math.set_book_id(10);
    Math.set_pop(20);
    // 输出花费
    std::cout << "Total cost" << Math.get_cost() << std::endl;

    Prog.set_book_id(100);
    Prog.set_pop(200);
    // 输出花费
    std::cout << Prog.get_cost() << std::endl;
}
