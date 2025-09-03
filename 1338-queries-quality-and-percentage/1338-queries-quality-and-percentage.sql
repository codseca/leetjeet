# Write your MySQL query statement below
select query_name, round(sum((rating/position))/count(*),2) as quality , round(100*sum(case when rating<3 then 1 else 0 end )/count(*),2) as poor_query_percentage from queries group by query_name;
-- SELECT 
--     query_name,
--     ROUND(SUM(rating/position) / COUNT(*), 2) AS quality,
--     ROUND(100 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage
-- FROM Queries
-- GROUP BY query_name;
