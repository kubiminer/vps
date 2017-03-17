# constant defination
mysql_config_file = '/home/karibu/.conf/mysql_config.ini'

from chouti_scrape_host import establish_mysql_connect

# main Program
if __name__ == '__main__':
	
    conn = establish_mysql_connect(mysql_config_file, False)

    dicts = get_rebang_json(1)
    print(dicts)

    query = dict_to_query(dicts, table_name)
    print(query, 'chouti')
