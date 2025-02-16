#CREATE VIEW historical_homefav as
SELECT *
FROM historical_games
Where left(spread, 1) = '-'
-- INNER JOIN gameday	
-- ON LOWER(TRIM(gameday.matchup)) REGEXP LOWER(CONCAT(' at ', TRIM(home_favorite.team), ' \\(-?[0-9.]+\\)$'))
-- ORDER BY CAST(REPLACE(home_favorite.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;

