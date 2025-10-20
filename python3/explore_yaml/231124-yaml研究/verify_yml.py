# coding=utf-8
# time: 2023/11/28 14:01
# file: -验证yaml嵌套.py
# author: wht
import os
import yaml
import os


# yaml文件嵌套yaml文件
class Loader(yaml.Loader):  # 继承
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        # print(self._root)
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        print(filename)
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include_', Loader.include)


def get_yml_data(file_path):
    with open(file_path,encoding='utf-8') as fo:
        # 非安全读入,如果想顺利实现引用，需要加载新的Loader对象
        return yaml.load(fo, Loader)
        # return yaml.load(fo.read(), Loader=yaml.FullLoader)

        # 安全读取单类型数据
        # return yaml.safe_load(fo.read())

        # 安全读取多类型数据
        # return yaml.safe_load_all(fo.read())


if __name__ == '__main__':
    # y1 = get_yml_data('./yamlData')
    # y1 = get_yml_data('./yamlData_反例')
    # y1 = get_yml_data('./yamlDataTuple')
    # print(y1)
    # print(next(y1))
    # print(next(y1))

    # data = [{"a": 123, "b": 234}, 8, 9, "中国"]
    # data2 = {"ooo":999,"xxxx":"yyy"}
    # with open("yamlDataWriteAll.yml", "w", encoding="utf-8") as f:
    # 单类型数据写成yml格式,allow_unicode避免中文乱码
    # yaml.safe_dump(data=data, stream=f, allow_unicode=True)

    # 多类型数据写成yml格式,documents=[,]或(,)都可以
    # yaml.safe_dump_all(documents=(data,data2), stream=f, allow_unicode=True)
    # yaml.dump_all(documents=[data, data2], stream=f, allow_unicode=True)

    # 嵌套
    # y3 = get_yml_data('./yamlQiantao.yml')
    # y3 = get_yml_data('./a.yml')
    # print(y3)
    # with  open('a.yml','r') as f:
    #     data = yaml.safe_load(f.read())
    #     print(data)


    ret=get_yml_data('./a.yml')
    print(ret,type(ret))
