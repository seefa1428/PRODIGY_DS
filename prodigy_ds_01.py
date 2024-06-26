# -*- coding: utf-8 -*-
"""PRODIGY_DS_01.ipynb


import pandas as pd
df= pd.read_csv('cereals.csv')
df

import pandas as pd
df = pd.read_csv('cereals.csv')
import matplotlib.pyplot as plt

fiber_distribution_per_calories = df.groupby('fiber')['calories'].mean()

fiber_distribution_per_calories.plot(kind='bar')

plt.title('Average Fiber by Calories')
plt.xlabel('Calories')
plt.ylabel('Average Fiber')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame(df)

plt.hist(df1['rating'], bins=10, edgecolor='black')

plt.title('Histogram of Ratings')
plt.xlabel('Ratings ')
plt.ylabel('Frequency')

plt.show()
