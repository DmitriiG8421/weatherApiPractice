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
    city = ".................."
    weather_display = ""
    if request.method == "POST":
        city = request.form.get("city")
        if city != "":
            data = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }
            data_received = requests.get(url, params=data)
            json_data = data_received.json()
            if data_received.status_code == 200:
                temp_data = json_data["main"]["temp"]
                humidity_data = json_data["main"]["humidity"]
                weather_description = json_data["weather"][0]["description"]


                wind_speed = json_data["wind"]["speed"]
                wind_direction_degrees = json_data["wind"]["deg"]
                directions = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest"]
                wind_direction = directions[round(wind_direction_degrees/45) % 8 ]

                weather_display = f"""
                <h3>Weather</h3>
                <p>Tempertature is {temp_data}°C</p>
                <p>The description of the weather is that it is {weather_description}</p>
                <p>Humidity is {humidity_data}%</p>
                <p>Wind speed is {wind_speed} km/h</p>
                <p>Wind direction is {wind_direction} ({wind_direction_degrees}°)</p>
                """
            else:
                weather_display = f"""
                we can not find the city you are looking at
                """


    return f"""
    <h1>Weather for your city</h1>
    <form method="POST">
        <input type="text" name="city" placeholder="Enter your city name">
            <button type="submit">Submit</button>
    </form>
    <p>Your city is {city}</p>
    {weather_display}
    """

app.run(debug=True)