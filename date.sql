UPDATE historical_games #data #games #kenpom
SET Date = CASE 
   WHEN LOWER(Date) LIKE '%jan%' THEN CONCAT('Jan ', REGEXP_REPLACE(SUBSTRING_INDEX(Date, ' ', -1), '[^0-9]', ''), 'th')
   WHEN LOWER(Date) LIKE '%feb%' THEN CONCAT('Feb ', REGEXP_REPLACE(SUBSTRING_INDEX(Date, ' ', -1), '[^0-9]', ''), 'th')
END
WHERE Date IS NOT NULL AND Date != '';