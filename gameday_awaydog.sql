CREATE VIEW gameday_awaydog as
SELECT DISTINCT gameday.*, away_underdog.*
FROM away_underdog
INNER JOIN gameday
  -- Match the team name exactly by using REGEXP or stricter patterns
ON LOWER(TRIM(gameday.matchup)) REGEXP LOWER(CONCAT('^', TRIM(away_underdog.team), ' at ', '[^()]+ \\(-[0-9.]+\\)$'))
ORDER BY 
  CAST(REPLACE(away_underdog.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;
