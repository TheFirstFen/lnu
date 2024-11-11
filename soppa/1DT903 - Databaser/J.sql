SELECT fname,lname
FROM EMPLOYEE AS E
INNER JOIN DEPARTMENT AS D ON E.dno = D.dnumber
WHERE E.address LIKE '%Houston, TX%' AND D.mgrssn = '333445555';
