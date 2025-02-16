Create VIEW gameday_evanmiya as
SELECT gs.matchup, gs.homefav, gs.awaydog, e.team, e.O_Rate, e.D_Rate, e.Net_Rate, e.Opponent_Adjust, e.Off_Rank, e.Def_Rank, e.Runs_per_game, e.Runs_conceded_per_game,
e.runs_Total, e.Runs_conceded_total
FROM ncaab.gameday_spread as gs
INNER JOIN evanmiya as e
ON e.team = gs.homefav OR e.team = gs.awaydog;

CREATE VIEW evanmiya_effeciency as
SELECT 
    h.matchup,
    h.Opponent_Adjust as home_opponent_adjustment,
    a.Opponent_Adjust as away_opponent_adjustment,
    h.homefav AS home_team,
    h.o_rate AS home_o_rate,
    h.d_rate AS home_d_rate,
    h.net_rate AS home_net_rate,
    a.awaydog AS away_team,
    a.o_rate AS away_o_rate,
    a.d_rate AS away_d_rate,
    a.net_rate as away_net_rate,
    -- Calculate the differences
    round((h.o_rate - a.o_rate),2) AS o_rate_diff,
    round((h.d_rate - a.d_rate),2) AS d_rate_diff,
    round((h.net_rate - a.net_rate),2) as net_rate_diff,
    round(((h.runs_per_game + a.runs_conceded_per_game) / 2),2) as home_killshot_avg,
    round(((a.runs_per_game + h.runs_conceded_per_game)/2),2) as away_killshot_avg,
    h.opponent_adjust as home_opp_adj,
    a.opponent_adjust as away_opp_adj
    
FROM 
    ncaab.gameday_evanmiya as h
JOIN 
    ncaab.gameday_evanmiya as a 
ON 
    h.matchup = a.matchup 
    AND h.team = h.homefav 
    AND a.team = h.awaydog;
