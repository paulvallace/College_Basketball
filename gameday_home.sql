CREATE VIEW gameday_home as
SELECT DISTINCT gameday.*, home.* 
FROM home
INNER JOIN gameday	
  ON gameday.matchup REGEXP CONCAT(' at #[0-9]+ ', TRIM(home.team), '$')
ORDER BY CAST(REPLACE(home.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;