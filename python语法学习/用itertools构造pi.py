# -*- coding=utf-8 -*-
import itertools
# pi计算过程
# 产生奇数序列
# 按顺序除正负4: 4/1 -4/3 4/5
def pi(N):
    return sum(next(itertools.cycle([4, -4]))/x for x in
               itertools.takewhile(lambda x: x < 2*N, itertools.count(1, step=2)))
print(pi(100))
