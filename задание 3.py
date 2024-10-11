import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')
x1 = list(df['Species']).count('Iris-setosa')
x2 = list(df['Species']).count('Iris-versicolor')
x3 = list(df['Species']).count('Iris-virginica')
 
y =list(df['PetalLengthCm'])
b1 = 0
b2 = 0
b3 = 0
for i in y:
    if i <= 1.2:
         b1 += 1
    if 1.2 < i < 1.5:
         b2 += 1
    if i >= 1.5:
         b3 += 1
        

fig = plt.figure(figsize=(16,9))
a1 = fig.add_subplot(121)
a2 = fig.add_subplot(122)
a1.pie([x1, x2, x3], labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
a2.pie([b1, b2, b3], labels = ['меньше 1.2','от 1.2 до 1.5','больше 1.5'])
plt.show()
