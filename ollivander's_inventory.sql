# MS SQL 

select id,age,coins_needed, power from 
(select id, age, coins_needed, power, dense_rank() over(partition by power,age order by coins_needed asc) w_rank
from Wands w
join Wands_Property wp on w.code = wp.code and wp.is_evil = 0) wands_ranked
where w_rank = 1
order by power desc, age desc;