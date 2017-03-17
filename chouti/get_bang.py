# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'
log_file = '/var/www/html/log.html' #/var/www/html/


from chouti_scrape_host import establish_mysql_connect, get_rebang_json, dict_to_query
import time

class Log():
    def __init__(self, filename='log.txt', mode='w'):
        self.handle = open(filename, mode, encoding='utf-8')
        self.handle.write(self.now() + filename + 'opened in ' + mode + ' mode' + '\n')
    def write(self, text):
        self.handle.write(self.now() + str(text) + '\n')
    def close(self):
        self.handle.write(self.now() + "log closed" + '\n')
        self.handle.close()
    def now(self):
        return time.strftime('%Y-%m-%D %H:%M.%S >>> ', time.localtime())        

# main Program
if __name__ == '__main__':

    #conn = establish_mysql_connect(mysql_config_file, False)

    log = Log() 

    dicts = get_rebang_json(10)
    print(len(dicts))
    log.write(dicts
             )
    query = dict_to_query(dicts, 'chouti')
    print(len(query))
    log.write(query)
    
    log.close()
    #conn.close()
