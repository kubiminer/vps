import mysql.connector

config = {
  'user': 'karibu',
  'password': '9002005',
  'host': '127.0.0.1',
  'database': 'wordpress',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = 'show tables'
cursor.execute(query)

for table in cursor:
  print(cursor)
cnx.close()
