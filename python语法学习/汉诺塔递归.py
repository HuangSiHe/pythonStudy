# -*- coding=utf-8 -*-
# 共n层 从 a 移动到 c
def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n-1, a, c, b)
        print(a, '->', c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C')
# ('A', '->', 'C')
# ('A', '->', 'B')
# ('C', '->', 'B')
# ('A', '->', 'C')
# ('B', '->', 'A')
# ('B', '->', 'C')
# ('A', '->', 'C')
