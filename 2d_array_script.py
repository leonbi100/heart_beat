from beat_site.models import Country
import csv
import itertools
import pandas as pd
import math

data = []
result = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#Filter for correct objects
countries = Country.objects.filter(year=2000)
countries.filter(gdp__isnull=False)

#Put into 2d array
for country in countries:
    rate = country.rate
    condition = math.log(country.gdp,10)
    if rate < 10:
        rate = 0
    elif 10 <= rate < 20:
        rate = 1
    elif 20 <= rate < 30:
        rate = 2
    elif 30 <= rate < 40:
        rate = 3
    elif 40 <= rate < 50:
        rate = 4
    elif 50 <= rate < 60:
        rate = 5
    elif 60 <= rate < 70:
        rate = 6
    elif 70 <= rate < 80:
        rate = 7
    elif 80 <= rate < 90:
        rate = 8
    elif 90 <= rate < 100:
        rate = 9
    else:
        rate = 10


    if condition < 7.5:
        condition = 0
    elif 7.5 <= condition < 8:
        condition = 1
    elif 8 <= condition < 8.5:
        condition = 2
    elif 8.5 <= condition < 9:
        condition = 3
    elif 9 <= condition < 9.5:
        condition = 4
    elif 9.5 <= condition < 10:
        condition = 5
    elif 10 <= condition < 10.5:
        condition = 6
    elif 10.5 <= condition < 11:
        condition = 7
    elif 11 <= condition < 11.5:
        condition = 8
    elif 11.5 <= condition < 12:
        condition = 9
    else:
        condition = 10
    
    #Categorize into bins
    data.append((rate, condition))

    for pair in data:
        result[pair[0]][pair[1]] += 1



