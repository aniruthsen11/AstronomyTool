import requests, ephem

class astroData:
    def __init__(self, city):
        URL = 'http://api.weatherapi.com/v1/astronomy.json'
        KEY = 'b8814e409a554c4888241017211505'
        params = {'q': city, 'key': KEY}
        astroData = requests.get(URL, params=params).json()
        try:
            self.name = astroData['location']['name'] + ", " + astroData['location']['region'] + ", " + \
                   astroData['location']['country']
            self.lat = astroData['location']['lat']
            self.lon = astroData['location']['lon']
            self.sunrise = astroData['astronomy']['astro']['sunrise']
            self.sunset = astroData['astronomy']['astro']['sunset']
            self.moonrise = astroData['astronomy']['astro']['moonrise']
            self.moonset = astroData['astronomy']['astro']['moonset']
            self.moonphase = astroData['astronomy']['astro']['moon_phase']
            self.moon_ill = astroData['astronomy']['astro']['moon_illumination']

            self.obs = ephem.Observer(lat=self.lat, lon=self.lon)
            self.format = '%a %I:%M %p'

            print('init statement complete')
        except:
            pass


    def getPlanetData(self):
        obs = ephem.Observer()
        obs.lat = self.lat
        obs.lon = self.lon
        format = '%a %I:%M %p'

        planet_data = []

        planets = {
            'mercury': ephem.Mercury(),
            'venus': ephem.Venus(),
            'mars': ephem.Mars(),
            'jupiter': ephem.Jupiter(),
            'saturn': ephem.Saturn(),
            'uranus': ephem.Uranus(),
            'neptune': ephem.Neptune()
        }

        for object in planets:
            print(planets[object].name)

    def format(self):
        return self.name + '\nLatitude: ' + str(self.lat) + ' Longitude: ' + str(self.lon) \
               + '\n\nSunrise: ' + self.sunrise + '\nSunset: ' \
               + self.sunset + '\n\nMoonrise: ' + self.moonrise + '\nMoonset: ' \
               + self.moonset + "\nPhase: " + self.moonphase + '\nIllumination: ' \
               + self.moon_ill + '%'



d = astroData('Naperville')
