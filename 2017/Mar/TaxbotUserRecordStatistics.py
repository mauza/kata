#This is just a file to save queries for User trip and expense statistics

#1 (get number of users) Users: 395956 (157405 active)
Select 
	Count(U.email)
from 
	users U
Where
	U.isactive = 't' 

#2 (get number of expenses) # of expenses: 7426285
SELECT
	count(E.id)
FROM
	expenses E

#3 (get total ammount of expenses) Total expenses: $838,591,341.51
SELECT
	SUM(E.total)
FROM
	expenses E
WHERE
	E.total < 1000000

#4 (get total ammount of users w/ expenses) Users w/ expenses: 128256
SELECT
	U.email,
	SUM(E.total) as total
FROM
	expenses E
	INNER JOIN users U on E.userid = U.id
GROUP BY
	U.email

#5 (get total ammount of users w/ trips) Users w/ trips: 108715
SELECT
	U.email,
	Count(T."id") as total
FROM
	trips T
	INNER JOIN users U on T.userid = U.id
GROUP BY
	U.email

#6 (get total number of trips) # of trips: 11554993
SELECT
	COUNT(T."id")
FROM
	trips T

#7 (get total number of unclassified trips) # of unclassified trips: 5948922
SELECT
	COUNT(T."id")
FROM
	trips_unclassified T

#8 (get number of unclassified trip miles) Unclassified trip total miles: 68691125.899
SELECT
	SUM(T.totalmileage)
FROM
	trips_unclassified T

#9 (get number of trip miles) total classified trip miles: 308938362.066
SELECT
	SUM(T.totalmileage)
FROM
	trips T
WHERE
	T.totalmileage < 10000

#10 (get total miles combined) Total miles: 377629487.965

#11 (get total number of records) total records: 24930200

#12 (get total number of users with records) users w/ records: 

