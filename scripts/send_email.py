from mail import send
con={'server'  : 'smtp.mail.yahoo.com',
     'port'    : '587',
     'from'    : '...@yahoo.com',
     'pass'     : '****',
     'to'      : '...@gmail.com',
     'subject' : 'python mail test ^_^'
    } 
	
fields={'name':'Python Programmer',
'Age':23,
'phone':'1234',
'message':'I Love Python ♥'
}

if send(con, fields):print('Done..')
else : print('failed..')
