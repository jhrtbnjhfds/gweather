from flask import Flask, render_template
import requests
from datetime import datetime as dt
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    api_key = '57f3be255ae69caa088f12eaf720476d'
    city = 'Adelaide'
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&APPID=" + api_key
    print(url)
    response = requests.get(url).json()
    print(response)
    city_name = response["city"]["name"]
    city_population = response["city"]["population"]
    print(city_name)
    print(city_population)

    forecast_list = response["list"]
    forecast_data = []
    index = 0
    while index < len(forecast_list):
        dt_txt = forecast_list[index]['dt_txt']
        temp = forecast_list[index]['main']['temp']
        icon = forecast_list[index]['weather'][0]['icon']
        description = forecast_list[index]['weather'][0]['description']

        date_object = dt.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        day_of_week = date_object.weekday()
        print(day_of_week)
        # You can also get the day name
        day_name = date_object.strftime('%A')
        print(day_name)
        dict = {
            "dt_txt": dt_txt,
            "day_name": day_name,
            "temp": temp,
            "icon_url": "http://openweathermap.org/img/w/" + icon + ".png",
            "description": description

        }
        forecast_data.append(dict)
        index += 8
    print(forecast_data)



    return render_template('home.html', forecast_data=forecast_data)


if __name__ == '__main__':
    app.run()

