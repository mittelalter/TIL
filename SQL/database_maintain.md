# About how to maintain database with mysql

contents
> * How to Create a Database and a Table and how to insert/update/delete the data in it ?
> * Handle the table
> * Foreign Key


### Create

* Create a Database
~~~ sql
CREATE DATABASE some_database
~~~

* Don't forget to use the database, so that only to write the table name (Database name no needed)

~~~sql
USE some_database 
~~~

~~~sql
SELECT * FROM just_only_table_name
~~~

* Create a table, Don't forget backtik `

~~~sql
CREATE TABLE `animal_info` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `type` VARCHAR(30) NOT NULL,
    `name` VARCHAR(10) NOT NULL,
    `age` TINYINT NOT NULL,
    `sex`CHAR(1) NOT NULL,
    `weight` DOUBLE NOT NULL,
    `feature` VARCHAR(500) NULL,
    `entry_date` DATE NOT NULL,
    PRIMARY KEY (`id`)
);
~~~

---

### Insert

* Insert row, if you want to create a row for all columns, it is not nesseary to write column names

~~~sql
INSERT INTO student
		(id, name, student_number, major, email, phone, admission_date) /*not nesseary to write */
		VALUES('1', 'ryu', '20220505', 'Data_Science', 'daesun.ryu96@gmail.com', '0171802', '20220101');


INSERT INTO food_menu (menu, price, ingredient) VALUES ('some_soup', 50, 'salad, carrot, onion..'); /*not nesseary to write id because it is auto incresement*/
~~~

------

### Update

* How to update the data in data table?

~~~sql
-- Update row
Update table_name SET column = "value" WHERE row = 1
~~~


~~~sql
-- Update coulmn name
ALTER TABLE table_name CHANGE COLUMN old_name new_name column_definition
~~~


~~~sql
-- Update original value as it is (기존값 그대로 사용하기)
Update exam_score SET score = score + 3
-- All score values will be + 3
~~~

------

### Delete

* How to delete the data in data table?

~~~sql
DELETE FROM table_name WHERE id(row) = 1;
~~~


-----

### Handle the Data

* Add column and rename

~~~sql
ALTER TABLE table_name ADD column col_type(ex, char(1)) property(ex, null)

ALTER TABLE table_name RENAME COLUMN old_col_name TO new_col_name

ALTER TABLE table_name DROP COLUMN column_name

-- property, null value or default set
ALTER TABLE table_name MODIFY column_name INT/STR/whatever NOT NULL/NULL DEFAULT 101
~~~


* CONSTRAINT

~~~sql
ALTER TABLE table_name ADD CONSTRAINT my_rule CHECK (price > 100)

ALTER TABLE table_name DROP my_rule
~~~


* COPY TABLE

~~~sql
-- copy all rows from the table which i want to copy
CREATE TABLE copy_table_name AS SELECT * FROM some_table
~~~

~~~sql
-- copy all columns from some_table 
CREATE TABLE copy_table_name LIKE some_table

-- now i have columns so copy all rows
INSERT INTO copy_table_name SELECT * FROM some_table
~~~



### Foreign Key

* Restrict
* Cascade
* Set null 