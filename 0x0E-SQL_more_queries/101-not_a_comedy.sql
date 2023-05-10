-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT DISTINCT `title`
FROM `tv_shows` AS tv
LEFT JOIN `tv_show_genres` AS show
ON show.`show_id` = tv.`id`

LEFT JOIN `tv_genres` AS genre
ON genre.`id` = show.`genre_id`

WHERE title.`title` NOT IN (
    SELECT `title`
    FROM `tv_shows` AS tv
    INNER JOIN `tv_show_genres` AS show
    ON show.`show_id` = tv.`id`

    INNER JOIN `tv_genres` AS genre
    ON genre.`id` = show.`genre_id`

    WHERE genre.`name` = "Comedy"
)

ORDER BY genre.`title`;
