#!/usr/local/python/bin/python3
# -*- coding: utf-8 -*-

from jinja2 import Template, Environment, FileSystemLoader

# ■if文サンプル
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample2.tpl')

data = {'x': 0}
disp_text = template.render(data)
print(disp_text)

data = {'x': 1}
disp_text = template.render(data)
print(disp_text)

data = {'x': -1}
disp_text = template.render(data)
print(disp_text)

# ■for文サンプル
data = {'x': 0, 'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
【実行結果】


xは0です



商品一覧



xは0より大きいです



商品一覧



xは0より小さいです



商品一覧



xは0です



商品一覧

・ みかん

・ りんご

・ バナナ
"""

# 【参考】
# http://www.python.ambitious-engineer.com/archives/760
