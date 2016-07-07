#include <iostream>
using namespace std;

int main(){
    int i = 5;
    double d = 11.7;
    int &ri = i;
    int *pi;
    pi = &i;
    // int *pi = &i;

    double & rd = d;
    cout << i << endl;
    cout << ri << endl;
    cout << pi << endl;
    cout << d << endl;
    cout << rd << endl;
}
