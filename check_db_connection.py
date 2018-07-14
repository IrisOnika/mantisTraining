import pymysql.cursors
from fixture.db import DbFixture
#from fixture.orm import ORMFixture
#from model.group import Group


connection = pymysql.connect(host="127.0.0.1", database="bugtracker", user="root", password="")
db = DbFixture(_host="127.0.0.1", _database="bugtracker", _user="root", _password="")

try:
    list = db.get_project_list()
    for item in list:
        print(item)
    print(len(list))
finally:
    connection.close()












#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():              #fetchall returns all info as list of rows(like in db)
#        print(row)
#finally:
#    connection.close()