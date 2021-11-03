import pandas as pd
import matplotlib.pyplot as plt
import joblib

data =joblib.load('jumlah.pkl')
cek = data[1]
print(cek)
pd.read_csv(cek+ '.csv')['c1'].plot()
plt.show()
