import tkinter as tk
from tkinter import ttk
import requests, ephem
import matplotlib.pyplot as plt
import numpy as np
from astro_data import AstroData
from weather_data import WeatherData

HEIGHT = 600
WIDTH = 800


# def getAstroData(city):
#     url = 'http://api.weatherapi.com/v1/astronomy.json'
#     key = 'b8814e409a554c4888241017211505'
#     params = {'q': city, 'key': key}
#     astroData = requests.get(url, params=params).json()
#     try:
#         name = astroData['location']['name'] + ", " + astroData['location']['region'] + ", " + astroData['location']['country']
#         lat =  astroData['location']['lat']
#         lon = astroData['location']['lon']
#         sunrise = astroData['astronomy']['astro']['sunrise']
#         sunset = astroData['astronomy']['astro']['sunset']
#         moonrise = astroData['astronomy']['astro']['moonrise']
#         moonset = astroData['astronomy']['astro']['moonset']
#         moonphase = astroData['astronomy']['astro']['moon_phase']
#         moon_ill = astroData['astronomy']['astro']['moon_illumination']
#         clouds = getWeather(city)
#         updateTreeTable(getPlanetData(str(lat), str(lon)))
#         label['text'] = formatAstroData(name, lat, lon, sunrise, sunset, moonrise, moonset, moonphase, moon_ill, clouds)
#
#         print(astroData)
#     except:
#         label['text'] = 'No Data Found'
#         index = 0
#         for item in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune']:
#             tree_table.insert(parent='', index=index, values=(item, 'N/A', 'N/A'))
#             index += 1

def getWeather(city):
    url = 'http://api.weatherapi.com/v1/current.json'
    key = 'b8814e409a554c4888241017211505'
    params = {'q': city, 'key': key}
    weatherData = requests.get(url, params=params).json()
    clouds = str(weatherData['current']['cloud']) + "%"

    return clouds


# def formatAstroData(name,lat,lon, sunrise, sunset, moonrise, moonset, moonphase, moon_ill, clouds):
#     return name + '\nLatitude: ' + str(lat) + ' Longitude: ' + str(lon) \
#            + '\n\nSunrise: ' + sunrise + '\nSunset: ' \
#            + sunset + '\n\nMoonrise: ' + moonrise + '\nMoonset: ' \
#            + moonset + "\nPhase: " + moonphase + '\nIllumination: ' \
#            +moon_ill +'%' + '\n\nCloud Coverage: ' + clouds

# def getPlanetData(lat, lon):
#     obs = ephem.Observer()
#     obs.lat = lat
#     obs.lon = lon
#     format = '%a %I:%M %p'
#
#     planet_data = []
#
#     planets = {
#         'mercury': ephem.Mercury(),
#         'venus': ephem.Venus(),
#         'mars': ephem.Mars(),
#         'jupiter': ephem.Jupiter(),
#         'saturn': ephem.Saturn(),
#         'uranus': ephem.Uranus(),
#         'neptune': ephem.Neptune()
#     }
#
#     for object in planets:
#         planets[object].compute(obs)
#         print(planets[object].name, planets[object].alt)
#
#         if '-' in str(planets[object].alt):  # If below horizon, calculate next rise and next set, adds to list
#             rise_time = obs.next_rising(planets[object], start=ephem.now())
#             local_rise_time = ephem.localtime(rise_time)
#             formated_rise_time = local_rise_time.strftime(format)
#
#             set_time = obs.next_setting(planets[object], start=ephem.now())
#             local_set_time = ephem.localtime(set_time)
#             formated_set_time = local_set_time.strftime(format)
#
#             new_entry = [str(planets[object].name), formated_rise_time, formated_set_time]
#             planet_data.append(new_entry)
#
#         else:   # If above horizon, calculates previous rise and next set
#             rise_time = obs.previous_rising(planets[object], start=ephem.now())
#             local_rise_time = ephem.localtime(rise_time)
#             formated_rise_time = local_rise_time.strftime(format)
#
#             set_time = obs.next_setting(planets[object], start=ephem.now())
#             local_set_time = ephem.localtime(set_time)
#             formated_set_time = local_set_time.strftime(format)
#
#             new_entry = [str(planets[object].name), formated_rise_time, formated_set_time]
#             planet_data.append(new_entry)
#
#     print(planet_data)
#     return planet_data

