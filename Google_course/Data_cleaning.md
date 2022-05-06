# About Data cleaning skills that i've leanred from the Google data analyse course.

contents
> * concepts of function or words
> * Data cleaning tools and techniques


### Concepts you must know
* Compatibility
    * How well two or more datasets are able to work together

* Data merge

* Data mapping
    * The process of matching fields from one data source to another

* Schema
    * A way of describing how something is organized

* Primary key
    * References a column in which each value is unique

* Foregin Key
    * A field within a table that is a primary key in another table




### Week2 Cleaning data in spreadsheets
1. Check out blanks
Range the data - **Format** - click conditional formatting - click is empty - select color

2. Remove duplicate
**Data** - click data clean up - remove duplicate

3. Make dates consistent
select column - **Format** - click number - date

4. Split a text string with delimeter
select column - **Date** - click split text to commas (to be abel to seelct other delimeter options)

5. Some useful functions
**COUNTIF(range, 'value')**: return the number of cells that match a specified value
**LEN** - for example use with conditional formatting like not euqal to 6 than the other numbers except 6 will be highlighted.
**LEFT(range, number)**, **RIGHT**, **MID**, **CONCATENATE(A2," ", B2)**, **TRIM**

3. Different data perspectives, sorting and filtering
**Pivot table**: data summarization tool
**VLOOKUP(data to look up, 'where to look'!Rangem, column, false)**: vertical lookup, function that searches for a certain value in a column to return a corresponding piece of information
**Insert** - click pivot table 
**Edit** - clikc find and replace 

4. Check if the numerical values is ok
select column - **Insert** - click chart
