# Message from developers
This is an open-source project. Feel Free to Fork it or Make Pull Requests to this project. We would love it if anyone wanted to contribute to this project and want to help in creating a perfect student platform. You can contact us at cyrixninja#0157 or ninnza#2681 if you got any doubts regarding implementing any new feature in this project. You should host each app individually and add their iframe in their respective HTML page. We used replit for hosting, you can use any services you like. If you face any difficulty in testing or usage, you can contact us for files with API or for our API keys. You can also use node js, go, or any programming language. Since the main page is static and features are embedded in the main page you can use always add a page with a hosted backend in any programming language and it would work flawlessly.
We can't wait to see how this platform turns out in the future. Thanks for showing your interest in our project.😁

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

# Example Code for futher development
<h3>Our Backend is hosted seperately and is embedded in our website</h3>

<h2>Python Example Code for Storing Data into Firebase in Flask Webapp</h2>

```
#importing libraries
import re
from click import prompt
from flask import Flask, render_template, request
import requests
import firebase_admin
from firebase_admin import db

#connecting with realtime database
cred_obj = firebase_admin.credentials.Certificate(" ")
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':" "
	})
	
#initializing flask app
 app = Flask(__name__)
 @app.route('/', methods=["GET", "POST"])
def index():

    ref = db.reference("/")
    databasetxt= (ref.get())

    if request.method == 'POST':
        #fetching data from the html webapp
        name = request.form['name']
        about = request.form['about']
        email = request.form['email']
        social = request.form['social']
	#feeding the data into the database
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
#importing libraries
from flask import Flask, render_template, request
import requests
url = "https://api.courier.com/send"
app = Flask(__name__)

#initializing flask app
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == 'POST':
        #fetching data from the html webapp
        username = request.form['username']
        question = request.form['question']
        email = request.form['email']
        reply = request.form['reply']
	#sending mail using courier api
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
# Usage
<h3>You can run each backend file by going into thier directory and using</h3>

```
flask run
```
<h3>You can host the backend anywhere you like and paste the url in iframe as follows in thier respective HTML</h3>
<img src="https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/screenshots/screenshot1.png" alt="image">
<br>
<h3>You should also add the respective API Keys in the backend </h3>
<br>
<h3>For Cohere in AI Advice</h3>
<img src="https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/screenshots/screenshot2.png" alt="image">
<br>
<h3>You should add api key in every app.py found in backend.You can add it here</h3>
<img src="https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/screenshots/screenshot3.png" alt="image">
<br>
<h3>You should also add database url and firebase json here</h3>
<img src="https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/screenshots/screenshot4.png" alt="image">
<h3>You can learn how to use firebase in python and generate json here <a href="https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/">here</a> </h3>
<br>

