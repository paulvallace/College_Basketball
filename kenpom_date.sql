UPDATE historical_games #data #games #kenpom
SET Date = CASE 
   WHEN LOWER(Date) LIKE '%jan%' THEN CONCAT('Jan ', REGEXP_REPLACE(SUBSTRING_INDEX(Date, ' ', -1), '[^0-9]', ''), 'th')
   WHEN LOWER(Date) LIKE '%feb%' THEN CONCAT('Feb ', REGEXP_REPLACE(SUBSTRING_INDEX(Date, ' ', -1), '[^0-9]', ''), 'th')
END
WHERE Date IS NOT NULL AND Date != '';

UPDATE historical_kenpom 
SET Date = CONCAT(
    CASE 
        WHEN SUBSTRING(Date, 6, 2) = '12' THEN 'Dec '
        WHEN SUBSTRING(Date, 6, 2) = '01' THEN 'Jan '
        WHEN SUBSTRING(Date, 6, 2) = '02' THEN 'Feb '
    END,
    CAST(SUBSTRING(Date, 9, 2) AS SIGNED)
)
WHERE Date IS NOT NULL 
AND Date REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

UPDATE historical_games
SET date = REPLACE(REPLACE(REPLACE(REPLACE(date, 'th', ''), 'st', ''), 'nd', ''), 'rd', '');

UPDATE historical_matchup
SET date = REPLACE(REPLACE(REPLACE(REPLACE(date, 'th', ''), 'st', ''), 'nd', ''), 'rd', '');

-- Update historical_kenpom to remove 'th' if it exists
UPDATE historical_kenpom
SET date = REPLACE(REPLACE(REPLACE(REPLACE(date, 'th', ''), 'st', ''), 'nd', ''), 'rd', '');
