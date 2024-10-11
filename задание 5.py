import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('BTC_data.csv')
plt.figure(figsize=(16,19))
t = df['time']
c = df['close']

plt.plot(t, c)
plt.xticks(t)
plt.ylabel('Цена')
plt.xlabel('Время')
plt.show()