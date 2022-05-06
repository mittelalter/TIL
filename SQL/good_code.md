# About just stroing good code to review them sometimes

contents
> * Save some SQL codes which brought me 'aha'


### By Hacker Rank

~~~sql
SELECT CITY FROM STATION WHERE LOWER(SUBSTR(CITY,1,1)) in ('a','e','i','o','u');
~~~

~~~sql
-- 프로그래머스 select 마지막 문제
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS)
~~~