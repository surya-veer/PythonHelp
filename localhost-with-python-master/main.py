import MySQLdb
#connecting with database
db=MySQLdb.connect(user="root",passwd="",db="test",unix_socket="/opt/lampp/var/mysql/mysql.sock")
#unix_socket="/opt/lampp/var/mysql/mysql.sock" it is important to connecting with the local mysql socket
cur = db.cursor()

# Use all the SQL you like
sql="INSERT INTO veer VALUES (NULL,Surya')"
number_of_rows = cur.execute(sql)
#for save the changes in database
db.commit() 
#closing database	
db.close()
