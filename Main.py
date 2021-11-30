import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('GasPrice.csv', index_col=['Halbjahr'], parse_dates=['Halbjahr'], sep=r'\s*;\s*')
print(data.tail(5))

plt.figure(figsize=(15, 7))
plt.plot(data['Endverbraucherpreis,  ct/KWh'])
plt.title('halbjährliche Daten')
plt.grid(True)
plt.show()
