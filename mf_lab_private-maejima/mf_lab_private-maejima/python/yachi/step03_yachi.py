#!/usr/bin/python
# -*- coding: utf-8 -*-

import errno
import os
import subprocess
import sys
import time
from datetime import datetime


def main(argument):
    if len(argument) != 1:
        print("エラー：引数が１つではありません。", file=sys.stderr)

    try:
        with open(argument[0], 'r', encoding='utf-8') as r_txt:
            txt_lines = r_txt.readlines()
    except IOError:
        print("エラー：指定されたファイルが存在しない。または、読み取りができません。", file=sys.stderr)
        return 1

    if os.path.getsize(argument[0]) == 0 or ''.join(txt_lines).strip() == '':
        print("エラー：指定されたファイルの中身が空です。", file=sys.stderr)
        return 1

    # Windowsでは必ずTrueで通ってしまう
    if not os.access("../", os.W_OK):
        print("エラー：ファイル作成の権限がありません。", file=sys.stderr)
        return 1

    try:
        with open("../output.{process_id}.txt".format(process_id=os.getpid()), 'x', encoding='utf-8') as w_txt:
            for row in range(len(txt_lines)):
                if txt_lines[row] != '\n' and txt_lines[row].rstrip() != '':
                    w_txt.write("{datetime}:{unix_time}:{main_text}".format(
                        datetime=datetime.now().strftime("%Y/%m/%d %H-%M-%S"),
                        unix_time=int(time.mktime(datetime.now().timetuple())),
                        main_text=txt_lines[row]))
    except IOError as e:
        # Windowsではos.accessでのチェックができないので、IOErrorのerr_noで判定を行う
        if e.errno == errno.EACCES:
            print("エラー：ファイル作成の権限がありません。", file=sys.stderr)
        elif e.errno == errno.EEXIST:
            print("エラー：出力先ファイルが既に存在しています。", file=sys.stderr)
        else:
            print("エラー：ファイル出力時にその他のIOエラーが発生しました。", file=sys.stderr)
        return 1

    res = subprocess.run('dir', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True, universal_newlines=True)
    for line in res.stdout.splitlines():
        print(line)

    return res.returncode


# if main
if __name__ == "__main__":
    sys.argv = sys.argv + ["../imput.txt"]
    sys.exit(main(sys.argv[1:]))
