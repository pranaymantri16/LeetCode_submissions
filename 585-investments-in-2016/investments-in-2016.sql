WITH DuplicateTIV AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
UniqueLocation AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM 
    Insurance i
JOIN 
    DuplicateTIV d ON i.tiv_2015 = d.tiv_2015
JOIN 
    UniqueLocation u ON i.lat = u.lat AND i.lon = u.lon;
