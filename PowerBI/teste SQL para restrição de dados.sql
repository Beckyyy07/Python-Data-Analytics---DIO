use world;
select * from country;
SELECT continent, COUNT(*) as quantidade_paises FROM country
GROUP BY continent;

SELECT Name from country where continent = 'Antarctica';
SELECT * from country where continent = 'Antarctica';

SELECT * from country where Name = 'Brazil';

SELECT * FROM country WHERE IndepYear LIKE '18%';