# 格式化输出字符串有三种方式

# 第一种
a = 'str'
b = 'str2'
print('a is ' + a + ', b is ' + b)

# 第二种
a = 's1'
b = 's2'
print('a is %s, b is %s' % (a, b))

# 第三种, 推荐此种
a = 'fstr'
b = 'fstr2'
print(f'a is {a}, b is {b}')