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

- Python 3.12
- Flask
- SQLAlchemy
- Requests (for making API calls)

You can install the required Python packages using the following command:

```bash
pip install flask sqlalchemy requests
'''

## Usage
- Open the app in your web browser.
- Enter the name of a city in the search bar.
- Click on the "Get Weather" button to fetch the current weather details for the entered city.
- Click the "Add" button to add the city to your list of tracked cities.
- The application will display the temperature, weather description, humidity, and other relevant information for the cities in your list.
- Click the cross button next to the city name to remove a city from the list.

## Screenshot
![image](https://github.com/user-attachments/assets/150f8a80-1734-464f-bbb6-6d89ec798b55)
