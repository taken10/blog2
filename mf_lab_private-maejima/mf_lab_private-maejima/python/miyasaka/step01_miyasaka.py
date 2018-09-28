#!/usr/local/python/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

import python.miyasaka.common_libs as cmn


C_ERR_MSG_01 = '引数の数は2つを指定してください。指定された引数の数:{}'
C_ERR_MSG_02 = '引数に数値以外が指定されています。'
C_ERR_MSG_03 = '割り算の結果：引数に0が指定されていますので計算しませんでした。'


def main(argvs):

    # 引数の受け取り
    argvs = argvs + ["-2", "-4"]
    print(argvs, sep=", ")

    # 引数の個数チェック
    argc = len(argvs) - 1
    if argc != 2:
        cmn.print_err(C_ERR_MSG_01.format(argc))
        return 1

    # 引数の数値チェック
    if (argvs[1].replace("-", "").isdigit() != 1
            or argvs[2].replace("-", "").isdigit() != 1):

        cmn.print_err(C_ERR_MSG_02)
        cmn.print_err(argvs[1:])
        return 1

    # 引数の取得
    argv1, argv2 = [int(argv) for argv in argvs[1:]]

    # 足し算
    result = argv1 + argv2
    print('足し算の結果：[{}]'.format(result))

    # 引き算
    if argv1 >= argv2:
        result = argv1 - argv2
    else:
        result = argv2 - argv1
    print('引き算の結果：[{}]'.format(result))

    # 掛け算
    result = argv1 * argv2
    print('掛け算の結果：[{}]'.format(result))

    # 割り算
    if (argv1 != 0) and (argv2 != 0):
        if argv1 < argv2:
            result = round(float(argv1) / float(argv2), 2)
        else:
            result = round(float(argv2) / float(argv1), 2)

        print('割り算の結果：[{}]'.format(result))
    else:
        cmn.print_err(C_ERR_MSG_03)

    # 正常終了
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))