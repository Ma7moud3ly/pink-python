"""
Falsk - Python Editable Portfolio.
By Mahmoud aly .. ma7moud3ly2012@gmail.com
"""

from flask import Flask, session, redirect, url_for,escape,request,render_template,jsonify
from mail import send
import os,binascii

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
myLoginEmail='login_email@mail.com'
myLoginPass='123456'

try:data=eval((open(app.root_path+'/data.json','rb').read().decode('utf-8', 'ignore')))
except:data={}

def is_admin():
    if 'isAdmin' in session:
        isAdmin=session['isAdmin']
        return isAdmin
    return False

@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return render_template('index.html',data=data,admin=is_admin())


@app.route('/login/',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        if(email==myLoginEmail and password==myLoginPass):
            session['isAdmin']=True
            return render_template('index.html',data=data,admin=True)
        else:
            return render_template('index.html',data=data,login=True,login_error=True)
    return render_template('index.html',data=data,login=True)

@app.route('/logout/')
def logout():
    session['isAdmin']=False
    return redirect(request.script_root+'/')


@app.route('/save_values/<key>/<val>/')
def save_values(key,val):
    if(is_admin()==False):return 'unauthorized'
    data[key]=val
    open(app.root_path+'/data.json','w').write(str(data))
    return 'done'

@app.route('/add_project/',methods=['POST', 'GET'])
def add_project():
    if request.method == 'POST':
        name = request.form['addmodal-name']
        description = request.form['addmodal-description']
        file = request.files['addmodal-image']
        image=file.filename;
        file.save(app.root_path+'/static/img/'+image)
        _id=binascii.b2a_hex(os.urandom(5)).decode('utf-8')
        if 'projects' not in data:data['projects']={}
        data['projects'][_id]={'name':name,'description':description,'image':image}
        open(app.root_path+'/data.json','w').write(str(data))
    return redirect(request.script_root+'/')

@app.route('/change_profile/',methods=['POST', 'GET'])
def change_profile():
    if request.method == 'POST':
        file = request.files['profile']
        profile=file.filename;
        file.save(app.root_path+'/static/img/'+profile)
        data['profile']=profile;
        open(app.root_path+'/data.json','w').write(str(data))
    return redirect(request.script_root+'/')

@app.route('/del_project/<_id>/')
def del_project(_id):
    if(is_admin()==False):return 'unauthorized'
    try:
        data['projects'].pop(_id)
        open(app.root_path+'/data.json','w').write(str(data))
        return 'done'
    except:return 'erorr'

@app.route('/email/',methods=['POST', 'GET'])
def email():
    if request.method == 'POST':
        con={'server'  : 'smtp.mail.yahoo.com',
             'port'    : '587',
             'from'    : '@yahoo.com',
             'pass'     : '',
             'to'      : '@gmail.com',
             'subject' : 'My Contact Form'
            }  
        form={}
        for key,val in request.form.items():
            if key=='submit':continue
            form[key]=val
        if send(con,form):return 'done'
    return 'error'      
    

