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
        email = request.form['email']
        books= request.form['books']
        description= request.form['desc']
        ref = db.reference("/")
        userno = "user"+str(len(ref.get())+1)
        txt= {
        "{}".format(userno):
          {
            "email": "{}".format(email),
            "book": "{}".format(books),
            "description": "{}".format(description)
          }
        }
        ref.update(txt)
        print(databasetxt)

    return render_template('index.html', **locals())


@app.route('/books', methods=["GET", "POST"])
def books():

    ref = db.reference("/")
    databasetxt= (ref.get())

    if request.method == 'POST':
        email = request.form['email']
        useremail = request.form['useremail']
        description = request.form['description']
        bookname = request.form['book']
        usermessage= request.form['message']
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
                    "title": "Someone wants your books"
                    },
                     {
                     "type": "image",
                     "src": "https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/img/4.png"
                     },
                    {
                    "type": "text",
                    "content": "**Book you put up for donation:** {}".format(bookname)
                    },
                    {
                    "type": "text",
                    "content": "** {}** is requesting your book ".format(useremail)
                    },
                                        {
                    "type": "text",
                    "content": "** Thier Message: **{}".format(usermessage)
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

    return render_template('books.html', **locals(), data=databasetxt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)