from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['DEBUG']=True
@app.route('/')
def index():

    city='Las Vegas'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1e9dd8dfac35cb3e8b7090f24c07f3e3"

    r=requests.get(url.format(city)).json()

    weather={
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    print(weather)


    return render_template('weatherApp.html', weather=weather)
