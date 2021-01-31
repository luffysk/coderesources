# 给定年龄，用户可以猜三次年龄
# 年龄猜对，让用户选择两次奖励
# 用户选择两次奖励后可以退出
default = 20
count = 1
while count <= 3:
  age = int(input(f'第{count}次输入年龄：'))
  if(age < default):
    print(f'第{count}次猜小了')
    count = count + 1
  elif(age > default):
    print(f'第{count}次猜大了')
    count = count + 1
  else:
    print(f'第{count}次猜对了，请选择奖励')
    count = 3
    choose = 0
    map = {1:'奖励1', 2:'奖励2', 3:'奖励3'}
    while(choose < 2):
      print(map)
      check1 = int(input('第一次输入编号：'))
      check2 = int(input('第二次输入编号：'))
      print(f'选取了：{map[check1]} 和 {map[check2]}')
      break
