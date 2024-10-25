-- Finds the dnums of the projects and than finds the first name and last name for the employees in these projects
-- 1.1
select fname, lname
from employee
where ssn in (
	select essn
    from works_on w
    inner join project p on p.pnumber = w.pno
    where p.pname in ('Middleware', 'DatabaseSystems')
);


-- 1.2
select fname, lname
from employee
where ssn in (
	select essn 
    from works_on w
    inner join project p on p.pnumber = w.pno
    where p.pname = 'DatabaseSystems' and w.hours > 40
);

-- 1.3
select project.pnumber, 
	project.dnum, 
    employee.lname, 
    employee.bdate, 
    employee.address

from project, employee
where project.plocation = 'Houston' and employee.ssn in (
        select department.mgrssn
        from department
        where department.dnumber = project.dnum
);

-- 1.4
select 
	emp.fname as employee_fname,
    emp.lname as employee_lname,
    mgr.fname as manager_fname,
    mgr.lname as manager_lname

from employee emp
left join employee mgr on emp.superssn = mgr.ssn;

-- 1.5
select fname, lname
from employee 
where address like '%Houston%' and sex = 'M'; 

-- 1.6
select *
from employee
where month(bdate) = 8; -- as august is the 8 month

-- 1.7
select department.dname, avg(employee.salary) as avg_salary
from department
inner join employee on department.dnumber = employee.dno
group by department.dname;

-- 1.8
select fname, lname 
from employee e
left join works_on w on e.ssn = w.essn
where w.essn is null;

-- 1.9
select e.fname, e.lname
from employee e
join works_on w on e.ssn = w.essn
join project p on w.pno = p.pnumber
where e.dno = 7 and p.pname = 'DatabaseSystems' and e.salary > 50000;

-- 1.10
select fname, lname
	from employee 
	where address like '%Houston, TX%' and superssn = 333445555;

-- 1.11
select fname, lname
from employee
where dno = (
    select dno
    from employee
    group by dno
    having avg(salary) = (
        select max(avg_salary)
        from (
            select avg(salary) as avg_salary
            from employee
            group by dno
		) as dep_avg
    )
);


-- 1.12
select dep.dnumber as department_number, dep.dname as dep_name, COUNT(emp.ssn) as number_of_employees
from department dep
join employee emp on dep.dnumber = emp.dno
where dep.dnumber in (
    select dno
    from employee
    group by dno
    having avg(salary) > 35000
)
group by dep.dnumber, dep.dname;

-- 1.13
select dependent_name, relationship
from dependent
where essn in (
	select ssn
    from employee
    where superssn = 333445555
)
order by dependent_name;

-- 1.14
select pname, sum(hours) as total_hours, count(distinct employee.ssn) as employee_count
from project
join works_on on project.pnumber = works_on.pno
join employee on works_on.essn = employee.ssn 
group by pname;

-- 1.15
select
  d.dname as department_name,
  count(distinct p.pnumber) as number_of_projects,
  count(distinct e.ssn) as number_of_employees

from department d

left join project p on d.dnumber = p.dnum
left join employee e on d.dnumber = e.dno

group by d.dname;

-- 1.16
select e.fname as manager_fname, 
	e.lname as manager_lname, 
	COUNT(w.pno) as num_projects
from department d
join employee e on d.mgrssn = e.ssn
left join works_on w on e.ssn = w.essn
group by e.ssn, e.fname;

-- 1.17
select 
	manager.fname, manager.lname,
    count(manager.ssn) as employee_count
from employee manager
join department d on manager.ssn = d.mgrssn
join employee on employee.dno = d.dnumber
group by manager.fname, d.dname;