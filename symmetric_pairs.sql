-- MS SQL

select X,Y from 
    (
        select (case when X < Y then X else Y end) X, (case when X < Y then Y else X end) Y from Functions
    ) Functions_sorted
    group by X, Y 
    having count(*) >= 2
    order by X