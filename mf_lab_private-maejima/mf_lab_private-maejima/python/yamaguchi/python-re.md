Title: requests<br>
Date: 2018-06-12 10:00<br>
Category: python<br>


# １．はじめに
Pythonの標準ライブラリである「re」について学んだことを記載していきます。

# ２．「re」とは？
正規表現の操作を提供するモジュール。<br>
<br>
※そもそも正規表現とは・・・<br>
いくつかの文字列を一つの形式で表現するための表現方法。<br>
つまり文字列を特定する際に、曖昧な感じで指定ができる表現方法のこと。<br>
プログラミングでは頻繁に登場する。
<br><br><br>
下記のようにインポートする

```
import re
```

# ３．正規表現： .   ^   $   [ ]   *   +   ?   { }  |   ( )
正規表現でよく使われる上記の記号（メタ文字）をそれぞれ簡単に解説。

#### ■ なんでもいい1文字：.
- なんでもいい１文字を表現する。<br>
- .自体を検索する場合は「\\」（エスケープ文字）を使用する。（例3）

|  |例1|例2|例3|
|:--:|:--:|:--:|:--:|
|正規表現|これは.です|これは....で私は...です|test\\.txt|
|検索できる文字列|これは犬です|これは正規表現で私は勉強中です|text.txt|

#### ■ 行の先頭：\^,　行の末尾：$
- 行の先頭や末尾にのみ存在する文字列を表現する。<br>
- 行の先頭の\^自体を検索する場合は、「\^\^」、<br>
- 行の末尾の$自体を検索する場合は、「$$」を使用する。（例3）

|  |例1|例2|例3|
|:--:|:--:|:--:|:--:|
|正規表現|\^おめでとう|おめでとう$|\^\^キャレット|
|検索できる文字列|おめでとう、よく頑張った。|お誕生日おめでとう|\^キャレット|

#### ■ 同じ文字の繰り返し：*,+,?
- 同じ文字の繰り返しを表現する。<br>
- *は「直前の文字がないか、直前の文字が１個以上連続する（0回以上連続）」<br>
- +は「最低でも１個は 直前の文字がないといけない（1回以上連続）」<br>
- ?は「直前の文字がまったくないか、１つだけある（0回か1回のみ）」<br>
?を使えばスペースがあるかないか不明な文字列でも検索できる。（例3）

|  |例1|例2|例3|
|:--:|:--:|:--:|:--:|
|正規表現|わー*い|わー+い|Version ?10|
|検索できる文字列|わい　わーい　わーーーーーーーい|わーい　わーーーーーーーい|Version 10　Version10|

#### ■ なんでもいい文字の連続：.*
- *,+,?は.と組み合わせて使うことで検索の幅が広がる。
- .*は「なんでもいい文字が0回以上連続」となる。

|  |例|
|:--:|:--:|
|正規表現|私は.*す|
|検索できる文字列|私はプログラマです　私はプログラマになりたいです<br>　私はプログラミングをします|

- **ここで1つ問題。<br>
例文に対して以下の正規表現で検索する。検索結果は①②のどちらか。**<br>

  - 例文：これは、ペンパイナッポーアッポーペン<br>
  - 正規表現：これは.*ペン
      - ① これは、ペン
      - ② これは、ペンパイナッポーアッポーペン
<br><br><br>
↓↓↓↓↓↓↓↓↓↓<br>
<br><br><br>

- **正解は②。**<br>
.\*というのは、**可能な限り合致するもの**まで繋がる。

#### ■ 文字数指定：{n}
- 直前の文字と同じ文字の繰り返し回数を指定することができる
- {n}だとn回の繰り返し<br>
{n,}だとn回以上の繰り返し<br>
{n, m}だとn回以上、m回以下の繰り返し<br>

|  |例1|例2|
|:--:|:--:|:--:|
|正規表現|Mis{2}is{2}ip{2}i|Yeah!{3,5}|
|検索できる文字列|Mississippi|Yeah!!!　Yeah!!!! Yeah!!!!!|


#### ■ いずれかの文字列：\|
- 複数の連続する文字について適用される正規表現。
- \|で区切られた文字列のいずれかの文字列が合致することで正規表現も合致することとなる。
- この\|はいくらでも並べられますが、大体70文字ぐらいに留めるのが無難。<br>

|  |例|
|:--:|:--:|
|正規表現|りんご&#124;Orange&#124;イチゴ&#124;葡萄&#124;123|
|検索できる文字列|りんご　Orange　イチゴ　葡萄　123|

#### ■ 指定した文字のどれか：[ ]
- [ ]で括られた中の文字のどれか１つに合致。
- 範囲指定は以下のような書き方をする。
  - 小文字の半角英字のいずれか（a～z）と一致：[a-z]
  - 大文字の半角英字のいずれか（A～Z）と一致：[A-Z]
  - 半角数字と一致：[0-9] <br>etc...
- 数字以外（範囲指定したもの以外）というのは[\^0-9]で表現できる（例3）<br>
→[ ]の先頭の\^は上記で出てきた行頭を示す\^とは意味が異なるので注意。<br>
　2文字目以降の指定で文字としての\^を指定できる。（例4）

|  |例1|例2|例3|例4|
|:--:|:--:|:--:|:--:|:--:|
|正規表現|iPhone[0-9]s|[A-Z][a-z][a-z]le|hoge-[\^0-9]-hoge|piyo[A,B,\^]|
|検索できる文字列|iPhone5s　iPhone6s|Title　Smile|hoge-A-hoge　hoge-b-hoge|piyoA　piyoB　piyo^|

