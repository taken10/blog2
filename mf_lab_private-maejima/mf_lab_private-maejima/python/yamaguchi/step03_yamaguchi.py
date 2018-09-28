#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime
import time
import subprocess
import os.path
import errno


def main(arg_file):
    # リターンコード
    return_code = 0
    # 引数は1つ指定
    if len(arg_file) != 1:
        print("エラー: 指定された引数は{cnt}つです。 引数は1つ指定してください。".format(cnt=len(arg_file)), file=sys.stderr)
        return 1
    # 指定されたファイルが存在しない/読み込めない
    if not os.path.exists(arg_file[0]):
        print("エラー: 指定されたファイルは存在しないか、正しく読み込むことが出来ませんでした。", file=sys.stderr)
        return 1
    else:
        # ファイルを開く(読み込みモード)
        with open(arg_file[0], "r", encoding="utf-8") as read_file:
            read_text = read_file.readlines()
        # 空白行を削除
        mod_text = [main_text for main_text in read_text if (main_text != '\n') and (main_text.rstrip() != '')]
        # 読み込んだファイルが空白行のみはエラー
        if len(mod_text) == 0:
            print("エラー: 指定されたファイルの中身が空白行のみです。", file=sys.stderr)
            return 1
    # プロセスID取得
    pid = os.getpid()
    # ファイルを開く(書き込みモード)
    try:
        with open("../output.{val}.txt".format(val=pid), "x", encoding="utf-8") as write_file:
            for row in range(len(mod_text)):
                # 日時取得
                date_time = datetime.now().strftime("%Y/%m/%d %H-%M-%S")
                # unixTime取得
                unix_time = str(time.mktime(datetime.now().timetuple()))
                # 書込み（YYYY/MM/DD HH-MI-SS:unixTime:text）
                write_file.write(date_time + ":" + unix_time + ":" + mod_text[row])
    except IOError as e:
        # ファイルの出力権限がなければエラー
        if e.errno == errno.EACCES:
            print("エラー: ファイル出力権限がありません。", file=sys.stderr)
            return 1
        if e.errno == errno.EEXIST:
            print("エラー: 既にファイルが存在します。", file=sys.stderr)
            return 1

    # コマンドで[ls -l]を出力
    cmd = 'dir .'
    response = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    print(response.stdout.decode("cp932"))

    # 正常終了
    return return_code


# if main
if __name__ == "__main__":
    sys.argv = sys.argv
    sys.exit(main(sys.argv[1:]))
