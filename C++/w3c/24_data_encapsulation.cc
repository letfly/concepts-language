#include <iostream>

class Adder{
    public:
        // 构造函数
        Adder(int i = 0){
            total = i;
        }
        // 对外的接口
        void add_num(int number){
            total += number;
        }
        // 对外的接口
        int get_total(){
            return total;
        }
    private:
        // 对外隐藏的数据
        int total;
};
int main(){
    Adder a;

    a.add_num(10);
    a.add_num(20);
    a.add_num(30);

    std::cout << "total" << a.get_total() << std::endl;
}
