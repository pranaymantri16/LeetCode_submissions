# Write your MySQL query statement below
select product_name, year, price
from Product p
Join Sales s
on p.product_id = s.product_id;