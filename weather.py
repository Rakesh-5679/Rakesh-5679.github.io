import numpy as np
import matplotlib.pyplot as plt
dates=["jun10","jun11","jun12","jun13","jun14","jun15","jun16","jun17","jun18","jun19"]
temp=[30,38,28,35,35,35,35,23,38,27]
wind=[28,35,29,23,29,28,21,22,18,21]
yp=np.arange(len(dates))
plt.bar(yp-0.2,temp,color='r',width=.4,label="Temp(in Celsius)")
plt.bar(yp+0.2,wind,color='b',width=.4,label="Wind(in km/hr)")
plt.xticks(yp,dates)
plt.xlabel("Dates---------->")
plt.ylabel("Temp and Wind---------->")
plt.title("Temperature and Wind For Next 10 Days")
plt.legend()