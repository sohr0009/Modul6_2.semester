import mysql.connector as mc
host = 'localhost'
user = 'root'
password = ''


def dbconnect():
    mydb = mc.connect(
        host=host,
        user=user,
        password=password,
        database='AgileTimeTracker'
    )
    return mydb
