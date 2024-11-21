select e.fname as manager_fname, 
	e.lname as manager_lname, 
	COUNT(w.pno) as num_projects
from department d
join employee e on d.mgrssn = e.ssn
left join works_on w on e.ssn = w.essn
group by e.ssn, e.fname
order by num_projects desc;