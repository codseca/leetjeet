# Write your MySQL query statement below
select e.name from employee e , employee m where e.id=m.managerid group by e.id having count(e.id)>=5;