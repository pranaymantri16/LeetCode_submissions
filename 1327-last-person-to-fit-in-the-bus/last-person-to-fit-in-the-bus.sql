WITH CumulativeWeight AS (
    SELECT person_id, person_name, weight, turn,
           SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
)
SELECT person_name
FROM CumulativeWeight
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;