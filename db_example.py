import pymysql

conn = pymysql.connect(host='localhost', port = 3306, user = 'root', passwd = 'Happy123', db = 'sakila')

cur = conn.cursor()

cur.execute('SELECT film_id, title FROM film')

for row in cur:
    print row
    
cur.close()
conn.close()
