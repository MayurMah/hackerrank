# MS SQL 

set quoted_identifier ON;
With temp as
(SELECT 2 AS val 
UNION ALL
SELECT t.val+1
FROM
    temp t
where 
    t.val < 1000
),
temp2 as (
select val
from 
    temp t1
where 
    NOT EXISTS(
        SELECT 1 
        FROM 
            temp t2 
        where 
            t1.val > t2.val and t1.val % t2.val = 0 
    )
)
SELECT CAST(STUFF((
          SELECT '&' + CAST(val as varchar) 
          from temp2 t1 
          FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS VARCHAR(8000))
OPTION (MAXRECURSION 0);