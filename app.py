from flask import Flask, render_template, request
#Flask creates the web application
#render_template loads the HMTL file
#request gets user input from the form
import requests

#sends HTTP requests to OpenWeather (chef) API (waiting staff)
import os

#reads env data (environment variables)

from dotenv import load_dotenv
#loads values from the .env file

#step-1:

load_dotenv()

#step-2: start creating the web app

app = Flask(__name__)

#step-3: GET the API key from the .env

API_KEY = os.getenv("API_KEY")