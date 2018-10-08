import csv
import numpy as np
import pandas as pd

weather = ['rainy', 'stormy', 'sunny', 'cloudy', 'hot', 'cold', 'dry', 'wet', 'windy', 'snow']
traffic = ['low', 'moderate', 'high']
elevation = ['low', 'moderate', 'high']
bikeLine = ['low', 'moderate', 'high']
dayTime = ['morning', 'afternoon', 'evening']
day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
distance = ['extremely_short', 'short', 'medium', 'long', 'extremely_long']
duration = ['low', 'moderate', 'high']
temperature = ['temp-0-10', 'temp-10-20', 'temp-20-30', 'temp-30-40', 'temp-40-50', 'temp-50-60', 'temp-60-70',
               'temp-70-80', 'temp-80-90', 'temp-90-100']
# arrays for history:
Elevation_Weather = np.zeros([9, 3], dtype=int)
Duration_weather = np.zeros([9, 3], dtype=int)
duration_Temperature = np.zeros([10, 3], dtype=int)
Elevation_Traffic = np.zeros([3, 3], dtype=int)
BikeLanes_Traffic = np.zeros([3, 3], dtype=int)

elevation_index=0
weather_index =0
duration_index=0
traffic_index=0
bikelane_index=0
temperature_index=0

#MATRICES = ['Elevation_Weather', 'Time_Weather', 'Time_Temperature', 'Elevation_Traffic', 'BikeLanes_Traffic',
      #      'Time_TimeOfDay', 'Time_Weekday']

with open('routes.csv', 'r')as f:
    routes = list(csv.reader(f))
routes = np.array(routes[1:])

#print(routes)
'''
# read routes and put it in dataFrame:
routes = pd.read_csv('routes.csv')
'''

for route in routes:
    print(route[0])
    print(elevation[0])
    if (route[0] in elevation) and (route[1] in weather):
        elevation_index = elevation.index(route[0])
        print(route[9])
        print(elevation_index)
        print(route[1])
        print(weather.index(route[1]))
        weather_index = weather.index(route[1])
        Elevation_Weather[weather_index, elevation_index] += int(route[9])

    if (route[8] in duration) and (route[1]in weather):
        weather_index = weather.index(route[1])
        duration_index = duration.index(route[8])
        Duration_weather[weather_index, duration_index] += int(route[9])

    if(route[8] in duration)and (route[2] in temperature):
        duration_index = duration.index(route[8])
        temperature_index = temperature.index(route[2])
        duration_Temperature[temperature_index, duration_index] += int(route[9])

    if(route[0]in elevation)and (route[3] in traffic):
        elevation_index = elevation.index(route[0])
        traffic_index = traffic.index(route[3])
        Elevation_Traffic[traffic_index, elevation_index] += int(route[9])

    if(route[3]in traffic) and (route[6] in bikeLine):
        traffic_index = traffic.index(route[3])
        bikelane_index = bikeLine.index(route[6])
        BikeLanes_Traffic[traffic_index, bikelane_index] += int(route[9])




print(Elevation_Weather)
print(Duration_weather)
print(duration_Temperature)
print(Elevation_Traffic)
print(BikeLanes_Traffic)






