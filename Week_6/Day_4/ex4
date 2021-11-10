--1--
--select first_name as "First Name", last_name as "Last Name" from employees
--select distinct department_id from employees
--select * from employees order by first_name desc
--select first_name, last_name, salary, (salary*0.15, 2) as PF from employees
--select employee_id, first_name, last_name from employees order by salary asc
--select sum(salary) from employees
--select min(salary), max(salary) from employees
--select avg(salary) from employees
--select count(employees) from employees
--select upper(first_name) from employees
--select substring(first_name from 1 for 3) from employees
--select concat(first_name, ' ', last_name) as "full name" from employees
--select first_name, last_name, length(concat(first_name, ' ', last_name)) as "full name" from employees
/*select first_name,
case when first_name ~'^[0-9]^' then 'true' else 'false' 
end as "contains numbers"
from employees*/
--select first_name from employees limit 10

--2--
--select first_name from employees where salary > 10000 and salary > 15000
--select first_name, last_name from employees where extract(year from hire_date) = 1987 
--select employees from employees where first_name like '%c%' and first_name like '%e%'
/*
select employees.last_name, jobs.job_title, employees.salary 
from employees
join jobs on employees.job_id = jobs.job_id
where salary in (4500, 10000, 15000) and jobs.job_title !='Programmers' and jobs.job_title !='Shipping Clerks'
*/
--select last_name from employees where length(last_name) = 6
--select last_name from employees where last_name like '__e%'
/*
select distinct jobs.job_title from employees
join jobs on employees.job_id = jobs.job_id order by jobs.job_title asc
*/
select * from employees where upper(last_name) in ('BLAKE', 'SCOTT', 'KING', 'FORD')