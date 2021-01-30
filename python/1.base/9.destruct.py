# python提供了类似ES6中的析构方式
a = [1, 2, 3, 4]
#原始取值
a1 = a[0]
a2 = a[1]
a3 = a[2]
a4 = a[3]
print(f'a1:{a1}, a2:{a2}, a3:{a3}, a4:{a4}')

# 析构方式
a1, a2, a3, a4 = a
print(f'a1:{a1}, a2:{a2}, a3:{a3}, a4:{a4}')

# 取部分值
a4 = None
a1, a2, a3 ,_ = a
print(f'a1:{a1}, a2:{a2}, a3:{a3}, a4:{a4}')

a2 = a3 = None
a1, *_, a4 = a
print(f'a1:{a1}, a2:{a2}, a3:{a3}, a4:{a4}')

# 字典也支持析构，只能对key进行析构