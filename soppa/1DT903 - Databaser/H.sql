SELECT fname,lname
FROM EMPLOYEE AS E
INNER JOIN WORKS_ON AS W ON E.ssn = W.essn
INNER JOIN PROJECT AS P ON W.pno = P.pnumber
INNER JOIN DEPARTMENT AS D ON E.dno = D.dnumber
WHERE D.dnumber = '5' AND E.salary > '30000' AND P.pname = 'ProductZ';