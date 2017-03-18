import chouti_scrap as cs

# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'
log_file = '/var/www/html/log.html'

# main Program
if __name__ == '__main__':
    log = cs.Log(log_file)

    dicts = cs.get_rebang_json(1)
    print('length of records', len(dicts))
    log.write(dicts)

    query = cs.dict_to_query(dicts, 'bang')
    print('length of query', len(query))
    log.write(query)

    conn = cs.mysql_connect(mysql_config_file)
    echo =  "connected to mysql. " + str(conn)
    print(echo)
    log.write(echo)

    query = query[0]
    if cs.mysql_insert(conn, query):
        print('insert success')
    else:
        print('insert failed')



    log.close()
    conn.close()
