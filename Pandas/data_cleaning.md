# About Data Cleaning with Pandas

Contents
> * Chekcing miss values



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