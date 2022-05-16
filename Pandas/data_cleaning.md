# About Data Cleaning with Pandas

Contents
> * Chekcing miss values
> * Scaling and Normalization (Transform numeric variables to have helpful properties.)



### Checking miss values

* How many missing data points do we have?
~~~python
# get the number of missing data points per column
missing_values_count = some_data.isnull().sum()
~~~

~~~python
# how many total missing values do we have?
total_cells = np.product(some_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
~~~

~~~python
# remove all the rows that contain a missing value
some_data.dropna()
# remove all rows that have at least one missing values
~~~

~~~python
# Instead, remove all columns with at least one missing value
columns_with_na_dropped = some_data.dropna(axis=1)
~~~

~~~python
# just how much data did we lose?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])
~~~

~~~python
# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
subset_nfl_data.fillna(method='bfill', axis=0).fillna(0)
~~~





# Scaling and Normalization

* in scaling, you're changing the range of your data, while
* in normalization, you're changing the shape of the distribution of your data.

* By scaling your variables, you can help compare different variables on equal footing.

* Scaling just changes the range of your data. Normalization is a more radical transformation. The point of normalization is to change your observations so that they can be described as a normal distribution.
* Normal distribution: Also known as the "bell curve", this is a specific statistical distribution where a roughly equal observations fall above and below the mean, the mean and the median are the same, and there are more observations closer to the mean. The normal distribution is also known as the Gaussian distribution.

****

* **Set up**
~~~python
# modules we'll use
import pandas as pd
import numpy as np

# for Box-Cox Transformation
from scipy import stats

# for min_max scaling
from mlxtend.preprocessing import minmax_scaling

# plotting modules
import seaborn as sns
import matplotlib.pyplot as plt
~~~


# Scailing
~~~python
# generate 1000 data points randomly drawn from an exponential distribution
original_data = np.random.exponential(size=1000)

# mix-max scale the data between 0 and 1
scaled_data = minmax_scaling(original_data, columns=[0])

# plot both together to compare
fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()
~~~


# Normalization
~~~python
# normalize the exponential data with boxcox
normalized_data = stats.boxcox(original_data)

# plot both together to compare
fig, ax=plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(original_data, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(normalized_data[0], ax=ax[1], kde=True, legend=False)
ax[1].set_title("Normalized data")
plt.show()
~~~