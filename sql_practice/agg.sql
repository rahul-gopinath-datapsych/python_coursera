


Select * from table
where upper(name) = 'TARUSH'

select name, count(*)
from table
group by 1
having  count(*) > 5