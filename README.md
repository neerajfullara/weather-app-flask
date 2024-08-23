# Weather App

A simple Weather App built using Flask and SQLAlchemy. This application allows users to fetch and display weather details for different cities using the OpenWeatherMap API. Users can search for their desired cities, add them to a list, and remove them if needed.

## Features

- Fetch current weather details for a city using the OpenWeatherMap API.
- Store user search queries and a list of favorite cities in a database using SQLAlchemy.
- Display city weather details, including temperature, humidity, weather description, and more.
- Users can search for a city and add it to their list of tracked cities.
- Cities can be removed from the list by clicking on the cross button next to the city name.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **OpenWeatherMap API**: Provides current weather data, forecasts, and historical data.
- **HTML/CSS**: For the front-end user interface.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- SQLAlchemy
- Requests (for making API calls)

You can install the required Python packages using the following command:

```bash
pip install flask sqlalchemy requests
