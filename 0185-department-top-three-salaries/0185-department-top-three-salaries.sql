SELECT d.name AS Department, 
       e.name AS Employee, 
       e.salary AS Salary
FROM (
    SELECT e.*,
           DENSE_RANK() OVER (
               PARTITION BY departmentId 
               ORDER BY salary DESC
           ) AS r
    FROM Employee e
) e
JOIN Department d 
  ON e.departmentId = d.id
WHERE r <= 3
ORDER BY d.name ASC, e.salary DESC;
