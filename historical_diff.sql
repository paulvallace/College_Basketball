CREATE VIEW historical_data AS
SELECT 
   hm.*,
   hk_home.NetRtg as home_netrtg,
   hk_home.ORtg as home_ortg, 
   hk_home.DRtg as home_drtg,
   hk_home.AdjT as home_adjt,
   hk_away.NetRtg as away_netrtg,
   hk_away.ORtg as away_ortg,
   hk_away.DRtg as away_drtg, 
   hk_away.AdjT as away_adjt,
   ROUND(hk_home.ORtg - hk_away.ORtg, 2) AS ORtg_diff,
   ROUND(hk_home.DRtg - hk_away.DRtg, 2) AS DRtg_diff,
   ROUND(hk_home.NetRtg - hk_away.NetRtg, 2) AS NetRtg_diff,
   ROUND(hk_home.AdjT - hk_away.AdjT, 2) AS AdjT_diff
FROM historical_matchup hm
INNER JOIN historical_kenpom hk_home 
   ON hk_home.Date = hm.date 
   AND hk_home.Team = hm.Home
INNER JOIN historical_kenpom hk_away
   ON hk_away.DATE = hm.date 
   AND hk_away.Team = hm.Away;