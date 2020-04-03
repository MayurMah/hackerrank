# MS SQL 

select distinct 
    b1.N
    ,(  case 
            when b1.P is NULL then 'Root'
            when b2.N is NULL then 'Leaf'
            else 'Inner'
        end
    ) NodeType 
from BST b1 
left join BST b2 
on b1.N = b2.P
order by b1.N;