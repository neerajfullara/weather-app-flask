from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()
    weather_data=[]

    # city = 'Las Vegas'
    for city in cities:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1e9dd8dfac35cb3e8b7090f24c07f3e3"

        r=requests.get(url.format(city.name)).json()

        weather={
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(weather)


    return render_template('weatherApp.html', weather_data=weather_data)
