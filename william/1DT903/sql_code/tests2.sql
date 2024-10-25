select fname, lname, address
from employee
where address like "%Houston, TX%" and ssn in (
	select essn
    from works_on w
    join project p on p.pnumber = w.pno
	join department d on d.dnumber = p.dnum
    where d.mgrssn = 333445555 
);


select *
from employee e
inner join works_on w on w.essn = e.ssn
join project p on p.pnumber = w.pno
join department d on d.dnumber = p.dnum
where e.address like "%Houston, TX%" and d.mgrssn = 333445555;


select * from department;