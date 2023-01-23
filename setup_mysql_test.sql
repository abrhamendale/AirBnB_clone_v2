-- Creates the hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets a password for the user
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- Grants privileges to a user on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants SELECT privileges to the user on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flushes privileges
FLUSH PRIVILEGES;