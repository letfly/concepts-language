#pragma once

typedef int Rank; //秩
#define DEFAULT_CAPACITY 3 //默认初始容量（实际应用中可设置为更大）
template <typename T> class Vector { //向量模板类
private:
    Rank _size; int _capacity; T* _elem; //规模、容量、数据区
protected:
    void copyFrom(T const* A, Rank lo, Rank hi); //复制数组区间A[lo, hi)
public:
// 构造函数
    Vector(int c = DEFAULT_CAPACITY, int s = 0, T v = 0) //容量为c、规模为s、所有元素初始为v
    { _elem = new T[_capacity = c]; for (_size=0; _size<s; _elem[_size++] = v); } //默认
    Vector(T const* A, Rank n) {copyFrom(A, 0, n);} //数组整体复制
    Vector(T const* A, Rank lo, Rank hi){copyFrom(A,lo,hi);} //数组区间复制
    Vector(Vector<T> const& V, Rank lo, Rank hi){copyFrom(V._elem, lo, hi);} //向量区间复制
    Vector(Vector<T> const& V){copyFrom(V._elem, 0, V._size);} //向量整体复制
    Rank insert(Rank r, T const& e); //插入元素
// 析构函数
    ~Vector() { delete [] _elem; } //释放内部空间
// 只读访问接口
    Rank size() const { return _size; } //规模
    Rank find(T const& e) const{return find(e, 0, _size);} //无序向量整体查找
    Rank find(T const& e, Rank lo, Rank hi) const; //无序向量区间查找
// 可写访问接口
    T& operator[] ( Rank r ) const; //重载下标操作符，可以类似于数组形式引用各元素
    Vector<T> & operator= ( Vector<T> const& ); //重载赋值操作符，以便直接克隆向量
};
template <typename T> T& Vector<T>::operator[] (Rank r) const //重载下标操作符
{ return _elem[r]; } // assert: 0 <= r < _size
template <typename T> Vector<T>& Vector<T>::operator= ( Vector<T> const& V ) { //重载
   if ( _elem ) delete [] _elem; //释放原有内容
   copyFrom ( V._elem, 0, V.size() ); //整体复制
   return *this; //返回当前对象的引用，以便链式赋值
}
