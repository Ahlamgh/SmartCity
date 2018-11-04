import csv
import numpy as np
import pandas as pd
from pandas import DataFrame

independent = ['rainy', 'stormy', 'sunny', 'cloudy', 'hot', 'cold', 'dry', 'wet', 'windy', 'snowy', 'temp-10-0',
               'temp-0-10', 'temp-10-20', 'temp-20-25', 'temp-25-30', 'temp-30-40', 'temp-40',
               'low_traffic', 'high_traffic', 'medium_traffic', 'morning', 'afternoon', 'evening'
    , 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dependent = ['low_elevation', 'high_elevation', 'medium_elevation', 'low_bikeLane', 'medium_bikeLane', 'high_bikeLane',
             'extremly-short_distance', 'short_distance', 'medium_distance', 'long_distance', 'extremly-long_distance',
             'low_duration', 'medium_duration', 'high_duration']

# create data frame for user route frequency:

userProfileFrequency = pd.DataFrame(index=independent, columns=dependent, dtype=int)
userProfileFrequency = userProfileFrequency.fillna(0)
# create data frame for rating matrix:
rateMatrix = pd.DataFrame(index=independent, columns=dependent, dtype=int)
rateMatrix = rateMatrix.fillna(0)

# read routes and put it in dataFrame:
routes = pd.read_csv('routes.csv')
print(routes.head())

# fill frequency matrix:
for route in routes.index:
    if (routes.loc[route, 'elevation'] in dependent) and (routes.loc[route, 'weather'] in independent):
        elevation_index = routes.loc[route, 'elevation']
        weather_index = routes.loc[route, 'weather']
        userProfileFrequency.loc[weather_index, elevation_index] += 1
    if (routes.loc[route, 'weather'] in independent) and (routes.loc[route, 'duration'] in dependent):
        weather_index = routes.loc[route, 'weather']
        duration_index = routes.loc[route, 'duration']
        userProfileFrequency.loc[weather_index, duration_index] += 1
    if (routes.loc[route, 'weather'] in independent) and (routes.loc[route, 'distance'] in dependent):
        weather_index = routes.loc[route, 'weather']
        distance_index = routes.loc[route, 'distance']
        userProfileFrequency.loc[weather_index, distance_index] += 1
    if (routes.loc[route, 'weather'] in independent) and (routes.loc[route, 'bikeLane'] in dependent):
        weather_index = routes.loc[route, 'weather']
        bikeLane_index = routes.loc[route, 'bikeLane']
        userProfileFrequency.loc[weather_index, bikeLane_index] += 1
    if (routes.loc[route, 'temp'] in independent) and (routes.loc[route, 'elevation'] in dependent):
        temp_index = routes.loc[route, 'temp']
        elevation_index = routes.loc[route, 'elevation']
        userProfileFrequency.loc[temp_index, elevation_index] += 1
    if (routes.loc[route, 'temp'] in independent) and (routes.loc[route, 'duration'] in dependent):
        temp_index = routes.loc[route, 'temp']
        duration_index = routes.loc[route, 'duration']
        userProfileFrequency.loc[temp_index, duration_index] += 1
    if (routes.loc[route, 'temp'] in independent) and (routes.loc[route, 'distance'] in dependent):
        temp_index = routes.loc[route, 'temp']
        distance_index = routes.loc[route, 'distance']
        userProfileFrequency.loc[temp_index, distance_index] += 1
    if (routes.loc[route, 'temp'] in independent) and (routes.loc[route, 'bikeLane'] in dependent):
        temp_index = routes.loc[route, 'temp']
        bikeLane_index = routes.loc[route, 'bikeLane']
        userProfileFrequency.loc[temp_index, bikeLane_index] += 1
    if (routes.loc[route, 'traffic'] in independent) and (routes.loc[route, 'elevation'] in dependent):
        traffic_index = routes.loc[route, 'traffic']
        elevation_index = routes.loc[route, 'elevation']
        userProfileFrequency.loc[traffic_index, elevation_index] += 1
    if (routes.loc[route, 'traffic'] in independent) and (routes.loc[route, 'duration'] in dependent):
        traffic_index = routes.loc[route, 'traffic']
        duration_index = routes.loc[route, 'duration']
        userProfileFrequency.loc[traffic_index, duration_index] += 1
    if (routes.loc[route, 'traffic'] in independent) and (routes.loc[route, 'distance'] in dependent):
        traffic_index = routes.loc[route, 'traffic']
        distance_index = routes.loc[route, 'distance']
        userProfileFrequency.loc[traffic_index, distance_index] += 1
    if (routes.loc[route, 'traffic'] in independent) and (routes.loc[route, 'bikeLane'] in dependent):
        traffic_index = routes.loc[route, 'traffic']
        bikeLane_index = routes.loc[route, 'bikeLane']
        userProfileFrequency.loc[traffic_index, bikeLane_index] += 1
    if (routes.loc[route, 'day'] in independent) and (routes.loc[route, 'elevation'] in dependent):
        day_index = routes.loc[route, 'day']
        elevation_index = routes.loc[route, 'elevation']
        userProfileFrequency.loc[day_index, elevation_index] += 1
    if (routes.loc[route, 'day'] in independent) and (routes.loc[route, 'duration'] in dependent):
        day_index = routes.loc[route, 'day']
        duration_index = routes.loc[route, 'duration']
        userProfileFrequency.loc[day_index, duration_index] += 1
    if (routes.loc[route, 'day'] in independent) and (routes.loc[route, 'distance'] in dependent):
        day_index = routes.loc[route, 'day']
        distance_index = routes.loc[route, 'distance']
        userProfileFrequency.loc[day_index, distance_index] += 1
    if (routes.loc[route, 'day'] in independent) and (routes.loc[route, 'bikeLane'] in dependent):
        day_index = routes.loc[route, 'day']
        bikeLane_index = routes.loc[route, 'bikeLane']
        userProfileFrequency.loc[day_index, bikeLane_index] += 1
    if (routes.loc[route, 'dayTime'] in independent) and (routes.loc[route, 'elevation'] in dependent):
        dayTime_index = routes.loc[route, 'dayTime']
        elevation_index = routes.loc[route, 'elevation']
        userProfileFrequency.loc[dayTime_index, elevation_index] += 1
    if (routes.loc[route, 'dayTime'] in independent) and (routes.loc[route, 'duration'] in dependent):
        dayTime_index = routes.loc[route, 'dayTime']
        duration_index = routes.loc[route, 'duration']
        userProfileFrequency.loc[dayTime_index, duration_index] += 1
    if (routes.loc[route, 'dayTime'] in independent) and (routes.loc[route, 'distance'] in dependent):
        dayTime_index = routes.loc[route, 'dayTime']
        distance_index = routes.loc[route, 'distance']
        userProfileFrequency.loc[dayTime_index, distance_index] += 1
    if (routes.loc[route, 'dayTime'] in independent) and (routes.loc[route, 'bikeLane'] in dependent):
        dayTime_index = routes.loc[route, 'dayTime']
        bikeLane_index = routes.loc[route, 'bikeLane']
        userProfileFrequency.loc[dayTime_index, bikeLane_index] += 1

# calculate summation for each row in userProfileFrequency:
userProfileFrequency['total_route'] = userProfileFrequency.sum(axis=1)
userProfileFrequency.loc['total'] = userProfileFrequency.sum()
# userProfileFrequency.to_csv('result3.csv')



# function to calcualte rating:

def fill_matrix(x_index, y_index):
    for route in routes.index:
        if (routes.loc[route, x_index] in dependent) and (routes.loc[route, y_index] in independent):
            x = routes.loc[route, x_index]
            y = routes.loc[route, y_index]
            rateMatrix.loc[y, x] += int(routes.loc[route,'rate'])

# rating matrix:

fill_matrix('elevation', 'weather')
fill_matrix('distance', 'weather')
fill_matrix('duration', 'weather')
fill_matrix('bikeLane', 'weather')
fill_matrix('elevation', 'temp')
fill_matrix('distance', 'temp')
fill_matrix('duration', 'temp')
fill_matrix('bikeLane', 'temp')
fill_matrix('elevation', 'traffic')
fill_matrix('distance', 'traffic')
fill_matrix('duration', 'traffic')
fill_matrix('bikeLane', 'traffic')
fill_matrix('elevation', 'day')
fill_matrix('distance', 'day')
fill_matrix('duration', 'day')
fill_matrix('bikeLane', 'day')
fill_matrix('elevation', 'dayTime')
fill_matrix('distance', 'dayTime')
fill_matrix('duration', 'dayTime')
fill_matrix('bikeLane', 'dayTime')

# average the rateMatrix:

for r in independent:
    for c in dependent:
        x= int(userProfileFrequency.loc[r,c])
        y= int (rateMatrix.loc[r,c])
        if x != 0 :
         rateMatrix.loc[r,c]= y/x

#-------------------------------------------------------------------
# test:
print(userProfileFrequency.loc[weather_index, elevation_index])
print(userProfileFrequency.loc['Friday', 'medium_bikeLane'])
print(userProfileFrequency.head())

print()
print(rateMatrix.head())

print(userProfileFrequency.loc[:, 'total_route'])
