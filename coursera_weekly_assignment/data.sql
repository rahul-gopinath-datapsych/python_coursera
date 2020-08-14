




CREATE TABLE employees_rawdata (
	employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	first_name varchar(100),
	last_name varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
	phone_number varchar(100),
	hire_date varchar(100) NOT NULL,
	job_id INTEGER NOT NULL,
	salary float NOT NULL,
	manager_id INTEGER,
	department_id INTEGER NOT NULL)
;

insert into employees_rawdata 
Select * from employees
where employee_id>115
and phone_number is null;