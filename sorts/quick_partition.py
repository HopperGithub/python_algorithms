#!/usr/bin/python
#coding:utf-8
from __future__ import print_function

def quick_partition_sort(iterable, start, end):
    '''快速排序 in-place 原地分割版本
    参数：可迭代序列，左边索引，右边索引
    返回：升序排序后的可迭代序列
    原理：
     1. 对序列选最后元素作为基准（pivot）。
     2. 从左到右循环，将序列中小于pivot排在前面，大于pivot排在后面，等于pivot排哪面都可以，这个过程为partition操作。
     3. 递归对pivot划分出的两个子序列partition操作，知道不需要再排序。
    时间复杂度：最好Θ(nlogn) 最坏Θ(n^2) 平均Θ(logn)
    空间复杂度：最好Θ(1) 最坏Θ(n) 平均Θ(logn)
    稳定性： 不稳定
    '''
    if start >= end:
        return
    i = start
    pivot = iterable[end]
    for j in range(start, end):
        if iterable[j] < pivot:
            i += 1
            iterable[i - 1], iterable[j] = iterable[j], iterable[i - 1]
    iterable[i], iterable[end] = iterable[end], iterable[i]
    quick_partition_sort(iterable, start, i - 1)
    quick_partition_sort(iterable, i + 1, end)

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(quick_partition_sort(unsorted, 0, len(unsorted) - 1))