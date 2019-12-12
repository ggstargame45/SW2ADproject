import pymysql

conn = pymysql.connect(host='localhost',user='root',password='devourstats@',db='diary',charset='utf8')

curs = conn.cursor()

sql = "select * from verifier"
curs.execute(sql)

rows = curs.fetchall()
print(rows)
print(rows[0])

conn.close()
