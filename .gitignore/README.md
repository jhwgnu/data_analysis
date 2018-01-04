# data_analysis

Basic Modules
from pandas import Series, DataFrame

Series: very basic unit of one vector in data analysis
created using a list or tuple
**series from a list -> dtype: int64
  series from a tuple -> dtype: int32
don't understand why this difference occurs**

##Series

series1 = Series([23, -52, 24])
=>
index values
0     23
1     -52
2     24
print(series1.index)
print(series1.values)

series2 = Series([23, -52, 24], index=['one', 'two', 'three'])
=>
one   23
two   -52
three 24

##DataFrame: bundle of multiple series(?)
