# python默认缓存一部分整数值作为一种优化
# python使用引用计数法，当引用为零时删除变量所占的内存空间
a = 10
del a
print(a)
