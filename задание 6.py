import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
price = [0, 1, 10, 13, 1000, 100, 430, 1000, 5000, 10000, 13000, 4000, 50000, 40000, 25000]
z = np.polyfit(year, price, 3)
print(z, z[1])

plt.plot(year, price)
plt.plot([i for i in range(2009, 2024)], [i**3*z[0] + i**2 * z[1] + i**1*z[2] + z[3] for i in range(2009, 2024)])


plt.ylabel('Price, $')
plt.xlabel('Year')

plt.show() #взял у Артема