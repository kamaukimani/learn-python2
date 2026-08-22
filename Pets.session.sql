-- CREATE TABLE IF NOT EXISTS cats(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     age INTEGER,
--     breed TEXT
-- );
-- INSERT INTO cats (name,age,breed) VALUES
-- ('Maru',3,'Scottish'),
-- ('Hana',1,'Tabby');
-- CREATE TABLE IF NOT EXISTS owners(
--     id INTEGER PRIMARY KEY,
--     name TEXT
-- );
--ALTER TABLE cats ADD COLUMN owner_id INTEGER;
--INSERT INTO owners (name) VALUES ('mugumogu');
UPDATE cats SET owner_id=1 WHERE name='Maru';
UPDATE cats SET owner_id=1 WHERE name='Hana';
SELECT * FROM cats WHERE owner_id=1;