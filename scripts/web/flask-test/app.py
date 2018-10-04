from flask import Flask,render_template,request,session,redirect
import time,platform
app = Flask(__name__)

app.secret_key = 'd0dd342ebe25a8f6b7360e8c4183a5fc'
myLoginEmail='login_email@mail.com'
myLoginPass='123456'

def is_admin():
    if 'isAdmin' in session:
        isAdmin=session['isAdmin']
        return isAdmin
    return False


@app.route('/')
@app.route('/home/')
@app.route('/index/')
def home():
  return render_template('home.html',time=time.ctime()
,os=platform.system(),admin=is_admin())


@app.route('/about/')
@app.route('/about/<name>/')
@app.route('/about/<name>/<age>/')
def about(name='',age=''):
  colors=['red','green','blue','orange']  
  return render_template('about.html',name=name,
                          age=age,colors=colors)

@app.route('/jquery/')
def jquery():
  msg="Hello Flasker ^_^"  
  return render_template('jquery.html',msg=msg)

@app.route('/form/', methods=['POST', 'GET'])
def form():
      result=num1=num2=''
      if request.method == 'POST':
          num1=request.form['num1']
          num2=request.form['num2']
          opr =request.form['opr']
          try:result=eval(num1+opr+num2)
          except:result='Math Error'
      return render_template('form.html',result=result,num1=num1,num2=num2)

@app.route('/upload/',methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        from werkzeug.utils import secure_filename
        f = request.files['myfile']
        f.save(app.root_path+'/static/uploads/'+secure_filename(f.filename))
        return render_template('upload.html',done=True,file=f.filename)
    return render_template('upload.html')

@app.route('/login/',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email    = request.form['email']
        password = request.form['password']
        if(email==myLoginEmail and password==myLoginPass):
            session['isAdmin']=True
            return redirect(request.script_root+'/')
        else:
            return render_template('login.html',incorrect=True)            
    return render_template('login.html')

 

@app.route('/logout/')
def logout():
    session['isAdmin']=False
    return redirect(request.script_root+'/')
