proc sql;
create table customer_kpi as
select
    customer_id,
    sum(amount) as total_amount,
    count(*) as transaction_count
from transactions
where status='Completed'
group by customer_id;
quit;
