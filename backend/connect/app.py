import email
from email import message
from email.message import EmailMessage
import re
from click import prompt
from flask import Flask, render_template, request
import requests
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate(" ")
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':" "
	})

app = Flask(__name__)

url = "https://api.courier.com/send"

@app.route('/', methods=["GET", "POST"])
def index():

    ref = db.reference("/")
    databasetxt= (ref.get())

    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']
        email = request.form['email']
        social = request.form['social']
        ref = db.reference("/")
        userno = "user"+str(len(ref.get())+1)
        txt= {
        "{}".format(userno):
          {
            "name": "{}".format(name),
            "about": "{}".format(about),
            "email": "{}".format(email),
            "social": "{}".format(social)
          }
        }
        ref.update(txt)
        print(databasetxt)

    return render_template('index.html', **locals())


@app.route('/connect', methods=["GET", "POST"])
def connect():

    ref = db.reference("/")
    databasetxt= (ref.get())

    if request.method == 'POST':
        nameofuser = request.form['nameofuser']
        useremail = request.form['useremail']
        email = request.form['email']
        message = request.form['message']
        ref = db.reference("/")
        payload = {
            "message": {
                "to": { 
                "email": "{}".format(email)
                },
                "content":{
                "elements": [
                    {
                    "type": "meta",
                    "title": "Someone wants to connect with you"
                    },
                                         {
                     "type": "image",
                     "src": "https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/img/3.png"
                     },
                    {
                    "type": "text",
                    "content": "** {} **wants to connect with you ".format(nameofuser)
                    },
                    {
                    "type": "text",
                    "content": "** Thier Email: ** {}".format(useremail)
                    },
                     {
                    "type": "text",
                    "content": "** Thier Message:  ** {}".format(message)
                    }
                ],
                "version": "2022-01-01",
                }
            }
            }
        headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Bearer pk_test_APIKEY"
                }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)

    return render_template('connect.html', **locals(), data=databasetxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)