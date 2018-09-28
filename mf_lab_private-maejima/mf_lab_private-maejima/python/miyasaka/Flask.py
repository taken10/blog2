""" WebAPI """
#!/usr/local/python/bin/python3
# _*_ coding: utf-8 _*_
import os
import sys
from time import sleep
from datetime import datetime
from logging import getLogger, FileHandler, StreamHandler, handlers
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

WERKZEUG_LOG_FILENAME = '/home/kanehira/work/sample/Flask/dsn_werkzeug.log'
werkzeug_log_handler = handlers.TimedRotatingFileHandler(
    WERKZEUG_LOG_FILENAME, when='W0', backupCount=5, encoding='utf-8')
ACCESS_LOG_FILENAME = '/home/kanehira/work/sample/Flask/dsn_access.log'
access_log_handler = handlers.TimedRotatingFileHandler(
    ACCESS_LOG_FILENAME, when='W0', backupCount=5, encoding='utf-8')

log = getLogger('werkzeug')
log.addHandler(werkzeug_log_handler)
access_log = getLogger(__name__)
access_log.setLevel(10)
access_log.addHandler(access_log_handler)

app = Flask(__name__)
auth = HTTPBasicAuth()
pattern_blank = "None"
pattern_0 = "0"
pattern_1 = "1"

users = {
    "admin": "infoblox",
    "kanehira": "kanehira",
    "miyasaka": "miyasaka",
    "kato": "kato"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
#@auth.login_required
def index():
    return "Index\n"


def writeLog(request):
    now = datetime.now()
    log_str = now.strftime("%Y/%m/%d %H:%M:%S") + " "
    for i, k in request.headers:
        log_str += i + ':' + k + ', '
        log_str += request.remote_addr + ', '
        log_str += request.url
        access_log.log(20, log_str)


@app.route('/before', methods=['GET'])
#@auth.login_required
def before():
    try:
        writeLog(request)
        process_flag = str(request.args.get('flag'))
        if process_flag == pattern_blank:
            response = {
                'name1':'kanehira',
                'name2':'miyasaka',
                'name3':'kato'
            }
            return jsonReturn(response)
        elif process_flag == pattern_0:
            response = {
                'name1':'kanehira',
                'name2':'miyasaka',
                'name3':'kato'
            }
            return jsonReturn(response)
        elif process_flag == pattern_1:
            response = {
                'name1':'kanehira',
                'name2':'kato',
                'name3':'miyasaka'
            }
            return jsonReturn(response)
        else:
            raise Exception("flagに[0|1]以外が設定されました。")
            # return "flagを設定してください。[ " + pattern_0 + " | " + pattern_1 + " ]\n"
    except:
        raise
        # print('Unexcepted error occer.')
        # return 'Unexcepted error ccer.'
@app.route('/after', methods=['GET'])
#@auth.login_required
def after():
    try:
        writeLog(request)
        process_flag = str(request.args.get('flag'))
        if process_flag == pattern_blank:
            response = {
                'name1':'kanehira',
                'name2':'miyasaka',
                'name3':'kato'
            }
            return jsonReturn(response)
        elif process_flag == pattern_0:
            response = {
                'name1':'kanehira',
                'name2':'miyasaka',
                'name3':'kato'
            }
            return jsonReturn(response)
        # jsonReturn(response)
        elif process_flag == pattern_1:
            response = {
                'name1':'miyasaka',
                'name2':'kato',
                'name3':'kanehira'
            }
            return jsonReturn(response)
        else:
            raise Exception("flagに[0|1]以外が設定されました。")
            # sleep(60)
            # return "flagを設定してください。[ " + pattern_0 + " | " + pattern_1 + " ]\n"
    except:
        raise
        # print('Unexcepted error occer.')
        # return 'Unexcepted error occer.'

"""
@app.route('/after/debug', methods=['GET'])
@auth.login_required
def after_debug_get():
return 'debug GET'

@app.route('/after/debug', methods=['POST'])
@auth.login_required
def after_debug_post():
return 'debug POST'


@app.route('/before/debug', methods=['GET'])
@auth.login_required
def before_debug_get():
return 'debug GET'

@app.route('/before/debug', methods=['POST'])
@auth.login_required
def before_debug_post():
return 'debug POST'
"""

def jsonReturn(response):
    # return jsonify(response)
    return "HTTP_DEMO"

if __name__ == '__main__':
    try:
        app.run(debug=False, host="192.168.32.113", port=8080)
    except:
        print('Unexcepted error occer.')
