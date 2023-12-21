import MySQLdb


# DB BAGLANTILARI
db_ip=""
db_user=""
db_pass=""
db_dbname="offline_test_db"


sqlresults =[]
# Database baglantisinin acilmasi
db = MySQLdb.connect(db_ip,db_user,db_pass,db_dbname)
cursor = db.cursor()
# Sorgunun kosulmasi
cursor.execute("SELECT * FROM elements" )
# Donen cevaplarin alinmasi
data = cursor.fetchall()
for sqlresult in data:
	print(data.ColumnName)
    sqlresults.append(sqlresult)
db.close()