# Write your MySQL query statement below
select name as Customers from Customers as c
left join Orders O
On c.id=O.customerId
where customerId is null;
