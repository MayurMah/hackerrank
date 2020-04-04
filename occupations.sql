-- MS SQL

select [Doctor],[Professor],[Singer],[Actor] from 
( 
    select *, ROW_NUMBER() over (partition by Occupation order by o.Name) RN from Occupations o
) t
PIVOT(
        MIN(Name)
        for Occupation in
        (
            [Doctor],
            [Professor],
            [Singer],
            [Actor]
        )
        
    ) as pvt;