# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：01_property学习.py
@Date    ：2024/4/12 9:30 
'''

flag = 11
if flag == 1:
    ...


    class Foo:
        def func(self):
            print('func')

        @property
        def prop1(self):
            print('getter...')
            return 'return prop1'

        @prop1.setter
        def prop1(self,value):
            print('setter...')


    foo_obj = Foo()
    # foo_obj.func()
    print(foo_obj.prop1)
    foo_obj.prop1 = '1000'
    print(foo_obj.prop1)

flag = 11
if flag == 1:
    ...


    class Good:
        @property
        def size(self):
            return 100


    obj = Good()
    print(obj.size)

flag = 11
if flag == 1:
    ...


    class Page(object):
        def __init__(self, current_page):
            self.current_page = current_page
            self.per_items = 10

        @property
        def start(self):
            val = (self.current_page - 1) * self.per_items
            return val

        @property
        def end(self):
            val = self.current_page * self.per_items
            return val


    p = Page(2)
    print(p.start)
    print(p.end)


flag = 11
if flag == 1:
    ...
    class Goods:
        '''新式类的property属性'''
        _money = 1000
        @property
        def price(self):

            return f'@property price {self._money}'

        @price.setter
        def price(self,value):
            print(f'@price.setter {value}')
            self._money += value

        @price.deleter
        def price(self):
            print('@price.deleter')
            self._money = 0

    g = Goods()
    g.price = 100
    print(g.price)

    del g.price
    print(g.price)


flag = 11
if flag == 1:
    ...
    class Goods(object):
        '三种@property装饰器'
        def __init__(self):
            self.origin_price = 100
            self.discount = 0.8
        @property
        def price(self):
            new_price = self.origin_price * self.discount
            return new_price

        @price.setter
        def price(self,value):
            self.origin_price = value

        @price.deleter
        def price(self):
            print('origin_price被删除掉了')
            del self.origin_price

    g = Goods()
    print(g.price)
    g.price = 200
    print(g.price)
    del g.price
    print(g.price)

flag = 11
if flag == 1:
    ...
    '类属性方式'
    class Foo:
        def get_bar(self):
            return 'laowang'

        BAR = property(get_bar)

    f = Foo()
    print(f.get_bar())
    print(f.BAR)
    print(f.BAR.__doc__)

flag = 11
if flag == 1:
    ...
    description = '''类属性方式:
    property方法中有个四个参数
    第一个参数是方法名，调用 对象.属性 时自动触发执行方法。
    第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法。
    第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法。
    第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息。
    '''

    class Foo(object):
        def get_bar(self):
            print("getter...")
            return 'laowang'

        def set_bar(self, value):
            """必须两个参数"""
            print("setter...")
            return 'set value' + value

        def del_bar(self):
            print("deleter...")
            return 'laowang'

        # BAR = property(get_bar, set_bar, del_bar, "description...")
        BAR = property(get_bar, set_bar, del_bar, description)

    f = Foo()
    print(f.BAR)
    f.BAR = 'alex'
    print(f.BAR)
    print(Foo.BAR.__doc__)
    del f.BAR
    print(f.BAR)


flag = 11
if flag == 1:
    ...


    class Goods(object):

        def __init__(self):
            # 原价
            self.original_price = 100
            # 折扣
            self.discount = 0.8

        def get_price(self):
            # 实际价格 = 原价 * 折扣
            try:
                new_price = self.original_price * self.discount
                return new_price
            except:
                return '没有价格属性了'

        def set_price(self, value):
            self.original_price = value

        def del_price(self):
            try:
                del self.original_price
            except:
                pass
            finally:
                print('价格属性已被删除了')

        PRICE = property(get_price, set_price, del_price, '价格属性描述...')


    obj = Goods()
    print(obj.PRICE)
    obj.PRICE = 1000
    print(obj.PRICE)
    del obj.PRICE
    del obj.PRICE
    print(obj.PRICE)


flag = 11
if flag == 1:
    ...

    class Goods(object):

        def __init__(self):
            # 原价
            self.original_price = 100
            # 折扣
            self.discount = 0.8

        def get_price(self):
            # 实际价格 = 原价 * 折扣
            try:
                new_price = self.original_price * self.discount
                return new_price
            except:
                return '没有价格属性了'

        def set_price(self, value=999):
            self.original_price = value

        def del_price(self):
            try:
                del self.original_price
            except:
                pass
            finally:
                print('价格属性已被删除了')

        PRICE = property(fget=get_price, fset=set_price, fdel=del_price, doc='价格属性描述...')

    g = Goods()
    print(g.PRICE)
    # g.PRICE = 1000
    # print(g.PRICE)

flag = 11
if flag == 1:
    ...

    class Foo:
        def func(self):
            print('func')

        # f1 = property(lambda self: print('f1...'))
        # 上下函数定义是等效的
        @property
        def f1(self):
            print('f1.../...')

        # f2 = property(lambda self,value: print(f'f1...,{value}'))
        f2 = property(lambda self: print('f1...'),lambda self,value: print(f'f1...,{value}'))

    f = Foo()
    f.f1
    f.f2 = 100

flag = 11
if flag == 1:
    ...


    class Person():

        def __init__(self, firstname, lastname):
            self.first = firstname
            self.last = lastname
            self.fullname = self.first + ' ' + self.last

        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)

    # 创建一个person对象
    person = Person('zhang', 'san')
    print(person.first)
    print(person.last)
    print(person.fullname)
    print(person.email())
    print('-'*40)
    person.last = 'si'
    print(person.first)
    print(person.last)
    print(person.fullname)
    print(person.email())


flag = 11
if flag == 1:
    ...


    # 将fullname属性，改为fullname()方法
    # 但是对于没有使用fullname()方法的旧代码，可以就没办法使用person.fullname的方式调用了
    # 所以这样更改后，要修改所有的旧代码
    class Person():
        def __init__(self, first_name, last_name):
            self.first = first_name
            self.last = last_name

        def fullname(self):
            return self.first + ' ' + self.last

        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)


    person = Person('zhang', 'san')
    print(person.fullname())
    print(person.email())
    print('-'*40)
    person.last = 'si'

    print(person.fullname())
    print(person.email())

flag = 1
if flag == 1:
    ...
    class Person():
        def __init__(self, first_name, last_name):
            self.first = first_name
            self.last = last_name
        @property
        def fullname(self):
            return self.first + ' ' + self.last

        def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)


    person = Person('zhang', 'san')
    print(person.fullname)
    print(person.email())
    print('-'*40)
    person.last = 'si'

    print(person.fullname)
    print(person.email())

