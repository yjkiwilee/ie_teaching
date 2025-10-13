import numpy as np

data = np.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')

max_change = np.max(np.diff(data, axis=1), axis=1)
print(np.shape(max_change))