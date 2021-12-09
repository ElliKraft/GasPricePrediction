import pandas as pd
from Extrapolation import extrapolate, plot, predict, calculateValues

#read data collection
df = pd.read_csv('GasPrice.csv',
                            index_col=['Halbjahr'],
                            parse_dates=['Halbjahr'],
                            sep=r'\s*;\s*')
print(df)

#Extrapolation der missing values Netzentgelt
cleanedData = df
cleanedData = cleanedData.drop(cleanedData.tail(6).index, inplace=False)
plot(cleanedData) #shows data without rows with

newVal = extrapolate(cleanedData, cleanedData["Netzentgelt,  ct/KWh"], 3, [18808, 18991])
df["Netzentgelt,  ct/KWh"][12] = round(newVal[0], 2)
df["Netzentgelt,  ct/KWh"][13] = round(newVal[1], 2)

#Extrapolation der missing values Vertrieb und Marge
cleanedData = df
cleanedData = cleanedData.drop(cleanedData.tail(5).index, inplace=False)

newVal = extrapolate(cleanedData, cleanedData["Vertrieb und Marge, ct/KWh"], 2, [18991])
df["Vertrieb und Marge, ct/KWh"][13] = round(newVal[0], 2)
print(df)

#Endverbraucherpreis kalkulieren
df["Endverbraucherpreis,  ct/KWh"][13] = df['Energiebeschaffung, ct/KWh'][13] + df['Steuern und Abgaben, ct/KWh'][13] + \
                                        df["Netzentgelt,  ct/KWh"][13] + df["Vertrieb und Marge, ct/KWh"][13]
df.to_csv('Cleaned Gasdata.csv')

#Datenvorhsersage für 2 Jahre
cleanedData = df
cleanedData = cleanedData.drop(cleanedData.tail(4).index, inplace=False)
predict(df, cleanedData)
calculateValues(df)

#Plotten und Speichern der vorhergesagten Daten
print(df)
plot(df)
df.to_csv('Cleaned prediction Gasdata.csv')
