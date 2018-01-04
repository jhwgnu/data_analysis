from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

os.chdir('C:\\practice')

list1 = [22,33,44,55]
obj = Series(list1, index=['a','b','c','d'])
# obj = Series(np.arange(4.), index=['a','b','c','d'])

print(obj)
print('\n')
# print(obj[0:2])
# print(obj[[1, 2]])
# print(obj[2])
# print(obj[0:2])
# print('\n')

# print(obj['c'])
# print(obj['a':'c'])
# print(obj[:'c'])

# print(obj[obj<30])

print(obj[[1, 2]])
# print(obj[obj<2])
# print(obj[:'c'])
