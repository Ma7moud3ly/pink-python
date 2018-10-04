"""
Face Detection Web Application based on Python - Falsk microframework and OpenCV library
By Mahmoud Aly .. ma7moud3ly2012@gmail.com
"""
from flask import Flask,render_template,request,url_for
from face_detector import detect
from random import randint

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        img1=app.root_path+'/static/before.png'
        img2=app.root_path+'/static/after.png'
        f = request.files['image']
        f.save(img1)
        faces=detect(img1,img2)
        rand=randint(0,10000)
        return render_template('home.html',faces=faces,rand=rand)
    return render_template('home.html',faces=-1)

