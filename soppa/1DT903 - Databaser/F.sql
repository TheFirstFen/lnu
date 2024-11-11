SELECT dname, AVG(E.salary) as average_salary
FROM EMPLOYEE AS E
INNER JOIN DEPARTMENT AS D ON E.dno = D.dnumber
GROUP BY D.dname;

