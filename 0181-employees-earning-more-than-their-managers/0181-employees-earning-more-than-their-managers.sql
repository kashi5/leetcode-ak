# Write your MySQL query statement below
select a.Name as Employee
from Employee a
inner join Employee b
on a.ManagerId = b.id
and a.salary > b.salary
