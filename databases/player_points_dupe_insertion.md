# Player Points (Error in table update)
We have a **players** table that gets updated every year, with the new lifetime total
of goals for the player after the latest season. This year, instead of updating the goals 
total, an employee errored and did an insert.

### Players table
| Column      | Type |
|-------------| ---- |
| id          | varchar |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int |
 | club_id     | int |

Please note that the id is a varchar.
<br><br>

## Question
Write a query to get current goal total for each player.  
Assume no players have the same first-last name combination.

### Expected output
| Column      | Type |
|-------------| ---- |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int |  

<br><br>

## Setup
```postgresql
DROP TABLE IF EXISTS public.players;

CREATE TABLE IF NOT EXISTS public.players
(
    id varchar NOT NULL,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    total_goals integer NOT NULL,
    club_id integer NOT NULL,
    CONSTRAINT players_pkey PRIMARY KEY (id)
);

insert into players values
('1', 'Jack', 'Spears', 333, 1),
('2', 'Samantha', 'Spears', 223, 2),
('3', 'Anne', 'Matte', 167, 3),
('4', 'Dick', 'Donaldson', 120, 3),
('5', 'Jill', 'Black', 33, 2),
('6', 'James', 'Green', 240, 2),
('7', 'Jock', 'Sespic', 27, 2),
('8', 'Gerard', 'Runner', 130, 2),
('9', 'Tom', 'Booths', 90, 1),
('10', 'Bill', 'Brady', 133, 1);

DROP TABLE IF EXISTS public.clubs;

CREATE TABLE IF NOT EXISTS public.clubs
(
    id integer NOT NULL,
    name varchar(30) NOT NULL,
    CONSTRAINT clubs_pkey PRIMARY KEY (id)
);

insert into clubs values
(1, 'Avocado Orchards'),
(2, 'Melaluka Farms'),
(3, 'Cane Cooks'),
(4, 'Cypress Sprinters');
```
<br><br>

## Solution
```postgresql
select p.first_name, p.last_name, p.total_goals
from players p
join (select max(id::int) as id, first_name, last_name
		from players
		group by first_name, last_name) as t
on e.id::int = t.id
```

