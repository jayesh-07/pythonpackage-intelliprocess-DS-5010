<div align="center">
  <img src="https://i.postimg.cc/kgLZDncT/Screen-Shot-2023-04-20-at-11-29-48-PM.png"><br>
</div>

-----------------

# intelliprocess: for machine learning data preprocessing

## What is intelliprocess?

**intelliprocess** is a comprehensive Python package aimed at providing limited data 
pre-processing capabilities to industry professionals, researchers, and 
academics of numerous backgrounds. The package can take in CSV files containing 
both numeric and categorical variable types and permits tidying, normalization/vector 
scaling and selection of data, with output selections available in various file types. 
In addition, this package supports data visualization with the use of external Python 
libraries to implement statistical plots for data evaluation and curation, alongside 
other machine learning techniques.

## Main Features
Here are just a few of the things that intelliprocess does well:

  - Imputing Missing Values
    - Numerical imputation using the mean.
    - Categorical imputation using the mode.

  - Encode Categorical data
    - Provide suggestions and recommends either One-hot encoding, Binary encoding, Label encoding based on the data.

  - Normalization of Data
    - Skewness number check using Pearson - Fisher method.
    - Calculate to detect outliers and return a dataframe as a csv file with outliers removed.

  - Scaling Numerical Data
    - Logarithmic transofrmation of individual variables with output plots comparing original to transformed data. 
    - Box-Cox transofrmation of individual variables with output plots comparing original to transformed data. 

  - Data Visualization
    - Histograms w/ different bin sizes (5,10,15,20)
    - Boxplots
    - Correlation matrix heatmap
    - Scatter plots

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/jayesh-07/pythonpackage-intelliprocess-DS-5010

```sh
# 
git clone https://github.com/jayesh-07/pythonpackage-intelliprocess-DS-5010
```


## Dependencies
  - numpy
  - pandas  
  - matplotlib 
  - seaborn
  - datetime
  - scipy
  - csv
  - statsmodels
  - os


## License
MIT License

Copyright (c) 2023 Jayesh Katade,Aditi Thakur,Shane Hussey,Tay Goodwin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Documentation



```sh
# import IntelliViz object to handle easy vizualizations! 
from intelliprocess.intelliviz import IntelliViz

# import a dataframe
i = IntelliViz(df)
```


