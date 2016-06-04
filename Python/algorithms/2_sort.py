'''
def short_bubble_sort(a_list):
    pass_num = len(a_list) - 1
    exchanges = True
    while pass_num and exchanges:
        exchanges = False
        for i in xrange(pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
                exchanges = True
        pass_num -= 1
        print pass_num

if __name__ == '__main__':
    a_list = [20, 40, 30, 90, 50, 80, 70, 60]
    short_bubble_sort(a_list)
    print(a_list)
'''
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    print first, last
    if first < last:
        split_point = partition(a_list, first, last)
        print split_point
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)
