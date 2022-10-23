import email
from email.message import EmailMessage
import re
from click import prompt
from flask import Flask, render_template, request
import requests
import cohere

co = cohere.Client('APIKEY')
app = Flask(__name__)

url = "https://api.courier.com/send"
@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        email = request.form['email']
        query = request.form['query']
        response = co.generate(
        model='xlarge',
        prompt='Question:{}\nAnswer:\n\n-'.format(query),
        max_tokens=150,
        temperature=1.1,
        k=0,
        p=0.75,
        frequency_penalty=0.48,
        presence_penalty=0,
        stop_sequences=["-"],
        return_likelihoods='NONE')
        txtresp= response.generations[0].text
        payload = {
        "message": {
            "to": { 
            "email": "{}".format(email)
            },
            "content":{
            "elements": [
                {
                "type": "meta",
                "title": "Reply from Education Advice"
                },
                {
                    "type": "image",
                     "src": "https://raw.githubusercontent.com/cyrixninja/CourierHacks/main/img/2.png"
                     },
                {
                "type": "text",
                "content": "**You asked: {}**".format(query)
                },
                {
                "type": "text",
                "content": "Response: {}".format(txtresp)
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

 

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)