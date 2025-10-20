# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : 20250911-study.py
@Time    : 2025/9/11 16:26
@Author  : Echo Wang
'''

# read yaml


'''
import yaml
def read_yml_1(filename):
    with open(filename, encoding="utf-8") as f:
        text = yaml.load_all(f, Loader=yaml.SafeLoader)
        # for one in text:
        #     print(one)
        print(type(text))
        return text
        # return yaml.load_all(f, Loader=yaml.FullLoader)
        # return yaml.full_load_all(f)


data = read_yml_1("20250911-yaml.yml")

print(type(data),data, list(data))


'''


import yaml

#
# def read_yml(filename):
#     with open(filename, encoding="utf-8") as f:
#         return yaml.load_all(f, Loader=yaml.SafeLoader)
#
#
# try:
#     content = read_yml("20250911-yaml.yml")
#     next(content)
# except Exception as e:
#     print(f"error: {e}")

# def read_yml_2(filename):
#     with open(filename, "r", encoding="utf-8") as f:
#         return yaml.safe_load(f)
#
#
# content = read_yml_2("20250911-yaml.yml")
# print(content)


'''
import yaml


def read_yml(filename):
    """读取 YAML 文件并返回生成器（支持多文档）"""
    try:
        with open(filename, encoding="utf-8") as f:
            # return yaml.load_all(f, Loader=yaml.SafeLoader)  # 使用 SafeLoader 更安全
            return list(
                yaml.safe_load_all(f))  # 使用 SafeLoader 更安全  //读取文本为生成器时，会因为延迟而导致生成器读取数据失败
    except FileNotFoundError:
        raise FileNotFoundError(f"文件 '{filename}' 不存在")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"YAML 解析错误: {e}")


try:
    content = read_yml("20250911-yaml.yml")
    print(type(content), content)
    docs = list(content)  # 转换为列表，方便随机访问
    if len(docs) >= 2:
        print("第一个文档:", docs[0])
        print("第二个文档:", docs[1])
        print("第三个文档:", docs[2])
    else:
        print(f"警告: YAML 文件仅包含 {len(docs)} 个文档")
except FileNotFoundError as e:
    print(f"文件错误: {e}")
except yaml.YAMLError as e:
    print(f"YAML 格式错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")


'''

import yaml
def read_yml_4(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()  # 如果一次性将文件读取所有内容，将不会产生IO报错
    return yaml.safe_load_all(text)


data = read_yml_4("20250911-yaml.yml")

print(type(data),data)
for i in data:
    print(i)
