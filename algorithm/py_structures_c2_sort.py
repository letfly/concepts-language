#def short_bubble_sort(a_list):
#    exchanges = True
#    pass_num = len(a_list) - 1
#    while pass_num > 0 and exchanges:
#        exchanges = False
#        for i in range(pass_num):
#            if a_list[i] > a_list[i + 1]:
#                exchanges = True
#                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
#        pass_num = pass_num - 1
#
#if __name__ == '__main__':
#    a_list = [20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
#    short_bubble_sort(a_list)
#    print(a_list)


#def selection_sort(a_list):
#    for fill_slot in range(len(a_list) - 1, 0, -1):
#        pos_of_max = 0
#        for location in range(1, fill_slot + 1):
#            if a_list[location] > a_list[pos_of_max]:
#                pos_of_max = location
#        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
#
#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#selection_sort(a_list)
#print(a_list)

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low = 0
        high = index - 1
        while low<= high:
            mid = (low+high)/2
            if a_list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
insertion_sort_binarysearch(a_list)
print(a_list)
