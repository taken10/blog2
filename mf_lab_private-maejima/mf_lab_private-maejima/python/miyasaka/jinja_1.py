#!/usr/local/python/bin/python3
# -*- coding: utf-8 -*-

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample1.tpl')

data = {'name1': 'Kanehira', 'lang1': 'PHP',
        'name2': 'Kato', 'lang2': 'VBA'}
disp_text = template.render(data) # 辞書で指定する
print(disp_text)

"""
【実行結果】
①NAME=Kanehira LANG=PHP
②NAME=Kato LANG=VBA
"""

# 【参考】
# http://www.python.ambitious-engineer.com/archives/760
