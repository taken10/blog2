Title: requests<br>
Date: 2018-06-12 10:00<br>
Category: python<br>


# １．はじめに
Pythonの標準ライブラリである「requests」について学んだことを記載していきます。


# ２．「requests」とは？
「requests」とは簡単に言えば、「人間の為のHTTP」です。<br>
HTTP(s)通信を行うためのライブラリで、HTTPリクエストを簡単に生成することができます。<br>


# ３．インストール
「requests」はpipでインストールできる。

```
$pip install requests
```

以下のようにインポートする。

```
import requests
```

<p>
<b>※Pycharmでのインストール方法</b><br>
File→Default Settings→Project Interpreter→▽（歯車の左）→<br>
インストールしたPythonを選択→＋（緑色）→<br>
検索マーク欄に追加したいパッケージ名（requests）を入力→<br>
Install Package
</p>


# ４．基本的な使い方

```
# requestsモジュールの読み込み
import requests

# GET通信を行う例
r = requests.get("http://httpbin.org/get")

# レスポンスのステータスコードの確認
print(r.status_code)  # 200

# レスポンスヘッダーの確認
print(r.headers)  # {'Connection': 'keep-alive', 'Server': ...
# 参照
print(r.headers['content-type'])  # application/json
# getメソッドを使用しても取得できる。また大文字小文字の区別はない。
print(r.headers.get("CONTENT-TYPE"))  # application/json

# レスポンス内容をテキストで取得
print(r.text)  # {"args":{},"headers":{"Accept": ...

# レスポンス内容をJSONで取得
print(r.json())  # {'args': {}, 'headers': {'Accept': ...
# キー検索
print(r.json()["url"])  # http://httpbin.org/get

# レスポンス内容をバイナリーで取得
print(r.content)  # b'{"args":{},"headers":{"Accept":...
```

※ インストールも問題なしなのに実行時に以下のようなエラーが出た場合。

```
AttributeError: module 'requests' has no attribute 'get'
```

**モジュール名と同名のディレクトリ名orファイル名にしない。**<br>
→「requests.py」というファイル名で作成していた。importしたモジュール名とファイル名が同一だと、<br>
　 import先が自ファイルになってしまうので注意。


# ５．リクエストの生成

```
requests.httpMethod(url, "任意の数の引数")
```

#### ■ GET通信
- パラメータはparams引数で指定

```
getArgs = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=args)
print(r.url)  # http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

- URLにパラメータ付与

```
r = requests.get("http://httpbin.org/get?key1=value&key1&key2=value2")
print(r.url)  # http://httpbin.org/get?key1=value1&key2=value2
```

#### ■ POST通信
- パラメータはdata引数で指定

```
postArgs = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.post('http://httpbin.org/post', data=postArgs)
# {
#     ・
#     ・
#     "form":{
#         "key1":"value1",
#         "key2":["value2","value3"]
#      },
#     ・
#     ・
# }

```

#### ■ ファイルアップロード
- パラメータはfiles引数で指定

```
files = {'file': open(../imput.xls, 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
# {
#     ・
#     ・
#      "files":{
#          "file":"This is a sample text"
#      },
#     ・
#     ・
# }
```

#### ■ ヘッダーカスタム
- HTTPリクエストヘッダをカスタムする場合は、header引数で指定。<br>
※HTTPリクエストヘッダ・・・ブラウザからサーバにページ表示の際などに要求する事項

```
import json

headers = {'content-type': 'application/json'}
r = requests.get('https://api.github.com/some/endpoint', headers=headers)
print(r.headers)
```

#### ■ Cookie
- レスポンスにCookieが含まれる場合、以下のようにCookieの値を取得することができる。

```
# 以下URLがCookieを返却する場合には
r = requests.get('http://example.com/some/cookie/setting/url')

# 以下のようにCookieを取得できます.
print(r.cookies['example_cookie_name']) # 'example_cookie_value'
```

- Cookieを付与してHTTP通信を行う場合は、cookies引数で指定。

```
cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)  # '{"cookies": {"cookies_are": "working"}}'
```

#### ■ セッション
- Sessionを用いることで、一連のHTTPリクエスト/レスポンスで、
Cookieやカスタムヘッダーなどを使い回すことができます。
例えば、直前のレスポンスで付与されたCookieを次のリクエストで
使いたい場合には、以下のようにSessionを利用します。

```
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)  # '{"cookies": {"sessioncookie": "123456789"}}'
```

#### ■ リダイレクト制御
- リダイレクトが発生するURLではリダイレクト先の情報を取得。

```
# リダイレクトされる
r = requests.get('http://github.com')

# 自動的にリダイレクト先(https)に切り替わっている.
print(r.url) # 'https://github.com/'

# ステータスコードもリダイレクト先の内容になる
print(r.status_code) # 200

# リダイレクト履歴を確認できます.
print(r.history) # [<Response [301]>]
```

- **allow_redirects=False**を指定すると、リダイレクトを制御できる

```
r = requests.get('http://github.com', allow_redirects=False)

print(r.status_code) # 301

print(r.history) # []
```
