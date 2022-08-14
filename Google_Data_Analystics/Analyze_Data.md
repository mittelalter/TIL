# About Data Analyze to answer the real questions

## Contents
> * Sorting datesets in Excel
> * Functions from Excel
> * Convert and Format data
> * SQL Functions / Subquery
> * Pivot table





### Sorting datesets in Excel

* **Difference beteween Sort sheet and Sort range**
    - Sort range is: only sorts fields within the specified range. Data across rows are not kept together when sorted.
    - But sort sheet sorts all fields within rows so it is common to use sort sheet, when it is about column.


* **Advanced range sorting options** (very useful)
    - It's possible to add mulitple condition and to sort only certain range what i want to sort.


* **Difference between menu sort and SORT function**
    -The sort from a spreadsheet's Data tab overwrites the cells containing the unsorted data with the sorted data, while a written SORT function inserts the sorted data in a different cell range. The sort in the Data tab can also exclude a header row in the data range from being sorted, while the data range for a written SORT function should never contain a header row.


****


### Functions
* **SORT**
    - Notice to write a number for a column not a alpahbet


* **CONVERT**
    - Convert the value to another value


* **Data Validation**
    - **Data** - Data validation

* **Value**
    - Convert a text string to a numerical value

* **VLOOKUP**
    - A spreadsheet function that vertically searches for a certain value in a column to return a corresponding piece of information
    - VLOOKUP(A2,'Employee Rates'!A2:B5, 2, False)

* **COUNTIF**
    - Just like SUMIF, you set the range and then the condition that needs to be met. For example, if you wanted to count the number of times Food came up in the Expenses column, you could use a COUNTIF function like this: =COUNTIF(A1:A9, "Food")

* **SUMIF**
    - The first range is where the function will search for the condition that you have set. The criterion is the condition you are applying and the sum_range is the range of cells that will be included in the calculation.

* **AVERAGEIF/S**
    - range, condition, what i want to
    - what i want to, range1, condition1, range2, condtion2


* **MAXIF**
    - The first argument, max_range, is the array over which you are finding the maximum. The second argument (range1) is the array you are checking. The third argument (criteria1) is the value that you are checking for. The inputs in the square brackets are for optional additional constraints.=MAXIFS(D2:D21, B2:B21, "NY")

    - The MAXIFS function can input more than one constraint. This is where the optional range2 and constraint2 come into play. Additional constraints follow the logic that every constraint must be satisfied for a cell in the max_range to be considered.

    For example, to find the maximum sales in New York where the Max Item Cost is below $400, type the following into the function bar: =MAXIFS(D2:D21, B2:B21, "NY", E2:E21, "<400").

* **SUMPRODUKT**

    ***

    
### SQL Functions / Subquery
* **JOIN**
    - The OUTER JOIN clause enables them to combine RIGHT and LEFT JOIN functionality to return matching records from either table. The INNER JOIN clause returns records that match in both tables. 

* **Return one column**
    - A subquery can't have more than one column specified in the SELECT clause.
    - For a subquery to compare multiple columns, those columns must be selected in the main query.

* **Return multiple rows**
    - Subqueries that return more than one row rely on multiple value operators such as the IN command.


***

* **Pivot table**
- Can create group by with right click menu
- The Summarize By drop-down menu changes the function applied to the values. The SUM function is the default function, but there are other options, such as COUNT