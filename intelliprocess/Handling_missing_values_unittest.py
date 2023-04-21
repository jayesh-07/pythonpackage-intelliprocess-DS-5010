import pandas as pd
import numpy as np
from Handling_missing_values import fill_missing_values

# Test case for numeric columns
df = pd.DataFrame({'A': [3, 2, np.nan, 4], 'B': [1.0, np.nan, 1.0, 1.0]})
assert np.allclose(fill_missing_values(df), pd.DataFrame({'A': [3, 2, 3, 4], 'B': [1.0, 1.0, 1.0, 1.0]}))

# Test case for boolean columns
df = pd.DataFrame({'A': [True, True, np.nan], 'B': [np.nan, False, False]})
assert fill_missing_values(df).equals(pd.DataFrame({'A': [True, True, True], 'B': [False, False, False]}))

# Test case for categorical columns
df = pd.DataFrame({'A': ['red', 'blue', 'green', np.nan], 'B': ['large', 'small', 'medium', 'small']})
assert fill_missing_values(df).equals(pd.DataFrame({'A': ['red', 'blue', 'green', 'red'], 'B': ['large', 'small', 'medium', 'small']}))

# Test case for string/object columns
df = pd.DataFrame({'A': ['apple', 'banana', np.nan, 'apple'], 'B': ['John', 'John', 'Sam', np.nan]})
assert fill_missing_values(df).equals(pd.DataFrame({'A': ['apple', 'banana', 'apple', 'apple'], 'B': ['John', 'John', 'Sam', 'John']}))

print("All assertion statements ran successfully.")