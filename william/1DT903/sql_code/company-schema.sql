
CREATE TABLE employee (
  fname    VARCHAR(15) not null, 
  minit    VARCHAR(1),
  lname    VARCHAR(15) not null,
  ssn      char(9),
  bdate    date,
  address  VARCHAR(50),
  sex      char,
  salary   BIGINT,
  superssn char(9),
  dno      INT,
  primary key (ssn),
  foreign key (superssn) references employee(ssn)
--  foreign key (dno) references department(dnumber)
);

CREATE TABLE department (
  dname        VARCHAR(25) not null,
  dnumber      INT,
  mgrssn       char(9) not null, 
  mgrstartdate date,
  primary key (dnumber),
  unique (dname),
  foreign key (mgrssn) references employee(ssn)
);

ALTER TABLE employee ADD (
  foreign key (dno) references department(dnumber)
);

CREATE TABLE dept_locations (
  dnumber   INT,
  dlocation VARCHAR(15), 
  primary key (dnumber,dlocation),
  foreign key (dnumber) references department(dnumber)
);


CREATE TABLE project (
  pname      VARCHAR(25) not null,
  pnumber    INT,
  plocation  VARCHAR(15),
  dnum       INT not null,
  primary key (pnumber),
  unique (pname),
  foreign key (dnum) references department(dnumber)
);


CREATE TABLE works_on (
  essn   char(9),
  pno    INT,
  hours  INT,
  primary key (essn,pno),
  foreign key (essn) references employee(ssn),
  foreign key (pno) references project(pnumber)
);

CREATE TABLE dependent (
  essn           char(9),
  dependent_name VARCHAR(15),
  sex            char,
  bdate          date,
  relationship   VARCHAR(8),
  primary key (essn,dependent_name),
  foreign key (essn) references employee(ssn)
);
