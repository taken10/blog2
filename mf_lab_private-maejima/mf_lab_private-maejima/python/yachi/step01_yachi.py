#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python3系ではデフォルトが「utf-8」なので記載しなくても可

import sys                                  # 引数受け取りと、処理終了の為
import re                                   # 正規表現を使用する為
from decimal import Decimal, ROUND_HALF_UP  # 割り算の計算用

# Python2系で3系記載を動かす場合に必要
# from __future__ import print_function, unicode_literals, division, absolute_import

"""
メモ
  print_function：
    2系の「print 文字列」を3系の「print(文字列)」にする

  unicode_literals：
    文字型を「Unicode」にする（2系は「str」と「Unicode」の二つが存在し、Unicodeには文字列のダブルクォーテーション前に「u」が必要だった）

  division：
    int同士の割り算について2系の小数点以下切り捨てから、3系の自動float化になる（逆に2系仕様の計算をする場合は「//」を使う）

  absolute_import：
    絶対インポート優先（2系はカレントディレクトリ優先だったので標準モジュールをいつの間にか上書きしてしまう可能性があった）
"""


# 引数の受け取り
arguments = sys.argv

# 引数の数を判定
if len(arguments) != 3:
    print('エラー：引数の数が{cnt}です。引数は２つ設定してください。'.format(cnt=len(arguments)-1), file=sys.stderr)
    sys.exit(1)


# isdigit()だと自然数＆0しか判定できないので正規表現で判定
# float型の正規表現チェックは「^-?\d+(\.\d+)?\Z」
def regex_integer_match(x): return bool(re.compile("^-?\d+\Z").match(x))


"""
メモ
  「^」 ：文字列の先頭
  「?」 ：?の前文字が0～1回繰り返される
  「\d」：Unicodeの10進数表記に含まれる文字（基本的に0～9だと思っておけば問題ない。その為「[0-9]」という記載もできる）
  「+」 ：+の前文字が1回以上繰り返される
  「()」：囲った表現を1つのグループとする
  「\Z」：文字列の末尾
  上記正規表現(float)は
  ≪先頭が「-」または数字で始まり、数字で完結する。途中に「.」が一つ含まれていて良い。≫
  という意味の正規表現となる
"""


def argument_check(x, y): return not(regex_integer_match(x)) or not(regex_integer_match(y))


if bool(argument_check(arguments[1], arguments[2])):
    print('エラー：引数に数値(整数)以外が含まれています。', file=sys.stderr)
    sys.exit(1)

# 引数を整数に変換
arguments1 = int(arguments[1])
arguments2 = int(arguments[2])

# 足し算
print('足し算の結果は{val}です。'.format(val=arguments1 + arguments2))

# 引き算(大きい値から小さい値を引く)
if arguments1 > arguments2:
    print('引き算の結果は{val}です。'.format(val=arguments1 - arguments2))
else:
    print('引き算の結果は{val}です。'.format(val=arguments2 - arguments1))

# 掛け算
print('掛け算の結果は{val}です。'.format(val=arguments1 * arguments2))

# 割り算に０が含まれると困るのでエラーにし、処理を終了
if arguments1 == 0 or arguments2 == 0:
    print('割り算エラー：引数に０が設定されています。', file=sys.stderr)
    sys.exit(0)


# Python3系ではround()を使うと四捨五入ではなく、偶数への丸めになるのでPython2系でも同じ動きになるDecimalを使うのが正確
def round_half_up(x): return Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


"""
メモ
  Decimal(x)で値をDecimal型に変換
  .quantize()で値を丸める
  第一引数のDecimalは桁数の指定
  第二引数として書いているroundingは丸め方の指定
  (Javaでも似たような記載があったハズ)
"""


# 割り算(大きい値で小さい値を割る)
if arguments1 < arguments2:
    print('割り算の結果は{val}です。'.format(val=round_half_up(arguments1 / arguments2)))
else:
    print('割り算の結果は{val}です。'.format(val=round_half_up(arguments2 / arguments1)))

sys.exit(0)
