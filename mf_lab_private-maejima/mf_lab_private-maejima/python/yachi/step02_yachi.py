#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy  # 一時的に引数配列を複写する為
import math  # 整数値への切り上げをする為
import re    # 正規表現を使用する為
import sys   # 引数受け取りと、処理終了の為


def regex_integer_match(x): return bool(re.compile("^-?\d+\Z").match(x))


def round_up(x): return math.ceil(x)


def main(arguments):
    ret_code = 0

    # 引数の数を判定
    if len(arguments) < 2:
        print('エラー：引数の数が{cnt}です。引数は２つ以上設定してください。'.format(cnt=len(arguments)), file=sys.stderr)
        return 1

    for argument in arguments:
        if not bool(regex_integer_match(argument)):
            print('エラー：エラー：引数に数値(整数)以外が含まれています。', file=sys.stderr)
            return 1

    values = [int(i) for i in arguments]
    values = set(values)

    if len(values) == 1:
        print('エラー：引数の値が全て同一値です。', file=sys.stderr)
        return 1

    # 引数の合計値を出力
    print('引数の合計値は{sum}です。'.format(sum=sum(values)))

    # 引数の最大値から最小値を引いた数を出力
    print('引数の最大値から最小値を引いた値は{num}です。'.format(num=(max(values)-min(values))))

    # 引数の掛け算
    if 0 in values or (min(values) >= -1 and max(values) <= 1):
        # 値に０が含まれると計算結果が０のままになる
        # 値の範囲が-１から１の場合、-１から１の間を行ったり来たりするだけ
        print('エラー：無限ループが発生する為、掛け算処理はスキップ', file=sys.stderr)
        ret_code = 2
    else:
        product = 1
        while product < 10000:
            # 掛け算結果が10000を超えるまで掛け続ける
            for value in values:
                product *= value
                if product >= 10000:
                    print('値が10000以上になったため、掛け算処理を終了します。')
                    break

        print('引数掛け算結果は{num}です。'.format(num=product))

    # 引数の最大値を最小値で割った数を出力
    if min(values) == 0:
        list_ = copy.deepcopy(values)
        list_.remove(min(values))
        min_ = min(list_)
    else:
        min_ = min(values)

    max_ = max(values)

    if max_ == 0 or min_ == 0:
        print('エラー：最大値または最小値が０の為、割り算ができません。', file=sys.stderr)
        return 2

    print('引数の最大値を最小値で割った値は{num}です。'.format(num=round_up(max_/min_)))

    return ret_code


# if main
if __name__ == '__main__':
    sys.argv = sys.argv + ["950000", "100", "200", "300"]
    sys.exit(main(sys.argv[1:]))
