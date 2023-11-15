-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genre.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
RIGHT JOIN tv_show_genres
ON tv_genre.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
