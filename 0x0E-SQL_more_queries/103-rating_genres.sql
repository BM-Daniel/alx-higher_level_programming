-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS genre INNER JOIN `tv_show_genres` AS show
ON show.`genre_id` = genre.`id`

INNER JOIN `tv_ahoq_ratings` AS tv_rating
ON rating.`show_id` = show.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
