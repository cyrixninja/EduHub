import re
from click import prompt
from flask import Flask, render_template, request
import requests
from gnews import GNews
import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate(' ')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':" "
	})


app = Flask(__name__)


url = "https://api.courier.com/send"


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        email = request.form['email']
        topictxt = request.form['topic']
        google_news = GNews(max_results=5)
        topic = google_news.get_news(topictxt)
        url1 = topic[0]['url'] 
        title1 = topic[0]['title']
        url2 = topic[1]['url']
        title2= topic[1]['title']
        url3 = topic[2]['url']
        title3= topic[2]['title']
        url4 = topic[3]['url']
        title4= topic[3]['title']
        url5 = topic[4]['url']
        title5= topic[4]['title']
        payload = {
 "message": {
    "to": { 
     "email": "{}".format(email)
    },
    "content":{
      "elements": [
        {
          "type": "meta",
          "title": "Your Daily News"
        },
        {
          "type": "image",
          "src": "https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/img/news-logo.png"
        },
        {
          "type": "text",
          "content": "**{}**".format(title1)
        },
        {
            "type": "action",
            "style": "button",
            "content": "Open",
            "align": "left",
            "href": "{}".format(url1)
        },
                {
          "type": "text",
          "content": "**{}**".format(title2)
        },
        {
            "type": "action",
            "style": "button",
            "content": "Open",
            "align": "left",
            "href": "{}".format(url2)
        },
                {
          "type": "text",
          "content": "**{}**".format(title3)
        },
        {
            "type": "action",
            "style": "button",
            "content": "Open",
            "align": "left",
            "href": "{}".format(url3)
        },
                {
          "type": "text",
          "content": "**{}**".format(title4)
        },
        {
            "type": "action",
            "style": "button",
            "content": "Open",
            "align": "left",
            "href": "{}".format(url4)
        },
                {
          "type": "text",
          "content": "**{}**".format(title5)
        },
        {
            "type": "action",
            "style": "button",
            "content": "Open",
            "align": "left",
            "href": "{}".format(url5)
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
        #adding to database
        ref = db.reference("/")
        userno = "user"+str(len(ref.get())+1)
        txt= {
        "{}".format(userno):
          {
            "email": "{}".format(email),
            "topic": "{}".format(topictxt)
          }
        }
        ref.update(txt)


 

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)