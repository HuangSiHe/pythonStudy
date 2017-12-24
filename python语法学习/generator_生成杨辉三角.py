# -*- coding=utf-8 -*-
def triangles():
    a = [1]
    first = 1
    while 1:
        yield a
        a.append(1)
        for i in range(1, len(a) - 1):
            second = a[i]
            a[i] = first + second
            first = second
n = 0
for v in triangles():
    print v
    n += 1
    if n == 6:
        break
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]

res = [v for v in triangles() if len(res) <= 6]
res = (v for v in triangles() if len(res) <= 6) #这是生成器形式list 可用res.next()或for循环遍历
