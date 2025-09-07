SELECT 
    c1.visited_on,
    SUM(c2.amount) AS amount,
    ROUND(SUM(c2.amount) / 7, 2) AS average_amount
FROM (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
) c1
JOIN (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
) c2
ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
GROUP BY c1.visited_on
HAVING COUNT(DISTINCT c2.visited_on) = 7;
-- # Write your MySQL query statement below
-- select c.visited_on,
-- (
--     select sum(amount)
--     from customer
--     where visited_on between date_sub(c.visited_on, interval 6 day)
--     and c.visited_on
-- ) as amount,
-- (
--     select round(sum(amount)/7,2)
--     from customer
--     where visited_on between date_sub(c.visited_on,interval 6 day)
--     and c.visited_on
-- ) as average_amount
-- from customer c
-- where c.visited_on>=(
--     select date_add(min(visited_on), interval 6 day)
--     from customer
-- )
-- group by c.visited_on
-- order by c.visited_on;