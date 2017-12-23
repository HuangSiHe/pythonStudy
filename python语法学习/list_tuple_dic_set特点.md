`list tuple dic set`一些易错易混点
===

`tuple`: 初始化后无法改变
---
+ 声明长度是1的tuple
```Python
t = (0) #错误,和数学中的小括号歧义了
t = (0,) #正确
```

+ tuple中的元素'可变'
```python 
t = (0, [0, 1])
t[1][0] = 2 #修改成功,tuple仅仅是保持指针一直指向里面的list 里面的list属性可以变
```

`list`:类似于数组,可以存不同类型的元素
---
```python
l = [1, 2, 3]
l.append(4) # l[4] = 4会下标越界
l.pop(0)
```
`dic`: 就是hashMap
---
```python
d = {'one': 1, 'two': 2}
d['three'] = 3 # 注意是方括号
print(d['three']) # 若three不存在会报错
print(d.get['three'])
d.pop('three')
```

`set`:去除重复的list
---
```python
s = set([31, 1, 2, 2 ,3])
s.add(3) # 唯一一个需要用add增加元素的
s.remove(3) # 唯一一个不用pop删除元素的类型
```
