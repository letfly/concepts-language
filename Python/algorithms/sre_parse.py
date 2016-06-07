# -*- coding: utf-8 -*-
# __author__ = 'letfly'


'''
import profile

def profile_test():
    total = 1
    for i in xrange(10):
        total = total * (i+1)
        print total
    return total

if __name__ == "__main__":
    profile.run("profile_test()")
'''
import re, profile

def splitWords(input_file):

    # 读入文件
    with open(input_file, 'r') as f:
        all_text = f.read()

    # 分割单词
    words = re.split('[^a-zA-Z]+', all_text)

    # 统计单词词频
    dic = {}
    for word in words:
        # if word in dic.keys():
            # dic[word] += 1
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
        # dic[word] = dic.get(word, 0)+1

    result = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)

    # 排序
    print result

if __name__ == '__main__':
    profile.run("splitWords('input.txt')")
