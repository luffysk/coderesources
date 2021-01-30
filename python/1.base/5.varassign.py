# 变量支持链式赋值
a = b = c = 100
print(a)
print(b)
print(c)


# 交叉赋值
a = 10
b = 20
a, b = b, a
print(a)
print(b)