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


"""About Missing values"""
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()
# Fill out the null values with fillna function
reviews_per_region = (
    reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
)

"""About renaming and combination"""
reviews.rename_axis("wines", axis="rows").rename_axis("fields", axis="columns")
pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(["title", "trending_date"])
right = british_youtube.set_index(["title", "trending_date"])
left.join(right, lsuffix="_CAN", rsuffix="_UK")
