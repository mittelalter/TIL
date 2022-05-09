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


~~~sql
-- 프로그래머스 GROUP BY 문제
-- HOUR함수와 WHERE절로 조건을 또 추가할 수 있다는 부분을 배움.
SELECT HOUR(datetime), COUNT(HOUR(datetime))

FROM ANIMAL_OUTS

WHERE HOUR(datetime) >= 9 and HOUR(datetime) < 20

GROUP BY HOUR(datetime)

ORDER BY HOUR(datetime)
~~~

