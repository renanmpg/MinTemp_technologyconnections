import numpy as np
import pandas as pd
import metpy.calc as mpcalc
from metpy.cbook import get_test_data
from metpy.units import units
import math


########## DATA FROM https://www.ncei.noaa.gov/access/past-weather/ #########


# pd.options.display.float_format = "{:,.3f}".format
colunas=['date','tavg', 'tmax','tmin','prcp','snow','snwd']
data = pd.read_csv("data_chicago.csv",names=colunas,skiprows=2,sep=',')
years = (data.shape[0]/360)

# print(data['tmin'])

Tmin_ef = data[data['tmin'] < 5]  
days_ef = (Tmin_ef.shape[0])
mean_dayperyear = days_ef/years

print("Number of years:","%.2f" % years, 'years')
print('Averaged days per year with minimum temperature below 5 °F:',"%.2f" %mean_dayperyear, 'days')

