SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
 ( 
    select *,
    count(*) over (partition by tiv_2015) as er,
    count(*) over (partition by lat,lon ) as tf
    from insurance 
)t
where 
er>1 and tf=1