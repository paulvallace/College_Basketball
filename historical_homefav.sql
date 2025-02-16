CREATE VIEW historical_matchup as
SELECT *
FROM historical_games
Where left(spread, 1) = '-'