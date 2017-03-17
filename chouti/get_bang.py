# constant defination
mysql_config_file = 'home/karibu/.conf/mysql_config.ini'

from chouti_scrape_host import establish_mysql_connect

if __name__ == '__main__':
    conn = establish_mysql_connect(mysql_config_file)
    print(conn)
