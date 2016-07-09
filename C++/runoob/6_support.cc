#include <iostream>

extern int count;
void write_extern(){
    std::cout << "Count is " << count << std::endl;
}
