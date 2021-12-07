from cgitb import handler

import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics.api as smg
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import matplotlib.patches as mpatches

originalData = pd.read_csv('GasPrice.csv',
                            index_col=['Halbjahr'],
                            parse_dates=['Halbjahr'],
                            sep=r'\s*;\s*')

cleanedData = originalData
cleanedData.drop(cleanedData.tail(4).index, inplace=False)

predictionData = originalData
print(predictionData)
# s = pd.Series(cleanedData["Netzentgelt,  ct/KWh"])
t = pd.Series(predictionData["Vertrieb und Marge, ct/KWh"])
w = pd.Series(predictionData["Energiebeschaffung, ct/KWh"])

u = pd.Series(cleanedData["Endverbraucherpreis,  ct/KWh"])
#
# cleanedData["Netzentgelt,  ct/KWh"] = s.interpolate()
predictionData["Vertrieb und Marge, ct/KWh"] = t.interpolate()
predictionData["Energiebeschaffung, ct/KWh"] = w.interpolate()
predictionData["Endverbraucherpreis,  ct/KWh"] = u.interpolate()
print("predictionData")
print(predictionData)


X = cleanedData[["Energiebeschaffung, ct/KWh", "Vertrieb und Marge, ct/KWh"]]
# X = cleanedData["Energiebeschaffung, ct/KWh"]
# print(X)
y = cleanedData["Endverbraucherpreis,  ct/KWh"]
Z = predictionData[["Energiebeschaffung, ct/KWh", "Vertrieb und Marge, ct/KWh"]]
# fit a OLS model with intercept on Energiebeschaffung and Marge und Vertrieb
X = sm.add_constant(X)
Z = sm.add_constant(Z)
model = sm.OLS(y, X).fit()
prediction = model.predict(Z)
model.summary()
print(model.summary())
print(prediction)

# corr_matrix = np.corrcoef(cleanedData[["Energiebeschaffung, ct/KWh", "Endverbraucherpreis,  ct/KWh"]])
# smg.plot_corr(corr_matrix, xnames=cleanedData["Endverbraucherpreis,  ct/KWh"], ynames=cleanedData["Energiebeschaffung, ct/KWh"])
# plt.show()
# print(corr_matrix)

plt.plot(cleanedData.index, cleanedData["Energiebeschaffung, ct/KWh"], label='Energiebeschaffung')
plt.plot(cleanedData.index, cleanedData["Steuern und Abgaben, ct/KWh"], label='Steuern und Abgaben')
plt.plot(cleanedData.index, cleanedData["Netzentgelt,  ct/KWh"], label='Netzentgelt')
plt.plot(cleanedData.index, cleanedData["Vertrieb und Marge, ct/KWh"], label='Vertrieb und Marge')
plt.plot(cleanedData.index, cleanedData["Endverbraucherpreis,  ct/KWh"], label='Endverbraucherpreis')
plt.subplots_adjust(right=0.77)
plt.title('Halbjährliche Daten zu Gaspreisen in Deutschland')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
