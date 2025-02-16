CREATE VIEW gameday_final as
SELECT *
FROM ncaab.gameday_spread
INNER JOIN kenpom
ON kenpom.team = gameday_spread.homefav OR kenpom.team = gameday_spread.awaydog;

CREATE VIEW gameday_effeciency_diff as
SELECT 
    h.matchup,
    h.homefav AS home_team,
    h.ORtg AS home_ORtg,
    h.DRtg AS home_DRtg,
    h.NetRtg AS home_NetRtg,
    a.awaydog AS away_team,
    a.ORtg AS away_ORtg,
    a.DRtg AS away_DRtg,
    a.NetRtg as away_NetRtg,
    -- Calculate the differences
    round((h.ORtg - a.ORtg),2) AS ORtg_diff,
    round((h.DRtg - a.DRtg),2) AS DRtg_diff,
    round((h.NetRtg - a.NetRtg),2) as NetRtg_diff,
    round((h.AdjT - a.NetRtg),2) as AdjT_diff
FROM 
    ncaab.gameday_final as h
JOIN 
    ncaab.gameday_final as a 
ON 
    h.matchup = a.matchup 
    AND h.team = h.homefav 
    AND a.team = h.awaydog;
