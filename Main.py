import pandas as pd
from Extrapolation import extrapolate, plot

#read data collection
df = pd.read_csv('GasPrice.csv',
                            index_col=['Halbjahr'],
                            parse_dates=['Halbjahr'],
                            sep=r'\s*;\s*')

print(df)
#extrapolate missing values Netzentgelt
cleanedData = df
cleanedData = cleanedData.drop(cleanedData.tail(2).index, inplace=False)
# print(cleanedData)
plot(cleanedData)

newVal = extrapolate(cleanedData, cleanedData["Netzentgelt,  ct/KWh"], 3)
df["Netzentgelt,  ct/KWh"][12] = round(newVal[0], 2)
df["Netzentgelt,  ct/KWh"][13] = round(newVal[1], 2)

print(df["Netzentgelt,  ct/KWh"])


#extrapolate missing values Vertrieb und Marge
cleanedData = df
cleanedData = cleanedData.drop(cleanedData.tail(1).index, inplace=False)
# print(cleanedData)

newVal = extrapolate(cleanedData, cleanedData["Vertrieb und Marge, ct/KWh"], 2)
df["Vertrieb und Marge, ct/KWh"][13] = round(newVal[1], 2)

print(df["Vertrieb und Marge, ct/KWh"])
print(df)

#calculate Endverbraucherpreis
df["Endverbraucherpreis,  ct/KWh"][13] = df['Energiebeschaffung, ct/KWh'][13] + df['Steuern und Abgaben, ct/KWh'][13] + \
                                        df["Netzentgelt,  ct/KWh"][13] + df["Vertrieb und Marge, ct/KWh"][13]

print(df)
plot(df)
df.to_csv('Cleaned Gas Data.csv')
print('Ende')
