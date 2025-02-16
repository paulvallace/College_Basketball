UPDATE ncaab.gameday
SET Spread = CASE 
    WHEN POSITION('(' IN matchup) < POSITION(' at ' IN matchup) THEN
        -- Away team spread, flip the sign
        CAST(TRIM(BOTH ' ' FROM REGEXP_REPLACE(REGEXP_SUBSTR(matchup, '\\((-?\\d+(?:\\.\\d+)?)\\)'), '[\\(\\)]', '')) AS FLOAT) * -1
    ELSE
        -- Home team spread, keep the sign
        CAST(TRIM(BOTH ' ' FROM REGEXP_REPLACE(REGEXP_SUBSTR(matchup, '\\((-?\\d+(?:\\.\\d+)?)\\)'), '[\\(\\)]', '')) AS FLOAT)
END;