{# コメント #}
①NAME={{ name1 }} LANG={{ lang1 }}
②NAME={{ name2 }} LANG={{ lang2 }}

【sample2.tpl】
{# if文のsample #}
{% if x > 0 %}
xは0より大きいです
{% elif x == 0 %}
xは0です
{% else %}
xは0より小さいです
{% endif %}

{# for文のsample #}
商品一覧
{% for item in items %}
・ {{ item }}
{% endfor %}
--
【】
#!/usr/local/python/bin/python3
# -*- coding: utf-8 -*-

import paramiko
import scp
from enum import Enum

# 未使用(Enum使おうと思ったけどクラスにした
class CommandIndex(Enum):
COMMAND = 0
EXPECTED_VALUE = 1
ERROR_MESSAGE = 2
BREAK_FLAG = 3

# コマンド情報
class CommandInfo():
# コマンド、期待値、エラー時メッセージ、エラーブレイクフラグ
def __init__(self, command, expected_value, error_message, break_flag):
self.command = command
self.expected_value = expected_value
self.error_message = error_message
self.break_flag = break_flag

# Getters
def getCommand(self):
return self.command
def getExpectedValue(self):
return self.expected_value
def getErrorMessage(self):
return self.error_message
def getBreakFlag(self):
return self.break_flag


print("start...")

C_NORMAL_STATUS = "0"
C_FLAG_TRUE = str(True)
C_FLAG_FALSE = str(False)

error_count = 0

connect_info = {"ip":"192.168.32.113", "port":"22",
"id":"miyasaka", "password":"miyasaka"}

cmd_list = []
cmd_list.append(CommandInfo("uname -n", "mf03host",
"ホスト名想定外エラー", C_FLAG_FALSE))
cmd_list.append(CommandInfo("mkdir -p /home/miyasaka/paramikos; echo $?", C_NORMAL_STATUS,
"ディレクトリ作成失敗", C_FLAG_TRUE))
cmd_list.append(CommandInfo("cd paramikos; echo $?", C_NORMAL_STATUS,
"ディレクトリ移動失敗", C_FLAG_TRUE))
cmd_list.append(CommandInfo("touch /home/miyasaka/paramikos/paramikos.txt; echo $?", C_NORMAL_STATUS,
"ファイル作成失敗", C_FLAG_TRUE))


# ■ssh clientオブジェクト(ssh)を作りコマンド実行
with paramiko.SSHClient() as ssh:

# どうやってhostname & keyを登録するのかわからないので、AutoAddPolicy()としておく
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh接続する
ssh.connect(hostname=connect_info["ip"], port=connect_info["port"],
username=connect_info["id"], password=connect_info["password"])

# コマンド を実行する
for cmd in cmd_list:
stdin, stdout, stderr = ssh.exec_command(cmd.getCommand())

# 実行結果のstdoutとstderrを読み出す
for o in stdout:
if o.strip() != cmd.getExpectedValue():	# 改行はstripで取り除いて比較
print("O:" + cmd.getErrorMessage())
if cmd.getBreakFlag() == C_FLAG_TRUE:
error_count += 1
else:
print("O:" + o.strip())

for e in stderr:
if e.strip() != cmd.getExpectedValue():
print("E:" + cmd.getErrorMessage())
if cmd.getBreakFlag() == C_FLAG_TRUE:
error_count += 1
else:
print("E:" + e.strip())

if error_count > 0:
print("break error_count={}".format(error_count))
break

print("コマンド実行終了.")
# ■scpでファイル取得、送信
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=connect_info["ip"], port=connect_info["port"],
username=connect_info["id"], password=connect_info["password"])

with scp.SCPClient(ssh.get_transport()) as scp:
# SCP取得(GET)
print(" scp get start...")
scp.get('/home/miyasaka/paramikos/paramikos.txt', './paramikos_get.txt')
print(" scp get end.")

# SCP送信(PUT)
print(" scp put start...")
scp.put('./sample1.tpl', '/home/miyasaka/paramikos/sample1.txt')
print(" scp get end.")

print("end.")


"""
【実行結果】
start...
O:mf03host
O:0
O:0
O:0
コマンド実行終了.
scp get start...
scp get end.
scp put start...
scp get end.
end.
"""

# 【参考】
# https://qiita.com/int_main_void/items/1cdec761b745010629d5

# 【環境】
#pip3 install --use-wheel --no-index ./scp-0.10.2-py2.py3-none-any.whl
#LD_LIBRARY_PATH=/usr/local/python/lib:/usr/local/ssl/lib:
#export LD_LIBRARY_PATH
--
