import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = [i for i in range(0, 10)]
y = [j**2 for j in x]
plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y, 'b', label='x**2')
plt.xticks([0,1.12,2.66,3,3.5])
plt.yticks([0,2,4,6,8,10])
plt.grid
plt.show()
