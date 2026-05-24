/* Write your T-SQL query statement below */
SELECT 
    MAX(SALARY) AS SecondHighestSalary
FROM (
    SELECT DISTINCT TOP 2 SALARY
    FROM Employee
    ORDER BY SALARY DESC
) AS t
WHERE SALARY < (SELECT MAX(SALARY) FROM Employee);