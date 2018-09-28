#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys


def main():
    data = {'employee_info': [
        {'employee_no': '1', 'name': '佐藤 一郎', 'age': '42'},
        {'employee_no': '2', 'name': '田中 二郎', 'age': '33'},
        {'employee_no': '3', 'name': '鈴木 三郎', 'age': '56'},
        {'employee_no': '4', 'name': '伊藤 四郎', 'age': '29'},
        {'employee_no': '5', 'name': '高橋 五郎', 'age': '77'}
    ]}

    # dict型でデータを作成する
    print(type(data))

    # json.dumps()でJSONに適した文字列に変換する
    encoded_data = json.dumps(data)
    print(type(encoded_data))
    print(encoded_data)

    # 単純に変換すると見にくいので、indentを指定して見やすくする
    encoded_data2 = json.dumps(data, indent=4)
    print(encoded_data2)
    # dict型ではなくなっているので、key指定で取り出すことはできない
    # print(encoded_data2['employee_info'][1]['name'])

    # JSONデータをdict型に変換する
    decoded_data = json.loads(encoded_data)
    print(type(decoded_data))
    print(decoded_data)
    # dict型なのでkeyやインデックスで取得が可能
    print(decoded_data['employee_info'][1]['name'])

    return 0


# if main
if __name__ == "__main__":
    sys.exit(main())
