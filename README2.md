# data_analysis

Basic Modules
```python
from pandas import Series, DataFrame
```

Series: very basic unit of one vector in data analysis
created using a list or tuple or numpy.arange(4.) or other various types of array

>series from a list -> dtype: int64
series from a tuple -> dtype: int32
don't understand why this difference occurs

## Series
```python
series1 = Series([23, -52, 24, 36])
>>>
index values
0     23
1     -52
2     24
3     36

print(series1.index)
print(series1.values)
```

setting index manually
```python
series2 = Series([23, -52, 24, 36], index=['one', 'two', 'three', 'four'])
=>
one   23
two   -52
three 24
four   36

series['two'] = -52
series['two':'three'] = [-52, 24]
series[:'three'] = [23, -52, 24]
series[series>20] = [23, 24, 36]
series[[1,2]] = [-52, 24]
```



##DataFrame: bundle of multiple series(?)
