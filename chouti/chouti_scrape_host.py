
# coding: utf-8

# In[12]:

import json, re
from configparser import ConfigParser
import urllib.request


# In[4]:


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


# In[35]:


# establishing mysql conection

def establish_mysql_connect(config_file, echo=True):
    def print_echo(text):
        if echo: print(text)
  
    """ Connect to MySQL database """
 
    db_config = read_db_config(config_file, 'mysql')
 
    try:
        print_echo('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
            print_echo('connection established.')
        else:
            print_echo('connection failed.')
            return False
 
    except Error as error:
        print(error)
        return False


# In[9]:


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


# In[33]:


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


# In[34]:

dict_list = get_rebang_json(1)
dict_to_query(dict_list, 'bang')


# In[ ]:

import pandas as pd
df = pd.DataFrame(data)
print(df[['id', 'url']])

def get_redirected_url(url):
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url
	
url = 'http://dig.chouti.com/mobile/link/10797361'
url = get_redirected_url(url)


from urllib.parse import urlparse
parsed = urlparse(url)
print(parsed)

