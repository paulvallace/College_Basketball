CREATE VIEW gameday_awayfav as
SELECT DISTINCT gameday.*, away_fav.*
FROM away_fav
INNER JOIN gameday
  ON gameday.matchup REGEXP CONCAT('#[0-9]+ ', away_fav.team, ' at') 
ORDER BY ATS ASC, CAST(REPLACE(away_fav.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;