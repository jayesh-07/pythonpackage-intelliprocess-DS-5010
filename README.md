<div align="center">
  <img src="https://i.postimg.cc/FRrgP3R7/logo-color.png"><br>
</div>

-----------------

# intelliprocess: for machine learning data preprocessing

## What is it?

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

  - Reccomendations to insturct users on Handling missing values in dataset
    - numerical (mean)
    - NaN
  - Encode Categorical data
    - One-hot encoding, Binary encoding, Label encoding
  - Scaling Numerical Data
  - Check for skew; apply appropriate transformation (box-cox, log transform, or rank-based methods
    - If normal perform standardization
    - Calculate outliers and return df with outliers removed 
  - Data Visualization
    - Boxplots
    - Correlation matrix heatmap
    - ScatterPlots

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/pandas-dev/pandas

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/pandas) and on [Conda](https://docs.conda.io/en/latest/).

```sh
# conda
conda install -c conda-forge pandas
```

```sh
# or PyPI
pip install pandas
```

The list of changes to pandas between each release can be found
[here](https://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html). For full
details, see the commit logs at https://github.com/pandas-dev/pandas.

## Dependencies
- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org)
- [python-dateutil - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [pytz - Brings the Olson tz database into Python which allows accurate and cross platform timezone calculations](https://github.com/stub42/pytz)

See the [full installation instructions](https://pandas.pydata.org/pandas-docs/stable/install.html#dependencies) for minimum supported versions of required, recommended and optional dependencies.

## Installation from sources
To install pandas from source you need [Cython](https://cython.org/) in addition to the normal
dependencies above. Cython can be installed from PyPI:

```sh
pip install cython
```

In the `pandas` directory (same one where you found this file after
cloning the git repo), execute:

```sh
python setup.py install
```

or for installing in [development mode](https://pip.pypa.io/en/latest/cli/pip_install/#install-editable):


```sh
python -m pip install -e . --no-build-isolation --no-use-pep517
```

or alternatively

```sh
python setup.py develop
```

See the full instructions for [installing from source](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html#installing-from-source).

## License
[BSD 3](LICENSE)

## Documentation
The official documentation is hosted on PyData.org: https://pandas.pydata.org/pandas-docs/stable

## Background
Work on ``pandas`` started at [AQR](https://www.aqr.com/) (a quantitative hedge fund) in 2008 and
has been under active development since then.

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/tagged/pandas).
Further, general questions and discussions can also take place on the [pydata mailing list](https://groups.google.com/forum/?fromgroups#!forum/pydata).
