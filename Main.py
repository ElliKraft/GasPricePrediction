import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import UnivariateSpline


originialData = pd.read_csv('GasPrice.csv', index_col=['Halbjahr'], parse_dates=['Halbjahr'], sep=r'\s*;\s*')
# print(originialData)


#Stack Overflow
# array = np.random.random_integers(0, 10, (10, 10)).astype(float)
#values greater then 7 goes to np.nan
# array[array > 7] = np.nan
# print(array)
#
# x = np.arange(0, data.shape[1]) #Spalten
# y = np.arange(0, data.shape[0]) #Zeilen
# #mask invalid values
# array = np.ma.masked_invalid(data)
# xx, yy = np.meshgrid(x, y)
# #get only the valid values
# x1 = xx[~array.mask]
# y1 = yy[~array.mask]
# newarr = array[~array.mask]
#
# GD1 = interpolate.griddata((x1, y1), newarr.ravel(),
#                            (xx, yy),
#                            method='cubic')

# print(GD1)
# print(array[~array.mask])
# print(np.meshgrid(x, y))

# x1 = data["Netzentgelt,  ct/KWh"]
# y1 = data["Halbjahr"]

# x = np.arange(0, 14)
# y = originialData['Netzentgelt,  ct/KWh']
# f = interpolate.interp1d(x, y)
# print(f)

#
# s = UnivariateSpline(x, y, k=1)
# y=s(x)

# fit = np.polyfit(x, data['Netzentgelt,  ct/KWh'], 1)
# fit = interpolate.interp1d(x, y, fill_value="extrapolate")
# print(fit(10))

# print(data["Netzentgelt,  ct/KWh"])


cleanedData = originialData

s = pd.Series(cleanedData["Netzentgelt,  ct/KWh"])
t = pd.Series(cleanedData["Vertrieb und Marge, ct/KWh"])
u = pd.Series(cleanedData["Endverbraucherpreis,  ct/KWh"])
cleanedData["Netzentgelt,  ct/KWh"] = s.interpolate()
cleanedData["Vertrieb und Marge, ct/KWh"] = t.interpolate()
cleanedData["Endverbraucherpreis,  ct/KWh"] = u.interpolate()
# print(cleanedData)
#

predictionData = originialData[["Energiebeschaffung, ct/KWh", "Endverbraucherpreis,  ct/KWh"]]
predictionData.index = predictionData['Halbjahr']
print(predictionData)




# print(data)
#
# plt.figure(figsize=(15, 7))
# plt.plot(data['Endverbraucherpreis,  ct/KWh'])
# plt.title('halbjährliche Daten')
# plt.grid(True)
# plt.show()
