import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

data = pd.read_csv('data.csv')
x = data.date.tolist()
for i in range(0, len(x)):
    x[i] = dt.datetime.strptime(x[i], '%Y-%m-%d').date()
y = data.mean_temperature.tolist()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=20)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Mean temperature")
plt.plot(x, y)
plt.show()
