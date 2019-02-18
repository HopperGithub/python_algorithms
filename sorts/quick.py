#!/usr/bin/python
#coding:utf-8
from __future__ import print_function

def quick_sort(iterable):
    '''快速排序（英语：Quick Sort）是冒泡排序的改进，也是二叉查找树的一个空间最优版本。
    使用分治法策略将一个序列分为2个子序列，递归排序。主要竞争对手有堆排序、归并排序
    参数：可迭代序列
    返回：升序排序后的可迭代序列
    原理：
     1. 对序列选一个元素作为基准（pivot）。
     2. 将序列中小于pivot排在前面，大于pivot排在后面，等于pivot排哪面都可以，这个过程为partition操作。
     3. 递归对pivot划分出的两个子序列partition操作，知道不需要再排序。
    时间复杂度：最好Θ(nlogn) 最坏Θ(n^2) 平均Θ(nlogn)
    空间复杂度：最好Θ(1) 最坏Θ(n) 平均Θ(logn)
    稳定性： 不稳定
    '''
    if len(iterable) <= 1:
        return iterable
    pivot = iterable[0]
    smaller = [n for n in iterable[1:] if x < pivot]
    larger = [n for n in iterable[1:] if x < pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    print(quick_sort([int(item) for item in user_input.split(',')]))