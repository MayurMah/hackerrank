# MS SQL 

select 
    hacker_id,name
    ,chl_count
from
    (
        select 
            *
            ,count(hacker_id) over(partition by chl_count) as same_chl_count
            ,max(chl_count) over() as max_chl_count 
        from 
            (
                select 
                    h.hacker_id
                    ,h.name
                    ,count(challenge_id) as chl_count
                from 
                    Hackers h
                    join Challenges c 
                        on h.hacker_id = c.hacker_id
                group by 
                    h.hacker_id,h.name
            ) hcc
    ) final
where 
    final.same_chl_count = 1 
    or chl_count = max_chl_count 
order by 
    chl_count desc,hacker_id;
 