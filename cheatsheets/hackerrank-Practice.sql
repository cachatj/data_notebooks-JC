--Queries the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

SELECT CITY,
       LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY),
         CITY ASC LIMIT 1;


SELECT CITY,
       LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1;


SELECT DISTINCT city
FROM STATION
WHERE city LIKE 'a%'
  OR city LIKE 'e%'
  OR city LIKE 'i%'
  OR city LIKE 'o%'
  OR city LIKE 'u%'



/*
City Names that start AND end with vowels, no duplicates
*/

SELECT DISTINCT city
FROM STATION
WHERE REGEXP_LIKE(City, '^[aeiou].*[aeiou]$');



^(?!.*[aeiou])$

/* BREAKDOWN OF REGEXP "^[aeiou].*[aeiou]$""

^ = start of string
[] = contains characters in bracket
. = any character except line break
* = matches zero or more occurences of preceeding expression
[] = contains characters in bracket
$ = anchor to match string at end of a line

*/


/*
List of City names that DO NOT end with Vowels, no duplicates
*/

SELECT city
FROM station
WHERE LOWER(SUBSTRING(City, LENGTH(CITY), 1)) NOT IN ('a','e','i','o','u')




/*
any NAME WHERE SCORE > 75, 
ORDER BY SUBSTRING(Name, LENGTH(NAME), 3)
SORT BY ID ASC
*/

SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY (SUBSTRING(Name, LENGTH(Name)-2, 3)) ASC, id ASC

SELECT name FROM STUDENTS
WHERE marks > 75
ORDER BY SUBSTRING(name, LENGTH(name)-2, 3) ASC, 
id ASC

