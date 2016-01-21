from time import time

start = time()
#def sequential_search(a_list, item):
#    for i in a_list:
#        if item == i:
#            return True
#    return False
#
#test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#print(sequential_search(test_list, 13))
#print(sequential_search(test_list, 3))

#def binary_search(a_list, item):
#    first = 0
#    last = len(a_list) - 1
#    found = False
#    while first <= last and not found:
#        midpoint = (first+ last) // 2
#        if a_list[midpoint] == item:
#            found = True
#        else:
#            if item < a_list[midpoint]:
#                last = midpoint - 1
#            else:
#                first = midpoint + 1
#    return found
#
#test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#print(binary_search(test_list, 3))
#print(binary_search(test_list, 13))

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    #put data in slot
    def put_data_in_slot(self, key, data, slot):
        if self.slots[slot] == None: # '==None' ? or 'is None' ?
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key: # not None
                self.data[slot] = data # replace
                return True
            else:
                return False

    def put(self, key, data):
        slot = self.hash_function(key, self.size)
        result = self.put_data_in_slot(key, data, slot)
        while not result:
            slot = self.rehash(slot, self.size)
            result = self.put_data_in_slot(key, data, slot)

    # reminder method
    def hash_function(self, key, size):
        return key % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
            return data
    
    def  __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

if __name__ == '__main__':
    table = HashTable()
    table[54] = 'cat'
    table[26] = 'dog'
    table[27] = 'lion'
    print table.slots
    print table.data
print time() - start

class DictDemo:
    def __init__(self, key, value):
        self.dict = {}
        self.dict[key] = value
    def __getitem__(self, key):
        return self.dict[key]
    def __setitem__(self, key, value):
        self.dict[key] = value
dictDemo = DictDemo('key0', 'value0')
print(dictDemo['key0'])
dictDemo['key1'] = 'value1'
print dictDemo['key1']
