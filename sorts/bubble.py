#!/usr/bin/python
#coding:utf-8
from __future__ import print_function

def bubble_sort(iterable):
    '''冒泡排序（英语：Bubble Sort）是一种典型的交换排序算法，也叫做升序排序
    参数：可迭代序列
    返回：升序排序后的可迭代序列
    原理：
     1. 比较相邻元素，若降序则交换它们，较小的数会向序列头部冒泡。
     2. 重复步骤1，冒泡直到结尾，此时第一轮冒泡结束，最大值元素沉到序列尾部。
     3. 除了尾部元素外，针对其余元素重复步骤2。
     4. 重复冒泡，每轮冒泡结束，靠近尾部元素逐渐呈现升序，无序元素越来越少，直到没有需要冒泡的元素。
    时间复杂度：最好Θ(n) 最坏Θ(n^2) 平均Θ(n^2)
    空间复杂度：Θ(1)
    稳定性： 稳定
    '''
    for i in range(len(iterable) - 1, 0, -1):
        bubbled = 0

        for j in range(i):
            if iterable[j] > iterable[j + 1]:
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
                bubbled = 1

        if not bubbled: break

    return iterable


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    print(bubble_sort([int(item) for item in user_input.split(',')]))
