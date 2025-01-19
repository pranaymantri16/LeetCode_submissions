# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans
from Visits v
Left Join Transactions t
on v.visit_id = t.visit_id
where t.visit_id is NULL
Group By v.customer_id;