# import required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('hearing_test.csv')
print(df.head())

x = df.drop('test_result', axis=1)
y = df['test_result']

# split the data into train and test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=123456)

from sklearn.linear_model import LogisticRegressionCV

# create the model
model = LogisticRegressionCV()

# train the model
model.fit(x_train, y_train)

y_prediction = model.predict(x_test)
# print(y_prediction)

# print(y_test)

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
print(classification_report(y_test, y_prediction))