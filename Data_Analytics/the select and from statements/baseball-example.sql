SELECT
    player_name,
    number_of_home_runs
FROM
    baseball_stats
WHERE
    team = 'Atlanta Braves'
    AND number_of_home_runs >= 10
    AND season = 2020