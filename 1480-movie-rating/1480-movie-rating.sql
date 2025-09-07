(select u.name as results from users u join movierating mr on u.user_id=mr.user_id group by u.user_id order by  count(mr.rating) desc ,u.name asc limit 1)
union all
(select m.title as results from movies m  join movierating mr on m.movie_id = mr.movie_id WHERE EXTRACT(YEAR_MONTH FROM mr.created_at) = 202002 group by m.movie_id order by avg(mr.rating) desc , m.title asc  limit 1)
