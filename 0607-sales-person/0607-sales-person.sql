/* Write your T-SQL query statement below */
select name 
from SalesPerson 
where name not in
(select SP.name 
from SalesPerson SP
JOIN Orders O
on O.sales_id = SP.sales_id
JOIN Company C
on O.com_id = C.com_id
where C.name = 'RED')