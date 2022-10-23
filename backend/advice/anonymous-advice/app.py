import email
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
        username = request.form['username']
        question = request.form['question']
        email = request.form['email']
        ref = db.reference("/")
        userno = "user"+str(len(ref.get())+1)
        txt= {
        "{}".format(userno):
          {
            "username": "{}".format(username),
            "question": "{}".format(question),
            "email": "{}".format(email)
          }
        }
        ref.set(txt)
        print(databasetxt)

    return render_template('index.html', **locals())


@app.route('/advice', methods=["GET", "POST"])
def advice():

    ref = db.reference("/")
    databasetxt= (ref.get())

    if request.method == 'POST':
        username = request.form['username']
        question = request.form['question']
        email = request.form['email']
        reply = request.form['reply']
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
                    "title": "Someone replied"
                    },
                                                             {
                     "type": "image",
                     "src": "https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/img/2.png"
                     },
                    {
                    "type": "text",
                    "content": "**Question you asked:** {}".format(question)
                    },
                    {
                    "type": "text",
                    "content": "** Reply from anonymous user:** {}".format(reply)
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

    return render_template('advice.html', **locals(), data=databasetxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)