import tkinter as tk
from tkinter import ttk
import requests, ephem
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import astro_data

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

def updateTreeTable(planetData):
    index = 0
    for item in planetData:
        tree_table.insert(parent='', index=index, values=(item[0], item[1], item[2]))
        index += 1

def search_button_click(city):
    astro = astro_data(city)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bkg_image = tk.PhotoImage(file='stars.png')
bkg_label = tk.Label(root, image=bkg_image)
bkg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#4286ff', bd=7)
frame.place(relwidth=0.85, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

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
tree_table.place(relwidth=0.90, relheight=0.42, rely=0.57)

index = 0
for item in ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune']:
    tree_table.insert(parent='', index=index, values=(item, 'N/A', 'N/A'))
    index += 1

root.mainloop()



# observer = ephem.Observer()
# observer.lat = '41.615913'  # lat and long must be string not float
# observer.lon = '-88.204071'
#
# planets = [ephem.Mercury(), ephem.Venus(), ephem.Mars(), ephem.Jupiter(),
#            ephem.Saturn(), ephem.Uranus(), ephem.Neptune()]
# data = []
# x = range(24)
#
# for planet in planets:
#     planet_alt = []
#     for hour in range(24):
#         observer.date = ephem.now() + hour * ephem.hour
#         planet.compute(observer)
#         alt = str(planet.alt)
#         formatted_alt = int(alt[0:alt.find(':')])
#         planet_alt.append(formatted_alt)
#     data.append(planet_alt)
#     plt.plot(planet_alt, 'o:', label=str(planet.name))
#
# plt.style.use("seaborn")
#
# plt.hlines(0, 0, 24,'black', label='Horizon') # Horizon Line
# plt.axis([0,24,-90,90])
# plt.grid(True,  linestyle='--', linewidth=1)
# plt.legend()
# plt.title('Altitude Over Time')
# plt.ylabel('Altitude (Degrees)')
# plt.xlabel('Time from Now (Hours)')
# plt.show()


