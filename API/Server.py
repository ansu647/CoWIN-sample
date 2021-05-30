from flask import Flask,render_template,request
import requests
import json
from datetime import date
app = Flask(__name__,template_folder="../template")
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
    
@app.route("/district_id", methods=["POST"])
def i():
    y = request.form["district_id"]
    today = date.today().strftime("%d-%m-%Y")
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(y,today)
    payload={}
    headers = {
        "User-Agent":"PostmanRuntime/7.28.0",
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Connection":"keep-alive"
    }
    w = {

    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res= response.json()
    print(res)
    for session in res['sessions']:
        if session['available_capacity'] > 0:
            w[session['center_id']]=session['address']
    return render_template("output.html", json_object = w)



