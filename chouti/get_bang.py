# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'

from chouti_scrape_host import establish_mysql_connect, get_rebang_json, dict_to_query

# main Program
if __name__ == '__main__':
	
    conn = establish_mysql_connect(mysql_config_file, False)

    log_file = open('/var/www/html/log.html', 'w', encoding="utf-8") 
	
    dicts = get_rebang_json(1)
    log_file.write(dicts)

    query = dict_to_query(dicts, 'chouti')

    log_file.write('<html>/n') 
    log_file.write(query) 
    log_file.write('</html>') 
    log_file.close()
    
    conn.close()
