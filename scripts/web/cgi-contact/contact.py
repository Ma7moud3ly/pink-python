#!python
import cgi, cgitb,os
from mail import send
 
con={'server'  : 'smtp.mail.yahoo.com',
     'port'    : '587',
     'from'    : '...@yahoo.com',
     'pass'     : '****',
     'to'      : '...@gmail.com',
     'subject' : 'CONTACT FORM'
    } 
form={}

print ("Content-type: text/html\n")


if os.environ['REQUEST_METHOD'] == 'POST':
   for key,val in dict(cgi.FieldStorage()).items():
       val=str(val)
       val=val[val.find(',')+3:len(val)-2]
       form[key]=val
   if send(con,form):
         print('<center><h1 style="color:green">Succeed<h1></center>')
   else:
         print('<center><h1 style="color:red">Failed<h1></center>')     
else:
   html=open('contact.html','r').read()
   print(html)
   
   
