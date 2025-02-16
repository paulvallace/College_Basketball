#CREATE VIEW gameday_spread_homedog_awayfav AS
SELECT gameday_homedog.matchup, gameday_homedog.team as homedog, gameday_homedog.`win-loss` as home_WL, 
gameday_awayfav.team as awayfav, gameday_awayfav.`win-loss` as away_WL,
gameday_homedog.MOV as homedog_MOV, gameday_awayfav.MOV as awayfav_MOV, gameday_homedog.ATS as homedog_ATS, gameday_awayfav.ATS as awayfav_ATS
#round((gameday_homefav.MOV - gameday_awaydog.MOV),2) as MOV, round((gameday_homefav.ATS - gameday_awaydog.ATS),2) as ATS
FROM ncaab.gameday_awayfav
INNER JOIN gameday_homedog ON gameday_awayfav.matchup = gameday_homedog.matchup
#ORDER BY ATS DESC, MOV DESC