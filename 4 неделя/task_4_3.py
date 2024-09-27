import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('iris_data.csv')
#print(df)
#plt.pie([0])
x1 = list(df['Species']).count('Iris-setosa')
x2 = list(df['Species']).count('Iris-versicolor')
x3 = list(df['Species']).count('Iris-virginica')
print(x1, x2, x3)
count1 = 0
count2 = 0
count3 = 0




