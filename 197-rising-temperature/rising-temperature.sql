# Write your MySQL query statement below
select id
from Weather w1
where temperature > (
    select temperature
    from Weather w2
    where w2.recordDate = Date_Sub(w1.recordDate, Interval 1 Day)
);