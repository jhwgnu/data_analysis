from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

os.chdir('C:\\practice')

obj = Series(np.arange(4.), index=['a','b','c','d'])

print(obj)
print('\n')
# print(obj[0:2])
# print(obj[[1, 2]])
print(obj[2])
print(obj[0:2])

# print(type(obj[[1, 2]]))
# print(obj[obj<2])
# print(obj[:'c'])

# print(type(np.arange(3.)[1]))