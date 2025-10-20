# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 01-将方法该给属性的property.py
@Time    : 2025/1/20 9:12
@Author  : Echo Wang
'''


#
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def fullname(self):
#         return self.first_name + ' ' + self.last_name
#
#     @fullname.setter
#     def fullname(self,name:str):
#         self.first_name = name.split()[0]
#         self.last_name = name.split()[1]
#         return self.first_name + ' ' + self.last_name
#
#     @fullname.deleter
#     def fullname(self):
#         self.first_name = None
#         self.last_name = None
#
#     def email(self):
#         return '{}.{}@email.com'.format(self.first_name, self.last_name)
#
#
# p1 = Person("张", "三")
# # print(p1.fullname())
# print(p1.fullname)
# print(p1.email())
#
# p1.fullname = "li si"
#
# print(p1.fullname)
# print(p1.email())
#
# del p1.fullname
# print(p1.first_name)
# print(p1.last_name)
# print(p1.email())


'''
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname1(self):
        return self.first_name + ' ' + self.last_name

    # @property  //随意更改property的位置会引起脚本混乱
    def fullname2(self, name: str):
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        return self.first_name + ' ' + self.last_name

    @property
    def fullname(self):
        self.first_name = None
        self.last_name = None

    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)


p2 = Person("刘", "能")
print(p2.fullname)


'''

#
# class Pager:
#     def __init__(self, current_page):
#         # 用户当前请求的页码（第一页、第二页...）
#         self.current_page = current_page
#         # 每页默认显示10条数据
#         self.per_items = 10
#
#     @property
#     def start(self):
#         val = (self.current_page - 1) * self.per_items
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
#
# p = Pager(2)
# print(p.start)
# print(p.end)
#

#
class Goods:
    '''@property 定义 getter，@price.setter 定义 setter，@price.deleter 定义 deleter。
    装饰器	作用	典型用法
    @property	定义属性的 getter	将方法转为只读属性
    @xxx.setter	定义属性的 setter	数据验证、修改逻辑
    @xxx.deleter	定义属性的 deleter	控制属性删除行为
    @property.getter	重新定义 getter	继承中覆盖父类属性行为'''

    @property
    def price(self):
        print('@price.getter...')

    @price.setter
    def price(self, value):
        print('@price.setter...',value)

    @price.deleter
    def price(self):
        print('@price.deleter')
g = Goods()
g.price
g.price = 100
del g.price
# g.price


# class Foo(object):
#     def get_bar(self):
#         print("getter...")
#         return 'laowang'
#
#     # def set_bar1(self, value):
#     #     """必须两个参数"""
#     #     print("setter...")
#     #     return 'set value' + value
#     def set_bar(self):
#         """必须两个参数; 如果不传参使用property()会报错"""
#         print("setter...")
#         return 'set value'
#
#     def del_bar(self):
#         print("deleter...")
#         return 'laowang'
#
#     BAR = property(del_bar, None,get_bar , "description...")
#
# obj = Foo()
# # 自动调用第一个参数中定义的方法：get_bar
# obj.BAR  # getter...
# # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
# # obj.BAR = "alex"  # setter...
# # 自动获取第四个参数中设置的值：description...
# desc = Foo.BAR.__doc__
# print(desc)  # description...
# # 自动调用第三个参数中定义的方法：del_bar方法
# del obj.BAR  # deleter...



# class Pe:
#     __slots__ = ("name",)
#     def __init__(self,name):
#         self.name = name
#
#
# p = Pe("王五")
# print(p.name)
# p.age = 100
# print(p.age)