- 全角ではＪＩＳ漢字コード表の並びとなっている。（例5）<br>
→範囲指定が50音順とは違うので注意が必要。
- メタ文字は[ ]の中では普通の文字となる。（例6)<br>
→但し、] と \ については例外。（例7）

|  |例5|例6|例7|
|:--:|:--:|:--:|:--:|
|正規表現|[か-こ]|[a.*]|[\\]abc]|
|検索できる文字列|か　が　き　ぎ　く　ぐ　け　げ　こ|a . *のいずれか|] a b c のいずれか|

#### ■ グループ化：( )
- ( )の中をグループ化してくれる。

|  |例1|例2|
|:--:|:--:|:--:|
|正規表現|GR(ee){1,3}N|今日(僕たち&#124;私たち)は卒業します|
|検索できる文字列|GReeN GReeeeN GReeeeeeN |今日僕たちは卒業します　今日私たちは卒業します|

#### ■

- - -

<p align="center"><b>
以上が正規表現の基本中の基本。この他にもまだまだ表現方法は存在する。<br>
下記の本題「re」の説明内でも使用しているので、どういった表現なのか考えてみてください。
</b></p>

# ４．re.match()
- re.match()は文字列の先頭がパターンにマッチするかどうかを調べる。

```
fruits = 'apple banana apple cherry'

result_match_1 = re.match('apple', fruits)
print(result_match_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>

result_match_2 = re.match('a[a-z]+e', fruits)
print(result_match_2)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>
```

- マッチする場合はmatchオブジェクトを返す。<br>
matchオブジェクトはgroup()、start()、end()、span()などのメソッドを持ち、<br>
マッチした文字列やその位置などを返す。

```
print(result_match_1.group())  # apple
print(result_match_1.start())  # 0
print(result_match_1.end())  # 5
print(result_match_1.span())  # (0, 5)
```

- 先頭にマッチする文字列がない場合はNoneを返す。

```
result_match_3 = re.match('banana', fruits)
print(result_match_3)  # None
```

# ５．re.search()
- re.search()は先頭に限らずパターンにマッチするかを調べる。<br>
re.match()と同じく、マッチする場合はmatchオブジェクトを返す。<br>
※文字列中にマッチする部分が複数あっても、返すのは最初にマッチした部分のみ。

```
result_search_1 = re.search('apple', fruits)
print(result_search_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>

result_search_2 = re.search('ba[a-z]+na', fruits)
print(result_search_2)  # <_sre.SRE_Match object; span=(6, 12), match='banana'>
```

# ６．re.findall()
- re.findall()はマッチする部分が複数ある場合、マッチした文字列すべてをリストにして返す。<br>
※返却値はmatchオブジェクトではないので注意。

```
result_findall_1 = re.findall('apple', fruits)
print(result_findall_1)  # ['apple', 'apple']

result_findall_2 = re.findall(r'a[a-z]+e\s*[a-z]+rry', fruits)
print(result_findall_2)  # ['apple cherry']
```

# ７．re.finditer()
- re.finditer()はマッチする部分すべてをmatchオブジェクトのイテレータで返す。<br>
matchオブジェクトを得られるので、マッチした位置なども取得することができる。

```
result_finditer_1 = re.finditer('apple', fruits)
print(result_finditer_1)  # <callable_iterator object at 0x028F3650>

for matchObj in result_finditer_1:
    print(matchObj)
# <_sre.SRE_Match object; span=(0, 5), match='apple'>
# <_sre.SRE_Match object; span=(13, 18), match='apple'>
```

# ８．re.sub()
- re.sub()はマッチした部分を他の文字列に置換することができる。

```
result_sub = re.sub('^a[a-z]+e', 'APPLE', fruits)
print(result_sub) # APPLE banana apple cherry
```

- パターンの一部を()で囲むと、置換後の文字列の中でマッチした文字列を使用することができる。<br>
\1、\2が、それぞれ一つ目の()にマッチした部分と二つ目の()にマッチした部分に対応している。<br>
' 'または" "で囲まれた通常の文字列だと\\\1のように\をエスケープする必要がある

```
result_sub_2 = re.sub('(apple) (banana)', '\\1AND\\2', fruits)
print(result_sub_2)  # appleANDbanana apple cherry
```

# ９．re.split()
- re.split()はパターンにマッチした部分で文字列を分割し、リストにして返す。

```
result_split = re.split(' ', fruits)
print(result_split)  # ['apple', 'banana', 'apple', 'cherry']
```

# １０．re.compile()
- 同じパターンを繰り返し使用する場合は、re.compile()で、あらかじめパターンをコンパイルして<br>
正規表現オブジェクトを生成したほうがよい。<br>
正規表現オブジェクトのメソッドとして、上で紹介したmatch()やsub()などを使うことができる。

```
pattern = re.compile('apple')

result_compile_1 = pattern.match(fruits)
print(result_compile_1)  # <_sre.SRE_Match object; span=(0, 5), match='apple'>

result_compile_2 = pattern.findall(fruits)
print(result_compile_2)  # ['apple', 'apple']

result_compile_3 = pattern.sub('APPLE', fruits)
print(result_compile_3)  # APPLE banana APPLE cherry
```