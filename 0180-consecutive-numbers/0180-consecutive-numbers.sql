-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM (
--     SELECT 
--         num,
--         LEAD(num, 1) OVER (ORDER BY id) AS next1,
--         LEAD(num, 2) OVER (ORDER BY id) AS next2
--     FROM Logs
-- ) t
-- WHERE num = next1 AND num = next2;



select distinct num as ConsecutiveNums from(select num,lead(num,1) over (order by id) as next1,lead(num,2)over (order by id)as next2 from logs)t where num=next1 and num=next2 ;