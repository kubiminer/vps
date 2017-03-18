# coding: utf-8
# importing modules
import json, re, time
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import urllib.request

# reading configration from config.ini file
def read_db_config(filename='mysql_config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

# establishing mysql conection
def mysql_connect(config_file):
    db_config = read_db_config(config_file, 'mysql')
    try:
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            return conn
        else:
            return False
    except Error as error:
        return False

# insert into database
def mysql_insert(conn, query):
    query = query
    conn = conn
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return None
    except Error as error:
        return error

# getting rebang json by urllib.request method
def get_rebang_json(page_num):
    url = 'http://m.chouti.com/m/link/more.do?type=hot&page={page}&limit=recent'.format(page=page_num)
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

# return the list of dict from json to mysql REPLACE SQL query
def get_underscore(text):
    return re.sub( '(?<!^)(?=[A-Z])', '_', text).lower()

def dict_to_query(dict_list, table_name):
    query = []
    for dict in dict_list:
        lower_keys = [get_underscore(i) for i in dict.keys()]
        fld_name = ", ".join(lower_keys)
        value_str =  str(list(dict.values()))[1:-1]
        query += ["REPLACE INTO `{table}` ({columns}) VALUES ({values});"
                  .format(table=table_name, columns=fld_name, values=value_str)]
    return query

class Log():
    def __init__(self, filename='log.txt', mode='w'):
        self.handle = open(filename, mode, encoding='utf-8')
        self.handle.write('<meta charset="utf-8" /> \n <html>')
        self.handle.write(self.now() + filename + 'opened in ' + mode + ' mode' + '\n')
    def write(self, text):
        self.handle.write(self.now() + str(text) + '\n')
    def close(self):
        self.handle.write(self.now() + "log closed" + '\n')
        self.handle.write('<\html>')
        self.handle.close()
    def now(self):
        return time.strftime('%Y-%m-%D %H:%M.%S >>> ', time.localtime())
