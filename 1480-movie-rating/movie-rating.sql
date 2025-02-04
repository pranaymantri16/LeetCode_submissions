WITH UserMovieCount AS (
    SELECT ur.name AS user_name, COUNT(mr.movie_id) AS num_movies
    FROM Users ur
    JOIN MovieRating mr ON ur.user_id = mr.user_id
    GROUP BY ur.user_id
),
MaxMovies AS (
    SELECT user_name
    FROM UserMovieCount
    WHERE num_movies = (SELECT MAX(num_movies) FROM UserMovieCount)
    ORDER BY user_name
    LIMIT 1
),
FebruaryRatings AS (
    SELECT mr.movie_id, AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id
),
MaxRatedMovie AS (
    SELECT m.title
    FROM Movies m
    JOIN FebruaryRatings fr ON m.movie_id = fr.movie_id
    WHERE fr.avg_rating = (SELECT MAX(avg_rating) FROM FebruaryRatings)
    ORDER BY m.title
    LIMIT 1
)
SELECT 
    (SELECT user_name FROM MaxMovies) AS results
UNION ALL
SELECT 
    (SELECT title FROM MaxRatedMovie) AS results;
