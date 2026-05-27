/* Write your T-SQL query statement below */
select Employee.name, bonus
from Employee LEFT JOIN BONUS
on Employee.empId = Bonus.empId
where (bonus < 1000 or bonus is NULL)