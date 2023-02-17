-- create table unique_id 
-- Description: id INT, name VARCHAR(256)
-- script shouldn't throw error if table already exist
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
