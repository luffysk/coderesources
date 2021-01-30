# 每种语言都会拥有一些内置的数据类型，比如java中的八大基本类型：byte、char、short、int、double、float、long、boolean
# python中也规定了一些数据类型，使用内置关键字type可以查看变量对应的类型

# int
a = 100
print(type(a))

# float
a = 100.0
print(type(a))
# 对于单精度和双精度统一使用float表示
a = 100.00
print(type(a))

# str字符串
a = '100'
print(type(a))
# 字符串使用单引号和双引号的类型一样
a = "100"
print(type(a))

# list数组类型
a = [100]
print(type(a))

# dict字典类型，表示键值对的映射关系
a= {'key': 100}
print(type(a))

# tuple元组类型
a = ()
print(type(a))

# bool布尔类型
a = True
print(type(a))

'''
通过上面可以发现python总共有七种数据类型：int、str、float、list、dict、tuple、bool
'''