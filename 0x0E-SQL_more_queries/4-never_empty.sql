-- create table id_not_null
-- Description: id INT, name VARCHAR(256)
-- script shouldn't throw error if table already exist
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
