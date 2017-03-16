from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
config_file = '/home/karibu/conf/mysql_config.ini' 
def query_with_fetchone():
    try:
        dbconfig = read_db_config(config_file, 'mysql')
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bang")
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    query_with_fetchone()
