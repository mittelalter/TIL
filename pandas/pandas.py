""" About pandas """

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

"""idxmax: "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html
Creating pandas Series with a map and lambda function"""
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=["tropical", "fruity"])


"""About groupby
value_counts() is just a shortcut to this groupby() operation
Grap a colum what you want to check (at this point i grouped points and grap a point column)
With agg fucntion it is possible to run a bunch of functions"""
reviews.groupby("points").points.count()
reviews.groupby("winery").apply(lambda df: df.title.iloc[1])
reviews.groupby(["country"]).price.agg([len, min, max])


"""About Multi-indexes
In general the multi-index method you will use most often
is the one for converting back to a regular index, the reset_index() method"""
countries_reviewed = reviews.groupby(["country", "province"]).description.agg([len])
countries_reviewed.reset_index()
