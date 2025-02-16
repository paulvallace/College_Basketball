Create View gameday_spread as
SELECT gameday_homefav.matchup,gameday_awaydog.spread, gameday_homefav.team as homefav, gameday_homefav.`win-loss` as home_WL, 
gameday_awaydog.team as awaydog, gameday_awaydog.`win-loss` as away_WL,
gameday_homefav.MOV as homefav_MOV, gameday_awaydog.MOV as awaydog_MOV, gameday_homefav.ATS as homefav_ATS, gameday_awaydog.ATS as awaydog_ATS
FROM ncaab.gameday_awaydog
INNER JOIN gameday_homefav ON gameday_awaydog.matchup = gameday_homefav.matchup
#ORDER BY ATS DESC, MOV DESC