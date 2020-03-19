import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston_data = load_boston()
boston_df = pd.DataFrame(boston_data['data'], columns=boston_data['feature_names'])
boston_df['PRICE'] = boston_data['target']
print(boston_df.head())
plt.figure(num=1,figsize=(20, 5))
features = ['TAX', 'RM']
reg = LinearRegression()
price = np.array(boston_df['PRICE']).reshape(-1,1)
for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    plt.scatter(boston_df[col], boston_df['PRICE'], marker='o')
    plt.xlabel(col)
    plt.ylabel('PRICE')
    column = np.array(boston_df[col]).reshape(-1,1)
    reg.fit(column,price)
    predicted_price = reg.predict(column)
    plt.plot(column, predicted_price, 'r')
pd.DataFrame.hist(boston_df,['TAX', 'RM'])
plt.show()