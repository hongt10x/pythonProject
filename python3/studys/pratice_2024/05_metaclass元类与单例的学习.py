# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：05_metaclass元类与单例的学习.py
@Date    ：2024/4/15 9:16 
'''
import time

flag = 11
if flag == 1:
    ...


    class BaseClass:
        def greeting(self):
            print('hello from baseclass')


    DerivedClass = type('DerivedClass', (BaseClass,), {
        'say_hi': lambda self: print('hi ,from derivedclass')
    })

    obj = DerivedClass()
    obj.greeting()
    obj.say_hi()

    # 用lambda创建一个函数
    say_hi2 = lambda x: print(f'hi ,from say_hi2 {x}')
    say_hi2('xxx')

flag = 11
if flag == 1:
    ...


    # 使用元类可以控制类的创建过程，其机制主要是通过重写元类的特殊方法__new__和__init__。在创建类时，__new__方法负责实际创建类对象，而__init__方法则负责初始化类对象。我们可以在元类中重写这些方法，从而在类创建过程中进行一些自定义操作，例如修改类的属性和方法
    class UpperMetaclass(type):
        # def __init__(cls,name,bases):
        #     print(cls.name)
        #     print(cls.bases)
        def __new__(cls, name, bases, dct: dict, *args, **kwargs):
            upppercase = {}
            for attr_name, attr_value in dct.items():
                if not attr_name.startswith('__'):
                    upppercase[attr_name.upper()] = attr_value
                else:
                    upppercase[attr_name] = attr_value
            return super().__new__(cls, name, bases, upppercase, *args, **kwargs)


    class MyClass(metaclass=UpperMetaclass):
        my_attr = 'hello'


    obj = MyClass()
    print(obj.MY_ATTR)

flag = 11
if flag == 1:
    ...


    # 通过类创建单例
    class SingleTon(type):
        _instance = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
            return cls._instance[cls]


    class MyClass(metaclass=SingleTon):
        pass


    a = MyClass()
    b = MyClass()
    print(id(a), id(b))

flag = 11
if flag == 1:
    ...
    '通过装饰器函数实现单例'


    def singleton(cls):
        _instance = {}

        # print(cls, _instance)
        def inner():
            if cls not in _instance:
                _instance[cls] = cls()
            for i, j in _instance.items():
                print(i, type(i))
                print(j, type(j))
            return _instance[cls]

        return inner


    @singleton
    class Cls(object):
        def __init__(self):
            pass


    c1 = Cls()
    c2 = Cls()
    c3 = Cls()
    c4 = Cls()
    print(id(c1), id(c2), id(c3), id(c4))

flag = 11
if flag == 1:
    ...
    '通过类装饰器实现单例'


    class Singleton(object):
        def __init__(self, cls):
            self._cls = cls
            self._instance = {}

        def __call__(self, *args, **kwargs):
            if self._cls not in self._instance:
                self._instance[self._cls] = self._cls()
            print(self._cls, self._instance)
            return self._instance[self._cls]


    @Singleton
    class Cls2:
        def __init__(self):
            print(self.__class__.__name__)


    c1 = Cls2()
    c2 = Cls2()
    print(id(c1), id(c2))

flag = 11
if flag == 1:
    ...
    '使用new关键字实现单例'


    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance


    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), id(s2), )

flag = 11
if flag == 1:
    ...
    'type类的创建'


    def f1(self):
        print('f1 ...')


    Klass = type('Klass', (), {'f1': f1})

    c = Klass()
    c.f1()

flag = 11
if flag == 1:
    ...


    class Singleton(type):
        _instance = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
            return cls._instance[cls]


    class Cls4(metaclass=Singleton):
        pass


    c1 = Cls4()
    c2 = Cls4()
    print(id(c1), id(c2))

flag = 11
if flag == 1:
    ...
    import threading
    from typing import Final, TypeVar, Generic

    T = TypeVar('T')


    class Singleton(Generic[T]):
        """
        类装饰器实现单例
        双重检查加锁保证了线程安全
        """

        _instance_lock = threading.Lock()
        uniqueInstance: Final[T]
        _cls: type[T]


    def __init__(self, cls: type[T]):
        self._cls = cls


    def __call__(self, *args, **kwargs) -> T:
        if not hasattr(self, 'uniqueInstance'):
            with self._instance_lock:
                if not hasattr(self, 'uniqueInstance'):
                    self.uniqueInstance = self._cls(*args, **kwargs)  # type: ignore
        return self.uniqueInstance

flag = 11
if flag == 1:
    ...
    from singleton import singlet

    c1 = singlet
    c2 = singlet
    print(id(c1), id(c2))

flag = 11
if flag == 1:
    ...
    import threading


    class Singleton:
        _instance_lock = threading.Lock()

        def __init__(self):
            time.sleep(1)

            # print(f'lock: {self._instance_lock}')

        def __new__(cls, *args, **kwargs):
            print(f'lock: {cls._instance_lock}')
            if not hasattr(cls, '_instance'):
                with cls._instance_lock:
                    if not hasattr(cls, '_instance'):
                        cls._instance = super().__new__(cls)
            return cls._instance


    b1 = Singleton()
    b2 = Singleton()

    print(b1)
    print(b2)
    print('-' * 40)


    def task(arg):
        obj = Singleton()
        print(obj)


    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

flag = 11
if flag == 1:
    ...
    from typing import TypeVar

    # AA = TypeVar('AA', int, str, list)
    AA = TypeVar('AA')
    n1: AA = 1
    n2: AA = '12SRT'

    print(n1)
    print(n2)
    n3: AA = ()
    print(n3)


flag = 11
if flag == 1:
    ...
    from typing import TypeVar


    class Animal:
        def speak(self):
            print('speak')
    class Animal2:
        def speak(self):
            print('speak')


    T = TypeVar('T', bound=(Animal,Animal2))


    def handle_animal(animal: T) -> None:
        print(animal,type(animal))
        animal.speak()

    a = Animal2()
    print(a,type(a))
    handle_animal(a)


flag = 11
if flag == 1:
    ...
    class MyMeta(type):
        def __new__(cls, name, bases, attrs):
            # name参数变成__name__对象属性，bases参数变成 __bases__ 对象属性，dict参数变成__dict__对象属性
            # 添加一个新的属性
            print(name)
            print(bases)
            print(attrs)
            attrs['version'] = 1.0
            # 创建类
            new_class = super().__new__(cls, name, bases, attrs)
            return new_class


    class MyClass(metaclass=MyMeta):
        pass
    # name参数变成__name__对象属性，bases参数变成 __bases__ 对象属性，dict参数变成__dict__对象属性
    # MyClass = type('MyMeta',(object,),{'version':2.0})
    # MyClass = type('MyClass',(),{'version':2.0})
    MyClass = type('MyClass',(MyMeta,),{'version':2.0})


    # 创建对象
    my_obj = MyClass()
    print(my_obj.version)


flag = 11
if flag == 1:
    ...
    class MyMetaclass(type):
        def __new__(cls, name, bases, attrs) -> type:
            # 此处给新创建的类赋予一些特殊属性或方法
            attrs = {'hello':'world'}
            def fly():
                print('i can fly...')
            attrs.update({'fly':fly()})
            return  super().__new__(cls, name, bases, attrs)

    class Mytest(metaclass=MyMetaclass):
        pass

    my = Mytest()
    print(my.hello)
    print(my.fly)
    # for _ in dir(my):
    #     if _.startswith('_'):
    #         continue
    #     print(_,type(_))
    #     print(my.__getattribute__())

flag = 11
if flag == 1:
    ...
    from singleton import Goods
    print(dir(Goods))

flag = 1
if flag == 1:
    ...
    '''命名：
    xx_ ：以单下划线结尾仅仅是为了区别该名称与关键词。
    _xx ：以单下划线开头，表示这是一个保护成员，只有类对象和子类对象自己能访问到这些变量。以单下划线开头的变量和函数被默认当作是内部函数，使用from module improt *时不会被获取，但是使用import module可以获取。
    __xx ：双下划线开头，表示为私有成员，只允许类本身访问，子类也不行。
    __xx__ ：双下划线开头，双下划线结尾。Python内部的名字，用来区别其他用户自定义的命名，以防冲突。Python不建议将自己命名的方法写为这种形式。
    '''
    class Good:
        __name = 'alex'
        def __f1(self):
            print('__f1__')

    g = Good()
    print(dir(g))
    # __xx ：双下划线开头，表示为私有成员，只允许类本身访问，子类也不行。
    # g.__f1()
    # print(g.__name)
    g._Good__f1()
    print(g._Good__name)
