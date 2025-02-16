CREATE VIEW gameday_away AS
SELECT DISTINCT gameday.*, away.*
FROM away
INNER JOIN gameday
  ON gameday.matchup REGEXP CONCAT('#[0-9]+ ', away.team, ' at') 
ORDER BY ATS ASC, CAST(REPLACE(away.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;