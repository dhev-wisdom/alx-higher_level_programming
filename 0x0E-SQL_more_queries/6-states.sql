-- creates database and table
-- states description: id INT UNIQUE AUTO-GENERATED NOT NULL PRIMARY KEY;
-- ... name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
