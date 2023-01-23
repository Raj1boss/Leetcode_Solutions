# Write your MySQL query statement below

select firstName,lastName,city,state from Address
RIGHT JOIN Person
ON Person.personId=Address.personId