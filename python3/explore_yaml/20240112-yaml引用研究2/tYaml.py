# coding=utf-8
# time: 2024/1/12 10:04
# file: tYaml.py
# author: wht

import os.path
import yaml
import sys


# print(os.path.abspath(__file__))
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("BASEDIR:", BASEDIR)


class Loader(yaml.Loader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        print("-->",self._root)
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as fr:
            return yaml.load(fr, Loader)


Loader.add_constructor('!include', Loader.include)


def load_yaml(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as fr:
            dict_obj = yaml.load(fr, Loader=Loader)
            # dict_obj = yaml.safe_load(fr)
        return dict_obj
    else:
        raise FileNotFoundError('Not found yaml file {}'.format(filename))


if __name__ == '__main__':
    yaml_dict = load_yaml('b.yml')
    print(yaml_dict)
