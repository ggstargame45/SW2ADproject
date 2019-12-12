import pymysql

conn = pymysql.connect(host='localhost',user='root',password='devourstats@',db='pushgame',charset='utf8')

curs = conn.cursor()

sql = "select * from records"
curs.execute(sql)

rows = curs.fetchall()
print(rows)
print(rows[0])

conn.close()
