from flask import Flask,redirect,render_template,url_for,session,request
from datetime import datetime,timedelta
import mysql.connector
import json
import random

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ajay@2002",
    database="mydatabase",
    
)
mycursor=mydb.cursor(dictionary=True)

app=Flask(__name__)
app.secret_key="jone"
app.permanent_session_lifetime=timedelta(days=3)


@app.route('/',methods=["GET","POST"])
def index():
    
    return render_template("project.html")

@app.route('/Home',methods=["GET","POST"])
def home():
    
    return render_template("project.html")

@app.route('/blog',methods=["GET","POST"])
def blog():
    
    
    return render_template("blog.html")

@app.route('/sports',methods=["GET","POST"])
def sports():
    
    
    return render_template("sports.html")

@app.route('/travel',methods=["GET","POST"])
def travel():
    
    
    return render_template("travel.html")



@app.route('/recent',methods=["GET","POST"])
def recent():
    if request.method=='GET':
        try:
            mycursor.execute("select * from blog")
            result=mycursor.fetchall()
            return render_template("recent.html" , result=result)
        except Exception as e:
            msg="Something Wrong"
            return render_template("blog.html" , msg=msg)
            
    else:
        return render_template("project.html")

@app.route('/publish',methods=["GET","POST"])
def publish():
    if request.method=='POST':
        data=request.data.decode("utf-8")
        jdata=json.loads(data)
        mycursor.execute("insert into blog(title , blog) values( %s, %s ) " ,(jdata['title'], jdata['blog']))
        mydb.commit()
        return "ok"
    else:
        return render_template("project.html")

if __name__=="__main__":
    app.run(debug=True)