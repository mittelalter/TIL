# About SQL Code

contents
> * How to Create a Database and a Table?


### Create
1. Create a Database
~~~ sql
CREATE DATABASE some_database
~~~

2. Don't forget to use the database, so that only to write the table name (Database name no needed)
~~~sql
USE some_database 
~~~

~~~sql
SELECT * FROM just_only_table_name
~~~

3. Create a table, Don't forget backtik `
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


4. Insert row, if you want to create a row for all columns, it is not nesseary to write column names
~~~sql
INSERT INTO student
		(id, name, student_number, major, email, phone, admission_date) /*not nesseary to write */
		VALUES('1', 'ryu', '20220505', 'Data_Science', 'daesun.ryu96@gmail.com', '0171802', '20220101');


INSERT INTO food_menu (menu, price, ingredient) VALUES ('some_soup', 50, 'salad, carrot, onion..'); /*not nesseary to write id because it is auto incresement*/
~~~


