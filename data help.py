import pandas as pd
import numpy as np

demo_data = pd.read_csv('data.csv', header=None)

demo_data.columns = list(np.arange(demo_data.shape[1]-1).astype('int')) + ['label']
demo_data.iloc[:, -1] = demo_data.iloc[:, -1].astype('int')

x = demo_data.values[:, :-1]
y = demo_data.values[:, -1]
