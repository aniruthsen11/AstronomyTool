import requests, json

class WeatherData():

    def __init__(self, city):
        URL = 'http://api.weatherapi.com/v1/forecast.json'
        KEY = 'b8814e409a554c4888241017211505'
        params = {'q': city, 'key': KEY, 'days': 4}
        self.weather = requests.get(URL, params=params).json()
        # print(json.dumps(self.weather, indent=4))

    def get_hourly_cloud_data(self, day=int):
        hourly_cloud_data = []
        for hour in range(24):
            data_point = self.weather['forecast']['forecastday'][day]['hour'][hour]['cloud']
            hourly_cloud_data.append(data_point)
        return hourly_cloud_data

w = WeatherData('Naperville')
print(w.get_hourly_cloud_data(0))
print(w.get_hourly_cloud_data(1))
print(w.get_hourly_cloud_data(2))