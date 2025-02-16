CREATE VIEW gameday_homedog as
SELECT DISTINCT gameday.*, home_dog.* 
FROM home_dog
INNER JOIN gameday	
  ON gameday.matchup REGEXP CONCAT(' at #[0-9]+ ', TRIM(home_dog.team), '$')
ORDER BY CAST(REPLACE(home_dog.win_percent, '%', '') AS DECIMAL) DESC, `win-loss` DESC;