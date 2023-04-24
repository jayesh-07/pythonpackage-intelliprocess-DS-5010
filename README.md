<div align="center">
  <img src="https://i.postimg.cc/kgLZDncT/Screen-Shot-2023-04-20-at-11-29-48-PM.png"><br>
</div>

-----------------

# IntelliProcess: data pre-processing and visualization for machine learning

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
git clone https://github.com/jayesh-07/pythonpackage-intelliprocess-DS-5010
```

## Documentation
For complete documentation and code examples, please see https://docs.google.com/document/d/13324RP0-XKVsjlOo9V-Dvz-BvhilVLXv0XmCQXoc0rU/edit?usp=sharing


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


## References

[1] Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). https://doi.org/10.1038/s41586-020-2649-2. (https://www.nature.com/articles/s41586-020-2649-2)

[2] J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.

[3] Waskom, M., Botvinnik, Olga,;O’Kane, Drew, et al.(2017). mwaskom/seaborn: v0.8.1 (September 2017). Zenodo. https://doi.org/10.5281/zenodo.883859

[4] McKinney, W., & others. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51–56).

[5] Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T., Cournapeau, D., … SciPy 1.0 Contributors. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17, 261–272. https://doi.org/10.1038/s41592-019-0686-2

[6] Seabold, S., & Perktold, J. (2010). statsmodels: Econometric and statistical modeling with python. In 9th Python in Science Conference.

[7] National Institute of Standards and Technology, US Department of Commerce.(2021). Exploratory Data Analysis. https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b.htm

[8] The pandas development team, “pandas-dev/pandas: Pandas”. Zenodo, Apr. 03, 2023. doi: 10.5281/zenodo.7794821.

