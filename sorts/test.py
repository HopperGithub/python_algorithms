#!/usr/bin/python
#coding:utf-8
from __future__ import print_function
from timeit import default_timer
from random import shuffle

from bubble import bubble_sort
from cocktail import cocktail_sort

def exec_time(func, data):
    start = default_timer()
    func(data)
    end = default_timer()

    return end - start

def test(length):
    test_iter = list(range(length))
    shuffle(test_iter)
    test_dict = {'sort_0_bubble': bubble_sort, 'sort_1_cocktail': cocktail_sort}
    # print('遍历数列：', test_iter)
    print('遍历长度：', length)
    for i,f in test_dict.items():
        print('排序方法 ', i, ' 耗时：', exec_time(f, test_iter), 's')


if __name__ == '__main__':
    test(5000)
