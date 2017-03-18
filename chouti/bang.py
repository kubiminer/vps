import chouti_scrap as cs

# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'
log_file = '/var/www/html/log.html' #/var/www/html/

# main Program
if __name__ == '__main__':

    #conn = establish_mysql_connect(mysql_config_file, False)

    log = cs.Log(log_file)

    dicts = cs.get_rebang_json(1)
    print('length of records', len(dicts))
    log.write(dicts)

    query = cs.dict_to_query(dicts, 'chouti')

    print('length of query', len(query))
    log.write(query)

    log.close()
    #conn.close()
