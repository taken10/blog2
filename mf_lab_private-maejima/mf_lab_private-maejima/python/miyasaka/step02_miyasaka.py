#!/usr/bin/python -tt
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import math
import sys
import python.miyasaka.common_libs as cmn

C_ERR_MSG_10 = '引数の数は2つ以上を指定してください。指定された引数の数:{cnt}'
C_ERR_MSG_11 = '引数に数値以外が指定されています。'
C_ERR_MSG_12 = '引数が全て同じです。'
C_ERR_MSG_13 = '掛け算の結果：無限ループに陥るため計算しませんでした。'
C_ERR_MSG_14 = '割り算の結果：0が指定されているため計算しませんでした。'


def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x))) / p


def main(argvs):
    # リターンコード定義（デフォルト正常:0）
    ret_code = 0

    # 引数の個数チェック
    if len(argvs) < 2:
        cmn.print_err(C_ERR_MSG_10.format(cnt=len(argvs)))
        return 1

    # 引数の数値チェック
    for tmp_argv in argvs:
        if tmp_argv[0] == '-':
            check_val = tmp_argv[1:]
        else:
            check_val = tmp_argv

        if not bool(check_val.isdigit()):
            cmn.print_err(C_ERR_MSG_11)
            return 1

    # リストの内容をすべてint型に変(内包表記)
    vals = [int(i) for i in argvs]

    # 重複要素を排除（ユニーク化）して昇順ソート
    uniq_vals = sorted(set(vals))

    # 引数の同一チェック（ユニーク化した結果、個数が1か？）
    if len(uniq_vals) == 1:
        cmn.print_err(C_ERR_MSG_12)
        return 1

    # 足し算
    val_sum = sum(vals)
    print('足し算の結果：{val}'.format(val=val_sum))

    # 引き算
    val_dif = max(vals) - min(vals)
    print('引き算の結果：{val}'.format(val=val_dif))

    # 掛け算
    # 値に0が含まれる or 値が-1から1の範囲内の場合は無限ループする
    if 0 in vals or (min(vals) >= -1 and max(vals) <= 1):
        cmn.print_err(C_ERR_MSG_13)
        ret_code = 2
    else:
        val_pro = 1

        # 10,000を超えていなければ繰り返し
        while val_pro < 10000:
            for i_pro in vals:
                val_pro = val_pro * i_pro
                if val_pro >= 10000:
                    # 計算結果が10,000を超えていればforループを終了
                    print("超えたのでbreak.")
                    break

        print('掛け算の結果：{val}'.format(val=val_pro))

    # 割り算
    # 昇順ソートした結果の最小値が0であれば次に大きな値を使う
    if uniq_vals[0] == 0:
        min_quo = uniq_vals[1]
    else:
        min_quo = uniq_vals[0]

    max_quo = max(uniq_vals)

    if min_quo == 0 or max_quo == 0:
        cmn.print_err(C_ERR_MSG_14)
        ret_code = 2
    else:
        # ceilで切り上げるパターン
        val_quo = math.ceil(max_quo / min_quo)
        print('割り算の結果(CEIL)：{val}'.format(val=val_quo))

        # roundで切り上げるパターン
        val_quo2 = my_round((max_quo / min_quo) + 0.4)
        print('割り算の結果(ROUND)：{val}'.format(val=val_quo2))

    # 終了
    return ret_code


# if main
if __name__ == '__main__':
    sys.argv = sys.argv + ["400", "100", "200", "300"]
    sys.exit(main(sys.argv[1:]))