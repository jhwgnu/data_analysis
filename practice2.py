from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

os.chdir('C:\\practice')

obj = Series(np.arange(7.), index=['a','b','c','d','e','f','g'])

new_obj = obj.drop('c')
new_obj = obj.drop(['f','g'])
# print(new_obj)

data = DataFrame(np.arange(16).reshape((4,4)))

data = DataFrame(
    np.arange(16).reshape((4,4)),
    index = ['Ohio', 'Colorado', 'Utah', "New York"],
    columns = ['one', 'two', 'three', 'four']
    )

print(data)
print('\n')
# print(data.drop(['Ohio', 'Utah'])) #행 삭제

# print(data.drop('two', axis=1))

# print(data[:2])
# print(data[data.three>5])

# print(data.ix[['Colorado'], ['two', 'three']])
# print(data.ix[['Colorado', 'Utah'], [3, 0, 1]])
# print(data.ix[:'Utah', 'two'])

df = data.T
print(df.sum())
print('\n')

print(df.sum(axis=1))
print('\n')

print(df.mean())
print('\n')

# data['temp'] = np.nan
# df2 = data.T
# print(df2.mean(skipna=False)) #skipna는 디폴트로 true임
# print('\n')

print(df.describe())
print('\n')

obj2 = Series(['a','a','b','c'])
print(obj2.describe())
print('\n')

result = data.apply(pd.value_counts).fillna(0)
print(result)