# Write your MySQL query statement below
WITH DailyRevenue AS (
    SELECT visited_on, SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
MovingAvg AS (
    SELECT d1.visited_on,
           SUM(d2.total_amount) AS amount,
           ROUND(AVG(d2.total_amount), 2) AS average_amount
    FROM DailyRevenue d1
    JOIN DailyRevenue d2 
        ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
    GROUP BY d1.visited_on
)
SELECT visited_on, amount, average_amount
FROM MovingAvg
WHERE visited_on >= (SELECT MIN(visited_on) + INTERVAL 6 DAY FROM Customer)
ORDER BY visited_on;
