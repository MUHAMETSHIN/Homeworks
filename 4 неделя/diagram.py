import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pos = 0
scale = 10
val1= np.random.normal(pos, 10, 1000)
val2= np.random.normal(pos, 10, 2000)
val3= np.random.normal(pos, 10, 3000)
val4= np.random.normal(pos, 10, 5000)
fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ax1.hist(val1,100)
ax2.hist(val2,100)
ax3.hist(val3,100)
ax4.hist(val4,100)
plt.show()