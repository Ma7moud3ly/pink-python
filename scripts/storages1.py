def insert():
  while True:
    name=input("Student Name : ")
    _class=input("Student Class : ")
    section=input("Student Section : ")
    percent=input("Student Percentage : ")
    student={'class':_class,'section':section,'percent':percent}
    students[name]=student
    agin=input("Any More ? ")
    if(agin!='yes'):break

       
def search():
    name=input("Enter Student Name : ")
    if name in students:
      print('Name :',name)
      for key,value in students[name].items():
        print(key,':',value)
    else : print('student not found')

def remove():
    name=input("Enter Student Name : ")
    if name in students:students.pop(name)
    else : print('student not found')

    
students={}

while True:
    x = input('1-Insert 2-Search 3-Remove 4-Students 0-Exit ? : ')
    if  (x=='1') : insert()
    elif(x=='2') : search()
    elif(x=='3') : remove()
    elif(x=='4') : print(list(students.keys()))
    elif(x=='0') : break


    
