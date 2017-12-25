# -*- coding=utf-8 -*-
# 因为python没有static将变量持久化, 只能使用闭包来制作计数器
def createCounter():
    def f():
        n = 0
        while True:
            n = n + 1
            yield n
    g = f() #注意这里,生成器g 声明在了counter函数的外面,g在内存中一直存在,但在createCounter()外面无法用g来访问
    def counter():
        return next(g)
    #或者将生成器f()换成list,目的都是将createCounter函数里面的局部变量持久化
    #l = [0]
    #def counter(): l[0] += 1 return l[0]
    #最后可以用python3新增的nonlocal 两list都不用
    # v = 0   def counter(): nonlocal v  v += 1 return v
    return counter
countA = createCounter()
print(countA(), countA())
