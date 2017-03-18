import chouti_scrap as cs

# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'
log_file = '/var/www/html/log.html'

# main Program
if __name__ == '__main__':
    log = cs.Log(log_file)
    page_num = 1
    dicts = cs.get_rebang_json(page_num)
    querys = cs.dict_to_query(dicts, 'bang')
    conn = cs.mysql_connect(mysql_config_file)

    for query, dict in zip(querys, dicts):
        res = cs.mysql_insert(conn, query)
        if res:
            print(dict['id'], ' insert success')
        else:
            print(dict['id'], 'insert failed')
            print(dict.keys())
    log.write('page {} added to database!'.format(page_num))
    log.close()
    conn.close()
