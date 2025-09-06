# Write your MySQL query statement below
select distinct m.employee_id,m.name , count(e.employee_id) OVER (PARTITION BY e.reports_to) as reports_count,round(avg(e.age) OVER (PARTITION BY e.reports_to),0) as average_age from employees e join employees m on e.reports_to=m.employee_id ;
-- SELECT DISTINCT
--     m.employee_id,
--     m.name,
--     COUNT(e.employee_id) OVER (PARTITION BY e.reports_to) AS reports_count,
--     ROUND(AVG(e.age) OVER (PARTITION BY e.reports_to), 0) AS average_age
-- FROM employees m
-- JOIN employees e
--   ON e.reports_to = m.employee_id;
