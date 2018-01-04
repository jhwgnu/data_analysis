from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

os.chdir('C:\\practice')
# 한글이 포함돼서 안될때 짝대기 두개씩 해보면 돌아감
# print(os.getcwd())

int_list = [23, -52, 22, 98]
# print(int_list)

int_series = Series(int_list)
print(int_series)
# print(int_series.values)
# print(int_series.index)

series2 = Series(int_list, index = ['a', 'b', 'c', 'd'])
# print(series2)

data = {
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

frame = DataFrame(data)
# print(frame)
# print(type(frame.year))

frame2 = DataFrame(data, columns=['year', 'state', 'pop'])
frame3 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])

# print(frame3['state'])
# print(frame3.state)
# print(frame3.ix['one'])

frame3.debt = 100

frame3.debt = np.arange(5.)
# print(np.arange(6.))
# print(type(np.arange(6.)))

temp_series = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame3.debt = temp_series

frame3['ddd'] = np.nan
#추가할때나 지울때는 인덱스 형식으로 해야함 frame3.ddd 안됨
# print(frame3)

frame3['eastern'] = frame3.state=='Ohio'
# print(frame3)

# if문 이용하는 방법?

del [frame3['eastern'], frame3['ddd']]
# print(frame3.columns)

frame3['big'] = frame3['pop'] > 2.0

# print(frame3.T)
