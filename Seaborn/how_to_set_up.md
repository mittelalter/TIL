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
some_data = pd.read_csv(ign_filepath, index_col='Platform') #since the row labels (from the 'Month' column) don't correspond to dates, we don't add parse_dates=True, it means you should wirte parse_dates=True when the row is date
~~~


### Review the Data
~~~python
some_data.head()
some_data.tail()
~~~


### Work on it (basic)
1. Bar chart
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

2. Heat map
~~~python
# Set the width and height of the figure
plt.figure(figsize=(10,10))
# Heatmap showing average game score by platform and genre, annot=True - This ensures that the values for each cell appear on the chart. (Leaving this out removes the numbers from each of the cells
sns.heatmap(ign_data, annot=True)
# Add label for horizontal axis
plt.xlabel("Genre")
# Add label for vertical axis
plt.title("Average Game Score, by Platform and Genre")
~~~

3. Scatter Plot
~~~python
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# sns.regplot to double-check the strength of this relationship use regression line
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# sns.scatterplot to display the relationship beteween 3 variables use color scatter plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# sns.lmplot command to add two regression lines, not insurance_data['bmi'] but just 'bmi' and to write data source
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)


sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
~~~