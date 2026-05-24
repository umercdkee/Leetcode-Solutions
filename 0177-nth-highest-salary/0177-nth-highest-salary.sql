CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    if (@N) <= 0
        return null;
    RETURN (
        /* Write your T-SQL query statement below. */
        select 
        case when count(t.salary) = (@N) then min(t.salary)
        else null
        end as NthHighestSalary
        from
        (select distinct top (@N)
        salary
        from Employee order by salary desc)t
    );
END