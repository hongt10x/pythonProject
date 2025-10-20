# coding=utf-8
# time: 2024/1/12 9:50
# file: tYaml.py
# author: wht

import yaml
with open('./father.yml', encoding='utf8') as f:
    father_yaml = yaml.safe_load(f)
    print(father_yaml)


def include_yaml(yaml_):
    if isinstance(yaml_,dict):
        yaml_copy = yaml_.copy()
        # print(yaml_copy,type(yaml_copy))
        # print(yaml_,type(yaml_))
        if yaml_.get('type')=='include_yaml':
            with open(yaml_.get('file','r')) as f:
                child_yaml = yaml.safe_load(f)
            yaml_copy = child_yaml.copy()

        else:
            for k,v in yaml_.items():
                yaml_copy[k] = include_yaml(v)

    elif isinstance(yaml_, list):
        yaml_copy = [include_yaml(x) for x in yaml_.copy()]

    else:
        yaml_copy = yaml_

    return yaml_copy


print(include_yaml(father_yaml))

