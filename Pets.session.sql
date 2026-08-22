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
-- UPDATE cats SET owner_id=1 WHERE name='Maru';
-- UPDATE cats SET owner_id=1 WHERE name='Hana';
-- SELECT * FROM cats WHERE owner_id=1;
--INSERT INTO owners (name) VALUES ('Sophie');
-- INSERT INTO cats (name,age,breed,owner_id)
-- VALUES('Nona',4,'Tortoise',2);
-- INSERT INTO cats (name,age,breed)
-- VALUES('Lil''Bub',2,'perma-kitten');

--INNER JOIN
SELECT cats.name,cats.breed, owners.name AS 'owner_name'
FROM cats
INNER JOIN owners
ON cats.owner_id=owners.id;

--LEFT JOIN
SELECT cats.name,cats.breed,owners.name AS 'owner_name'
FROM cats
LEFT OUTER JOIN owners     --use either LEFT JOIN OR LEFT OUTER JOIN
ON cats.owner_id=owners.id;

