import base64

from flask import Flask, render_template, request, session, url_for, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from io import BytesIO
from datetime import datetime
import os
import smtplib
from datetime import *

app = Flask(__name__)
app.secret_key = "abcd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///burrowBuddy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
APP_ROOT=os.path.dirname(os.path.abspath(__file__))

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(50))
    email=db.Column(db.String(100))
    password=db.Column(db.String(50))
    contactNo=db.Column(db.String(15))
    Resp_pts=db.Column(db.Integer)
    bonus_pts=db.Column(db.Integer)
    

    def __init__(self, Name,email,password, contactNo, Resp_pts, bonus_pts):
        self.Name=Name
        self.email=email
        self.password=password
        self.contactNo=contactNo
        self.Resp_pts=Resp_pts
        self.bonus_pts=bonus_pts

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    category=db.Column(db.String(100))
    owner_id=db.Column(db.String(50))
    isAvailable=db.Column(db.String(15))
    assignedTo=db.Column(db.String(50))
    returnDate=db.Column(db.String(50))
    img=db.Column(db.Text)
    mimetype=db.Column(db.Text)
    img_name=db.Column(db.String(300))
    

    def __init__(self, title, category, owner_id, isAvailable, assignedTo, returnDate, img, mimetype, img_name):
        self.title=title
        self.category=category
        self.owner_id=owner_id
        self.isAvailable=isAvailable
        self.assignedTo=assignedTo
        self.returnDate=returnDate
        self.img=img
        self.mimetype=mimetype
        self.img_name=img_name

class RequestsList(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer)
    product_title= db.Column(db.String(50))
    owner_id=db.Column(db.Integer)
    assignedTo=db.Column(db.String(50))
    assignedToId=db.Column(db.Integer)
    returnDate=db.Column(db.String(50))
    requestsMade=db.Column(db.String(50))
    requestsMadeId=db.Column(db.Integer)

    def __init__(self, product_id, owner_id, assignedTo, returnDate, requestsMade, assignedToId, requestsMadeId):
        self.product_id=product_id
        self.owner_id=owner_id
        self.returnDate=returnDate
        self.requestsMade=requestsMade
        self.requestsMadeId=requestsMadeId
        self.assignedTo=assignedTo
        self.assignedToId=assignedToId

@app.route("/",methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        
        email = request.form['email']
        print(email)
        password = request.form['password']
        print(password)
        session['email'] = email
        
        admins = Users.query.all()
        print(admins)
        for admin in admins:
            #try:
            if email == admin.email:
                if password == admin.password:
                    session['userid']=admin.id
                    print(session['userid'])
                    products = Products.query.all()
                    users = Users.query.all()
                    print(products)
                    return render_template('home.html', products=products, users=users)
                else:
                    return render_template('login.html', credentials_incorrect=1)
            else:
                return render_template('login.html', credentials_incorrect=1)
            #except:
                #return "There is an error in logging in"
            
    else:
        return render_template('login.html', credentials_incorrect=0)

@app.route("/home",methods=['POST','GET'])
def home():
    if 'email' in session:
        if request.method == "POST" :
            return render_template('home.html', login=1)
            
        else:
            products = Products.query.all()
            users = Users.query.all()
            return render_template('home.html', products=products, users=users)

    else:
        return redirect(url_for('login'))

@app.route("/new_product",methods=['POST','GET'])    #title, category, owner_id, isAvailable, assignedTo, returnDate, img, mimetype, img_name
def new_product():
    if 'email' in session:
        if (request.method == 'POST') and (request.form.get("submit") == "submit"):
            title=request.form['title']
            category=request.form['category']
            print(title)
            print(category)
            owner_id=session['userid']
            isAvailable = 'yes'
            assignedTo = 'null'
            returnDate='null'
            img = request.files['img']
            filename = secure_filename(img.filename)
            mimetype = img.mimetype
            target = os.path.join(APP_ROOT, 'static/images/')
            destination = "/".join([target, filename])
            img.save(destination)
            new_entry=Products(title=title, category=category, owner_id=owner_id, isAvailable=isAvailable, assignedTo=assignedTo, returnDate=returnDate, img=img.read(), mimetype=mimetype, img_name=filename)

            try:
                db.session.add(new_entry)
                db.session.commit()
                return render_template('home.html')
            except:
                return "There is an error in sending the form"
            
        else:
            return render_template('newprod.html')

    else:
        return redirect(url_for('login'))

@app.route("/request", methods=['POST','GET'])
def request_pg():
    if 'email' in session:
        if request.method == "POST":
            return render_template('request.html')
            
        else:
            requestlist = RequestsList.query.all()
            return render_template('request.html', requestlist=requestlist)

    else:
        return redirect(url_for('login'))
    

if __name__ == "__main__":
    db.create_all()
    app.run()