template <typename T> //将e作为秩为r元素插入
Rank Vector<T>::insert (Rank r, T const& e){ //assert: 0 <= r <= size
    for (int i = _size; i > r; i--) _elem[i] = _elem[i-1]; //自后向前，后继元素顺次后移一个单元
    _elem[r] = e; _size++; //置入新元素并更新容量
    return r; //返回秩
}
