def insert():
  while True:
    name=input("Student Name : ")
    _class=input("Student Class : ")
    section=input("Student Section : ")
    percent=input("Student Percentage : ")

    not_found=cur.execute("SELECT name FROM students WHERE name='%s'"%name).fetchall() == []

    if not_found:
        query="""INSERT INTO students(name,class,section,percent)
                 VALUES('%s','%s','%s','%s')"""%(name,_class,section,percent)
    else:
        query="""UPDATE students SET class='%s',section='%s',percent='%s'
                 WHERE name='%s' """%(_class,section,percent,name)

    cur.execute(query)
    con.commit()
    
    agin=input("\nAny More ? ")
    if(agin!='yes'):break


def search():
    name=input("Enter Student Name : ")
    rows=cur.execute("""SELECT * FROM students
    WHERE name='%s'"""%name).fetchall()
    for row in rows:
        print('Name :',row[0])
        print('Class :',row[1])
        print('Section :',row[2])
        print('Percent :',row[3])
        return    
    print('student not found')



def remove():
    name=input("Enter Student Name : ")
    result=cur.execute("DELETE FROM students WHERE name='%s'"%name)
    con.commit()
    
    
def students():
    col=cur.execute("SELECT name FROM students").fetchall()
    for name in col:print(name[0])

    
import sqlite3 as sql
con=sql.connect("database.db")
cur=con.cursor()
query="""CREATE TABLE IF NOT EXISTS students(
            name VARCHAR(20),
            class VARCHAR(5),
            section VARCHAR(5),
            percent int
        )
"""
cur.execute(query)

while True:
    x = input('\n1-Insert 2-Search 3-Remove 4-Students 0-Exit ? : ')
    if  (x=='1') : insert()
    elif(x=='2') : search()
    elif(x=='3') : remove()
    elif(x=='4') : students()
    elif(x=='0') : break

    
