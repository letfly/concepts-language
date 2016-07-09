#include <iostream>

class Books{
    public:
        char title[50];
        char author[50];
        char subject[100];
        int book_id;
};
// 该函数以结构指针作为参数
void printBook(struct Books *book){
    std::cout << "Book title : " << book->title << std::endl;
    std::cout << "Book author : " << book->author << std::endl;
}

int main(){
    Books Book1; //声明Box1，类型为Box
    Books Book2; //声明Box2，类型为Box

    // Book详述
    strcpy(Book1.title, "Learn C++ Programming");
    strcpy(Book1.author, "Chand Miyan");
    strcpy(Book1.subject, "C++ Programming");
    Book1.book_id = 6495407;

    // Book2详述
    strcpy(Book2.title, "Telecom Billing");
    strcpy(Book2.author, "Yakit Singha");
    strcpy(Book2.subject, "Telecom");
    Book2.book_id = 6495700;

    // 通过传Book1的地址来输出Book1信息
    printBook(&Book1);
    // 通过传Book2的地址来输出Book2信息
    printBook(&Book2);
}
