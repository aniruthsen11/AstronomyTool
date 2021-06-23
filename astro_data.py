import requests, ephem

class AstroData:
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

            self.obs = ephem.Observer()
            self.obs.lat = str(self.lat)
            self.obs.lon = str(self.lon)
            self.format = '%a %I:%M %p'

        except:
            pass

    def get_planet_rise_set(self):
        obs = ephem.Observer()
        obs.lat = str(self.lat)
        obs.lon = str(self.lon)
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
            planets[object].compute(obs)

            if '-' in str(planets[object].alt):  # If below horizon, calculate next rise and next set, adds to list
                rise_time = obs.next_rising(planets[object], start=ephem.now())
                local_rise_time = ephem.localtime(rise_time)
                formated_rise_time = local_rise_time.strftime(format)

                set_time = obs.next_setting(planets[object], start=ephem.now())
                local_set_time = ephem.localtime(set_time)
                formated_set_time = local_set_time.strftime(format)

                new_entry = [str(planets[object].name), formated_rise_time, formated_set_time]
                planet_data.append(new_entry)
            else:  # If above horizon, calculates previous rise and next set
                rise_time = obs.previous_rising(planets[object], start=ephem.now())
                local_rise_time = ephem.localtime(rise_time)
                formated_rise_time = local_rise_time.strftime(format)

                set_time = obs.next_setting(planets[object], start=ephem.now())
                local_set_time = ephem.localtime(set_time)
                formated_set_time = local_set_time.strftime(format)

                new_entry = [str(planets[object].name), formated_rise_time, formated_set_time]
                planet_data.append(new_entry)

        return planet_data

    def format(self):
        return self.name + '\nLatitude: ' + str(self.lat) + ' Longitude: ' + str(self.lon) \
               + '\n\nSunrise: ' + self.sunrise + '\nSunset: ' \
               + self.sunset + '\n\nMoonrise: ' + self.moonrise + '\nMoonset: ' \
               + self.moonset + "\nPhase: " + self.moonphase + '\nIllumination: ' \
               + self.moon_ill + '%'


d = AstroData('Naperville')
print(d.get_planet_rise_set())