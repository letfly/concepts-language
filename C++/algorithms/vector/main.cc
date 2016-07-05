#include<iostream>
using namespace std;

#include "rand.h" //随机数
#include "vector.h"
#include "vector_constructor_by_copying.h"
#include "vector_find.h"
#include "vector_insert.h"

int test_id = 0; //测试编号

/******************************
 * 测试：无序向量的（顺序）查找
 *****************************/
template <typename T> //元素类型
void TestFind(Vector<T> & V, int n) {
    for (int i=0; i<V.size();i++){//依次查找向量中元素，当然成功
        cout << V.size()<< "aaa" << endl;
        T e = V[i];
        Rank r = V.find(e);
        if(r < 0) printf(":not found until rank V[%d] <> %d", r, e);
        else printf(":found at rank V[%d] = %d", r, V[r]);
        printf("\n");
    }
    for (int i=0; i<=V.size(); i++){//依次查找每对相邻元素的均值，可能成功
        T a = (0<i) ? V[i-1]: -INT_MAX/2;
        T b = (i<V.size()) ? V[i]:INT_MAX/2;
        T e = (a+b)/2;
        cout << a << b << e << "ddd" << endl;
        Rank r = V.find(e);
        if(r<0) printf(":not found until rank V[%d] <> %d", r, e);
        else printf(":found at rank V[%d]=%d", r, V[r]);
        printf("\n");
    }
}
/***********
 * 测试向量
 ***********/
template <typename T> //元素类型
void TestVector(int testSize){
    printf("\n ==== Test %2d. Generate a random vector\n", test_id++);
    Vector<T> V;
    for (int i=0;i<testSize;i++)V.insert(dice(i+1), dice((T)testSize *3));//在[0, 3n)中选择n个数，随机插入向量
    TestFind<T> (V, testSize);
}
/****************
 * 测试向量
 ***************/
int main(int argc, char* argv[]){
    if(2>argc){printf("Usage:%s <size of test>\a\a\n", argv[0]);return 1;}
    TestVector<int>(atoi(argv[1]));//元素类型可以在这里任意选择
    return 0;
}
