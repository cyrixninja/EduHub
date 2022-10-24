# API,Frameworks and Plaforms used in development

<a href="https://www.courier.com/docs/guides/getting-started/python/">Courier API</a>

<a href="https://flask.palletsprojects.com/en/2.2.x/">Python Flask </a>

<a href="https://firebase.google.com/docs/database">FireBase Realtime Database</a>

<a href="https://docs.cohere.ai/">Cohere's NLP API</a>

<a href="https://replit.com/">Replit </a>

<a href="https://code.visualstudio.com/">Visual Studio Code</a>
 
 <a href="https://github.com/">Github</a>

# What we used API's and Framworks for 

Courier API- Courier provides app-to-user notifications and is  central to our app as it is based totally on receiving Email Notification.We used <a href="https://www.courier.com/docs/elemental/">Courier Elemental </a> for our app to user notifications.It provides really good and quick notification to our users.

Python Flask- Flask serves as an backend to our project

Firebase Realtime Database- We used it as an database to store user data.It's very safe and secure to use.

Cohere's NLP API- We used to generate responses in our AI Advice Feature.

Github Pages- We used it to host our website

# How does our webapp work?
<h3>Our Backend is hosted seperately and is embedded in our website</h3>

<h2>Python Example Code for Storing Data into Firebase in Flask Webapp</h2>

```
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
 if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

```
<br>
<h2>Python Example Code for sending email to user using Courier in Flask Webapp</h2>

```

from flask import Flask, render_template, request
import requests
url = "https://api.courier.com/send"
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
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

    return render_template('index.html', **locals(), data=databasetxt)

```

# Feel Free to Fork it or Make Pull Requests to this project.We would love it if anyone wants to contribute to this project and want to help in creating a perfect student platform
You can contact us on- cyrixninja#0157 or ninnza#2681 if you got any doubts in implementing any feauture in this project
