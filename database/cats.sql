-- CREATE TABLE cats(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     age INTEGER,
--     breed TEXT
-- );
--INSERT INTO cats(name,age,breed) VALUES('Lil',5,'American');
SELECT * FROM cats;
SELECT '----------------name=''Maru''--------------------------';
SELECT * From cats WHERE name='Maru';
SELECT '------------------age < 5 ---all------------------------';
SELECT * FROM cats WHERE age < 5;
SELECT '------------------age < 5----name and age--------------------';
SELECT name,age FROM cats WHERE age < 5;
SELECT '----------------UPDATE-----------------------------------------';
UPDATE cats SET name='Hann' WHERE name='Hannah';
SELECT * FROM cats;
UPDATE cats SET name ='Hana' WHERE name='Hann';
SELECT name FROM cats WHERE name='Hana';
SELECT '----------------DELETE ROW-----------------------------------------';
DELETE FROM cats WHERE name='Hana';
SELECT * FROM cats;