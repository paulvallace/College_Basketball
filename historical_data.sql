#Create View historical_data as
SELECT 
   hm.*,
   hk_home.NetRtg as home_netrtg,
   hk_home.ORtg as home_ortg, 
   hk_home.DRtg as home_drtg,
   hk_home.AdjT as home_adjt,
   hk_away.NetRtg as away_netrtg,
   hk_away.ORtg as away_ortg,
   hk_away.DRtg as away_drtg, 
   hk_away.AdjT as away_adjt
FROM historical_matchup hm
INNER JOIN historical_kenpom hk_home 
   ON hk_home.Date = hm.date 
   AND hk_home.Team = hm.Home
INNER JOIN historical_kenpom hk_away
   ON hk_away.Date = hm.date 
   AND hk_away.Team = hm.Away