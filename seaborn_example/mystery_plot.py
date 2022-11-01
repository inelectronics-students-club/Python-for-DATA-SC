import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('mystery_dataset.csv')
dataFrame['Vavg (Volts)'] = (dataFrame['V1 (Volts)'] + dataFrame['V2 (Volts)'] + dataFrame['V3 (Volts)']) / 3.0
sns.lineplot(x = "Time interval (seconds)", y = "Vavg (Volts)", data=dataFrame)
plt.show()
