-- list all records in table
SELECT `score`, `name`
FROM `second_table` 
WHERE `name` != ""
ORDER BY `score` DESC
