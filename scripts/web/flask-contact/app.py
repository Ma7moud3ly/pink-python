"""
Flask Python Contact Form.
By : Mahmoud Aly
ma7moud3ly2012@gmail.com
"""
from flask import Flask,render_template,request
from mail import send

app = Flask(__name__)

con={'server'  : 'smtp.mail.yahoo.com',
     'port'    : '587',
     'from'    : '@yahoo.com',
     'pass'     : '',
     'to'      : '@gmail.com',
     'subject' : 'Falsk Contact Form'
    }  
form={}

@app.route('/', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        for key,val in request.form.items():
            if key=='submit':continue
            form[key]=val
        return render_template('contact.html',sent=True,success=send(con,form))    
       
    else:return render_template('contact.html',sent=False)

