#include <iostream>

double division(int a, int b){
    if(b==0){
        throw "Division by zero condition!";
    }
    return (a/b);
}
int main(){
    int x = 50;
    int y = 0;
    double z;

    try{
        z = division(x, y);
        std::cout << z << std::endl;
    }catch(const char *msg){
        std::cerr << msg << std::endl;
    }
}
