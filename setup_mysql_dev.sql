-- Creates the hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets a password for the user
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- Grants privileges to a user on the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants SELECT privileges to the user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flushes privileges
FLUSH PRIVILEGES;