CREATE VIEW gameday_FINAL_effeciency AS
select gameday_effeciency_diff.matchup, gameday_effeciency_diff.home_team, gameday_effeciency_diff.home_ORtg, 
gameday_effeciency_diff.home_DRtg, gameday_effeciency_diff.home_NetRtg, gameday_effeciency_diff.away_team, 
gameday_effeciency_diff.away_ORtg, gameday_effeciency_diff.away_NetRtg, gameday_effeciency_diff.ORtg_diff,
gameday_effeciency_diff.DRtg_diff, gameday_effeciency_diff.NetRtg_diff, round((homefav_ats - awaydog_ats), 2) as ATS_diff 
from gameday_effeciency_diff 
INNER Join gameday_spread ON gameday_spread.homefav = gameday_effeciency_diff.home_team
