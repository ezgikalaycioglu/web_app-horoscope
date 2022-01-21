from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()
import os
posgres=os.getenv("POSGRES")

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=posgres #connecting database to app
db=SQLAlchemy(app) #creating SQLAlchemy object(database) for the flask app



class Data(db.Model): #Creating database model
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120))
    birth_=db.Column(db.Date)
    sign_=db.Column(db.String)
    stone_=db.Column(db.String)

    def __init__(self,email_,birth_,sign_,stone_): #initialization of variables
        self.email_=email_
        self.birth_=birth_
        self.sign_=sign_
        self.stone_=stone_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST']) #normalde get method alıyor. başka bir metod varsa yazmamız lazım
def success():
    if request.method=='POST':
        email=request.form["email_name"] #getting values from app
        birth=request.form["birth_name"]
        birthdate=datetime.strptime(birth, '%Y-%m-%d')
        month=birthdate.month
        day=birthdate.day
        sign="sign"
        stone="stone"
        if (month==4 and day<=20) or (month==3 and day>=21):
            sign="Aries"
            stone="BloodStone"
        elif (month==5 and day<=21) or (month==4 and day>=20):
            sign="Taurus"
            stone="Sapphire"
        elif (month==6 and day<=21) or (month==5 and day>=21):
            sign="Gemini"
            stone="Agate"
        elif (month==7 and day<=23) or (month==6 and day>=21):
            sign="Cancer"
            stone="Emerald"
        elif (month==8 and day<=23) or (month==7 and day>=23):
            sign="Leo"
            stone="Onyx"
        elif (month==9 and day<=23) or (month==8 and day>=23):
            sign="Virgo"
            stone="Carnelian"
        elif (month==10 and day<=23) or (month==9 and day>=23):
            sign="Libra"
            stone="Peridot"
        elif (month==11 and day<=22) or (month==10 and day>=23):
            sign="Scorpio"
            stone="Beryl"
        elif (month==12 and day<=22) or (month==11 and day>=23):
            sign="Sagittarius"
            stone="Topaz"
        elif (month==1 and day<=20) or (month==12 and day>=22):
            sign="Capricorn"
            stone="Ruby"
        elif (month==2 and day<=19) or (month==1 and day>=20):
            sign="Aquarius"
            stone="Garnet"
        else:
            sign="Pisces"
            stone="Amethyst"

        print(email,sign, stone)
        #send_email(email,height)
        data=Data(email,birth,sign,stone) #creating an object of database class
        db.session.add(data) #adding values to database
        db.session.commit() #committing chances
        send_email(email,sign,stone)
        return render_template("success.html")

if __name__=='__main__':
    app.debug=True
    app.run()
