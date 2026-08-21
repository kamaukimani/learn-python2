CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY,
    car_make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT
);
-- INSERT INTO cars(car_make,model,year,color)
-- VALUES
--     ('Toyota','Camry XLE',2005,'Gray'),
--     ('Honda','Accord EX',2002,'Black'),
--     ('Lexus','ES 350',2008,'Gray'),
--     ('BMW','3 series Coupe',2008,'Red');
-- SELECT * FROM cars;
-- SELECT COUNT(*) FROM cars WHERE color='Gray';
SELECT '................MINIMUM..............';
SELECT MIN(year) FROM cars;
SELECT '................MAXIMUM..............';
SELECT MAX(year) FROM cars;
SELECT '................AVERAGE..............';
SELECT AVG(year) FROM cars;
SELECT '................SUM..................';
SELECT SUM(year) FROM cars;