# def updateTreeTable(planetData):
#     index = 0
#     for item in planetData:
#         tree_table.insert(parent='', index=index, values=(item[0], item[1], item[2]))
#         index += 1

def search_button_click(city):
    astro = AstroData(city)


def hourly_cloud_vis_chart(city, day):
    weather = WeatherData(city)

    plt.rcParams['toolbar'] = 'None'

    cloud_data = weather.get_hourly_cloud_data(day)
    vis_data = weather.get_hourly_visibility_data(day)
    x_data = ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm',
              '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']

    fig, axs = plt.subplots(2)

    axs[0].plot(x_data, cloud_data, 'o-', color='black', linewidth=2)
    axs[0].set_title('Cloud Coverage', fontsize=14, fontweight='bold')
    axs[0].set_xlabel('Time', fontsize=11)
    axs[0].set_ylabel('Cloud Coverage (%)', fontsize=11)

    axs[1].plot(x_data, vis_data, 'o-', color='black', linewidth=2)
    axs[1].set_title('Visibility', fontsize=14, fontweight='bold')
    axs[1].set_xlabel('Time', fontsize=11)
    axs[1].set_ylabel('Visibility (miles)', fontsize=11)

    gradient = np.linspace(0, 1, 800).reshape(-1, 1)
    axs[0].imshow(gradient, extent=[-0.9, 23.5, -1, 105], aspect='auto', cmap='RdYlGn')
    axs[1].imshow(gradient, extent=[-0.9, 23.5, -1, 11], aspect='auto', cmap='RdYlGn_r')


    fig.tight_layout()
    fig.set_figwidth(13)
    fig.set_figheight(8)
    plt.show()




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bkg_image = tk.PhotoImage(file='stars.png')
bkg_label = tk.Label(root, image=bkg_image)
bkg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#4286ff', bd=7)
frame.place(relwidth=0.85, relheight=0.08, relx=0.5, rely=0.05, anchor='n')

today_weather = tk.Frame(root, bg='#4286ff', bd=4)
today_weather.place(relwidth=0.33, relheight=0.2, relx=0, rely=0.15, anchor='nw')
today_weather_text = tk.Label(today_weather, text='Today')
today_weather_text.place(relwidth=1, relheight=1)

tomorrow_weather = tk.Frame(root, bg='#4286ff', bd=4)
tomorrow_weather.place(relwidth=0.34, relheight=0.2, relx=0.33, rely=0.15, anchor='nw')
tom_weather_text = tk.Label(tomorrow_weather, text='Tomorrow')
tom_weather_text.place(relwidth=1, relheight=1)

day_after_weather = tk.Frame(root, bg='#4286ff', bd=4)
day_after_weather.place(relwidth=0.33, relheight=0.2, relx=0.67, rely=0.15, anchor='nw')
day_after_weather_text = tk.Label(day_after_weather, text='Day After')
day_after_weather_text.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#4286ff', bd=7)
lower_frame.place(relwidth=0.85, relheight=0.70, relx=0.5, rely=0.25, anchor='n')

cityEntry = tk.Entry(frame, bg='white')
cityEntry.place(relwidth=0.70, relheight=1)

button = tk.Button(frame, text="Search", command= lambda: search_button_click(cityEntry.get()))
button.place(relx=0.70, rely=0, relwidth=0.30, relheight=1)

# test_button = tk.Button(frame, text="Test", command= lambda: formatPlanetData(getPlanetData('41.79', '-88.15')))
# test_button.place(relx=0.850, rely=0, relwidth=0.15, relheight=1)

label = tk.Label(lower_frame, text='Enter your city in the box above.')
label.place(relwidth=1, relheight=0.55)

tree_table = ttk.Treeview(lower_frame)
tree_table['columns']=('Planet', 'Rises At', 'Sets At')
tree_table.column('#0', width=0, stretch='no')
tree_table.column('Planet', anchor='center', width=80)
tree_table.column('Rises At', anchor='center', width=80)
tree_table.column('Sets At', anchor='center', width=80)
tree_table.heading('#0', text='', anchor='center')
tree_table.heading('Planet', text='Planet', anchor='center')
tree_table.heading('Rises At', text='Rises At', anchor='center')
tree_table.heading('Sets At', text='Sets At', anchor='center')
tree_table.place(relwidth=1, relheight=0.42, rely=0.57)

index = 0
for item in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune']:
    tree_table.insert(parent='', index=index, values=(item, 'N/A', 'N/A'))
    index += 1

root.mainloop()


