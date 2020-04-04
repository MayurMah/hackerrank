-- MS SQL

select (case when Grade >= 8 then Name else NULL end), Grade, Marks   
from Students s 
join Grades g
on s.Marks >= g.Min_Mark and s.Marks <= g.Max_Mark
order by Grade desc, Name asc, Marks asc;