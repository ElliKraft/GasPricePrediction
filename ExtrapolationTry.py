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
from datetime import datetime
from datetime import timedelta
from datetime import date

originalData = pd.read_csv('GasPrice Alt.csv',
                           index_col=['Halbjahr'],
                           parse_dates=['Halbjahr'],
                           sep=r'\s*;\s*')

cleanedData = originalData
dates = cleanedData.index


def __get_future_date(base_date, additional_days):
    future_date = base_date + timedelta(days=180)
    return future_date


polynomial_coefficients = np.polyfit(cleanedData.index, cleanedData["Netzentgelt,  ct/KWh"], 2)
f = np.poly1d(polynomial_coefficients)

fig, cx = plt.subplots()
difference = 0
future_date = cleanedData.date2num(__get_future_date(dates[-1], 4))
difference = future_date - cleanedData.index.max()

x = np.linspace(cleanedData.index.min(), cleanedData.index.max() + difference)
datetime_dates = cleanedData.index.num2date(x)

# cx.plot(dates, y_data, '.k')
# cx.plot(datetime_dates, f(x), '-g')
# cx.grid()
# cx.set_ylim(0, f(x).max())
# plt.show()

# plt.plot(cleanedData.index, cleanedData["Energiebeschaffung, ct/KWh"], label='Energiebeschaffung')
# plt.plot(cleanedData.index, cleanedData["Steuern und Abgaben, ct/KWh"], label='Steuern und Abgaben')
# plt.plot(cleanedData.index, cleanedData["Netzentgelt,  ct/KWh"], label='Netzentgelt')
# plt.plot(cleanedData.index, cleanedData["Vertrieb und Marge, ct/KWh"], label='Vertrieb und Marge')
# plt.plot(cleanedData.index, cleanedData["Endverbraucherpreis,  ct/KWh"], label='Endverbraucherpreis')
# plt.subplots_adjust(right=0.77)
# plt.title('Halbjährliche Daten zu Gaspreisen in Deutschland')
# plt.grid(True)
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# plt.show()
