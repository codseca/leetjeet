# Write your MySQL query statement below
select person_name from (select person_id,person_name,sum(weight) over (order by turn) as cw from queue ) as sub where cw<=1000 ORDER BY cw DESC
LIMIT 1;
 ;