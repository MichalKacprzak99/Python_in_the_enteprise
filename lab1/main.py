import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

boston_data = load_boston()
boston_df = pd.DataFrame(boston_data['data'], columns=boston_data['feature_names'])
boston_df['target'] = boston_data['target']
print(boston_df.head())

pd.DataFrame.hist(boston_df,['AGE','TAX'])
plt.show()