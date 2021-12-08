import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
import matplotlib.dates as mdates
import pandas as pd


def get_future_date(base_date):
    future_date = base_date + timedelta(weeks=108)
    return future_date

def extrapolate(cleanedData, y_data, degree):
    dates = cleanedData.index

    polynomial_coefficients = np.polyfit(mdates.date2num(dates), y_data, degree)
    f = np.poly1d(polynomial_coefficients)

    fig, cx = plt.subplots()
    prediction_date = mdates.date2num(get_future_date(dates[-1]))
    difference = prediction_date - mdates.date2num(dates.max())

    x = np.linspace(mdates.date2num(dates.min()), mdates.date2num(dates.max()) + difference)
    datetime_dates = mdates.num2date(x)

    cx.plot(dates, y_data, '.k')
    cx.plot(datetime_dates, f(x), '-g')
    cx.grid()
    # plt.show()
    data = [f(18808), f(18991)]
    df = pd.Series(data)
    return df


def plot(df):
    plt.plot(df.index, df["Energiebeschaffung, ct/KWh"], label='Energiebeschaffung')
    plt.plot(df.index, df["Steuern und Abgaben, ct/KWh"], label='Steuern und Abgaben')
    plt.plot(df.index, df["Netzentgelt,  ct/KWh"], label='Netzentgelt')
    plt.plot(df.index, df["Vertrieb und Marge, ct/KWh"], label='Vertrieb und Marge')
    plt.plot(df.index, df["Endverbraucherpreis,  ct/KWh"], label='Endverbraucherpreis')
    plt.subplots_adjust(right=0.77)
    plt.title('Halbjährliche Daten zu Gaspreisen in Deutschland')
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()
