# 对于两个具有特定的数据类型变量，只允许进行指定的操作

# int, 加减乘除等，对于数字的常规操作都支持
a = 10
b = 20
print(a + b)

# float， 和int类似
a = 100.00
b = 100.00
print(a + b)

# str, 允许+和*, 其中*表示将字符串重复指定次数
a = 'stra '
b = 'strb '
print(a + b)
a = a * 10
print(a)

# list, 下标从0开始, 支持嵌套， 即多维数组
a =[1, 2, 3]
print(a[0])

# dict, 通过key找value, 不使用索引的方式
a = {'k1': 'v1'}
print(a['k1'])

# tuple，和list一样，唯一的区别为元组不可以修改元素
a = (1, 2, 3)
print(a[0])

#bool, 每种数据类型中都有此类型的值，int：0，str：''，float：0.0，list:[],dict:{}, tuple:(),对应的值都为False
a = True
b = False