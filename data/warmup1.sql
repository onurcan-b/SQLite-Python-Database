
--Onurcan Buyukkalkan 
SELECT name FROM parks 
WHERE name LIKE 'W%';

SELECT name, address FROM parks 
WHERE address LIKE '%60637%';


-- I think this is the usual way to join but
-- I am used to the one below
SELECT parks.name, parks.address
FROM parks
JOIN park_times ON parks.id == park_times.id
WHERE park_times.close_time > 2100; 


SELECT parks.name, parks.address, park_times.close_time
FROM parks, park_times
WHERE park_times.close_time > 2100 and parks.id == park_times.id; 
-------------

SELECT name, address FROM parks 
WHERE tokens LIKE '%basketball%';


--See how "day" is structured
SELECT id, day FROM park_times LIMIT 10;

SELECT name, address, description FROM parks 
JOIN park_times ON parks.id == park_times.id
WHERE park_times.open_time <= 0500 and 
            parks.tokens LIKE '%reformer%' and
            park_times.day LIKE "%sat%";


