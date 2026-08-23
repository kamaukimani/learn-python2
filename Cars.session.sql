-- CREATE TABLE IF NOT EXISTS cars(
--     id INTEGER PRIMARY KEY,
--     company TEXT,
--     country TEXT,
--     model TEXT,
--     year INTEGER,
--     color TEXT
-- );
-- INSERT INTO cars (company,country,model,year,color) VALUES
-- ('Toyota','Japan','Camry',2014,'Silver'),
-- ('Toyota','Japan','Avalon',2012,'Grey'),
-- ('Honda','Japan','Accord',2012,'Black'),
-- ('Chevrolet','USA','Maliu',2014,'Red'),
-- ('Ford','USA','Fusion',2014,'Whote'),
-- ('BMW','Germany','BMW 3',2013,'Red'),
-- ('Audi','Germany','A4',2014,'Blue');

--SELECT * FROM cars;
--SELECT company,country,model FROM cars;
--SELECT DISTINCT company,country FROM cars;  --remove duplicat

--SELECT * INTO car_copies FROM cars;  --Microsoft SQL Server.
--CREATE TABLE IF NOT EXISTS car_copies AS SELECT * FROM cars;   --create table copy with data

--SELECT * FROM cars WHERE color='Silver';

--DELETE FROM car_copies;  --deletes all rows
--DROP TABLE car_copies;  --deletes table
--DELETE FROM car_copies WHERE color='Silver' OR color='Grey';   --DELETES 2 ROWS
--DELETE FROM cars WHERE color IN ('Silver','Grey');  --DELETES 2 ROWS

--UPDATE cars SET model='Malibu' WHERE company='Chevrolet';
--UPDATE cars SET color='White' WHERE color='Whote';

--SELECT company,year FROM cars ORDER BY year DESC;
SELECT company,country,year,color FROM cars ORDER BY year ASC, color DESC;