with Employee(name, salary) as
(
 select 'Rick',3000 from dual union all
 select 'John',4000 from dual union all
 select 'Shane',3000 from dual union all
 select 'Peter',5000 from dual union all
 select 'Jackob',7000 from dual
)
 select name, salary
   from Employee
   join ( select max(salary) as max_sal, 
                 min(salary) as min_sal
           from Employee )
      on  salary in ( min_sal, max_sal )
  group by name, salary
  order by salary desc, name;

 NAME   SALARY
 ------ -------
 Jackob  7000
 Rick    3000
 Shane   3000