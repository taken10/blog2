#!/usr/bin/python -tt
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
import calendar
import codecs
import os
import sys
import time
import subprocess

import python.miyasaka.common_libs as cmn

C_ERR_MSG_21 = '引数の数は1つ指定してください。指定された引数の数:{cnt}'
C_ERR_MSG_22 = '指定されたファイルが存在しません。指定された引数:{x}'
C_ERR_MSG_23 = '指定されたファイルが読み取れません。指定された引数:{x}'
C_ERR_MSG_24 = '指定されたディレクトリに書き込めません。ディレクトリ:{x}'
C_ERR_MSG_25 = '指定されたファイルが存在します。指定された引数:{x}'
C_ERR_MSG_26 = '出力後のファイルサイズがゼロです。'


def getUnixttime():
    now = time.time()
    loc = datetime.fromtimestamp(now)
    return calendar.timegm(loc.timetuple())


def main(argvs):

    # リターンコード定義
    ret_code = 0

    # 引数の個数チェック
    if len(argvs) != 1:
       cmn.print_err(C_ERR_MSG_21.format(cnt=len(argvs)))
       return 1

    # filename
    imput_file = argvs[0]

    # file check
    if os.path.exists(imput_file) == False:
        cmn.print_err(C_ERR_MSG_22.format(x=imput_file))
        return 1

    # file check
    if os.access(imput_file, os.R_OK) == False:
        cmn.print_err(C_ERR_MSG_23.format(x=imput_file))
        return 1

    # output dir
    output_dir = os.path.dirname(imput_file)

    # output dir check
    if os.access(output_dir, os.W_OK) == False:
        cmn.print_err(C_ERR_MSG_24.format(x=imput_file))
        return 1

    # output_file name
    pid = os.getpid()
    output_file = output_dir + '/output.' + str(pid) + '.txt'

    # file check
    if os.path.exists(output_file) == True:
        cmn.print_err(C_ERR_MSG_25.format(x=output_file))
        return 1

    # read file
    with codecs.open(imput_file, 'r', 'utf-8') as rfd:
        input_lists = rfd.read().split('\n')

    # write file
    with codecs.open(output_file, 'w', 'utf-8') as wfd:
        for row_tmp in input_lists:
            # 空白行はスキップ
            if row_tmp.strip() == '':
                continue

            # 改行コード削除
            row = row_tmp.rstrip('\n')
            wfd.write('{dt}:{dtu}:{row}\n'.format(
                row=row,
                dt=datetime.now().strftime("%Y/%m/%d %H-%M-%S"),
                dtu=getUnixttime()))

    # file size check
    if os.path.getsize(output_file) == 0:
        cmn.print_err(C_ERR_MSG_26)
        os.remove(output_file)
        return 1

    # ls command
    # res = subprocess.call(['dir', '-B', output_dir])
    res = 0
    if res != 0:
        return res

    # 正常終了
    return ret_code


# if main
if __name__ == '__main__':
    sys.argv = sys.argv + ["../imput.txt"]
    sys.exit(main(sys.argv[1:]))
