-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT `name`
    FROM `tv_genres` AS genre
        INNER JOIN `tv_show_genres` AS show
        ON genre.`id` = show.`genre_id`

        INNER JOIN `tv_shows` AS t
        ON show.`show_id` = t.`id`
        WHERE genre.`name` NOT IN
            (SELECT `name`
                FROM `tv_genres` AS genre
                    INNER JOIN `tv_show_genres` AS show
                    ON genre.`id` = show.`genre_id`

                    INNER JOIN `tv_shows` AS t
                    ON show.`show_id` = t.`id`
                    WHERE t.`title` = "Dexter")
 ORDER BY genre.`name`;
