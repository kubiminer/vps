import json, re
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import urllib.request

def get_rebang_json(page_num):
    url = 'http://m.chouti.com/m/link/more.do?type=hot&page={page}&limit=recent'.format(page=page_num)
    print('searching web: ', url)
    user_agent = ('MQQBrowser/26 Mozilla/5.0 '
                  '(Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7)'
                  'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req).read().decode('utf-8')   
    data = json.loads(res)['result']
    if data['code'] != '9999':
        data = None
    else:
        data = data['data']['items']
    return data
    
json = get_rebang_json(10)
print(len(json))
