#!/usr/bin/python
#coding:utf-8
from __future__ import print_function
from timeit import default_timer

'''
穷举法，从 2 遍历到 n / 2， 复杂度 O(n)
'''
def _is_prime0(n):
    if n < 2:
        return 0

    i = 2
    while i < n - 1:
        if n % i == 0:
            return 0
        i += 1
    return 1

'''
提示：一个数如果可以进行因数分解，那么分解时得到的两个数
一定是一个小于等于 sqrt(n)，一个大于等于 sqrt(n)，
据此，判断 n 是否素数不需要遍历到 n-1，遍历到 sqrt(n) 即可，
因为若 sqrt(n) 左侧找不到约数，那么右侧也一定找不到约数
复杂度 O(√n)
'''

def _is_prime1(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1

    squareRoot = 1
    i = 2

    while squareRoot * squareRoot < n:
        squareRoot += 1

    while i <= squareRoot:
        if n % i == 0:
            return 0
        i += 1
    return 1

'''
提示：优化1算法，关于素数分布有一个规律，
即大于等于5的质数一定和6的倍数相邻。
意味判断步长可以增大到6
复杂度 O(√n)，但比方法2快3倍左右
'''
def _is_prime(n):
    if n == 2 or n == 3:
        return 1
    if n % 6 != 1 and n % 6 != 5:
        return 0

    squareRoot = 3
    i = 5

    while squareRoot * squareRoot < n:
        squareRoot += 1

    while i <= squareRoot:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 1

'''
埃拉托斯特尼筛法是指，要得到自然数n以内的全部素数，
必须把不大于根号n的所有素数的倍数剔除，剩下的都是素数。
'''
def sieve_of_eratosthenes(n):
    nums = [1] * (n + 1)
    s = 2
    # 筛到sqrt(n)即可
    while s * s <= n:
        # 若未被剔除，说明是素数，此时要筛掉它的倍数
        if nums[s]:
            for i in range(s * 2, n + 1, s):
                nums[i] = 0
        s += 1
    # 将列表（以 0、1 标识的索引）转换成对应素数
    nums = [s for s in range(2, n) if nums[s]]
    return nums

def exec_time(func, data):
    start = default_timer()
    func(data)
    end = default_timer()

    return end - start

def test(length):
    test_iter = list(range(length))
    print('遍历长度：', length)
    for i,f in enumerate([_is_prime0, _is_prime1, _is_prime]):
        print('筛选素数方法', i, '耗时：', exec_time(lambda x: filter(f, x), test_iter), 's')

if __name__ == '__main__':
    test(50000)
    # print(sieve_of_eratosthenes(20))

