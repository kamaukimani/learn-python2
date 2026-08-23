-- CREATE TABLE IF NOT EXISTS cats(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     age INTEGER,
--     breed TEXT
-- );
-- INSERT INTO cats (name,age,breed) VALUES
-- ('Maru',3,'Scottish'),
-- ('Hana',1,'Tabby'),
-- ('Nona',4,'Tortoise'),
-- ('Lil'' Bub',2,'perma-kitten');
--SELECT * FROM cats;

-- CREATE TABLE IF NOT EXISTS owners(
--     id INTEGER PRIMARY KEY,
--     name TEXT
-- );
-- INSERT INTO owners (name) VALUES('Mugumogu'),('Sophie'),('Penny');
--SELECT * FROM owners;

-- CREATE TABLE IF NOT EXISTS cat_owners(
--     cat_id INTEGER,
--     owner_id INTEGER
-- );


-- INSERT INTO cat_owners(cat_id,owner_id) VALUES 
-- (3,2),(3,3),(1,2);

--QUERING JOIN TABLE
-- SELECT owners.name
-- FROM owners
-- INNER JOIN cat_owners
-- ON owners.id=cat_owners.owner_id
-- WHERE cat_owners.cat_id=3;

-- SELECT cats.name
-- FROM cats
-- INNER JOIN cat_owners
-- ON cats.id=cat_owners.cat_id
-- WHERE cat_owners.owner_id=2;

SELECT 
cats.name AS 'cat_name',
owners.name AS 'owner_name'
FROM cats
INNER JOIN cat_owners
    ON cats.id=cat_owners.cat_id
INNER JOIN owners
    ON cat_owners.owner_id=owners.id;
