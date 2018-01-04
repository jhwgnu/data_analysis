from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

os.chdir('C:\\practice')

data = {
    'name': ['Kim', 'Han', 'Lee', 'Seo', 'Jin'],
    'age': [19, 20, 35, 60, 18],
    'gradyear': [2017, 2016, 2008, 1990, 2016],
    'gender': ['F', 'M', 'M', 'F', 'F']
}

practice = DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])

practice['grade'] = np.nan
practice.gradyear = 2000

# print(practice)
# print('\n')
# print(practice.ix['three'])

practice2 = DataFrame(data, columns=['name', 'age', 'gradyear', 'gender'], index=['one', 'two', 'three', 'four', 'five'])
practice2['Male'] = practice2.gender=='M'
print(practice2)
print('\n')

# practice4 = practice2[practice.age>=20]
# print(practice4)
# print('\n')

# practice5 = practice2[practice2.Male==True]
# print(practice5)
# print('\n')

print(practice2.name[practice2.age.idxmax()])
print('\n')

print(practice2.gender.value_counts()['F'])

print(practice2.describe())