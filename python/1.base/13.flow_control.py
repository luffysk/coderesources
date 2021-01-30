# 三个经典的流程控制块：顺序、选择、循环

# 顺序，从上到下依次执行
a = 10
b = 20
print(a + b)

# 选择， if，else， elif
if a == 10 and b == 10:
  print(a)
  print(b)
elif b == 20:
  print(b)
else:
  print('None')

# 循环， for， while
for num in range(6):
  print(num)
while a > 0:
  print(a)
  a = a - 1