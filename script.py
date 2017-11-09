from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from email.mime.text import MIMEText
import smtplib

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:madhushree@localhost/email_1'
db = SQLAlchemy(app)

def send_email(email):
    from_email="interntask01@gmail.com"
    from_pass="01interntask"
    message="Hey there!!! Check out our website http://www.mysnippt.com/ "
    subject="Website"

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pass)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=email
    msg['From']=from_email

    gmail.send_message(msg) 



class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=False)
    

    def __init__(self, email_):
        self.email_=email_
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email = request.form['email_data']
       
        print(email)
        print(db.session.query(Data).filter(Data.email_==email).count())
        if  db.session.query(Data).filter(Data.email_==email).count() == 0:
            reg=Data(email)
            db.session.add(reg)
            db.session.commit()
            count=db.session.query(Data).count()
            send_email(email)
            return render_template('success.html')
        else:
            return render_template('test1.html')

if __name__=='__main__':
    app.debug=True
    app.run()

