SELECT employee_id,
       department_id
FROM Employee e
WHERE CASE 
          -- keep rows where the department is marked primary
          WHEN e.primary_flag = 'Y' THEN TRUE
          -- keep rows where this employee has only 1 department
          WHEN (SELECT COUNT(*) 
                  FROM Employee 
                  WHERE employee_id = e.employee_id) = 1 
          THEN TRUE
          ELSE FALSE
      END;
