# require packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm

# grab the data
# get the help about the data
# print(sm.datasets.sunspots.NOTE)

# load the data in the form of pd's df
df = sm.datasets.sunspots.load_pandas().data
# print(df)
# print(df.describe())
# df.info()

print(df.head())
# print(df.tail())

# change the index to the time component (YEAR)
df.index = pd.Index(sm.tsa.datetools.dates_from_range('1700', '2008'))
# print(df.index)
# print(df.head())

df.plot()
plt.show()
