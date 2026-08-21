CREATE TABLE IF NOT EXISTS bears(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    sex CHAR(1),
    color TEXT,
    temperament TEXT,
    alive BOOLEAN
);
INSERT INTO bears(name,age,sex,color,temperament,alive) VALUES
('Mr. Chocolate',20,'M','dark brown','calm',0),
('Rowdy',10,'M','black','intense',1),
('Tabitha',6,'F','dark brown','nice',1),
('Seargent Brown',19,'M','Green','slimy',0),
('Grinch',2,'M','Black','grinchy',1),
('Melissa',13,'F','dark brown','goofy',1),
('Wendy',6,'F','Blue','naive',1),
(NULL,20,'M','black','aggresive',0);

--DROP TABLE IF EXISTS bears;
SELECT name,age FROM bears WHERE sex='F';
SELECT name FROM bears ORDER BY name ASC;
SELECT name,age,alive FROM bears WHERE alive=1 ORDER BY age ASC;
SELECT name,age FROM bears ORDER BY age DESC LIMIT 1;
SELECT name,age FROM bears ORDER BY age ASC LIMIT 1;