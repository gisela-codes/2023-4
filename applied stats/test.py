import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ndtv_data_final.csv")

d = pd.DataFrame(data)
freq_table = pd.crosstab(d['Brand'], 'frequency')
#print(freq_table)
#print(plt.hist(d['Battery capacity (mAh)']))
plt.scatter(d['Screen size (inches)'], d['Resolution x'])
plt.xlabel('screen size')
plt.ylabel('resolution')
plt.show()