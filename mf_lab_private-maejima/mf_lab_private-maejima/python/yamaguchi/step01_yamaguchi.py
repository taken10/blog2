#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
from decimal import Decimal, ROUND_HALF_UP

# 引数受け取り
args = sys.argv
# 引数は2つを指定（ファイル名も引数として受け取る為、3つ）
if len(args)-1 != 2:
    print("エラー: 指定された引数は{cnt}つです。 引数は2つ指定してください。".format(cnt=len(args)-1), file=sys.stderr)
    sys.exit(1)

# 引数は数値のみ
if re.match("^-?\d+\Z", args[1]) is None:
    print("エラー: 指定された引数は数値ではありません。 引数は数値を指定してください。", file=sys.stderr)
    sys.exit(1)
if re.match("^-?\d+\Z", args[2]) is None:
    print("エラー: 指定された引数は数値ではありません。 引数は数値を指定してください。", file=sys.stderr)
    sys.exit(1)

# 引数をint型に変換
arg_1 = int(args[1])
arg_2 = int(args[2])


def main():
    # 足し算
    result_sum = arg_1 + arg_2
    print("足し算: {val}".format(val=str(result_sum)))
    # 引き算
    if arg_1 >= arg_2:
        result_diff = arg_1 - arg_2
    else:
        result_diff = arg_2 - arg_1
    print("引き算: {val}".format(val=str(result_diff)))
    # 掛け算
    result_prod = arg_1 * arg_2
    print("掛け算: {val}".format(val=str(result_prod)))
    # 割り算
    if arg_1 == 0 or arg_2 == 0:
        print("割り算: エラー: 割り算に0を指定することはできません。")
    else:
        if arg_1 >= arg_2:
            result_quot = arg_2 / arg_1
        else:
            result_quot = arg_1 / arg_2
        print("割り算: {val}".format(val=str(Decimal(result_quot).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))))
    sys.exit(0)


if __name__ == '__main__':
    main()
