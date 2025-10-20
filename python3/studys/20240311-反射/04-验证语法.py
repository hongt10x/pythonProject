# coding: utf8
# 04-验证语法.py
# 2024/3/22

# !r仅在format语法中使用，可以将变量的所有符号保留下来

a = 'alex'
age= 33
print('{!r}，你好，你的年龄是{!r}岁。'.format(a,age))
print(f'{a}')
print(F'{a}')


b = [1,3,5]
print(b[::-1])