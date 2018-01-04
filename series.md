

```python
from pandas import Series
series1 = Series([23, 44, -19, 8])
series1
```




    0    23
    1    44
    2   -19
    3     8
    dtype: int64




```python
series1.index
```




    RangeIndex(start=0, stop=4, step=1)




```python
series1.values
```




    array([ 23,  44, -19,   8], dtype=int64)




```python

```


```python
series2 = Series([23, 44, -19, 8], index=['A', 'B', 'C', 'D'])
series2
```




    A    23
    B    44
    C   -19
    D     8
    dtype: int64




```python
series2[2:3]

```




    C   -19
    dtype: int64




```python
series2[[1,3]]
```




    B    44
    D     8
    dtype: int64




```python
series2[series2 < 20]
```




    C   -19
    D     8
    dtype: int64




```python
series2[:'B']
```




    A    23
    B    44
    dtype: int64




```python
series2['A':'C']
```




    A    23
    B    44
    C   -19
    dtype: int64




```python

```
