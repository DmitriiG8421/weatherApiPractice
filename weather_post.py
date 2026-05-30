from flask import Flask, render_template, request
# Flask creates the web application
# render_template loads the HMTL file
# request gets user input from the form
import requests

# sends HTTP requests to OpenWeather (chef) API (waiting staff)
import os

# reads env data (environment variables)

from dotenv import load_dotenv

# loads values from the .env file
load_dotenv()

app = Flask(__name__)  # creates the Flask website app

API_KEY = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST", "PATCH"])  # decorator
def home():
    username = ""
    city = ""
    if request.method == "POST":
        username = request.form.get("username")
        city = request.form.get("city")

    return f"""
    <h1>My First Flask Website</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Enter your user name">
            <button type="submit">Submit</button>
        <input type="text" name="city" placeholder="Enter your city name">
            <button type="submit">Submit</button>
    </form>
    <p>Your username is {username}</p>
    <p>Your city is {city}</p>
    """


app.run(debug=True)