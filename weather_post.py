from crypt import methods

from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__) #creates the Flask website app
@app.route("/",methods=["GET","POST","PATCH"]) #decorator
def home():
    if request.method == "POST":
        username = request.form.get("username")



    data = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    data_received = requests.get(url, params=data)
    json_data = data_received.json()

    return f"""
    <h1> Weather Data for {json_data['sys']['name']} </h1>
    <p> The temperature is {json_data['main']['temp']} </p>
    <p> The humidity is {json_data['main']['humidity']}% </p>
    <p> The wind speed is {json_data['wind']['speed']} </p>
    """
app.run(debug=True)