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

# GET
getArgs = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=getArgs)
print(r.url)  # http://httpbin.org/get?key1=value1&key2=value2
# URLにパラメータ
r = requests.get("http://httpbin.org/get?key1=value&key1&key2=value2")
print(r.url)  # http://httpbin.org/get?key1=value1&key2=value2

# POST
postArgs = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.post('http://httpbin.org/post', data=postArgs)
print(r.text)
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


# ファイル
files = {'file': open('./text_requests.txt', 'rb')}
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

# カスタムヘッダ
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.headers)
# {'Date': 'Wed, 13 Jun 2018 06:25:36 GMT', "Content-Type":'application/json; charset=utf-8',...

# Cookieの取得
# 以下URLがCookieを返却する場合には
# r = requests.get('http://example.com/some/cookie/setting/url')
# 以下のようにCookieを取得できます.
# print(r.cookies['example_cookie_name'])  # 'example_cookie_value'

# Cookieを付与してHTTP通信を行う
cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)  # '{"cookies": {"cookies_are": "working"}}'

# Session
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)  # '{"cookies": {"sessioncookie": "123456789"}}'

# リダイレクト
# 「http://」にアクセスすると「https://」にリダイレクトされる
r = requests.get('http://github.com')
# 自動的にリダイレクト先に切り替わっている.
print(r.url)  # 'https://github.com/'
# ステータスコードもリダイレクト先の内容になる
print(r.status_code)  # 200
# リダイレクト履歴を確認できます.
print(r.history)  # [<Response [301]>]

# リダイレクト制御
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)  # 301
print(r.history)  # []
