#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math
import re


# 無限ループになるエラーを定義
class InfinityError(Exception):
    pass


# 引数を定義
args = []

# 引数は2個以上
if len(sys.argv) - 1 < 2:
    print("エラー: 指定された引数は{cnt}つです。 引数は2つ以上指定してください。".format(cnt=len(sys.argv) - 1), file=sys.stderr)
    sys.exit(1)
else:
    for argument in sys.argv[1:]:
        if re.match("^-?\d+\Z", argument) is None:
            # 引数は数値のみ
            print("エラー: 指定された引数は数値ではありません。 引数は数値を指定してください。", file=sys.stderr)
            sys.exit(1)
        else:
            # int型に変換して配列に挿入
            args.append(int(argument))

# 一意な値に変換してから昇順にソート
sortedArgs = sorted(set(args))

# 一意な値が2つ以上
if len(sortedArgs) == 1:
    print("エラー: 引数に全て同じ値は指定できません。「{val}」以外の数値を1つ以上指定してください。".format(val=sortedArgs[0]), file=sys.stderr)
    sys.exit(1)


def main():
    # リターンコード
    returnCode = 0
    # 足し算
    resultSum = 0
    for element in args:
        resultSum += element
    print("足し算: {val}".format(val=resultSum))

    # 引き算
    resultDiff = max(args) - min(args)
    print("引き算: {val}".format(val=resultDiff))

    # 掛け算
    resultProd = 1
    try:
        if min(args) >= -1 and max(args) <= 1:
            raise InfinityError()
        else:
            while resultProd <= 10000:
                for element in args:
                    if element == 0:
                        raise InfinityError()
                    resultProd = resultProd * element
                    if resultProd >= 10000:
                        print("引数を順番に掛けていき、積が10000を超えました。")
                        break
    except InfinityError:
        print("無限ループとなる為、掛け算は出来ませんでした。", file=sys.stderr)
        returnCode = 2
    else:
        print("掛け算: {val}".format(val=resultProd))

    # 割り算
    if min(args) == 0:
        # 引数の最小値が0の場合は2番目に小さい値で割り算
        resultQuot = math.ceil(sortedArgs[-1] / sortedArgs[1])
        print("割り算: {val}".format(val=resultQuot))
    elif max(sortedArgs) == 0:
        # 割り算に0が指定は指定できない
        print("割り算: エラー: 割り算に0を指定することはできません。", file=sys.stderr)
        returnCode = 2
    else:
        resultQuot = math.ceil(sortedArgs[-1] / sortedArgs[0])
        print("割り算: {val}".format(val=resultQuot))

    # 正常終了
    sys.exit(returnCode)


if __name__ == '__main__':
    main()
