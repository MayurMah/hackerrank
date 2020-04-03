# MS SQL

select s.Name 
from Students s 
join Packages p1 on s.ID = p1.ID
join Friends f on s.ID = f.ID 
join Packages p2 on f.Friend_ID = p2.ID and p1.Salary < p2.Salary
order by p2.Salary;