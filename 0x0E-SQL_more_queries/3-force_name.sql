-- Write a script that creates the table
-- force_name on your MySQL server.
-- id INT; name VARCHAR(256)
-- If table exists, script shouldn't throw error
CREATE TABLE IF NOT EXISTS force_table
(id INT, name VARCHAR(256) NOT NULL);
