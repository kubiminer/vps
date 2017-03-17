# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'
log_file = '/var/www/html/log.html'

# 
def list_to_string(l):
    string = ''
    for i in l:
        string += str(i) + '\n'

from chouti_scrape_host import establish_mysql_connect, get_rebang_json, dict_to_query

# main Program
if __name__ == '__main__':

    #conn = establish_mysql_connect(mysql_config_file, False)

    log_file = open(log_file, 'w', encoding="utf-8") 

    dicts = get_rebang_json(10)
    print(len(dicts)
          
    #log_file.write(list_to_string(dicts))

    query = dict_to_query(dicts, 'chouti')
    print(len(query))
    #log_file.write('<html>/n') 
    #log_file.write(list_to_string(query))
    #log_file.write('</html>') 
    
    log_file.close()
    conn.close()
