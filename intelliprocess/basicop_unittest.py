import pandas as pd
from basicop import datatype_frequency,feature_type_frequency,nan_frequency

# Test datatype_frequency function
data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
df = pd.DataFrame(data)
result = datatype_frequency(df)
assert result == [['int64', 1], ['float64', 1], ['object', 1], ['datetime64[ns]', 1]]

# Test feature_type_frequency function
data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
df = pd.DataFrame(data)
result = feature_type_frequency(df)
assert result == [['Categorical', 1], ['Numerical', 2]]

# Test nan_frequency function with NaN values
data = {'A': [1, 2, None], 'B': [4.5, None, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
df = pd.DataFrame(data)
result = nan_frequency(df)
assert result == [['A', 1], ['B', 1], ['C', 0], ['D', 0]]

# Test nan_frequency function without NaN values
data = {'A': [1, 2, 3], 'B': [4.5, 6.7, 8.9], 'C': ['foo', 'bar', 'baz'], 'D': pd.date_range('20220101', periods=3)}
df = pd.DataFrame(data)
result = nan_frequency(df)
assert result == []

print("All assertion statements ran successfully.")