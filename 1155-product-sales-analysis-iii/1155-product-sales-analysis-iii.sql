# Write your MySQL query statement below
select product_id , year as first_year,quantity , price from 
(select * , RANK() OVER (PARTITION BY product_id ORDER BY year ) as rk from sales )ranked
where rk=1
;


