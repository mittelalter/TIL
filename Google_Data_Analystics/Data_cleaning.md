# About Data cleaning skills that i've leanred from the Google Data Analystics course.

## Contents
> * concepts of function or words
> * Data cleaning tools and techniques
> * SQL concepts
> * SQL functions that are useful to clean the data




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






### Week2 Cleaning data in spreadsheets + Week 4 Documenting results and the cleaning process

* **Check out blanks**
    * Range the data - **Format** - click conditional formatting - click is empty - select color


* **Remove duplicate** 
    * **Data** - click data clean up - remove duplicate


* **Make dates consistent** 
    * select column - **Format** - click number - date


* **Split a text string with delimeter** 
    * select column - **Date** - click split text to commas (to be abel to seelct other delimeter options)


* **Some useful functions** 
    * **COUNTIF(range, 'value')**: return the number of cells that match a specified value
    * **LEN** - for example use with conditional formatting like not euqal to 6 than the other numbers except 6 will be highlighted.
    * **LEFT(range, number)**, **RIGHT**, **MID**, **CONCATENATE(A2," ", B2)**, **TRIM**


* **Different data perspectives, sorting and filtering** 
    * **Pivot table**: data summarization tool
    * **VLOOKUP(data to look up, 'where to look'!Rangem, column, false)**: vertical lookup, function that searches for a certain value in a column to return a corresponding piece of information
    * **Insert** - click pivot table 
    * **Edit** - clikc find and replace 


* **Check if the numerical values is ok** 
    * select column - **Insert** - click chart

* **Find typo and replace it** 
    * **Edit** - click find and replace

* **time track and to see who changes the file and how** 
    * **file** - clikc version history - see version history

* **Advanced functions for speedy data cleaning**
    * **IMPORTRAGEN**
        * Keeping data clean and in sync with a sourceimport, date from one sheet to another and keeps it automatically updated

    * **QUERY**
        * Keeping data clean and in sync with a source

    * **FILTER**:
        * Filtering data to get what you want





### SQL concepts

* Getting data from a table using SELECT statements.

* De-duplicating data using commands like DISTINCT and COUNT + WHERE.

* Manipulating string data with TRIM() and SUBSTR.

* Creating/dropping tables with CREATE TABLE and DROP TABLE.

* Changing data types with CAST.





### Useful SQL functions

* Advanced funtions
    * **CAST()** - The CAST() function converts a value (of any type)  into the specified datatype.
    * **COALESCE** - The COALESCE() function returns the first non-null value in a list.

* String function
     **CCONCAT** - The CONCAT() function adds two or more expressions together.

