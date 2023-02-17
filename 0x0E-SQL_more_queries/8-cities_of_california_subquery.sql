-- script list all cities of california found in database
SELECT id, name FROM cities
WHERE stat_id = (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY id;
