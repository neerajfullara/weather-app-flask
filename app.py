from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY'] = 'thisisasecret'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

def get_city_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=1e9dd8dfac35cb3e8b7090f24c07f3e3"
    r=requests.get(url).json()
    return r

@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        error_msg = ""
        new_city = request.form.get('city')

        if new_city:
            exist_city = City.query.filter_by(name=new_city).first()

            if not exist_city:
                new_city_data = get_city_weather_data(new_city)
                if new_city_data['cod'] == 200:
                    new_city_obj = City(name=new_city)
                    db.session.add(new_city_obj)
                    db.session.commit()
                else:
                    error_msg = "City doesn't exists in the world"
            else:
                error_msg = "City already exists in the database!"
        
        if error_msg:
            flash(error_msg, 'error')
        else:
            flash("City added successfully!", 'success')

    cities = City.query.all()
    weather_data=[]

    for city in cities:
        
        r = get_city_weather_data(city.name)

        weather={
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(weather)


    return render_template('weatherApp.html', weather_data=weather_data)


@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()
    flash(f"City {city.name} has been deleted!", 'success')
    return redirect(url_for('index'))