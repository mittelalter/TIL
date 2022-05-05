# About how to set up to use Seaborn 

contents
> * Set up to start
> * Load the Data
> * Review the Data
> * Work on it!


### Set up
~~~python
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
~~~


### Load the Data
~~~python
some_data_file_path = "../input/ign_scores.csv"
some_data = pd.read_csv(ign_filepath, index_col='Platform')
~~~


### Review the Data
~~~python
some_data.head()
some_data.tail()
~~~


### Work on it (basic)
~~~python
# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
# Notice that x and y can be always changed. Depends on the length of name
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")
~~~