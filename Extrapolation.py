import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def extrapolate(cleanedData, y_data, degree, timedata):
    data = [0, 1, 2, 3]

    polynomial_coefficients = np.polyfit(mdates.date2num(cleanedData.index), y_data, degree)
    f = np.poly1d(polynomial_coefficients)

    for i in range(len(timedata)):
        data[i] = f(timedata[i])

    df = pd.Series(data)
    return df


def predict(df, cleanedData):
    for column in df:
        if column=="Vertrieb und Marge, ct/KWh":
            newVal = extrapolate(cleanedData, cleanedData[column], 2, [19173, 19356, 19538, 19721])
        else:
            newVal = extrapolate(cleanedData, cleanedData[column], 3, [19173, 19356, 19538, 19721])
        for i in range(4):
            df[column][14 + i] = round(newVal[i], 2)


def calculateValues(df):
    for i in range(4):
        df["Steuern und Abgaben, ct/KWh"][14 + i] = round((df["Energiebeschaffung, ct/KWh"][14 + i] + df["Netzentgelt,  ct/KWh"][14 + i]+0.55+0.75)*0.19+0.55+0.75, 2)
        df["Endverbraucherpreis,  ct/KWh"][14 + i] = round(df['Energiebeschaffung, ct/KWh'][14 + i] + df['Steuern und Abgaben, ct/KWh'][14 + i] + \
                                                     df["Netzentgelt,  ct/KWh"][14 + i] + df["Vertrieb und Marge, ct/KWh"][14 + i], 2)


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
